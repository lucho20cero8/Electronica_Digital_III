#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import time
import sys
import socket


def talker():
    pub = rospy.Publisher('JX', String, queue_size=10)#Inicialiacion del publisher por el topico JX
    rospy.init_node('JX', anonymous=True) #Inicialiacion del nodo JY
    rate = rospy.Rate(0.00000000000001)

    while not rospy.is_shutdown():
        data, ip = socket.recvfrom(1024) #Data que le llega del socket 1024
        rospy.loginfo(data)
        pub.publish(data) #Publicador de la variable
        socket.sendto(data, ip)

if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind(("10.42.0.1", 9900)) #Inicializacion del servidor en el puerto 9900
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
