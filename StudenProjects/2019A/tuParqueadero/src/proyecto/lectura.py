#!/usr/bin/env python
import serial
import rospy
import numpy as np
from std_msgs.msg import String

def talker():
    pubsensor1 = rospy.Publisher('sensor1', String)
    pubsensor2 = rospy.Publisher('sensor2', String)
    rospy.init_node('arduino', anonymous=True)
    rate = rospy.Rate(500)
    arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
    while not rospy.is_shutdown():
    	line = arduino.readline()
        a = line.strip(" \r\n")
        b = str(a)
        c = b.split(':')
        sensor_1 = c[0]
        sensor_2 = c[1]
        """rospy.loginfo(sensor_1)
        rospy.loginfo(sensor_2)"""
        pubsensor1.publish(sensor_1)
        pubsensor2.publish(sensor_2)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
