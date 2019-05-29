# SinglePot
SinglePot is a project that link Python-ROS-Raspberry-Arduino-IoT which storage information in a .txt file and control soil moisture in a planbt.
This reposity contents:
  - data
  - source code (Python|ROS|Arduino)

### Hardware elements
  - Raspberry Pi B+
  - Arduino
  - DS18B20 - Temperature sensor
  - DHT22 - Temperature-humidity sensor
  - FC-28 - Soil moisture sensor
  - GY-30 - Lighting sensor
  
### Software requirements
  - Ubiquity Robotics [Operative System](https://downloads.ubiquityrobotics.com/)
  - Python 2.7.16
  - ROS Kinetic

## Installation
The installation process consists of installing the necessary programs and libraries.

### Install-Lib Python
Extra libraries for the codes
```
$ sudo apt-get install python-request
```
### Programs to install
```
$ pip install Flask
```
### ROS installing
Installing ROS Kinetic on the Raspberry Pi, the steps are explained in:
 * See [Ros Kinetic](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi)
 
### Folders in the repository

| /your_root | - path |
|-|-
| - - src | / source code
| - - data| / report + experimental data
| Readme.md

### Configuration and execution
6 codes are executed at the same time:
```
$ roscore
$ python /src/nodoserial.py
$ python /src/pagina.py
$ python /src/nodocontrol.py
$ python /src/nodorele.py
$ python /src/nododatos.py
```

### Authors:
Universidad de Ibagué
Programa de Electrónica
Electrónica Digital III - 2019A
 * Oscar Rodriguez  - [2420162008@estudiantesunibague.edu.co](mailto:2420162008@estudiantesunibague.edu.co)
 * Santiago Ariza - [2420161008@estudiantesunibague.edu.co](mailto:2420161008@estudiantesunibague.edu.co)
 * Francisco Franco - [2420171077@estudiantesunibague.edu.co](mailto:2420171077@estudiantesunibague.edu.co)
 * Prof. Harold Murcia - [Web page](http://haroldmurcia.com/)
