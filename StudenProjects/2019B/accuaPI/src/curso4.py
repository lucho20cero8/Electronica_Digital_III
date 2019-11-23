from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import socket
import netifaces as ni
#from email.mime.text import MIMEText
#import smtplib
from flask import Flask, render_template, url_for, redirect, request
from flask_socketio import SocketIO, send
from multiprocessing import Process 
import urllib
import time
import interaccion
import serial
import formulario
import pandas as pd
import numpy as np
import RPi.GPIO as GPIO
import RPi.GPIO as GPIO    #Importamos la librería GPIO
import time
GPIO.setwarnings(False) #Importamos time (time.sleep)
GPIO.setmode(GPIO.BOARD)     #Ponemos la placa en modo BCM
GPIO_TRIGGER = 19          #Usamos el pin GPIO 25 como TRIGGER
GPIO_ECHO    = 15           #Usamos el pin GPIO 7 como ECHO
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  #Configuramos Trigger como salida
GPIO.setup(GPIO_ECHO,GPIO.IN)      #Configuramos Echo como entrada
GPIO.output(GPIO_TRIGGER,False) 
GPIO.setup(13,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
time.sleep(1)





"""def mensaje():
    while(1):
        print (str(phnum))
        time.sleep(1)
 """


        
app=Flask(__name__)

socketio=SocketIO(app)





arduino = serial.Serial('/dev/ttyACM0',9600)
    

def subir():
    while(1):
        direccion = "https://api.thingspeak.com/update?api_key=HJAN065OSHP4UC8D"
    
        dsensores = arduino.readline()
        dtsensores = dsensores.decode()
        sensores = dtsensores.split(",")
    #################### temperatura ####################
        
        temp=sensores[0]
        
        ph=sensores[1].replace("\r\n","")
        #temp = sensores.replace("\r\n","")
    
        
        numero=float(temp)
        letranum=str(temp)
        #global phnum
        letraph=str(ph)
        phnum=float(ph)
        referencias=pd.read_csv('NUMEROS.csv')
        valmaximo=referencias.iloc[0][1]
        valminimo=referencias.iloc[0][2]
        promedio=(valmaximo+valminimo)/2
        print ("el promedio es:  "+ str(promedio))
        
        if (numero<promedio):
                GPIO.output(12,True)
                GPIO.output(13,False)

        else:
                GPIO.output(13,True)
                GPIO.output(12,False)
    #if (numero>valmaximo and numero<numero):
        #interaccion.
        #datos={'TEMPERATURA':[numero],'PH':[phnum]}
        
        #nuevo=pd.DataFrame(datos)
        #nuevo.to_csv('NUMEROS.csv')
        #df=pd.read_csv('NUMEROS.csv')
        #print (df)

        #df=pd.DataFrame(np.array([[numero,phnum]]))
        
        #df=pd.DataFrame(datos)
        #print (datos)
        #print ("esto puede ser" +str(df.iloc[0][1]))
        #print (nuevo)
        
        #if phnum<8.6:
        #        interaccion.Calentador()
        fd = "&field1={}&field2={}".format(temp,ph)
        graficar = urllib.request.urlopen(direccion+fd)
        
        print("la temperatura del agua es: "+ str(numero))
              
        print("el ph del agua es: " + str(phnum))
        
        
        
        


def ultrasonico():
    while (1):     #Iniciamos un loop infinito
        GPIO.output(GPIO_TRIGGER,True)   #Enviamos un pulso de ultrasonidos
        time.sleep(0.00001)              #Una pequeñña pausa
        GPIO.output(GPIO_TRIGGER,False)  #Apagamos el pulso
        start = time.time()              #Guarda el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==0:  #Mientras el sensor no reciba señal...
            start = time.time()          #Mantenemos el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==1:  #Si el sensor recibe señal...
            stop = time.time()           #Guarda el tiempo actual mediante time.time() en otra variable
        elapsed = stop-start
                                        #Obtenemos el tiempo transcurrido entre envío y recepción
        distance = (elapsed * 34300)/2
        if distance<10:
                ni.ifaddresses('eth0')
                IP= ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
                mailServer = smtplib.SMTP('smtp.gmail.com',587)
                mailServer.ehlo()
                mailServer.starttls()
                mailServer.ehlo()
                mailServer.login("2420171086@estudiantesunibague.edu.co","fernanda10")
                print (mailServer.ehlo())
                   #mensaje=MIMEText("Queremos ir al SOFA"
                mensaje = MIMEMultipart()
                mensaje.attach(MIMEText("comida"))
                mensaje['From']="2420171086@estudiantesunibague.edu.co"
                mensaje['To']="2420171086@estudiantesunibague.edu.co"
                mensaje['Subject']="Tienes un mensaje "
                file = open("descarga.jpeg", "rb")
                contenido = MIMEImage(file.read())
                contenido.add_header('Content-Disposition', 'attachment; filename =  "descarga.jpeg"')
                mensaje.attach(contenido)
                mailServer.sendmail("2420171086@estudiantesunibague.edu.co","2420171086@estudiantesunibague.edu.co",mensaje.as_string())
   #Distancia es igual a tiempo por velocidad partido por 2   D = (T x V)/2
        print (str(distance))                  #Devolvemos la distancia (en centímetros) por pantalla
        time.sleep(5)
               #Pequeña pausa para no saturar el procesador de la Raspberry

        
        
"""
#ard= serial.Serial('/dev/ttyACM0',9600)
dsensores = ard.readline()
dtsensores = dsensores.decode()
sensores = dtsensores
#################### temperatura ####################
temp = sensores.replace("\r\n","")
numero=float(temp)"""
def pagina():
    
    #data=arduino.readline()

    #app=Flask(__name__)

    @app.route('/')         
    def inicio():
    
        return render_template('pagina.html')

    @app.route('/menu')
    def menu():
    
        return render_template('menu.html')

    @app.route('/alimentar')
    def Alimentar():
        #arduino= serial.Serial('/dev/ttyACM0',9600)
        time.sleep(2)
        arduino.write('1'.encode())
        #Alimentar()
        #interaccion.Alimento()
        #flash('Se esta alimentando al pez')
        return redirect(url_for('menu'))

    @app.route('/oxigeno')
    def Oxigeno():
        
        interaccion.Oxigeno()
        #flash('se encendio motobomba')
        return redirect(url_for('menu'))

    @app.route('/luces')
    def Luces():
    
        interaccion.Luces()
        #flash('juego de luces')
        return redirect(url_for('menu'))

    @app.route('/calentador')
    def Calentador():
        #if nvalormaximo<9:
        interaccion.Calentador()
        # Imprimir el mesaje con flash
        #flash('se encendio el calentador')
        return redirect(url_for('valores'))
    @app.route('/contacto')
    def contacto():
        return render_template('contacto.html')
    @app.route('/valores')
    def valores():
        return render_template('valores.html')
    @app.route('/valores2', methods=['POST'])
    def valores2():
        valormaximo = request.form['valormaximo']
        global nvalormaximo
        nvalormaximo=float(valormaximo)
        valorminimo=request.form['valorminimo']            
        nvalorminimo=float(valorminimo)
        datos={'MAXIMO':[nvalormaximo],'MINIMO':[nvalorminimo]}

        nuevo=pd.DataFrame(datos)
        nuevo.to_csv('NUMEROS.csv')
        #df=pd.read_csv('NUMEROS.csv')
        #print (df)

        #referencias=pd.read_csv('NUMEROS.csv')
        #referenciatemp=referencias.iloc[0][1]
        #referenciaph=referencias.iloc[0][2]
        #while(nvalormaximo>referenciaph):
               # valormaximo = request.form['valormaximo']
                
                #nvalormaximo=float(valormaximo)
                #valorminimo=request.form['valorminimo']            
                #nvalorminimo=float(valorminimo)
                #referencias=pd.read_csv('NUMEROS.csv')
                #referenciatemp=referencias.iloc[0][1]
                #referenciaph=referencias.iloc[0][2]

                #interaccion.Calentador()
                      
        #while(nvalormaximo>phnum):
        #    interaccion.Calentador()
             
        #return "<h1>el valor del sensor de temperatura es:  "+str(referenciatemp)+"el valor del sensor de ph que entra es de: " + str(referenciaph)+"el valor maximo desde la pagina es"+ valormaximo +"su valor minimo es: " + valorminimo +"</h1>"
        return render_template('valores.html')
    @socketio.on('message')
    def handleMessage(msg):
        print("Message" +msg)

    app.run(host='192.168.1.14', port=7001, debug=True)
    socketio.run(app)
        #return render_template('valores.html')
#subir()
#pagina()
if __name__  == '__main__':
    
    ultrasonic=Process(target=ultrasonico) 
    Servidor=Process(target=pagina)
    Monitoreo=Process(target=subir)
       
    #Prueba=Process(target=tomarvalores,args=(numero,phnum))
    #Prueba=Process(target=mensaje)
    ultrasonic.start()
    Servidor.start()
    Monitoreo.start()
    #Prueba.start()
    #Prueba.start()


    ultrasonic.join()
    Servidor.join()
    Monitoreo.join()
    #Prueba.join()
    #Prueba.join()
