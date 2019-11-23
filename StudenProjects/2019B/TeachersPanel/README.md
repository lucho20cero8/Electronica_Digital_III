# TEACHER´S PANEL
A repository for a attention panel of students to help communicate with teachers in counseling schedule.
* Watch the Youtube video :
# This repository contents:

* Source code
* Data files
* Dev script

# **Hardward Requirements:**

* A Raspberry py 3 [https://www.raspberrypi.org/products/raspberry-pi-3-model-b/]
* 2 module Nodemcu ESP8266 [https://naylampmechatronics.com/espressif-esp/153-nodemcu-esp8266.html]
* A Touch screen 3.5" for raspberry py 3 [http://www.lcdwiki.com/3.5inch_RPi_Display]
* A servomotor to 5V [http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf]

# **Software Requirements:**

* Ubuntu 16.04
* Python 2.7 necessary libraries(mqtt,flask,xlrd)
* Arduino IDE
# **How to install**

It´s neccesary to install the libraries as follows

* To install mqtt:
``` sh 
sudo apt install -y mosquitto mosquitto-clients 
```
This library is needed because it is a lightweight open network protocol that usually runs over tcp / ip which allows sending and receiving data via Wi-Fi and is perfect for IoT applications.

* to install paho-mqtt
``` sh 
pip install paho-mqtt
```
that library helps to implement versions 3.1 and 3.1.1 of the MQTT protocol.
* to install fask: 
``` sh 
sudo pip install flask
```
This library is where you can use the rasberry pi 3 to host the website i.e, the server where all the information will go.

* to install xlrd: 
``` sh
pip install xlrd"
```
With this library you will be able to link the excel documents with the website and thus be able to read the information files that will be run.

# Connection between the rasberry pi to touch screen 3.5" 

Usually when you use the rasberry pi you connect way to hdmi with a monitor. In this case, you use a touch screen 3.5" directly connect to raspberry pinout, so you need to put some commands:
``` sh
sudo rm -rf LCD-show 

git clone https://github.com/goodtft/LCD-show.git 

chmod -R 755 LCD-show 

cd LCD-show/

sudo ./LCD35-show
```
In the last line this 35 indicates the size of touch screen that is so important because if you will to work with another touch screen, you will need another commands.

If you want to come back to work since the monitor , just need to put the next commands in the terminal.

``` sh
chmod -R 755 LCD-show 

cd LCD-show/ 


sudo ./LCD-hdmi 
```
# Programming of Nodemcu ESP8266
In firts time you need to install a library into arduino IDE

file is opened then preferences and enter 
``` sh
https://arduino.esp8266.com/stable/package_esp8266com_index.json
```
into the Additional Board Manager URLs field. You can add multiple URLs, separating them with commas.
next to go to the card manager and the search engine write " esp8266"  and select "esp0266 community" then tool plate and select generic esp8266 module the flash size is set to " 4M (1M SPIFFS) " and "upload speed: 115200" and the serial port is configured.

# **How to RUN**

The first thing is to create a folder to deposit all the necessary files
``` sh
cd
cd Desktop/
mkdir web
cd web/
```
Now, the files "app.py, Timetables.xlsx" are copied into this folder and the templates folder is created "
``` sh
mkdir templates
```
the files "main.html and schedules.html" are copied into the templates folder

# **University of Ibague**
Programa de Ingeniería Electrónica
Electrónica Digital III 2019B
Authors:
  - Julian David Alcala Forero
  - Jhon Faver Mendoza 
  - Juan Camilo Leon Martinez
  
# Tutor
[Harold F Murcia](www.haroldmurcia.com)


***
Visit the YouTube channel to see the video of the project and future improvements of [here](https://www.youtube.com/watch?time_continue=1&v=uIdCQleRSG4&feature=emb_logo).
***
