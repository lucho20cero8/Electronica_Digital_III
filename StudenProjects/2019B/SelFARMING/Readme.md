# SelFARMING
To solve the problem, it is decided to create a system in which the crops can be automated through 3 types of sensors (inputs) and 2 actuators (outputs). The sensors send data for which, by means of the codes explained in the following file, the actuators can be activated or deactivated as needed by the plant. This system seeks to reduce the face-to-face attention necessary for the care and proper growth of a plant, whether decorative or food. This system was implemented in a vertical crop because this type of distribution facilitates the automation of the aforementioned.

# Hardware Requirements:
- YL-69 soil moisture sensor
- 2 Water level float sensors
- BH1750 light sensor https://www.alldatasheet.com/datasheet-pdf/pdf/350139/ROHM/BH1750FVI.html
- Stepper motor 28BYJ-48 https://datasheetspdf.com/pdf-file/1167006/Purelogic/28BYJ-48/1
- ULN2003 module https://www.alldatasheet.com/datasheet-pdf/pdf/25575/STMICROELECTRONICS/ULN2003.html
- Raspberry Pi 3B https://www.raspberrypi.org/products/
- Arduino Nano https://www.arduino.cc/en/Main/Products

# Software Requirements:
- Raspbian
- ARDUINO IDE
- Python
- Ubuntu 18.04

# How to install the libraries?
```sh
- pip install stmplib
- pip install ssh
- pip install flask
- pip install pandas
- pip install netifaces
- pip install serial
- pip install urllib2
- pip install python3
```
These libraries are required for the correct operation of all the code, in their corresponding order, each one serves to establish communication correctly with GMAIL, or to be able to remotely access another terminal, create pages on the internet, save and read data, establish an email via GMAIL, communication with Arduino and running the files with the new version of Python

# Connection with Raspberry
For the correct connection with the Raspberry Pi 3B, it is first necessary to install the operating system in an SD which will be inserted in the aforementioned card. After this we must enable ssh to control the terminal of this through another computer
```sh
ssh pi@172.17.92.133
```
Being 172.17.92.133 the IP that our Raspberry has, this command is written on the computer that will control the raspberry

# How to run the code?

The system has two main codes in which the actions will be executed as certain actions are loaned, in order to automate the cultivation of the plant, which can be found in the SelFARMING folder located on the Raspberry Desktop.

The first of the two already mentioned is called "pagina.py", to access it we need to type in the terminal the following command
```sh
cd Desktop/SelFARMING/python page.py
```
It is recommended to run the programs separately before running them both in parallel. For this code, libraries such as Serial, pandas and RPi.GPIO are used (available only in Raspberry)
```sh
import RPi.GPIO as GPIO
import serial
import pandas as pd
```
A variable is created in which the communication with the arduino nano is established
```sh
arduino = serial.Serial ("/dev/ttyUSB0", baudrate = 9600)
```
After this, the output pin that will be used on the Rasberry (it controlls the pump) is established
```sh
GPIO.stewarnings (False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup (7, GPIO.OUT)
```
Variables and entries for the code are established. This is communicated with a page previously created with Flask
```sh
email = ""
mode = ""
estRiego = ""
estCubierta = ""
lmin = 0
lmax = 0
hmin = 0
hmax = 0
```
These variables are the ones that automatically set the program in "manual" mode in the options menu of the main page. After this process, the personalized messages are defined, which will change content according to the data thrown by the different sensors and actuators
```sh
def datos ()
```
The next step is to add the actions that each button of the "Manual" mode will perform, by means of conditionals it is ordered to activate or deactivate the actuators (stepper motor or motor pump)
```sh
if opcion == "activado":
elif opcion == "desactivado":
if opcion == "plegada":
elif opcion == "desplegada":
```
Finally, the global variables of humidity and maximum and minimum light will be defined
```sh
def limites ():
```
For the second main code (sensors.py) it is required to import libraries such as urllib2, serial, smtplib, netifaces in addition to pandas and GPIO
```sh
import urllib2, serial, time, smtplib, netifaces, pandas as pd, RPi.GPIO as GPIO
```
As in the previous code, the communication between arduino and python has to be established in one variable and in another the ThingSpeak link is established, which saves the graphics provided by the sensors
```sh
arduino = serial.Serial ("/dev/ttyUSB0",baudrate = 9600)
direccion = (ThingSpeak address)
```
Again, variables, flags are set and you are ordered to output a Raspberry pin
```sh
mode = "automatico"
bdCorreo = 0
usPromL = 0
usPromH = 0.0
contador = 0

GPIO.setwarnings (False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup (7, GPIO.OUT)
```
A method is defined which will provide the data taken by the sensors to thingSpeak so that it can graph their values. In addition, initial variables are defined for the automatic mode, in addition to the conditions for sending the respective messages via GMAIL, these emails will be personalized, since they will have the levels set by the user, then they will change according to your opinion. In addition, preliminary messages are set in the "automatic" mode for when the user has not set all the required parameters.
Finally, the mail route is established and you are given the relevant permissions to interact with GMAIL, in addition to defining an infinite loop so that you can keep taking samples of the sensors via Arduino
```sh
while 1:
```
Finally, both codes must be run in parallel if the correct functioning of the page and system is sought
```sh
python sensoress.py & python pagina.py
```
Finally, it is recommended to load the preset code in the arduino for the step motor, which works by means of conditionals in which they activate the object in one direction or another as they fulfill their sentence.

# YouTUBE

Explanatory video of the project on the youtube platform: https://www.youtube.com/watch?v=6eAcHAibcwQ&feature=youtu.be 

# Authors

Sofia Luisa Carolina Bonilla Beltrán

Juan Fernando Ardila Duque

Miguel Angel Gonzalez Flórez


# Tutor
[Harold F Murcia](www.haroldmurcia.com)


***
Visit the YouTube channel to see the video of the project and future improvements of [here](https://www.youtube.com/watch?v=f434fJBXz5Y&t=1s).
***

