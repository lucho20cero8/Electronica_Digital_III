import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
class Listener():

    def __init__(self):
        rospy.loginfo("Starting node")
        rospy.Subscriber('B_A' , String, self.callback) #Se subscribe al topico JY en la funcion callback
        self.flag=0 #Inicializa una variable llamada flag en 0
        rospy.spin()

    def callback(self,data):

        A=data.data #Obtenemos los datos del topico
        if self.flag == 0:
            GPIO.output(12, GPIO.LOW) #El pin 12 del GPIO se vuelve 0
        elif self.flag == 1:
            GPIO.output(12, GPIO.HIGH) #El pin 12 del GPIO se vuelve 1

        if A == '1':
            self.flag=not(self.flag) #Cambia el estado de la variable flag a su contraria si cambia el estado del topico
	rospy.loginfo(A)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD) #Inicia el GPIO de la raspberry
    GPIO.setup(12,GPIO.OUT) #Inicia el pin 12 como una salida
    rospy.init_node('Lis_But_A', anonymous=True) #Inicialiacion del nodo Lis_But_A
    lis=Listener()
