#!/usr/bin/env python
import rospy
import datetime
from std_msgs.msg import String

flama1 = ""
flama2 = ""
flama3 = ""
temperatura = ""
contador1 = ""
contador2 = ""
#contador3 = ""
nfc = ""

print("listo")

def metodoflama1(datoflama1):
    global flama1
    flama1 = datoflama1.data  
    textoflama1 = "flama1= "
    textoflama2 = "flama2= "
    textoflama3 = "flama3= "
    textotemperatura = "temperatura= "
    textocontador1 = "contador1= "
    textocontador2 = "contador2= "
    #textocontador3 = "contador3= "
    textonfc = "nfc= "
    ahora = datetime.datetime.now()
    ano = ahora.year
    mes = ahora.month
    dia = ahora.day
    hora = ahora.hour
    minutos = ahora.minute
    f = open('/home/ubuntu/Desktop/cajanegra/texto','a')
    f.write(str(dia) + "/" + str(mes) + "/" + str(ano) + "\t" + str(hora) + ":" +str(minutos) +"\t" + textoflama1 + str(flama1) + "\t"+ textoflama2 + str(flama2) + "\t" + textoflama3 + str(flama3) + "\t" + textotemperatura + str(temperatura) + "\t" + textocontador1 + str(contador1) + "\t" + textocontador2 + str(contador2) + "\t" + textonfc + str(nfc) + "\n")
    f.close()
    #print("flama1="+flama1)
    
def metodoflama2(datoflama2):
    global flama2
    flama2 = datoflama2.data 
    textoflama1 = "flama1= "
    textoflama2 = "flama2= "
    textoflama3 = "flama3= "
    textotemperatura = "temperatura= "
    textocontador1 = "contador1= "
    textocontador2 = "contador2= "
    #textocontador3 = "contador3= "
    textonfc = "nfc= "
    ahora = datetime.datetime.now()
    ano = ahora.year
    mes = ahora.month
    dia = ahora.day
    hora = ahora.hour
    minutos = ahora.minute
    f = open('/home/ubuntu/Desktop/cajanegra/texto','a')
    f.write(str(dia) + "/" + str(mes) + "/" + str(ano) + "\t" + str(hora) + ":" +str(minutos) +"\t" + textoflama1 + str(flama1) + "\t"+ textoflama2 + str(flama2) + "\t" + textoflama3 + str(flama3) + "\t" + textotemperatura + str(temperatura) + "\t" + textocontador1 + str(contador1) + "\t" + textocontador2 + str(contador2) + "\t" + textonfc + str(nfc) + "\n")
    f.close()
    #print("flama2="+flama2)
    
def metodoflama3(datoflama3):
    global flama3
    flama3 = datoflama3.data   
    textoflama1 = "flama1= "
    textoflama2 = "flama2= "
    textoflama3 = "flama3= "
    textotemperatura = "temperatura= "
    textocontador1 = "contador1= "
    textocontador2 = "contador2= "
    #textocontador3 = "contador3= "
    textonfc = "nfc= "
    ahora = datetime.datetime.now()
    ano = ahora.year
    mes = ahora.month
    dia = ahora.day
    hora = ahora.hour
    minutos = ahora.minute
    f = open('/home/ubuntu/Desktop/cajanegra/texto','a')
    f.write(str(dia) + "/" + str(mes) + "/" + str(ano) + "\t" + str(hora) + ":" +str(minutos) +"\t" + textoflama1 + str(flama1) + "\t"+ textoflama2 + str(flama2) + "\t" + textoflama3 + str(flama3) + "\t" + textotemperatura + str(temperatura) + "\t" + textocontador1 + str(contador1) + "\t" + textocontador2 + str(contador2) + "\t" + textonfc + str(nfc) + "\n")
    f.close()
    #print("flama3="+flama3)
    
def metodotemperatura(datotemperatura):
    global temperatura
    temperatura = datotemperatura.data 
    textoflama1 = "flama1= "
    textoflama2 = "flama2= "
    textoflama3 = "flama3= "
    textotemperatura = "temperatura= "
    textocontador1 = "contador1= "
    textocontador2 = "contador2= "
    #textocontador3 = "contador3= "
    textonfc = "nfc= "
    ahora = datetime.datetime.now()
    ano = ahora.year
    mes = ahora.month
    dia = ahora.day
    hora = ahora.hour
    minutos = ahora.minute
    print("flama1="+flama1)
    print("flama2="+flama2)
    print("flama3="+flama3)
    print("temperatura="+temperatura)
    print("contador1="+contador1)
    print("contador2="+contador2)
    #print("contador3="+contador3)
    print("nfc="+nfc)
    f = open('/home/ubuntu/Desktop/cajanegra/texto','a')
    f.write(str(dia) + "/" + str(mes) + "/" + str(ano) + "\t" + str(hora) + ":" +str(minutos) +"\t" + textoflama1 + str(flama1) + "\t"+ textoflama2 + str(flama2) + "\t" + textoflama3 + str(flama3) + "\t" + textotemperatura + str(temperatura) + "\t" + textocontador1 + str(contador1) + "\t" + textocontador2 + str(contador2) + "\t" + textonfc + str(nfc) + "\n")
    f.close()
    #print("temperatura="+temperatura)

def metodocontador1(datocontador1):
    global contador1
    contador1 = datocontador1.data
    textoflama1 = "flama1= "
    textoflama2 = "flama2= "
    textoflama3 = "flama3= "
    textotemperatura = "temperatura= "
    textocontador1 = "contador1= "
    textocontador2 = "contador2= "
    #textocontador3 = "contador3= "
    textonfc = "nfc= "
    ahora = datetime.datetime.now()
    ano = ahora.year
    mes = ahora.month
    dia = ahora.day
    hora = ahora.hour
    minutos = ahora.minute
    f = open('/home/ubuntu/Desktop/cajanegra/texto','a')
    f.write(str(dia) + "/" + str(mes) + "/" + str(ano) + "\t" + str(hora) + ":" +str(minutos) +"\t" + textoflama1 + str(flama1) + "\t"+ textoflama2 + str(flama2) + "\t" + textoflama3 + str(flama3) + "\t" + textotemperatura + str(temperatura) + "\t" + textocontador1 + str(contador1) + "\t" + textocontador2 + str(contador2) + "\t" + textonfc + str(nfc) + "\n")
    f.close()
    #print("contador1="+contador1)
    
def metodocontador2(datocontador2):
    global contador2
    contador2 = datocontador2.data 
    textoflama1 = "flama1= "
    textoflama2 = "flama2= "
    textoflama3 = "flama3= "
    textotemperatura = "temperatura= "
    textocontador1 = "contador1= "
    textocontador2 = "contador2= "
    #textocontador3 = "contador3= "
    textonfc = "nfc= "
    ahora = datetime.datetime.now()
    ano = ahora.year
    mes = ahora.month
    dia = ahora.day
    hora = ahora.hour
    minutos = ahora.minute
    f = open('/home/ubuntu/Desktop/cajanegra/texto','a')
    f.write(str(dia) + "/" + str(mes) + "/" + str(ano) + "\t" + str(hora) + ":" +str(minutos) +"\t" + textoflama1 + str(flama1) + "\t"+ textoflama2 + str(flama2) + "\t" + textoflama3 + str(flama3) + "\t" + textotemperatura + str(temperatura) + "\t" + textocontador1 + str(contador1) + "\t" + textocontador2 + str(contador2) + "\t" + textonfc + str(nfc) + "\n")
    f.close()
    #print("contador2="+contador2)
    
"""def metodocontador3(datocontador3):
    global contador3
    contador3 = datocontador3.data 
    textoflama1 = "flama1= "
    textoflama2 = "flama2= "
    textoflama3 = "flama3= "
    textotemperatura = "temperatura= "
    textocontador1 = "contador1= "
    textocontador2 = "contador2= "
    textocontador3 = "contador3= "
    textonfc = "nfc= "
    ahora = datetime.datetime.now()
    ano = ahora.year
    mes = ahora.month
    dia = ahora.day
    hora = ahora.hour
    minutos = ahora.minute
    f = open('/home/ubuntu/Desktop/cajanegra/texto','a')
    f.write(str(dia) + "/" + str(mes) + "/" + str(ano) + "\t" + str(hora) + ":" +str(minutos) +"\t" + textoflama1 + str(flama1) + "\t"+ textoflama2 + str(flama2) + "\t" + textoflama3 + str(flama3) + "\t" + textotemperatura + str(temperatura) + "\t" + textocontador1 + str(contador1) + "\t" + textocontador2 + str(contador2) + "\t" + textocontador3 + str(contador3) + "\t" + textonfc + str(nfc) + "\n")
    f.close()
    #print("contador3="+contador3)"""
    
def metodonfc(datonfc):
    global nfc
    nfc = datonfc.data 
    textoflama1 = "flama1= "
    textoflama2 = "flama2= "
    textoflama3 = "flama3= "
    textotemperatura = "temperatura= "
    textocontador1 = "contador1= "
    textocontador2 = "contador2= "
    #textocontador3 = "contador3= "
    textonfc = "nfc= "
    ahora = datetime.datetime.now()
    ano = ahora.year
    mes = ahora.month
    dia = ahora.day
    hora = ahora.hour
    minutos = ahora.minute
    f = open('/home/ubuntu/Desktop/cajanegra/texto','a')
    f.write(str(dia) + "/" + str(mes) + "/" + str(ano) + "\t" + str(hora) + ":" +str(minutos) +"\t" + textoflama1 + str(flama1) + "\t"+ textoflama2 + str(flama2) + "\t" + textoflama3 + str(flama3) + "\t" + textotemperatura + str(temperatura) + "\t" + textocontador1 + str(contador1) + "\t" + textocontador2 + str(contador2) + "\t" + textonfc + str(nfc) + "\n")
    f.close()
    #print("nfc="+nfc)
    
def listener():    
    rospy.init_node('cajanegra', anonymous=True)

    rospy.Subscriber("flama1", String, metodoflama1)
    rospy.Subscriber("flama2", String, metodoflama2)
    rospy.Subscriber("flama3", String, metodoflama3)
    rospy.Subscriber("temperatura", String, metodotemperatura)
    rospy.Subscriber("contador1", String, metodocontador1)
    rospy.Subscriber("contador2", String, metodocontador2)
    #rospy.Subscriber("contador3", String, metodocontador3)
    rospy.Subscriber("nfc", String, metodonfc)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
if __name__ == '__main__':
    listener()
