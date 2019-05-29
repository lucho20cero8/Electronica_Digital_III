"""
    nombre:
    nodorele

    descripcion:
    este codigo lo que hace es controlar el estado del auctuador

    autores:
    Oscar Daniel Rodriguez Gallego
    Santiago Felipe Ariza londono
    Francisco Javier Franco Beleno

"""
import rospy
import RPi.GPIO as gpio#importo la libreria GPIO
from std_msgs.msg import String

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
class rele():
    """docstring for ."""
    def __init__(self):

        rospy.init_node('rele', anonymous=True ) # nombre del nodo
        rospy.Subscriber('activar_rele', String, self.activar)
        rospy.spin()
    def activar(self,data):

        act=data.data
        print 'activacion: '+ act
        if act=='1':
            print 'Moto bomba on'
            gpio.output(12, False)
            estado_rele='1'
            print estado_rele

        elif act =='0':
            print 'Moto bomba off'
            gpio.output(12  , True)
            estado_rele='0'
            print estado_rele
if __name__ == '__main__':
    while True:
        r=rele()
