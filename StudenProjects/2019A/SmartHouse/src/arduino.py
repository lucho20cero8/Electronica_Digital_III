#!/usr/bin/env python
# license removed for brevity
import rospy
import serial
from std_msgs.msg import String

Arduino=serial.Serial("/dev/ttyACM0",baudrate=9600,timeout=5) 
Arduino.flushInput()

def talker():
    #topicos
    pubflama1 = rospy.Publisher('flama1', String, queue_size=10)
    pubflama2 = rospy.Publisher('flama2', String, queue_size=10)
    pubflama3 = rospy.Publisher('flama3', String, queue_size=10)
    pubtemperatura = rospy.Publisher('temperatura', String, queue_size=10)
    pubcontador1 = rospy.Publisher('contador1', String, queue_size=10)
    pubcontador2 = rospy.Publisher('contador2', String, queue_size=10)
    pubnfc = rospy.Publisher('nfc', String, queue_size=10)
    #nodo
    rospy.init_node('arduino', anonymous=True)
    rate = rospy.Rate(1000) # 1000hz
    if not rospy.is_shutdown():     
        pubflama1.publish(flama1)
        pubflama2.publish(flama2)
        pubflama3.publish(flama3)
        pubtemperatura.publish(temperatura) 
        pubcontador1.publish(contador1)
        pubcontador2.publish(contador2)
        pubnfc.publish(nfc)          
        rate.sleep()
        
if __name__ == '__main__':
    print("publicando")
    while True:
        try:       
            data_Arduino=Arduino.readline()
            data = str(data_Arduino)
            data = data.split(':')  
            flama1 = data[1]
            flama2 = data[3]
            flama3 = data[5]
            temperatura = data[7]
            contador1 = data[9]
            contador2 = data[11]
            nfc = data[12].strip("\r\n")   
            talker()
        except IndexError:
            pass
    
