import rospy
from std_msgs.msg import String
import time
import sys
import serial


def talker():
    pub = rospy.Publisher('Hum', String, queue_size=10) #Inicialiacion del publicador de la variable hum(Humedad)
    pub1 = rospy.Publisher('Temp', String, queue_size=10) #Inicialiacion del publicador de la variable temp(Temperatura)
    pub2 = rospy.Publisher('Ultra', String, queue_size=10) #Inicialiacion del publicador de la variable ultra(Ultrasonido)
    rospy.init_node('talker_tem_hum_ultra', anonymous=True)  #Inicialiacion del nodo talker_tem_hum_ultra
    arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=30) #Inicialiacion del puerto serial ACM0
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        datos= arduinoPort.readline() #Lee el puerto serial del arduino
        hume=datos[0:2] #Separa los datos que llegan del arduino
        temp=datos[3:8]
        ultra=datos[9:15]
	    ultra1=float(ultra)
        rospy.loginfo(hume + " %RH")
        rospy.loginfo(temp + " C")
        rospy.loginfo(ultra + " CM")
        pub.publish(hume) #Publica la variable hume por el topico Hum
        pub1.publish(temp) #Publica la variable temp por el topico Temp
        pub2.publish(ultra) #Publica la variable ultra por el topic Ultra
	    if ultra1 < 10.0:
		     print ("Muy cerca de algun objeto, cuidado") #Imprime en pantalla si el Ultrasonido detecta que esta a menos de 10 cm de distancia
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
