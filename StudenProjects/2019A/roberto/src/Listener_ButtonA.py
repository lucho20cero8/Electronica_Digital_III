import rospy
from std_msgs.msg import String
import datetime
import socket

def callback(data):
    A=data.data #Obtiene los datos del topico
    rospy.loginfo(str(A))
    message = A
    message = message.encode() #Codifica la variable message para enviarla
    try:
        socket.sendto(message, ("10.42.0.1", 8080)) #Envio del mensaje por el puerto 8080
    except socket.error:
        print("Error! {}".format(socket.error)) #Imprime si hubo un error en el envio
        exit()

def listener():
    rospy.init_node('ListenerC3', anonymous=True) #Inicialiacion del nodo ListenerC3
    rospy.Subscriber("B_A", String, callback) #Se subscribe al topico B_A
    rospy.spin()

if __name__ == '__main__':
    try:
        socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Se conecta al servidor
    except socket.error:
        print("Ops, something went wrong connecting the socket") #Mensaje de error por el servidor 
        exit()
    listener()
