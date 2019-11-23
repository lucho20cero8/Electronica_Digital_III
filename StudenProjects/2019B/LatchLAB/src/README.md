# Desbloqueo automatico y manual de los laboratorios


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Es un proyecto el cual  un problema bastante común en los laboratoios de la universidad de ibague con el se podría ayudar a los encargados de los laboratorios en su labores.
# Breve Explicación de Funcionamiento

El sistema fue diseñado con el fin de poder acceder de manera automática en las horas de clases, además de poder desbloquear los laboratorios de manera manual sin necesidad de ir hasta algún laboratorio. También se implemento una función en laboratorios especiales la cual restringe el acceso para que solo personas autorizadas en ciertos horarios puedan acceder alos mismos.

# Harware

El harware que se usó para poder recrear este sistema fue:
* Una raspberry Pi Zero W
* Un arduino ESP8266
* Un arduino UNO
* Un servo-motor (arduino)

# Software
El sofware que se implementó fue un conjunto de librerias que en su gran mayoria ya se ecuentran instaladas en ubuntu.
```sh
-Ubuntu
-Python 3
-Socket Library
-Flask
-Html
-Css
-MySQL
-Arduino
-start_new_thread() from Thread Library
```

# ¿Como instalar programas necesario para este proyecto?

Primero que todo se tiene que tener ubuntu instalado dado que fue en el sistema operativo que se trabajo.
**Python3**
Lo siguiente se intala para poder instalar los diferentes paquetes en python 3
```sh
sudo apt install pip3
```
**Flask**
```sh
sudo pip3 install flask
```
**Socket**
No es necesario mencionar la instalación de esto debido a que ya se encuentra instalado por defecto.

**MySQL**

Este se puede instalar de diferentes maneras pero por comodidad se instaló desde la web con un programa paquete XAMPP que es el que nos ayudara con nuestra base de datos.
https://www.apachefriends.org/es/index.html

**Arduino**

Este es otro programa que se puede descargar desde la web facilmente yendo a la página oficial de Arduino IDE. https://www.arduino.cc/en/Main/Software

# ¿Como usar este proyecto?

En este repositorio existe una carpeta llamada arduino allí se encuentran los codigos que se necesitan para programar en cada uno de los arduinos mencionados anteriormente. El archivo en Wifiblink es para el modulo y el que se encuentra guardado en nfc es para el arduino Uno.

Es simple el uso de esta proyecto debido a que solo hay iniciar la página, pero el dispositivo donde se vaya a correr la página tiene que tener comunicación Serial con el Arduino uno, Además que se tiene que agregar la IP del Modulo Arduino WiFi.


css: https://startbootstrap.com/themes/grayscale/
login: https://pythonspot.com/login-authentication-with-flask/
html: https://www.w3schools.com/html/default.asp
