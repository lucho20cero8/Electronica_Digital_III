"""
    nombre:
    nodoserial

    descripcion:
    Este codigo lo que hace es tomar la lectura que se hace en el micro controlador
    de forma serial y poderlos usar en python

    autores:
    Oscar Daniel Rodriguez Gallego
    Santiago Felipe Ariza londono
    Francisco Javier Franco Beleno

"""
import serial, rospy, time
from std_msgs.msg import String
##_______________________
#import random
#import requests

#importar la libreria
def serialardunio():
    #publicaciones de los diferenres sensores
    pubabs = rospy.Publisher('ds18b20', String)
    pubhumsuelo = rospy.Publisher('YL69', String)
    pubtemperatura = rospy.Publisher('tempdthsensor', String)
    pubhumedadaire = rospy.Publisher('humedaddthsensor',String)
    publuz = rospy.Publisher('luxometro', String)

    rospy.init_node('serial',anonymous=True)
    rate = rospy.Rate(10000) # 10hz
    arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

    while not rospy.is_shutdown():
        #guardo los datos leidos en un archivo

        lectura= arduinoPort.readline()
        a=lectura.strip(" \r\n")
        c=str(a)
        b=c.split(':')
        print b

        ####humedad suelo
        #time.sleep(1)
        humedad_suelo=b[3]
        #print "humedad del suelo %: "+ humedad_suelo
        ###temperatura del ambiente
        Temperatura_dth=b[5]
        #print "la temperatura: "+Temperatura_dth
        ###para la humedad del aire
        humedad_aire=b[7]
        #print "la humedad_aire: "+humedad_aire
        ###cantidad de luz
        lux=b[9]
        #print "light_intesnsity:"+lux
        ####temperatura del suelo
        tempsuelo=b[11]
        #print "Temp suelo: "+ tempsuelo


        pubhumsuelo.publish(humedad_suelo)
        pubtemperatura.publish(Temperatura_dth)
        pubhumedadaire.publish(humedad_aire)
        publuz.publish(lux)
        pubabs.publish(tempsuelo)

if __name__ == '__main__':
    try:
        serialardunio()
    except IndexError:
        print 'se reinico el sistema '
        time.sleep(1)
        serialardunio()
    #except rospy.ROSInterruptException:
        #serialardunio()
