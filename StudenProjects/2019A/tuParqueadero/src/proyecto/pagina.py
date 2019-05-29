import rospy, requests, time, sys
from std_msgs.msg import String
numero_anterior=0
disponible_anterior=0

def ini():
  #   Enlace con ROS
    rospy.init_node('ThingSpeak', anonymous=True)
    rospy.Subscriber('numero', String, numero)
    rospy.Subscriber('disponible', String, disponible)
    rospy.spin()


def numero(data):
    global numero_anterior
    numero = data.data
    if numero != numero_anterior:
        print 'El proceso de envio a empezado'
        msg = 'https://api.thingspeak.com/update?api_key=3KP49Z4E0GVT17WA&field1=0'
        msg += str(numero)
        print msg
        print numero
        requests.get(msg)
        sys.exit(1)
    numero_anterior = numero


def disponible(data):
    global disponible_anterior
    disponible = data.data
    if disponible != disponible_anterior:
        print 'humedad_suelo'
        msg1 = 'https://api.thingspeak.com/update?api_key=3KP49Z4E0GVT17WA&field2=0'
        msg1 += str(disponible)
        print msg1
        print disponible
        requests.get(msg1)
        sys.exit(1)
    disponible_anterior = disponible
if __name__ == '__main__':
    ini()
