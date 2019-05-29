import rospy
from std_msgs.msg import String

class Listener():

    def __init__(self):
        rospy.loginfo("Starting node")
        self.pub = rospy.Publisher("MD", String , queue_size=10) #Nodo publicador por el topico MD
        self.pub1 = rospy.Publisher("ML", String , queue_size=10) #Nodo publicador por el topico ML
        rospy.Subscriber('JY' , String, self.callback) #Se subscribe al topico JY en la funcion callback
        rospy.Subscriber('JX' , String, self.callback1) #Se subscribe al topico JX en la funcion callback1
        rospy.spin()

    def callback(self,data):
        global jy   #Se vuelve jy una variable global
        jy=data.data #Obtenemos el dato del topico
        jy= float(jy) #jy se vuelve un dato de tipo float

    def callback1(self,data):
        global jx   #Se vuelve jx una variable global
        jx=data.data #Obtenemos el dato del topico
        jx=float(jx) #jx se vuelve un dato de tipo float

        MD=jy
        ML=jx
        MD=str(MD)
        ML=str(ML)
        self.pub.publish(MD) #Se publica MD
        rospy.loginfo(MD)
        self.pub1.publish(ML) #Se publica ML
        rospy.loginfo(ML)


if __name__ == '__main__':
    jy="" #Inicializa las variables globales
    jx=""
    rospy.init_node('Lis_Mot', anonymous=True) #Inicializa el nodo Lis_Mot
    lis=Listener()
