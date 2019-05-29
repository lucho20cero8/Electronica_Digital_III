#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import requests

#variables
flama1 = 1
flama2 = 1
flama3 = 1
temperatura = 0.0
contador1 = 0
contador2 = 0
#contador3 = 0
nfc = ""
comprobacion = 0
#variables TS
enviardatoflama1 = None
enviardatoflama2 = None
enviardatoflama3 = None
enviardatotemperatura = None
enviardatocontador1 = None
enviardatocontador2 = None
#enviardatocontador3 = None
enviardatonfc = None

print("listo")

def metodoflama1(datoflama1):
    global flama1
    global enviardatoflama1
    flama1 = int(datoflama1.data)
    print("flama1= "+str(flama1))
    RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field1=0'
    RequestToThingspeak +=(str(flama1))
    enviardatoflama1 = requests.get(RequestToThingspeak)
    
def metodoflama2(datoflama2):
    global flama2
    global enviardatoflama2
    flama2 = int(datoflama2.data) 
    print("flama2= "+str(flama2))
    RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field2=0'
    RequestToThingspeak +=(str(flama2))
    enviardatoflama2 = requests.get(RequestToThingspeak)

    
def metodoflama3(datoflama3):
    global flama3
    global enviardatoflama3
    flama3 = int(datoflama3.data)   
    print("flama3= "+str(flama3))
    RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field3=0'
    RequestToThingspeak +=(str(flama3))
    enviardatoflama3 = requests.get(RequestToThingspeak)
    
def metodotemperatura(datotemperatura):
    global temperatura
    global enviardatotemperatura
    temperatura = float(datotemperatura.data) 
    print("temperatura= "+str(temperatura))
    RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field4=0'
    RequestToThingspeak +=(str(temperatura))
    enviardatotemperatura = requests.get(RequestToThingspeak)

def metodocontador1(datocontador1):
    global contador1
    global enviardatocontador1
    contador1 = int(datocontador1.data)
    print("contador1= "+str(contador1))
    RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field5=0'
    RequestToThingspeak +=(str(contador1))
    enviardatocontador1 = requests.get(RequestToThingspeak)
    
def metodocontador2(datocontador2):
    global contador2
    global enviardatocontador2
    contador2 = int(datocontador2.data)
    print("contador2= "+str(contador2))
    RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field6=0'
    RequestToThingspeak +=(str(contador2))
    enviardatocontador2 = requests.get(RequestToThingspeak)
    
"""def metodocontador3(datocontador3):
    global contador3
    global enviardatocontador3
    contador3 = int(datocontador3.data) 
    print("contador3= "+str(contador3))
    RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field7=0'
    RequestToThingspeak +=(str(contador3))
    enviardatocontador3 = requests.get(RequestToThingspeak)"""
   
"""def metodonfc(datonfc):
    global nfc
    global enviardatonfc
    global comprobacion    
    nfc = datonfc.data 
    print("nfc= "+str(nfc))
    if nfc == "Bienvenido":
        comprobacion = 1
    else:
        comprobacion = 0
    RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=M6HN1UX596VL7KAC&field8=0'
    RequestToThingspeak +=(str(comprobacion))
    enviardatonfc = requests.get(RequestToThingspeak)"""

def listener():
    
    rospy.init_node('control', anonymous=True)

    rospy.Subscriber("flama1", String, metodoflama1)
    rospy.Subscriber("flama2", String, metodoflama2)
    rospy.Subscriber("flama3", String, metodoflama3)
    rospy.Subscriber("temperatura", String, metodotemperatura)
    rospy.Subscriber("contador1", String, metodocontador1)
    rospy.Subscriber("contador2", String, metodocontador2)
    #rospy.Subscriber("contador3", String, metodocontador3)
    #rospy.Subscriber("nfc", String, metodonfc)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
