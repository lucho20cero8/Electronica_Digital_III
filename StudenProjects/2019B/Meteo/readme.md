![N|Solid](https://www.ecured.cu/images/6/6b/Univ_ibague.jpg)

---
# WEATHER STATION 
---
This project was born from analyzing the need for the Colombian farmer to know in real time the behavior of different climatic variables that may affect their productive activities such as planning and planting crops. In this case we decided to create a meteorological station that allows us through the use of the internet of things (IOT), monitor these variables in real time and graphically display them on the Thingspeak web platform.
#
-----
## HARDWARE REQUIREMENTS:
---
- [Raspberry pi 3b+](https://static.raspberrypi.org/files/product-briefs/Raspberry-Pi-Model-Bplus-Product-Brief.pdf) 
- [MicroSD 16 GB](https://www.alliedelec.com/m/d/04db416b291011446889dbd6129e2644.pdf)
- Module sensor air quality Ref: [MQ135.](https://www.olimex.com/Products/Components/Sensors/Gas/SNS-MQ135/resources/SNS-MQ135.pdf)
- Module temperature and humidity Ref: [DHT11.](https://www.mouser.com/datasheet/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf)
- Atmospheric pressure sensor module Ref: [BMP180.](https://cdn-shop.adafruit.com/datasheets/BST-BMP180-DS000-09.pdf)
- Rain Sensor Ref: [LM-393.](https://www.mactronica.com.co/sensor-de-lluvia-yl83-44083259xJM)
- Module GPS Ref: [NEO-6M](https://www.u-blox.com/sites/default/files/products/documents/NEO-6_DataSheet_(GPS.G6-HW-09005).pdf)
- [Arduino nano](https://www.arduino.cc/en/uploads/Main/ArduinoNanoManual23.pdf)
- [Electrical boxes for interperies.](https://www.linio.com.co/p/cctv-100-cajas-de-paso-10x10-paquete-wzusm5?adjust_t=1zira0_f1h7ws&adjust_google_network=g&adjust_google_placement=&adjust_campaign=col-semun-spla&adjust_adgroup=80047128844&utm_term=other&gclid=EAIaIQobChMIvajxxKP85QIVJYFaBR0u_wQqEAQYAyABEgJEdPD_BwE) 
---
## SOFTWARE REQUIREMENTS:
---
- SO Raspbian
- Python 3
- Thingspeak
- Arduino IDE
- Archivo .txt
---
## OPERATING SYSTEM INSTALLATION & LIBRARIES
---
### Rasbian OS installation:
---
- It is essential to have Ubuntu operating system, in the following [Website](https://ubuntu.com/download/desktop), you will find the step by step and the requirements for its installation.
- Download the OS Raspbian operating system from the [Raspberry Main Website](https://www.raspberrypi.org/downloads/).
- Format the MicroSD card in format [FAT32](https://www.sdcard.org/downloads/formatter/).
- Download and install the [BALENAETCHER](https://www.balena.io/etcher/), which will allow us to install the OS Raspbian operating system in the MicroSD Memory.
- Once the operating system is in memory, we proceed to insert the MicroSD card into the Raspberry pi 3 + b, initialize it and follow the steps requested by the Raspberry.
---
### Installation & Update of Libraries:
---
Once we have the Raspbian OS on the Raspberry Pi 3b + and we have an internet connection, we enter the console to update the libraries already installed at the factory, using the following instructions:

```sh
$ Ctrl + t
$ sudo apt-get uptgrade
```
Later we install the Python 3 library and its PIP add-on, which allows us to download the Github libraries, as follows:
```sh
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
```
We proceed to install the Barometric Pressure sensor library [BMP180](https://pypi.org/project/Adafruit-BMP/), as follows:
```sh
$ pip3 install Adafruit-BMP.
```
Next we install the Humidity & Temperature sensor library [DHT11](https://pypi.org/project/Adafruit-DHT/) with the following instructions:
```sh
$ pip3 install Adafruit-DHT.
```
Then we proceed to install the libraries necessary for the operation of the GPS-NEO6M:
```sh
$ sudo pip3 install pynmea3.
$ sudo apt-get install gpsd gpsd-clients python-gps minicom.
```
Once these libraries are installed, we proceed to the following [Website](https://github.com/FranzTscharf/Python-NEO-6M-GPS-Raspberry-Pi), where the step-by-step explanation of the changes will be found that must be made to the system files, for proper GPS operation. Once the GPS installation has been completed, we proceed to install the library [GPS3](hts://pypi.org/project/gps3/), which will allow us to display the data collected by the GPS in STR form.
```sh
$ pip3 install gps3.
```

For the acquisition of data from the MQ-135 Air Quality and Rain Sensor sensors, an arduino nano is programmed using [Arduino IDE](https://www.arduino.cc/en/main/software#) . After having it installed, we proceed to create the SCRIPT that will allow the sensors to be read in an analogous way, to convert them into digital and send them to the Raspberry pi 3b + in the form of serial communication as follows:

```sh
$ sudo apt-get install serial.
```
---
# SSH EXECUTION & COMMUNICATION
---
The execution of the code can be done in two ways, the first one automatically generating a .sh file and calling it from the bash as follows:
```sh
$ nano NOMBRE DEL ARCHIVO.sh
$ sudo nano .bashrc
```
Having already entered nano. bashrc, we modify the following instruction at the end of the document:
```sh
$ bash /ruta del archivo.sh
$ ctrl + O
$ ctrl + X
```
The second way is by accessing through an external terminal under the ssh instruction as follows:
```sh
$ ctrl + t
$ ssh nombredelaRpi@ip.
$ contraseña : La asiganada a la Rpi
```
Finally we go to the location of the codes belonging to the Raspberry pi 3b +, for this we use the following command:
```sh
$ ls
```
And we choose the code to execute, in this case:
```sh
$ python3 estacion_final.py
```
Source code which is responsible when executing to send the information of the reading of Temperature, Humidity, Atmospheric Pressure, Air Quality, and Presipitation; the URL of the Thingspeak platform to which the data is being uploaded; the position generated by the GPS seen from Longitude and Latiud. And finally the acquisition and saving of the automatic data in the file.txt

---
## DATA STORAGE AND MAIL SHIPPING
---
For data storage we generate a .txt file, as follows:
```sh

def txt():
    archivos=open("datos.txt",'a')
    cadena="Datos de la fecha"+"\t"+str(now[0:11])+"\n"+"temperatura = "+str(tc)+" °C"+"\t "+"precion = "+str(p)+" KPa"+"\t "+"humedad = "+str(h)+" %"+"\t "+"lluvia = $+str(w)+"\t"+"contaminacion = "+str(cont)+"\t"+"fecha = "+str(now[0:4])+"\t"+str(now[5:7])+"\t"+str(now[8:11])+"\t"+str(now[11:19])+"\n"
    archivos.write(cadena)
    archivos.close()
    print("dato guardado")
```
To upload them to the web platform  [Thinspeak](https://thingspeak.com/login), the first thing we should do is create an account on that platform, then generate the following code:

```sh
$ def ts():
    URL='https://api.thingspeak.com/update?api_key='
    KEY='NB9V0UIQYJI8Kl'
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}'.format(tc,h,p,w,cont)
    new_URL=URL+KEY+HEADER
    print(new_URL)
    data=urllib.request.urlopen(new_URL)
    print(data)
```
Once the measurement data is saved in the .txt file, a function is created in the source code, which is responsible for generating the sending of a message every 12 hours through the GMAIL platform, which contains the .txt file, the IP address and a link to the station's real-time location, as shown below:

```sh
def send_email():
    password = "mustang96"
    remitente = '2420142004@estudiantesunibague.edu.co'
    destinatarios = ['2420151034@estudiantesunibague.edu.co']
    asunto = '[RPI] Correo de prueba'
    ruta_adjunto = '/home/pi/datos.txt'
    nombre_adjunto = 'datos.txt'
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    ni.ifaddresses('wlan0')
    IP= ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
    cuerpo = "Informe modulo"+"\t" + coordenada +"\t "+"ip actual"+"\t"+ IP
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    archivo_adjunto = open(ruta_adjunto, 'rb')
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    adjunto_MIME.set_payload((archivo_adjunto).read())
    encoders.encode_base64(adjunto_MIME)
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    mensaje.attach(adjunto_MIME)
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    sesion_smtp.login(remitente,password)
    texto = mensaje.as_string()
    sesion_smtp.sendmail(remitente, destinatarios, texto)
    sesion_smtp.quit()
    print ("correo enviado")

```
---
# CODE
> python3 estacion_final.py
---
#### Authors:
----
- Manuel Felipe Sarmiento Gonzalez.
- Kelly Diomara Ladino Polanco.
- Luis Fernando Sanchez.

## Tutor:
- [Harold F. Murcia Moreno](http://haroldmurcia.com/) 
---
----
Visit our YOUTUBE chathe nnel, to see the project and its future improvements [METEREOLOGICAL STATION](https://www.youtube.com/watch?v=SbNZvlzlS4U).
---
