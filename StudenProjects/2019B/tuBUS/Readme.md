# U.I TU BUS

This project presents an initiative to solve a problem in the public transport of our city. With this system you can make payments by passing a smart card, through a reader, these make the discount and play an audio with the balance. Once the cost of the ticket exceeds the balance, issued an alert, "insufficient balance". To recharge the card you have an online page. Here are the options to: search, register, modify, delete or reload a user. All information is stored in a database in "MySQL". In addition, the page will have a button where you will send an email with the balance collected due to refills. 
In addition, the system contacts the sensors that record the number of users entering or leaving through each of the doors and emitting an alert when someone enters through the back door (a "colado"), as well as sending an automatic mail to certain time with the information of how many people entered, left and sneaked into the bus.

This repository contents:
  - Source codes
  - libraries to use 
# Hardware requirements:
- Raspberry PI 2/3 (x1)
- Arduino nano (x3)
- RFID Reader / Writer Kit (x2)
- Rfid card (x3)
- Laser (x4)
- Laser receptor(x4)
- Leds (x3)
- Bluetooth speaker
- Push buttons(x2)
- Resistors 
- 5v/3A adapter (x1)
- 12v/1A adapter (x1)
- MicroSD 16 GB
# Software Requirements:

- Ubiquity OS
- Python 3
- Phpmyadmin
- Arduino IDE
- Atom
- Filezilla.
# Pasos para instalar O.S y bibliotecas:
#### Installation Rasbian O.S
- It is essential that you have the Ubuntu Operating System, visit this [web page] for installation.
- To format your MicroSD card install this [program].
- To flash your MicroSD, download this [program.]

#### Libraries
Now is important install this libraries in Rasberry

```sh
$ Ctrl + T
$ sudo apt-get update
$ sudo apt/get upgrade
$ sudo apt-get install python-serial 
$ sudo apt-get install python-datetime 
$ sudo apt-get install python-requests
$ pip install Flask
$ pip install pyttsx3
$ sudo apt-get install espeak
```
### How to execute code to pay an sensors

To execute the codes in raspberry, a connection command must be executed with this establishing the communication between a PC and the Ras. From this way it is not necessary to connect the peripherals to this one and still be able to execute codes. The codes are edited on PC and then transferred to the "Ras" for execution. The transfer is done by filezilla.

##### to establishing the communication
Execute:
```sh
$ Ctrl + T
$ ssh pi@172.17.92.127 (pi=name_ras, 172.17.92.127= ip_ras)
```
once connected ras will ask for the password
```sh
$ tubus
```
At this moment everything that runs will run in the Ras. The codes are transferred. To know how this tutorial [explains]

## configure ports 
To configure the ports for every code, execute 
```sh
$ ls /dev/tty*
```
Then open every code to configurate the port:
```sh
$ nano tubusbus2pago.py
$ nano tubusbus2pago.py
```
In the line 
```sh
   ...=serial.Serial('/dev/ttyUSB0', 9600)
```
Change ...ttyUSB' for the USB# in port

Find the folder where the codes:
```sh
$ cd/.../.../
$ cd Tubus
$ cd src
```
Run the code to pay:
```sh
$ python3 tubusbus2pago.py
```
And run the code to sensors

```sh
$ python3 tubusbus2pago.py
```
### How to execute code to refills

to execute code: 

```sh
$ Ctrl + T
$ cd/.../.../
$ cd Tubus
$ cd src
```
Run the code to web page:
```sh
$ python3 index.py
```
In the terminal the url appears where the page is running, we click and it will open. 
Verify the deployment by navigating to your server address in your preferred browser.
```sh
Usually is http://127.0.0.1:3000/
```
#### Universidad de Ibagué
#### Programa de Ingeniería Electrónica
#### Electrónica Digital III 2019B
Authors:
- Nestor Duvan Rivera Nuñez
- Gildardo Hernandez Palma
- Juan Camilo Ferreira Rodriguez
Tutor:
[Harold Murcia] 


   [web page]: <https://downloads.ubiquityrobotics.com/pi.html>
   
   [program]: <https://www.raspberrypi.org/downloads/raspbian/>
   [program.]: <https://www.balena.io/etcher>
   [explains]: <https://www.youtube.com/watch?v=073kWNi3s8g>
   [Harold Murcia]: <http://haroldmurcia.com/>
 
