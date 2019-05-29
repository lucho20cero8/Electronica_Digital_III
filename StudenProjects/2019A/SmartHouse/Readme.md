# Smart House
A repository for a smart house. For this project we opted for a low cost implementation method because the sensors used are economical and an automatic action was developed under certain conditions, as the sensors read the same way you can add a system of Monitoring of what is happening inside the home, thanks to the monitoring of sensors that in turn are handled wirelessly through a mobile device in which it is ordered to meet the respective requirements such as the temperature of a room, Control of access to the home and lighting of the zones of that place.

This repository contents:
 * Source codes
 * Dev scripts(Python|ROS)

## Hardware requirements:
- [Raspberry PI 2/3](didacticaselectronicas.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=118&virtuemart_product_id=3675&Itemid=101) (x1)
- [Arduino uno R3](https://didacticaselectronicas.com/index.php/sistemas-de-desarrollo/arduino/arduino-2/arduino-uno-smd-rev-3-original-italiano-a000073-detail) (x1)
- [Card with 8 opto-coupled relays 5V](https://didacticaselectronicas.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=542&virtuemart_product_id=1991&Itemid=101) (x1)
- [Flame sensor](www.fdfgdf) (x3) 
- [Photoresist](https://didacticaselectronicas.com/index.php/componentes-pasivos/fotorresistencias/fotorresistencia-ldr-5mm-fotoresistor-fotorresistor-ldr-sensor-de-luz-detail) (x6)
- [Laser](https://didacticaselectronicas.com/index.php/sensores/luz/laser-rojo-650nm-5mw-laser-650nm-5mw-detail) (x6)
- [Dupont wire (M/H (30cm), M/H (30cm))](https://didacticaselectronicas.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=286&virtuemart_product_id=1850&Itemid=101)
- [Borneras](https://didacticaselectronicas.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=60&virtuemart_product_id=5141&Itemid=101) (x6)
- [Separator kit](https://didacticaselectronicas.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=341&virtuemart_product_id=1652&Itemid=101) (x10)
- [RFID Reader / Writer Kit](https://didacticaselectronicas.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=151&virtuemart_product_id=2910&Itemid=101) (x1)
- [Buzzer](https://didacticaselectronicas.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=409&virtuemart_product_id=3479&Itemid=101) (x1)
- [PCB universal 9*15cm](https://didacticaselectronicas.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=505&virtuemart_product_id=1208&Itemid=101) (x1)
- [5v/3A adapter](https://didacticaselectronicas.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=118&virtuemart_product_id=3675&Itemid=101) (x1)
- [12v/1A adapter](https://didacticaselectronicas.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=118&virtuemart_product_id=6379&Itemid=101) (x1)
- [AWG Wire](https://didacticaselectronicas.com/index.php/cables/otros-cables/cable-awg12-rojo-flexible-siliconado-batería-dron-rc-cabflex-12awg-r-detail) (20m)
- [Servomotor FS90MG](https://didacticaselectronicas.com/index.php/robotica/ruedas-1/kit-rueda-y-servomotor-fs90r-kit-rueda-servo-rotación-continua-detail) (x1)
- [Temperature sensor DS18B20](https://didacticaselectronicas.com/index.php/sensores/temperatura/m%C3%B3dulo-sensor-de-temperatura-ds18b20-sen-18b20-eco-detail) (x1)
- Lamp (x3)

## Software requirements:
  - Python 2.7, *serial, std_msgs.msg, rospy, datetime, RPi.GPIO, requests, SimpleHTTPServer
  - ROS kinetic 1.12.13
  - Ubiquity robotics OS
  - MIT App Inventor
  
## Installing:

`sudo apt-get install python-serial`
`sudo apt-get install python-datetime`
`sudo apt-get install python-requests`

## ROS Installing
For ROS installing you must follow the next steps:
* http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi

## Repository Folders
```
|--src         / scripts used in the project
|--data        / txt for the information of the sensors
```
## How to config?
### Arduino:
In the `src` folder you can find `proyecto.ino` in this script, you have to config the RFID cards that are authorized and calibrate the photoresistors.
```sh
byte Usuario1[4]= {0x61, 0xC5, 0xE3, 0x73} ;    // UID de tarjeta leido en programa 1
byte Usuario2[4]= {0xB6, 0xD5, 0xE6, 0x1F} ;    // UID de llavero leido en programa 1
```
You can see in the script this lines, you can run the MFRC522 `DumpInfo` example and see what UID has your card, copy that UID and put it in the script. 
```sh
if(valorLDR0<100 && valorLDR1>100)
  {
    contador1++;
  }
```
For photoresist's calibration you can use serial print to see the analog read from photoresist and calibrate it, when the laser is shining or not the photoresist and modifying `600` for the number you sensing.

### Raspberry:

```sh
Arduino=serial.Serial("/dev/ttyACM0",baudrate=9600,timeout=5) 
```
don't forget that the arduino's baudrate and the node arduino's baudrate are the same and config the usb port that you are using.
```sh
f = open('/home/ubuntu/Desktop/cajanegra/texto','a')
```
At the node 'cajanegra.py' you can config the txt's directory.
```sh
RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field1=0'
```
At the node 'thingspeak.py' you can put your API Key from thingspeak, copy the 'Update a Channel Feed' link and you can config the fields.
```sh
RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field1=0'
RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field2=0'
...
```
At the node 'usuario.py' you have to config your IP address and your port. Don't forget to config the same IP and port in the App Inventor on the smartphone.
```sh
server_address_httpd = ('192.168.0.104',8080)
```
## How to run:
```sh
python /yourRoot/src/arduino.py
python /yourRoot/src/cajanegra.py
python /yourRoot/src/thingspeak.py
python /yourRoot/src/usuario.py
python /yourRoot/src/control.py
```
***
### Authors:
**Universidad de Ibagué**
**Programa de Electrónica**
**Asignatura: Electrónica Digital III A2019**

* [Daniel Flórez Mendez](mailto:2420152008@estudiantesunibague.edu.co)
* [Miguel Antonio Villa](mailto:2420131033@estudiantesunibague.edu.co)
* [Andres Camilo Moncaleano](mailto:2420161014@estudiantesunibague.edu.co)
* [Harold F MURCIA](www.haroldmurcia.com) - Tutor
***