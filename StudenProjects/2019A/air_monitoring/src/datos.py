import os
import rospy
import time
from std_msgs.msg import String


class caja():
	def __init__(self):
		
		self.datohumedad=0
		self.datotemperatura=0
		self.datoaire=0
		self.datomonoxido=0
		self.datolongitud=0
		self.datolatitud=0
		self.carpeta=os.getcwd()
		self.carpeta=self.carpeta.split("code")
		self.carpeta=self.carpeta[0]+"data/archivos.txt"
		
		

		

	def datoh(self,data):
		self.datohumedad=data.data
		


	def datot(self,data):
		self.datotemperatura=data.data



	def datoa(self,data):
        	self.datoaire=data.data
	



	def datol(self,data):
        	self.datolongitud=data.data

	def datola(self,data):
        	self.datolatitud=data.data
	


	def datom(self,data):
		self.datomonoxido=data.data
		cadena=str(self.datohumedad)+" "+str(self.datotemperatura)+" "+str(self.datoaire)+" "+str(self.datomonoxido)+" "+str(self.datolatitud)+" "+str(self.datolongitud)+"\n"
		rospy.loginfo(cadena)

		archivos = open(self.carpeta,"a")
		archivos.write(cadena)
		#archivos.write("\n")
		archivos.close()
		
		

	def listener(self):
	
	
		rospy.init_node('listener', anonymous=True)   
       		rospy.Subscriber("humedad", String, self.datoh)
		rospy.Subscriber("aire", String, self.datoa)
		rospy.Subscriber("temperatura", String,self.datot)
		rospy.Subscriber("longitud", String, self.datol)
		rospy.Subscriber("latitud", String, self.datola)
		rospy.Subscriber("monoxido", String, self.datom)
		rospy.spin()


if __name__ == '__main__':
	try:
		saiz= caja()
		saiz.listener()   
	except rospy.ROSInterruptException:
        	pass
	