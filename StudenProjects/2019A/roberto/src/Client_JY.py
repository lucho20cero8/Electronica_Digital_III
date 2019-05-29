import socket
import rospy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import numpy as np

class Client1():

    def __init__(self):
        self.pub = rospy.Publisher("JY1", String, queue_size=10) #Inicialiacion del publisher por el topico JY1
        rospy.Subscriber('/joy', Joy, self.Joy_Y)#Se subscribe al nodo joy
        rospy.spin()

    def Joy_Y(self, data):
        datos_laser = np.asarray(data.axes)#Datos de los analogos enviados del joy
        data_buttons = np.asarray(data.buttons)#Datos de los botones enviados del joy
        jy1=datos_laser[1]#Obtenemos el dato del eje Y del analogo izquierdo
        jy= round(jy1,1) #Se redondea el valor para no trabajar con tantos decimales
        jy=str(jy)
        if jy[0] != '-'  :
            jy="+"+jy
    	rospy.loginfo(jy)
        self.pub.publish(jy) #Publica el dato de jy
if __name__ == '__main__':
    rospy.init_node("Client1") #Inicialiacion del nodo Client1
    cv = Client1()
