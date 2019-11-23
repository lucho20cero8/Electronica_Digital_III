
______________[![N|Solid](https://www.ecured.cu/images/6/6b/Univ_ibague.jpg)](https:http:https://www.unibague.edu.co/)
# UNI GYM: sistema de control en el gimnasio de la Universidad de Ibagué
This repository presents the process del proceso de como crear un sistema de control de ingreso.

* link del  video : https://drive.google.com/file/d/102OU-uezXLByYRSEcv4hhQTKCX__D3LY/view?usp=sharing

# Este repositorio contiene:

* Código fuente
* Archivos de información
* Script de desarrollo

# Repositorio de hardware:

* Modulo Relé :https://www.vistronica.com/potencia/modulo-rele-de-2-canales-detail.html?gclid=Cj0KCQiAiNnuBRD3ARIsAM8KmlvKu1OsLLj2f1v3_M37RQ9z3bZeedvF-MK_U-YOIhiK0kF-tS2quo4aAoY4EALw_wcB
* Arduino :https://www.dynamoelectronics.com/tienda/arduino-uno-r3/?gclid=Cj0KCQiAiNnuBRD3ARIsAM8KmltRdE1reLVw2Ld-6UQwaSnY2RHy3PdUPfCBtxLXO9i95YUO0hzpWVwaAh-HEALw_wcB
* Cerradura Inteligente Turbolock Seguridad Avanzada, Acceso: https://articulo.mercadolibre.com.co/MCO-494151729-cerradura-inteligente-turbolock-seguridad-avanzada-acceso-_JM?matt_tool=24497864&matt_word&gclid=Cj0KCQiAiNnuBRD3ARIsAM8Kmlu89j6uHJSS8UtjVS4zwD6Bxrcboct044f2XQ9sE-nejcqtR0aBroYaAmkkEALw_wcB&quantity=1
*Lector / Escaner Usb Código De Barras Alta Velocidad X-718 :https://articulo.mercadolibre.com.co/MCO-514614632-lector-escaner-usb-codigo-de-barras-alta-velocidad-x-718-_JM?matt_tool=44486125&matt_word&gclid=Cj0KCQiAiNnuBRD3ARIsAM8KmlsBTu21omypiCNl9cqqWR33P5Lns1k10o5mqfF4WjsOqQ4UOGTiZfUaAg6pEALw_wcB&quantity=1

# Requisitos de Software:

* Ubuntu 16.04
* Python 2.7 bibliotecas necesarias (mqtt, flask, xlrd)
* IDE Arduino

# Cómo instalar 

Es necesario instalar las bibliotecas de la siguiente manera

- Instalar pandas
~~~

sudo pip install pandas
ó sudo pip3 install pandas
~~~
Esta biblioteca es necesario porque puede extraer la información de la base de datos.
* Para instalar flask:
~~~
sudo pip install flask
ó sudo pip3 install flask
~~~
Esta biblioteca es la que se encarga de general la página.

* Para instalar serial :
~~~
python -m pip install pyserial
~~~

Esta biblioteca es la responsable de enlazar la pagina con el Arduino

# Códigos PC

* doc_exportar.pyc

En este código podremos encontrar cada una de las funciones que se encargan de habilitar las opciones de la página las cuales se van a exporta al código principal,se implementa este metodo para poder llevar una secuencia a la hora de programar.

* login
* calificacion
* promedio
* correo
* guardar


* PromedioSemana.py

Este código se encarga de generar la grafica que se encuentra en la opcion de horarios .

* Codigo_Paralelo.py

Es el encargado de leer la informacion del lector de códigos de  barras y permitir mediante el arduino que el estudiante ingrese al gym, este debe estar ejecutandose al mismo tiempo que el de la página web. 

* Flask1.py

Código principal es el encargado de la página principal, en este se llaman las funciones de doc_exportar.py y todos los códigos (html, css) de las carpetas de plantillas y static.

# Ejecución código

Códigos a ejecutar en la terminal 

* Codigo_Paralelo.py
* Flask1.py

# Authors:
*Universidad de Ibagué Ingeniería Electronica - Electronica digital III 2019*

___
- [Laura Valentina Ruiz González]( mailto:2420161037udiantesunibague.edu.co)
- [Juan Pablo Ocampo Fierro](mailto:2420171051@estudiantesunibague.edu.co)
- [Johan Steven Ávila Paramo](mailto:2420171062@estudiantesunibague.edu.co)
-  [Harold F MURCIA](www.haroldmurcia.com) - tutor
***

***
Visit the YouTube channel to see the video of the project and future improvements of [here](https://www.youtube.com/watch?v=wcRaPDu8tyg&t=3s).
***

