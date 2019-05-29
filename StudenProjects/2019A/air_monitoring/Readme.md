# MOBILE STATION FOR AIR QUALITY MONITORING

This project presets an initiative to solve a measurement problem in our city. In this case, our interest is to obtain  indicators to evaluate the air quality at different moments and in different places of Ibague, Colombia. This work is part of our project for the course: Electrónica Digital III 2019A at Universidad de Ibagué.


##

## Hardware Requirements:
 * Raspberry Pi 3 b+
 * MicroSD 16 GB
 * Module sensor CO Ref: MQ7 
 * Module sensor air quality Ref: MQ135
 * Module temperature and humidity Ref: DHT11
 * Module GPS Ref: NEO-6M
 * Module converter USB-TTL Ref: FTDI
 * Arduino UNO
 
## Software Requirements:
 * Ubiquity OS
 * Python 3
 * Excel
 * NMEA

#

## Steps to install O.S and libraries:
#
#### Installation Ubiquiti O.S

- It is essential that you have the Ubuntu Operating System, visit this [web page](https://downloads.ubiquityrobotics.com/pi.html) for installation.

- To format your MicroSD card install this [program](https://www.sdcard.org/downloads/formatter/eula_windows/index.html).

- To flash your MicroSD, download this [program](https://www.balena.io/etcher).
 
##

#### Libraries
Once you have Ubiquiti on your Raspberry Pi, it is necessary to install and update the libraries.

```sh
$ Ctrl + T
$ sudo apt-get update
$ sudo apt/get upgrade
```

Install Excel in Ubiquiti:

```sh
$ Ctrl + T
$ sudo apt-get install python-xlwt
```

Library to modify files in Excel:

```sh
$ Ctrl + T
$ pip install xlwt
```

Install library NMEA:
```sh
$ Ctrl + T
$ pip install pynmea2
```

### How to execute:
The Raspberry Pi and Ubiquiti have their own network, which allows connecting to another computer through SSH, as well, to exercise the programs and have a preview of what is being done. On a Pi3, the image comes up as a Wifi access point. The SSID is ubiquityrobotXXXX where XXXX is part of the MAC address. The wifi password of R.A.S is: robotseverywhere.

Commands:

```sh
$ Ctrl + T
$ ssh ubuntu@ip
Password:
$ robotseverywhere
```

Find the folder where the codes:

```sh
$ Ctrl + T
$ cd/.../.../
$ cd air_monitoring
$ cd src
```

Run the program arduino

```sh
$ Ctrl + T
$ python arduino.py
```

This program will open a node with four topics: humidity, temperature, air, monoxide.

Open another terminal to run the "lugar" node, which will take the GPS sensor data and create another node with two different topics: Longitude and Latitude.

```sh
$ Ctrl + Shift + T
$ python lugar.py
```

See that the GPS module is sending data to run this program to avoid problems.

Finally, in another terminal, execute the program "datos" which will subscribe to all the topics and create a database, which will be stored in the folder .../gps_movil/data in a .txt file.

```sh
$ Ctrl + Shift + T
$ python datos.py
```

Ready, the programs are already in the Raspberry Pi sensad and obtaining the variables, which is ready to take data by the route that is traveled in the city.

At the end of the tour, a document readable by Google Maps must be generated, the program that allows making this process is "convertidor", the one that runs:

```sh
$ Ctrl + T
$ python convertidor.py
```

The program will generate an Excel sheet, which is saved in the "datos" folder, which is now understandable for Google Maps and it allows graphing the route carried out together with the sensed variables.

#
***
#
#### Universidad de Ibagué
#### Programa de Ingeniería Electrónica
#### Electrónica Digital III 2019A

### Authors:
  - Juan Camilo Sandoval Salguero
  - Thomás Sebastián Bolaños Muñoz
  - Juan Camilo Saiz San Juan
  - Juan David Rodríguez Cerón

### Tutor:
  - [Harold F. Murcia](http://haroldmurcia.com/) 

***

***
Visit the YouTube channel to see the video of the project and future improvements of [MOBILE STATION FOR AIR QUALITY MONITORING - IoT](https://www.youtube.com/channel/UC0cMiU3eNB0K3zbbPz0Uesg/featured?view_as=subscriber).
***