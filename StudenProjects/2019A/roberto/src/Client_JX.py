import socket
import rospy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import numpy as np

class Client2():

    def __init__(self):
        self.pub = rospy.Publisher("JX1", String, queue_size=10) #Inicialiacion del publisher por el topico JX1
        rospy.Subscriber('/joy', Joy, self.Joy_X)#Se subscribe al nodo joy
        rospy.spin()

    def Joy_X(self, data):
        datos_laser = np.asarray(data.axes)#Datos de los analogos enviados del joy
        data_buttons = np.asarray(data.buttons) #Datos de los botones enviados del joy
        jx1=datos_laser[3] #Obtenemos el dato del eje X del analogo derecho
        jx= round(jx1,1) #Se redondea el valor para no trabajar con tantos decimales
        jx=str(jx)
        if jx[0] != '-'  :
            jx="+"+jx
	    rospy.loginfo(jx)
        self.pub.publish(jx) #Publica el dato de jx
if __name__ == '__main__':
    rospy.init_node("Client2") #Inicialiacion del nodo Client2
    cv = Client2()
