# tuParqueadero

The system TuParqueadero consists of the installation of an intelligent parking with capacity for 50 vehicles that will inform in advance the availability of free places to park via a free web platform called ThingSpeak. This purpose will be achieved through a network of ultrasound sensors that will detect the presence of the vehicle at the entrance of the parking area, whose data will be received by an Arduino uno, which with the help of RaspBerry Pi3 will be responsible for processing the information and send it to the cloud, internet, where users can find out about available spaces through the aforementioned route. In this way it is possible for drivers to spend the least amount of time possible while waiting for a parking place.

 * [YouTube video](https://www.youtube.com/watch?v=vQ7cdZmJis8&feature=youtu.be).

## Hardware Requirements:
For the implementation of our system is necessary to have a Raspberry pi 3, arduino uno, 16x2 lcd screen and HC-SR04 sensors, after this follow the next steps

## Software Requirements:
 * As a first step you need to install Ubiquity operating system following the link:
https://downloads.ubiquityrobotics.com/pi.html.

 * After the ubiquity installation is necessary to install some "python libraries" that will help us to make the functioning of our system effective.

 * For the operation of the LCD we will go to a tutorial where they will indicate how to configure the lcd to make it work together with the Raspberry pi 3 : https://www.youtube.com/watch?v=fR5XhHYzUK0 - Website


The Raspberry Pi allows you to connect to another computer by using SSH, in order to have a preview of what is being done. In a Pi3, the SSID (Service Set Identifier) ​​is ubiquityrobot "XXXX" where XXXX is the address and the wifi password is: robotseverywhere.

To be able to visualize it, the following commands must be exercised:

- Ctrl + T
- ssh ubuntu @ ip
- robotseverywhere -- Password

### How to run:
In terminal:
```sh
cd /yourRoot
cd /tuParqueadero
ls # to visualize the files of our system
```
We will find 5 nodes necessary for the operation which are:
-  Lectura - Take the data from the arduino and send it as topics to the Rosmaster
-  Logical - It has all the logic of the system
-  Pagina - Take the data produced by the "Logical" and upload it to the ThingSpeak
-  LCD - Take data data from "Logical" and display it on our LCD
-  Load - Take the data and store it in a .Txt file as a database backup.

To access each node you must compile with a specific order and also follow the following instructions:
```sh
python lectura.py # the reading node will open
Ctrl T # Open another terminal
python Logical.py
Ctrl T # Open another terminal
python LCD.py
Ctrl T # Open another terminal
python Pagina.py
Ctrl T # Open another terminal
python Load.py
```

Finally we can see the data that is being uploaded to Thing Speak through the assigned link:

https://thingspeak.com/channels/781069 - Website
***
### Authors:
**Universidad de Ibagué** - **Programa de Electrónica**
**Asignatura: Electrónica Digital III 2019A**

 * Julian Felipe Montaña Aguilar
 * Luis Alberto Echeverry Henao
 * Angela Maria Moncaleano
 * [Harold F MURCIA](www.haroldmurcia.com) - Tutor
***
