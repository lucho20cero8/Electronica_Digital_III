import rospy #Importacion de Librerias
from std_msgs.msg import String
import datetime
import serial
import time

def callback(data):
    global MD #Se vuelve MD en una variable global
    MD=data.data #Obtenemos el dato del topico
    if MD=='-0.0':
	    MD='0.0'   #Si MD es -0.0(Dato que envia el nodo joy cuando es 0.0 o vuelvo 0.0)
    rospy.loginfo("Y," + MD + ", X," + ML +",B,") #Manda la informacion de MD y ML
    ser.write("MD," + MD + ", ML," + ML ) #Escribe por puerto serial al arduino
    time.sleep(0.000000001) #Duerme

def callback1(data):
    global ML #Se vuelve ML en una variable global
    ML=data.data    #Obtenemos el dato del topico
    if ML=='-0.0':
	    ML='0.0'   #Si ML es -0.0(Dato que envia el nodo joy cuando es 0.0 o vuelvo 0.0)

def listener():
    rospy.init_node('Motores', anonymous=True) #Inicia el nodo Motores
    rospy.Subscriber("MD", String, callback) #Se subscribe al topico MD en a funcion callback
    rospy.Subscriber("ML", String, callback1) #Se subscribe al topico ML en la funcion callback1
    rospy.spin()



if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600)   #Inicializamos el puerto de serie a 9600 baud
    listener()
