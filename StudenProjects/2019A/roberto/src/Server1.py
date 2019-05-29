#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import time
import sys
import socket


def talker():
    pub = rospy.Publisher('JY', String, queue_size=10) #Inicialiacion del publisher por el topico JY
    rospy.init_node('JY', anonymous=True) #Inicialiacion del nodo JY
    rate = rospy.Rate(0.000000000000000000001)

    while not rospy.is_shutdown():
        data, ip = socket.recvfrom(1024) #Data que le llega del socket 1024
        rospy.loginfo(data)
        pub.publish(data) #Publicador de la variable
        socket.sendto(data, ip)

if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind(("10.42.0.1", 9999)) #Inicializacion del servidor en el puerto 9999

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
