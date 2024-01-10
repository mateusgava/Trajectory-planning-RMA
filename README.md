# Introdução à Robôtica Móvel:
<div align="center">Universidade Federal de São Carlos</div>
<div align="center">🗺️ Trajectory Planning RMA 🗺️</div>

<br />
<br />

# Projeto #01:
 A proposta deste trabalho é o desenvolvimento e simulação de algoritmo de trajetoria para robô movél autônomo e a implementação em um prototipo equivalente. Foram implementados topologias e arquitituras em ambiente virtual por meio de recurso computacional utilizando a ferramenta **ROS** (_Robotic Operating System_), que permite simular caracteristicas e modelos em um ambiente controlado e simulado antes da implementação no mundo real, utilizando tecnicas de **HIL** (_Hardware-in-the-loop_).
 
  
 O algoritimo desenvolvido tem como premissa desvio de obstáculos durante o deslocamento do robô em um percurso fechado e pré-definido. Para correção e predição de trajetoria são utilizados metodos de Monte Carlo e A-Star, que combinados analisam os dados coletados pelo sensor acoplado no prototipo, e consequentemente enviando instruções para que o robô consiga corrigir a direção e sentido do seu deslocamento.   

O robô possui um sensor laser que capta objetos e obstaculos a sua frente, e com base nas informações coletadas permite que o algortimo de correção de trajetória possa agir com uma ação de controle corriginto a direção e sentido do deslocamento. O laser é instalado em um ponto central localizado na frente do robô, emitindo feixes de luz distribuidos em um arco de **180 graus**, cuja o valor absoluto mensurado pode variar a medida que detecta um obstaculo. 


O algoritmo de correção de trajetoria implementado utiliza os metodos de **Monte Carlo** e **A-Star**, que possui as finalidades de predizer a posição do robô autonomo em termos de coordenadas em um espaço eucletiano e inferir uma nova trajetoria com base nas informações de contorno e nos dados coletatos durante um deslocamento, respectivamenente.


### 👣 Inicializar o Gazebo
```bash
# Faça uma cópia do repositório
$ git clone <link aqui>

# Acesse a pasta do repositório pelo terminal utilizando:
$ cd DCrobot

# Inicialize o catkin com:
$ catkin build

# Navegue até a pasta de iniciar o gazebo:
$ cd src/mobile_rob_dev_sim/launch

# Inicialize o Roz com:
$ rosrun launch navigation.launch

# Em alguns segunos o script irá abrir o Gazebo e o Rviz...
```


### 👣 Inicializar o Script
```bash
# Caso não tenha feito, faça uma cópia do repositório
$ git clone <link aqui>

# Acesse a pasta do repositório pelo terminal utilizando:
$ cd DCrobot

# Agora será necessário caminhar até a pasta de execução do ambiente simulado
$ cd bla/bla/bla

# Ative o arquivo de execução com o comando:
$ rosrun launch <nomeDoArquivo>.launch

# Aguarde até que todos as aplicações se abram

# Agora caminhe para a pasta 'scripts'
$ cd /<Repo Directory>/Scripts

# Abra o código no seu editor de texto, por exemplo, vscode
$ code .

# Execute o script python para aguardar intereções com o rviz (demarcar ponto de trajetória)
$ python3 <nomeDoArquivo>.py
```


### ❔Como Utilizar:
- 1º Dentro do RViz selecione **Publish Point**
- 2º Escolha um ponto que deseja
- 3º Clique com o botão esquerdo no ponto desejável
- 4º Aguarde o script calcular a trajetória


### 🗒️ Respostas para o Formulário
```text
1. Teste em Ambiente Simulado
Descreva os requisitos de configurações necessários adotado no ambiente simulado.

🔸**RESPOSTA:**

O mapeamento do ambiente está sendo realizado conforme o algoritmo especificado?

🔸**RESPOSTA:**

A navegação está respondendo corretamente no ambiente simulado?

🔸**RESPOSTA:** 

Os sensores estão atuando conforme os requisitos durante o teste simulado?

🔸**RESPOSTA:**

O algoritmo de planejamento de trajetória está gerando trajetórias adequadas no ambiente simulado?

🔸**RESPOSTA:**


 A detecção de obstáculos está funcionando conforme o esperado no ambiente simulado?

🔸**RESPOSTA:**

2. Teste Físico
O mapeamento do ambiente está sendo realizado conforme o algoritmo especificado no ambiente real?

🔸**RESPOSTA:**

A navegação está respondendo corretamente no ambiente real?

🔸**RESPOSTA:**

Os sensores, incluindo câmeras e sensores de distância, estão operando conforme os requisitos no ambiente real?

🔸**RESPOSTA:**

O algoritmo de planejamento de trajetória está gerando trajetórias adequadas no ambiente real controlado?

🔸**RESPOSTA:** 

A detecção de obstáculos está funcionando conforme o esperado no ambiente real controlado?

🔸**RESPOSTA:** 

3. Análise

A simulação no Gazebo foi utilizada para analisar o comportamento do robô em cenários diversos? Descreva o que foi analisado e em quais cenários.

🔸**RESPOSTA:**

Os algoritmos de planejamento de trajetória e mapeamento estão sendo analisados quanto ao desempenho e conformidade com os requisitos? 

🔸**RESPOSTA:**

Descreva as análises realizadas para os algoritmos de planejamento de trajetória.

🔸**RESPOSTA:**

4. Demonstração:
    
Descreva os cenários  de testes das demonstrações para o 2o piso realizada para em ambiente simulado e reais para demonstrar suas capacidades?

🔸**RESPOSTA:**

O robô validou o cumprimento dos requisitos durante a demonstração?

🔸**RESPOSTA:** 



🗒️Observação: Alguns pontos que serão avaliados 

Outputs:
1. Produto Verificado: O robô autônomo passou pelo processo de verificação com sucesso?
2. Resultados da Verificação: Documentos com os resultados dos testes foram elaborados?
3. Relatórios de Discrepância: Foram gerados em caso de áreas onde o robô não atende completamente aos requisitos?
4. Documentação de Verificação:  Todos os documentos para embasamento do processo de verificação, tais como resultados e relatórios, foram inclusos?
5 Decisões sobre Redesign ou Reteste: Decisões foram tomadas pela equipe em caso de discrepâncias significativas?
6. Registro Histórico: Um registro histórico do processo de verificação foi mantido para referências futuras e auditorias?
7. Requisitos Funcionais e de Desempenho: Todos os requisitos funcionais e de desempenho foram verificados conforme especificado?
8 Interfaces: As interfaces relacionadas à navegação e mobilidade foram verificadas?
9. Versionamento de Código: O código foi compartilhado conforme os procedimentos estabelecidos?

```


### Integrantes
- João G. Bortoletto
- Mateus Gava
- Joelmir Teixeira
