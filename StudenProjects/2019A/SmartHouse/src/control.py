#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

gpio.setup(12, gpio.OUT) ######
gpio.setup(16, gpio.OUT) #
gpio.setup(18, gpio.OUT) #
gpio.setup(22, gpio.OUT) #reles
gpio.setup(32, gpio.OUT) #
gpio.setup(36, gpio.OUT) #
gpio.setup(38, gpio.OUT) #
gpio.setup(40, gpio.OUT) ######

#variables reles
reletemperatura = 0 #pin 12, rele1
#relebombillo1 = 0   #pin 16, rele2 
#relebombillo2 = 0   #pin 18, rele3
#relebombillo3 = 0   #pin 22, rele4
#variables
temperatura = 0.0
contador1 = 0
contador2 = 0

print("listo")
    
def metodotemperatura(datotemperatura):
    global temperatura
    global reletemperatura
    temperatura = float(datotemperatura.data) 
    print("temperatura= " + str(temperatura))
    if temperatura >30:      
        gpio.output(12, True)      
        reletemperatura = 1
    else:
        gpio.output(12, False)
        reletemperatura = 0
        
    if reletemperatura == 1:
        print("ventilador encendido")
    else:
        print("ventilador apagado")

def metodocontador1(datocontador1):
    global contador1
    contador1 = int(datocontador1.data)
    print("contador1= " + str(contador1))
    if contador1>0:
        gpio.output(18, True)
    else:
        gpio.output(18, False)
    
def metodocontador2(datocontador2):
    global contador2
    contador2 = int(datocontador2.data) 
    print("contador2= " + str(contador2))
    if contador2>0:
        gpio.output(22, True)
    else:
        gpio.output(22, False)
    
    
def listener():
    
    rospy.init_node('control', anonymous=True)

    rospy.Subscriber("temperatura", String, metodotemperatura)
    rospy.Subscriber("contador1", String, metodocontador1)
    rospy.Subscriber("contador2", String, metodocontador2)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    gpio.output(12, False)
    gpio.output(16, False)
    gpio.output(18, False)
    gpio.output(22, False)
    gpio.output(32, False)
    gpio.output(36, False)
    gpio.output(38, False)
    gpio.output(40, False)
    listener()