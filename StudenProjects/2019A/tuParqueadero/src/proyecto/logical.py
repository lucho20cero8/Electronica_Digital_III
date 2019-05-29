#!/usr/bin/env python
import rospy
import time
import numpy as np
from std_msgs.msg import String
class cuenta(object):
	def __init__(self):
		rospy.init_node("logical", anonymous = True)
		self.sensor_2 = 0
		self.t = 0
		self.q = 0
		self.crack=0
		self.makia=0
		self.count = 0
		self.gas=0
		self.pubnumero = 0
		self.pubdisponible = 0
		self.countanterior = 0
		self.disponible = 0
		self.pubnumero = rospy.Publisher('numero', String)
		self.pubdisponible = rospy.Publisher('disponible', String)
		self.rate = rospy.Rate(500)
		rospy.Subscriber("sensor1", String, self.sensor1)
		rospy.Subscriber("sensor2", String, self.sensor2)
		rospy.spin()

	def sensor1(self, data):

		sensor_1 = int(data.data)
		sensor_2 = int(self.sensor_2)
		print "dato 1 = " + str(sensor_1) + " dato 2 = " + str(sensor_2)

		if(sensor_1==1 and self.gas>70):
			self.t=1
			if(self.makia==0):
				self.crack=1
		if(sensor_2==1 and self.gas>70):
			self.q=1
			if(self.crack==0):
				self.makia=1
		if(self.t==1 and self.q==1 and self.crack==1):
			self.count = self.count + 1
			self.t=0
			self.q=0
			self.crack=0
			self.makia=0
			self.gas=0
		if(self.t==1 and self.q==1 and self.makia==1):
			self.count = self.count - 1
			self.t=0
			self.q=0
			self.crack=0
			self.makia=0
			self.gas=0
		if(self.countanterior==self.count):
			self.gas=self.gas+1
		self.countanterior=self.count
		sensor_anterior = sensor_1
		print self.count
		print self.disponible
		self.disponible = 50 - self.count


		if self.disponible > 50:
		    self.disponible=50

		if self.disponible<0:
		    self.disponible=0

		if self.count > 50:
		   self.count = 50

		if self.count < 0:
		   self.count = 0

		self.pubdisponible.publish(str(self.disponible))
		"""rospy.loginfo(self.count)"""
		self.pubnumero.publish(str(self.count))
		self.rate.sleep()

	def sensor2(self, data):
		self.sensor_2 = int(data.data)

if __name__ == '__main__':
    l = cuenta()
