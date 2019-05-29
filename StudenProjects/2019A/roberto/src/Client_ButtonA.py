import socket
import rospy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import numpy as np

class Client3():

    def __init__(self):
        self.pub = rospy.Publisher("B_A", String, queue_size=10) #Inicialiacion del publisher por el topico B_A
        rospy.Subscriber('/joy', Joy, self.A) #Se subscribe al nodo joy
        rospy.spin()

    def A(self, data):
        datos_laser = np.asarray(data.axes) #Datos de los analogos enviados del joy
        data_buttons = np.asarray(data.buttons) #Datos de los botones enviados del joy
        A=data_buttons[2] #Dato del boton en la posicion 2
        A=str(A)
        rospy.loginfo(A)
        self.pub.publish(A) #Publica el estado del boton en la posicion 2
if __name__ == '__main__':
    rospy.init_node("Client3") #Inicialiacion del nodo Client3
    cv = Client3()
