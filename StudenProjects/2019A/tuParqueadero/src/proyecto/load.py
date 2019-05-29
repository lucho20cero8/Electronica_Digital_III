#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import String
numero_anterior=0

def ini():
  #   Enlace con ROS
    rospy.init_node('load', anonymous=True)
    rospy.Subscriber('numero', String, callback)
    rospy.spin()


def callback(data):
    global numero_anterior
    numero = data.data
    if numero != numero_anterior:
        print numero
        hora = time.strftime("%I:%M:%S")
        archivo = open("prueba.txt","a")
        archivo.write('\n' + numero + " personas a las ")
        archivo.write(hora)
        archivo.close()
    numero_anterior = numero

if __name__ == '__main__':
    ini()
