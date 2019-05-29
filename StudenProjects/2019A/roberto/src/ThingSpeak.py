import rospy
from std_msgs.msg import String
import time
import requests

def callback(data):
    global hum #Inicializa la variable global hum
    fecha=time.strftime("%y/%m/%d") #año/mes/dia actual
    hora=time.strftime("%H:%M:%S") #hora/minuto/segundo actual
    hum=data.data #Obtenemos el dato del topico
    rospy.loginfo(str(fecha) + "\t" + str(hora) + "\t \t"  + str(hum))


def callback1(data):
    global temp #Inicializa la variable global temp
    fecha=time.strftime("%y/%m/%d") #año/mes/dia actual
    hora=time.strftime("%H:%M:%S") #hora/minuto/segundo actual
    temp=data.data #Obtenemos el dato del topico
    rospy.loginfo(str(fecha) + "\t" + str(hora) + "\t \t"  + str(temp))


def callback2(data):
    global ultra #Inicializa la variable global ultra
    fecha=time.strftime("%y/%m/%d") #año/mes/dia actual
    hora=time.strftime("%H:%M:%S") #hora/minuto/segundo actual
    ultra=data.data #Obtenemos el dato del topico
    f=open("/home/ubuntu/Desktop/Black_Box.txt","a") #Abre el archivo .txt en el cual se van a guardar los cambios de los sensores
    rospy.loginfo(str(fecha) + "\t" + str(hora) + "\t \t"  +str(ultra))
    f.write(str(fecha) + "\t" + str(hora) + "\t \t" + str(hum) + " % RH " + str(temp) + " C " + str(ultra) + " cm " + "\n") #Escribe en el archivo las variables
    f.close() #Cierra el archivo guardando los datos

def listener():
    rospy.init_node('ThingSpeak', anonymous=True) #Inicializa el nodo ThingSpeak
    rospy.Subscriber("Hum", String, callback) #Se subscribe al topico Hum en la funcion callback
    rospy.Subscriber("Temp", String, callback1) #Se subscribe al topico Temp en la funcion callback1
    rospy.Subscriber("Ultra", String, callback2) #Se subscribe al topico Ultra en la funcion callback2
    rospy.spin()



if __name__ == '__main__':
    temp=0
    hum=0
    ultra=""
    listener()
