"""
    nombre:
    pagina

    descripcion:
    Este codigo lo que permite es enviar los datos de lectura a una pagina thingspeak
    autores:
    Oscar Daniel Rodriguez Gallego
    Santiago Felipe Ariza londono
    Francisco Javier Franco Beleno

"""
import rospy, requests, time
from std_msgs.msg import String

def ini():
    #   Enlace con ROS
    rospy.init_node('ThingSpeak', anonymous=True)
    rospy.Subscriber('ds18b20', String, send)
    rospy.Subscriber('YL69', String, humedad_suelo)
    rospy.Subscriber('tempdthsensor', String, tempdthsensor)
    rospy.Subscriber('humedaddthsensor', String, humedaddthsensor)
    rospy.Subscriber('luxometro', String, luxometro)
    rospy.Subscriber('activar_rele', String, estado_rele)
    rospy.spin()

def send(data):
    g = data.data
    print 'El proceso de envio a empezado'
    msg = 'https://api.thingspeak.com/update?api_key=MRYXRD1QWTXZY8RH&field1=0'
    msg += str(g)
    print msg
    requests.get(msg)
def humedad_suelo(data):
    hume=data.data
    print 'humedad_suelo'
    msg1 = 'https://api.thingspeak.com/update?api_key=MRYXRD1QWTXZY8RH&field3=0'
    msg1 += str(hume)
    print msg1
    requests.get(msg1)
def tempdthsensor(data):
    tempdth=data.data
    print 'Temperatura_dth'
    msg2 = 'https://api.thingspeak.com/update?api_key=MRYXRD1QWTXZY8RH&field5=0'
    msg2 += str(tempdth)
    print msg2
    requests.get(msg2)
def humedaddthsensor(data):
    humedaddth=data.data
    print 'humedad_aire'
    msg3 = 'https://api.thingspeak.com/update?api_key=MRYXRD1QWTXZY8RH&field2=0'
    msg3 += str(humedaddth)
    print msg3
    requests.get(msg3)
def luxometro(data):
    lux=data.data
    print 'lux'
    msg4 = 'https://api.thingspeak.com/update?api_key=MRYXRD1QWTXZY8RH&field4=0'
    msg4 += str(lux)
    print msg4
    requests.get(msg4)
def estado_rele(data):
    rele=data.data
    print 'estado rele'
    msg5 = 'https://api.thingspeak.com/update?api_key=MRYXRD1QWTXZY8RH&field6=0'
    msg5 += str(rele)
    print msg5
    requests.get(msg5)
ini()
