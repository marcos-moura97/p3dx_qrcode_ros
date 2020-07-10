# Um robô leitor de código QR no ROS <img src="https://lh3.googleusercontent.com/proxy/sQCSagzVuc1X3_zgLypJlEX_iDNLzb1urNU3lP54BJETeKExkKnuugvMpng6r_ULUjPqgUGKNjHDiqP78PxPzPPEm8maDXc0UOdgAxr-xg" width="40" />

## Visão geral

Este simples projeto usa **[opencv](https://pypi.org/project/opencv-python/)** e **[pyzbar](https://pypi.org/project/pyzbar/)** para simular um robô rastreador de  QR Code. O robô usado, o [P3DX, disponível no ROS](http://wiki.ros.org/Robots/AMR_Pioneer_Compatible), tem uma câmera e um escaneador alaser. Neste projeto, o robô gira em torno do eixo Z até encontrar um QR Code. Ao achar ele para de se mexer e espreve a mensagem no tela e no terminal.

![QR Code readed](/qr_coder/photo_qrcode.png "photo_qrcode.png")
 
O OpenCV é uma biblioteca que ajuda muito o  processamento de imagens. É a mãe do **Pyzbar**, uma biblioteca que pode facilmente identificar, ler e decodificar códigos de barras e códigos QR.

Este projeto é apenas uma forma simples de usar os conceitos de pyzbar para processar alguma mensagem e fazer alguns movimentos. Além disso, no futuro quero usar QR codes para identificar salas para que o robô consiga identificar um local específico sem precisar entrar nele.

## Arquivos principais

### Launch

No arquivo launch é carregado o robô em sua posição inicial no mundo do gazebo. O arquivo que faz isso é qr_coder.launch.

### Mundo

O mundo é o palco em que a simulação opera. É carregado no gazebo. Nesse caso, o mundo carrega um pequeno terreno e uma grande estrutura que
representa uma parede carregada com um QR Code como material.

![Gazebo World](/qr_coder/gazebo_qrcode.png "gazebo_qrcode")

A estrutura e o terreno estão disponíveis no arquivo models.

### Script

O arquivo **qrcoder_p3dx.py** é onde a mágica acontece. Quando está em execução, ele recebe 2 dados importantes do robô.

  - A posição do nó /p3dx/odom, responsável pelo pose, posição e orientação, do robô;
  - A imagem da câmera de /p3dx/front_camera/image_raw, que dá a visão do robô.

Com esses dados, o OpenCV e o Pyzar são usados para verificar se algum QR Code está na imagem. Enquanto não houver QR Code, o
robô vai girar. Quando um QR Code é identificado, o robô para de se mover e a mensagem é decodificada e impressa no terminal e na imagem.

Todo o fluxo de nós e tópicos pode ser visto no **rqt_graph**

![Nodes](/qr_coder/nodes_rqt_graph.png "nodes_rqt_graph")

## Requesitos

  - ROS Melodic
  - Catkin
  - Gazebo
  - OpenCV
  - Pyzbar
  - CV_bridge
  - Numpy
  
## Montar

Você deve fazer no terminal:

- Criar o espaço de trabalho catkin:

``` sh
$ mkdir catkin_ws
$ cd catkin_ws
$ mkdir src
$ catkin_make
```

- Clonar o repositório e construí-lo:

``` sh
$ cd ~ /catkin_ws/src
$ git clone https://github.com/marcos-moura97/p3dx_qrcode_ros.git
$ cd ..
$ catkin_make
```

## Para rodar

Para executar o projeto no gazebo, execute as seguintes etapas:


- Executar o roscore

``` sh
$ cd ~ /catkin_ws/
$ source devel/setup.bash
$ roscore
```

- Lançar o programa

``` sh
$ roslaunch qr_coder qr_coder.launch
```

- Executar o código python

``` sh
$ rosrun qr_coder qrcoder_p3dx.py
```

Como resultado, quando o robô encontra o QR Code, você pode vê-lo na imagem e no terminal.

![Nodes](/qr_coder/photo_qrcode.png "photo_qrcode")

![Nodes](/qr_coder/text.png "text")


# A QR Code reader robot in ROS <img src="https://www.championprofessional.com/wp-content/uploads/2015/07/en-icon.png" width="40" />

## Overview

This simple project uses **[opencv](https://pypi.org/project/opencv-python/)** and **[pyzbar](https://pypi.org/project/pyzbar/)** to simulate a QR Code tracker robot. The robot used, a  [P3DX robot available in ROS](http://wiki.ros.org/Robots/AMR_Pioneer_Compatible),
has a camera and a laser scan. In this project, the robot spin in a base until it find a QR Code. Then, it stop moving and print the message in the
screen and in the terminal

![QR Code readed](/qr_coder/photo_qrcode.png "photo_qrcode.png")
 
OpenCV is a library that helps a lot the process of image processing. It's the mother of **Pyzbar**, a library that can easily identify, read and 
decode barcodes and QR Codes. 

This project is just a simple form to use the concepts of pyzbar to process some message than do some moves. Further, i want to apply some QR Codes t
o identify entries for the robot identify a specific place without have to go inside of it.

## Main Files

### Launch

In the launch file is loaded the robot in it's initial position in gazebo's world. The file that make this is qr_coder.launch.

### World

The world is the stage on which the simulation operates. It is loaded in gazebo. In this case, the world loads a small ground and a big structure that
represents a wall loaded with a QR Code as it's material.

![Gazebo World](/qr_coder/gazebo_qrcode.png "gazebo_qrcode")

The structure and the ground are available in models file.

### Script

The **qrcoder_p3dx.py** file is where the magic happens. When it's running, it recieves 2 important data from the robot. 

  - The position from node /p3dx/odom, responsible for the pose, position and orientation, of the robot;
  - The image of the camera from /p3dx/front_camera/image_raw, that gives the vision of the robot.

With these data,the OpenCV and Pyzar are used for check if some QR Code is in the image. While there are no QR Code, the
robot will spin. When a QR Code is identified, the robot stop moving and the message is decoded and printed both in the 
terminal and in the image.

All the flow of nodes and topics can be seen in the **rqt_graph**

![Nodes](/qr_coder/nodes_rqt_graph.png "nodes_rqt_graph")

## Dependencies

  - ROS Melodic
  - Catkin
  - Gazebo
  - OpenCV
  - Pyzbar
  - CV_bridge
  - Numpy
  
## To build

You must follow in terminal:

- Create the catkin workspace:

```sh
$ mkdir catkin_ws
$ cd catkin_ws
$ mkdir src
$ catkin_make
```

- Cloning the repository and building:

```sh
$ cd ~/catkin_ws/src
$ git clone https://github.com/marcos-moura97/p3dx_qrcode_ros.git
$ cd ..
$ catkin_make
```

## To Run

To run the project in gazebo, execute the following steps:


- Running roscore

```sh
$ cd ~/catkin_ws/
$ source devel/setup.bash
$ roscore
```

- Launching the program

```sh
$ roslaunch qr_coder qr_coder.launch
```

- Running the python code

```sh
$ rosrun qr_coder qrcoder_p3dx.py
```

As result, when the robot find the QR Code, you can see it in the image and in terminal.

![Nodes](/qr_coder/photo_qrcode.png "photo_qrcode")

![Nodes](/qr_coder/text.png "text")
