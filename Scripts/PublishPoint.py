import rospy
import networkx as nx
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, PoseStamped, Point, Twist, PoseWithCovarianceStamped, PointStamped
from tf.transformations import euler_from_quaternion
from heapq import heappop, heappush
from math import atan2
from move_base_msgs.msg import MoveBaseActionGoal
MoveBaseActionGoal


global x,y,z
x = 0.0
y = 0.0
z = 0.0

class RobotController:

    def __init__(self):
        print("passei no início")
        rospy.init_node('robot_controller')
       
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.amcl_pose_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.amcl_callback)
        self.goal_sub = rospy.Subscriber('/clicked_point', PointStamped, self.callback)
        self.cmd_vel_pub = rospy.Publisher('/robot/cmd_vel', Twist, queue_size=10)
        self.graph = nx.Graph()
        self.current_pose = None
        
    def callback(self, msg): 
        x = msg.point.x    
        y = msg.point.y
        z = msg.point.z
        rospy.loginfo("coordinates:x=%f y=%f" %(x,y))
        paths = self.calculate_astar_path(self.get_current_pose(), msg)

        self.follow_path(paths)
        goalPose = Pose(position = Point(x = x, y = y, z = z))
        self.send_goal(goalPose)

    def odom_callback(self, odom_msg):
        
        self.current_pose = odom_msg.pose.pose
        self.update_graph()
        print("self current pose", self.current_pose)
        #print("chamei o ODOM")

    def amcl_callback(self, amclpose):
        print("chamei o AMCL")
        pose = amclpose.pose.pose
        #print(pose)
        self.update_graph()

    def goal_callback(self, goal_msg):
        print("chamei o GOAL")
        current_pose = self.get_current_pose()
        if current_pose:
            print("passei condicao GOAL")
            path = self.calculate_astar_path(current_pose, goal_msg.pose)
            self.follow_path(path)

    def send_goal(self, goal_pose):
        print("Enviei o GOAL")
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = "map"  
        goal_msg.pose = goal_pose
        self.goal_pub.publish(goal_msg)

    def update_graph(self):
        #print("chamei o UPDATE GRAPH")
        if self.current_pose:
            node_id = len(self.graph.nodes) + 1
            self.graph.add_node(node_id, pose=self.current_pose)
            #print("passei condicao UPDATE GRAPH")

    
    
    def calculate_astar_path(self, start_pose, goal_pose):
        print("chamei o CALCULAR A*")
        print("start pose", start_pose)
        print("goal pose", goal_pose)
        start_node = (round(start_pose.position.x), round(start_pose.position.y))
        goal_node = (round(goal_pose.point.x), round(goal_pose.point.y))
        

        def get_neighbors(node):
            x, y = node
            return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        def heuristic(node, goal):
            return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

        frontier = [(0, start_node)]
        came_from = {start_node: None}
        cost_so_far = {start_node: 0}

        while frontier:
            current_cost, current_node = heappop(frontier)

            if current_node == goal_node:
                break

            for next_node in get_neighbors(current_node):
                new_cost = cost_so_far[current_node] + 1  

                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + heuristic(next_node, goal_node)
                    heappush(frontier, (priority, next_node))
                    came_from[next_node] = current_node

        path = []
        current_node = goal_node
        while current_node != start_node:
            path.append(current_node)
            current_node = came_from[current_node]
        path.reverse()

        path_poses = [Pose(position=Point(x=node[0], y=node[1], z=0.0)) for node in path]
        print("teste", path_poses)

        return path_poses

    def follow_path(self, path):
        print('chamei o FOLLOW PATH')
        current_p = self.get_current_pose()
        print("current_p", current_p.position)
        for pose in path:
            print("Pose", pose)
            cmd_vel_msg = self.convert_pose_to_cmd_vel(target_pose = pose)
            self.cmd_vel_pub.publish(cmd_vel_msg)
            print("enviei o comando para o CMD_VEL")
            rospy.sleep(1)  

    def convert_pose_to_cmd_vel(self, target_pose, linear_speed=0.2, angular_speed=0.2):
        current_pose = self.get_current_pose()
        print("transformei a POSE em CMD_VEL")
        cmd_vel = Twist()

        cmd_vel.linear.x = linear_speed

        print("current pose", current_pose)
        print("target pose", target_pose)

        _,_,currentio = euler_from_quaternion([
            current_pose.orientation.x,
            current_pose.orientation.y,
            current_pose.orientation.z,
            current_pose.orientation.w
        ])

        angle_to_target = atan2(target_pose.position.y - current_pose.position.y,
                                target_pose.position.x - current_pose.position.x)
        cmd_vel.angular.z = angular_speed * (angle_to_target - currentio)


        return cmd_vel

    def get_current_pose(self):
        print('chamei o POSE')
        return self.current_pose

if __name__ == '__main__':
    try:
        #rospy.init_node("robot_controller")
        controller = RobotController()
        rospy.spin()
    except rospy.ROSInterruptException as e:
        print("erro: " + e)