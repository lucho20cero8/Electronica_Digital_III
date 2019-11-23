import serial, time
import RPi.GPIO as GPIO
import time
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import socket
import netifaces as ni

#from email.mime.text import MIMEText
#import smtplib

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
#arduino = serial.Serial('/dev/ttyACM1',9600)
"""p=GPIO.PWM(7,50)
p.start(7.5)"""

def Alimento():
    ard.write('1'.encode())
    """ni.ifaddresses('eth0')
    IP= ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']





    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login("2420171086@estudiantesunibague.edu.co","fernanda10")
    print (mailServer.ehlo())



    #mensaje=MIMEText("Queremos ir al SOFA"
    mensaje = MIMEMultipart()
    mensaje.attach(MIMEText("comida"))
    mensaje['From']="2420171086@estudiantesunibague.edu.co"
    mensaje['To']="2420171086@estudiantesunibague.edu.co"
    mensaje['Subject']="Tienes un mensaje "
    file = open("descarga.jpeg", "rb")
    contenido = MIMEImage(file.read())
    contenido.add_header('Content-Disposition', 'attachment; filename = "descarga.jpeg"')
    mensaje.attach(contenido)


    mailServer.sendmail("2420171086@estudiantesunibague.edu.co","2420171086@estudiantesunibague.edu.co",mensaje.as_string())"""

    #GPIO.output(7,True)
    #time.sleep(2)
    #GPIO.output(7,False)
    """try:
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()"""

def Oxigeno():
    if GPIO.input(13)==False:
        GPIO.output(13,True)
        time.sleep(5)
    else:
        GPIO.output(13,False)
        time.sleep(5)
    #GPIO.output(13,True)
    #time.sleep(2)
    #GPIO.output(13,False)
    

def Luces():
    if GPIO.input(5)==False:
       GPIO.output(5,True)
    else:
        GPIO.output(5,False)

def Calentador():
    if GPIO.input(12)==False:
        GPIO.output(12,True)
        time.sleep(5)
    else:
        GPIO.output(12,False)
        time.sleep(5)
    #GPIO.output(12,True)
    #time.sleep(2)
    #GPIO.output(12,False)
    

    
