#saiz
import sys
import serial
import os, time
import rospy
import pynmea2
from std_msgs.msg import String
ser = serial.Serial('/dev/ttyUSB0',9600)
def lugar():
#####################################
    latitud=0
    a=0
    b=0
    cadena=0
    longitud=0
####################################
    publa = rospy.Publisher('latitud', String, queue_size=10)
    publo = rospy.Publisher('longitud', String, queue_size=10)
    rospy.init_node('gps', anonymous=True)
    rate = rospy.Rate(1) # 40hz
    while not rospy.is_shutdown():
		data = ser.readline()
		if (data.startswith("$GPGGA")):
			pynmea2.parse(data)
    			data =   data.split(",")
			a=data[2]
			b=a[2:]	 
			a=a[:2]
			while True:
				try:
        				b=float(b)/60
					b=float(a)+b
					latitud=b
					a=data[4]
					b=a[3:]
					a=a[:3]
					b=float(b)/60
					b=(float(a)+b)*-1
					longitud=b
        				break
				except:
        				pynmea2.parse(data)
    					data =   data.split(",")
					a=data[2]
					b=a[2:]	 
					a=a[:2]
			
		cadena=str(latitud)+" "+str(longitud)
	 	rospy.loginfo(cadena)
		publa.publish(str(latitud))
		publo.publish(str(longitud))
		rate.sleep()

if __name__ == '__main__':
    try:
        lugar()
    except rospy.ROSInterruptException:
        pass