#!/usr/bin/env python
import time
import rospy
import lcddriver
from std_msgs.msg import String
numero_anterior=0

def ini():
    display = lcddriver.lcd()
    rospy.init_node('lcd', anonymous=True)
    rospy.Subscriber('disponible', String, callback)
    rospy.spin()

def callback(data):
    global numero_anterior
    numero = data.data
    if numero != numero_anterior:
       display = lcddriver.lcd()
       display.lcd_display_string("Disponibles:", 1)
       display.lcd_display_string(str(numero), 2)
    numero_anterior = numero


if __name__ == '__main__':
    ini()
