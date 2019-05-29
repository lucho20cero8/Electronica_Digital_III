# Remote robot:  Roberto Explora.
___

Roberto Explora, will be an ideal assistant, because its small size will allow to navigate places with difficult access. Also, its wireless connection, through IoT, will help monitor, store and display different variables such as temperature, relative humidity, distance between obstacles and send images of the environment in real time.



This repository contents:
  - Source codes.
  - Hardware requirements
  - Software Requeriments
  - Installation
  - Repository Folders
  - Authors
  
## Hardware requirements:
  - Raspberry PI B
  - 4 x Motor DC - TGP01D-A130
  - 4 x Tires for DC Motor
  - Mechanical structure
  - 2 x Arduino Uno
  - Jumpers
  - 6 x While LED'S
  - USB Camera
  - Driver L298N
  - RPI Power Pack V1.1 - 3800 mAh - 3.7V
  - Switch
  - Xbox Controller
  - Sensor Ultrasonic HC-SR04
  - Sensor DTH11, temperature and humidity sensor
  - High discharge LI-PO Battery 1600 mAh
  
## Software Requeriments:
  - Ubiquity Robotics V.2019-02-19-ubiquity-xenial-lxde 
  - Motion [Motion](https://motion-project.github.io/)
  - Python 2.7.15, *numpy, scipy, rospy
  - ROS kinetic

# Installation
___
Roberto Explora requires [Motion](https://motion-project.github.io/).

##### Install Motion
#
~~~
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install motion
~~~

The file motion.config must be replaced by another file, which we find in the src folder

# Repository Folders
___
#
#### PC code
#
~~~
 Client_ButtonA.py
 Client_JY.py
 Client_JX.py
 Listener_ButtonA.py
 Listener_JY.py
 Listener_JX.py
~~~
#
#### Raspberry code
#
~~~
Server1.py
Server2.py
Server3.py
List_Mot.py
Arduino.py
List_But_A.py
TalkerTempHumUltra.py
ThignSpeak.py
Motion.config
~~~

# Authors:
**Universidad de Ibagué**
**Programa de Electrónica**
**Asignatura Electrónica Digital III 2019A**

___
  - [Jean Carlo Garcia Alfonso](mailto:2420161033@estudiantesunibague.edu.co)
  - [Laura Camila Pizza Vargas](mailto:2420161021@estudiantesunibague.edu.co)
  - [Camila Andrea Duran Varon](mailto:2420171076@estudiantesunibague.edu.co)
  - [Harold F MURCIA](www.haroldmurcia.com) - Tutor
***