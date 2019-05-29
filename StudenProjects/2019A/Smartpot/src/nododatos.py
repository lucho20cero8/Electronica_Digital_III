"""
    nombre:
    nododatos

    descripcion:
    este codigo lo que hace es guardad los datas de lectura
    en un archivo txt

    autores:
    Oscar Daniel Rodriguez Gallego
    Santiago Felipe Ariza londono
    Francisco Javier Franco Beleno

"""
import rospy, time
from std_msgs.msg import String

class datos():
    """docstring fo datos."""
    def __init__(self):
        self.tempsuelo = 0
        self.humedad_suelo = 0
        self.temp_aire = 0
        self.temp_aire = 0
        self.lux = 0
        self.rele =0

    def listener(self):
        rospy.init_node('datos',anonymous=True)
        rospy.Subscriber('ds18b20',String,self.ds18b20)
        rospy.Subscriber('activar_rele', String,self.activar_rele)
        rospy.Subscriber('YL69',String,self.YL69)
        rospy.Subscriber('tempdthsensor',String,self.tempdthsensor)
        rospy.Subscriber('humedaddthsensor',String,self.humedaddthsensor)
        rospy.Subscriber('luxometro',String,self.luxometro)

        rospy.spin()
    ###funciones
    def ds18b20(self,data):
        self.tempsuelo=data.data
        d = time.strftime("%d/%m/%y")
        t = time.strftime("%H:%M:%S")
        d = d + '\t'
        t = t +'\t'
        c = 'temperatura tempsuelo: '+ str(self.tempsuelo) + '\n'
        print 'guardando tempsuelo: '+ str(c)
        f = open ('datos.txt','a')
        f.write(d)
        f.write(t)
        f.write(c)
        f.close()
    def YL69(self,data):
        self.humedad_suelo=data.data
        d = time.strftime("%d/%m/%y")
        t = time.strftime("%H:%M:%S")
        d = d + '\t'
        t = t +'\t'
        c = 'humedad suelo: '+str(self.humedad_suelo) + '\n'
        print 'guardando humedad suelo: '+ str(c)
        f = open ('datos.txt','a')
        f.write(d)
        f.write(t)
        f.write(c)
        f.close()
    def tempdthsensor(self,data):
        self.temp_aire=data.data
        d = time.strftime("%d/%m/%y")
        t = time.strftime("%H:%M:%S")
        d = d + '\t'
        t = t +'\t'
        c = 'temperatura aire: ' + str(self.temp_aire) + '\n'
        print 'guardando temperatura aire: '+ str(c)
        f = open ('datos.txt','a')
        f.write(d)
        f.write(t)
        f.write(c)
        f.close()
    def humedaddthsensor(self,data):
        self.humedad_aire=data.data
        d = time.strftime("%d/%m/%y")
        t = time.strftime("%H:%M:%S")
        d = d + '\t'
        t = t +'\t'
        c = 'humedad aire: ' + str(self.humedad_aire) + '\n'
        print 'guardando humedad aire: '+ str(c)
        f = open ('datos.txt','a')
        f.write(d)
        f.write(t)
        f.write(c)
        f.close()
    def luxometro(self,data):
        self.lux=data.data
        d = time.strftime("%d/%m/%y")
        t = time.strftime("%H:%M:%S")
        d = d + '\t'
        t = t +'\t'
        c = 'lux: ' + str(self.lux) + '\n'
        print 'guardando luz: '+ str(c)
        f = open ('datos.txt','a')
        f.write(d)
        f.write(t)
        f.write(c)
        f.close()
    def activar_rele(self,data):
        self.rele=data.data
        d = time.strftime("%d/%m/%y")
        t = time.strftime("%H:%M:%S")
        d = d + '\t'
        t = t +'\t'
        c = 'rele: ' + str(self.rele) + '\n'
        print 'guardando estado rele: '+ str(c)
        f = open ('datos.txt','a')
        f.write(d)
        f.write(t)
        f.write(c)
        f.close()
if __name__ == '__main__':
#listener()
    while True:
        a=datos()
        a.listener()
        #a.infodatos()
