import sys
import serial
import time
import rospy
from std_msgs.msg import String
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=0)
def talker():
    humedad=0
    temperatura=0
    aire=0
    monoxido=0
    real=0
    real2=0
    pubh = rospy.Publisher('humedad', String, queue_size=10)
    pubt = rospy.Publisher('temperatura', String, queue_size=10)
    puba = rospy.Publisher('aire', String, queue_size=10)
    pubm = rospy.Publisher('monoxido', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 40hz
    while not rospy.is_shutdown():
		
 		line = arduino.readline()
  		line=  line.split(",")
 		
		
		while True:
			try:
        			h=int(line[0])
  				t=int(line[1])
				a=int(line[2])
				m=int(line[3])
        			break
			except:
        			line = arduino.readline()
				
  				line=line.split(",")
 		
		
				
				rospy.loginfo("h: "+"No"+"%  "+"t: "+"No"+"c  "+"a:  "+"No" +"     m:  "+"NO")
				time.sleep(0.1)
		
		a=int(a)*100/1023
		
		m=int(m)*100/1023
		
		
	
		cadena = "h: "+str(h)+"%  "+"t: "+str(t)+"c  "+"a:  "+str(a)+"%    "+"CO2:  "+str(m)+"%"
		
		
		rospy.loginfo(cadena)
		pubh.publish(str(h))
		pubt.publish(str(t))
		puba.publish(str(a))
		pubm.publish(str(m))





        	rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
