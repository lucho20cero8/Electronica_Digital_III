#!/usr/bin/env python3 -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:47:45 2019

@author: pi
"""
import os
#librerias correo electronico
import smtplib
from datetime import datetime
import netifaces as ni
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import urllib.request
from email import encoders
#libreria tiempo
from time import sleep
#librerias sensores
import board
import adafruit_dht
import serial
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT
#libreria gps
from gps3 import gps3


BMP180 = BMP085.BMP085()
dht11 = adafruit_dht.DHT11(board.D4)
now = str(datetime.now())
flag1=0
flag2=0
w=0
cont=0

def sensores():
    while True:
      try:
            global p
            global h
            global w
            global cont
            global tc
            p = int((BMP180.read_pressure())/1000.0)
            te = BMP180.read_temperature()
            tc = int(dht11.temperature)
            tf = int(tc * (9 / 5) + 32)
            h = int(dht11.humidity)
            y = arduino.readline()
            y=y.strip()
            y=y.decode("utf-8")
            y1 = y.split(",")
            lluvia = y1[1]
            cont = y1[0]
            print("lluvia:"+str(lluvia)+"  , contaminacion: "+str(cont))
            if (lluvia == str("0")):
                w=0
                print("No hay lluvia")
            if (lluvia != str("0")):
                w=1
                print("hay lluvia")
            print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% " .format(tf, tc, h))
            print('Temp={}*C' .format(tc))
            print('Temp={}*C' .format(te))
            print('Humidity={}%' .format(h))
            print('Pressure={}KPa' .format(p))
            break
      except:
            print ("cargando")
            sleep(0.1)

def txt():
    archivos=open("datos.txt",'a')
    cadena="Datos de la fecha"+"\t"+str(now[0:11])+"\n"+"temperatura = "+str(tc)+" °C"+"\t "+"precion = "+str(p)+" KPa"+"\t "+"humedad = "+str(h)+" %"+"\t "+"lluvia = "+str(w)+"\t"+"contaminacion = "+str(cont)+"\t"+"fecha = "+str(now[0:4])+"\t"+str(now[5:7])+"\t"+str(now[8:11])+"\t"+str(now[11:19])+"\n"
    archivos.write(cadena)
    archivos.close()
    print("dato guardado")


def ts():
    URL='https://api.thingspeak.com/update?api_key='
    KEY='NB9V0UIQYXEBJI8K'
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}'.format(tc,h,p,w,cont)
    new_URL=URL+KEY+HEADER
    print(new_URL)
    data=urllib.request.urlopen(new_URL)
    print(data)

def send_email():
    password = "mustang96"
    remitente = '2420142004@estudiantesunibague.edu.co'
    destinatarios = ['2420151034@estudiantesunibague.edu.co','2420162033@estudiantesunibague.edu.co' ]
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

def gps():
    global pos
    global coordenada
    global ct
    ct=0
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()
    gps_socket.connect()
    gps_socket.watch()
    for new_data in gps_socket:
        sleep(0.1)
        if new_data:
            data_stream.unpack(new_data)
            pos = data_stream.TPV['lat'], data_stream.TPV['lon']
            Latitud = data_stream.TPV['lat']
            Longitud = data_stream.TPV['lon']
            coordenada = "http://www.google.com/maps/place/"+str(Latitud)+","+str(Longitud)
            if pos != ('n/a', 'n/a'):
                ct = 0
                print (pos)
                print (coordenada)
                break


while True:
    try:
            arduino = serial.Serial('/dev/ttyUSB0',9600)
            sensores()
            txt()
            ts()
#            gps()
            print (now[11:16])
            if (now[11:13] == str("20")) & (flag1 == 0):
                send_email()
                print("mail enviado")
                os.remove('/home/pi/datos.txt')
                flag1=1
                flag2=0

            if (now[11:13] == str("06")) & (flag2 == 0):
                send_email()
                print("mail enviado")
                os.remove('/home/pi/datos.txt')
                flag2=1
                flag1=0
            print (flag1)
            print (flag2)
            sleep(60)
    except:
            print ("cargando")
