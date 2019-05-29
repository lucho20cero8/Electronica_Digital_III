"""
    nombre:
    nodocontrol

    descripcion:
    este nodo permir hace control de las variables y en base a eso
    se toman deciciones.

    autores:
    Oscar Daniel Rodriguez Gallego
    Santiago Felipe Ariza londono
    Francisco Javier Franco Beleno

"""
import rospy,time
from std_msgs.msg import String

def ini():
    #   Enlace con ROS
    rospy.init_node('control',anonymous=True)
    rospy.Subscriber('ds18b20', String)
    rospy.Subscriber('YL69', String, control)
    rospy.Subscriber('tempdthsensor', String)
    rospy.Subscriber('humedaddthsensor', String)
    rospy.Subscriber('luxometro', String)
    #   rospy.Subscriber('estado_rele', String)
    rospy.spin()
def control(data):
    pub=rospy.Publisher('activar_rele', String)
    rate = rospy.Rate(10000)
    humedad_suelo= data.data
    print 'humedad en porcentaje: '+ humedad_suelo
    if humedad_suelo <= '35':
        estado_rele='1'
        print estado_rele
    elif humedad_suelo > '35':
        estado_rele='0'
        print estado_rele
    else:
        pass
    pub.publish(estado_rele)
if __name__ == '__main__':
    ini()
