#AQUAPY
This project was made with the aim of optimizing the time that people invest in the care of their fish without losing the autonomy they have on their tanks, that's why we designed an intelligent aquarium whose function is to ensure the right conditions for the proper development of their pets This is a project for the subject of digital electronics 3 semester 2019B of the university of ibague 

##Hardware Requirements:
Raspberry Pi 3 b+
MicroSD 16 GB
Module of relay of 4 calanes to 5 volts
bnc PH probe
bnc connector
Module temperature ref:ds18b20
ultrasonic sensor ref: HC-SR04
LED strip rgb 12v
motor pump 200L/h
Arduino ONE
   
##Software Requeriments
   - Raspbyan
   - python 3
   - pandas
   - sockets
   - netifaces
- flask
- multiprocess
- multipart
- SMTPLib


## Steps to install o.s and libraries:

###installation raspbian 
go to the official raspbian [web](https://www.raspberrypi.org/downloads/) site and download either the image of the operating system or Noobs, proceed to download extract them and move them to microSD to finally insert it to the raspberry where when turned on will proceed to install the raspbian.


###Libraries
after having installed raspian is necessary to update our repository of libraries and update them, for that, open the terminal ctrl +alt+t and write
sudo apt-get update
sudo apt/get upgrade


####pandas
we need to install pandas because there we will be uploading and updating our values entered on the page to then be called from the pickup where the sensors are to install we execute the following instruction from the terminal
$ip install pandas

####multipart
for our alert messages was required to send alarm emails to python users is why it was necessary to install this library
$pip install python-multipart

####sockets
to send emails was also necessary the installation of this library
pip install sockets

####flask
This library was one of the most important and thanks to this was able to create the website of the aquarium with its different routes where the user will have power to manage their fish tank as you want.
pip install Flask

You may need to be an administrator for the installation. In that case run:

sudo pip install Flask

####multiprocceses
the use of this library was required because during the construction of the source code arose the need to perform 3 processes in parallel.
pip install multiprocces

####request
for this project was required to send and receive data so we used this library
$pip install request

####MTPLib
was installed as it is essential when sending emails.
$pip install smptlib

####Netifaces
This library was used to acquire web addresses.

$pip install netifaces


##How to run
from the terminal open a single file that will run all the source code this due to the multiproccesing library that allowed us to run several functions in parallel in a single file.
$ /../../src/curso4.py


Universidad de Ibagué
Programa de Ingeniería Electrónica
Electrónica Digital III 2019B
##authors

  - Michelle Fernanda Bonilla Castro
  - Daniel Bejarano Vega
  - Miguel Angel Murillo C.

##Tutor

 [Harol F murcia](http://haroldmurcia.com/) 


***
Visit the YouTube channel to see the video of the project and future improvements of [here](https://www.youtube.com/watch?v=0-knqD2kovI).
***

