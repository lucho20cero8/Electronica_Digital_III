#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from flask import Flask, render_template

app = Flask(__name__)
i = -1

# Variables Ambientales

tA = 'No se ha recibido el valor de "Temperatura Absoluta"'
hA = 'No se ha recibido el valor de "Humedad Absoluta"'
hR = 'No se ha recibido el valor de "Humedad Relativa"'
lx = 'No se ha recibido el valor de "Luxios"'
tR = 'No se ha recibido el valor de "Temperatura Relativa"'

# Definiciones

def listener():
 # Se inicia el nodo
 print ('Se iniciara el node listener')
 rospy.init_node('Flask')
 # Subscripciones
 rospy.Subscriber('ds18b20', String, ds18b20)
 rospy.Subscriber('YL69', String, YL69)
 rospy.Subscriber('humedaddthsensor', String, humedaddthsensor)
 rospy.Subscriber('luxometro', String, luxometro)
 rospy.Subscriber('tempdthsensor', String, tempdthsensor)
 #rospy.spin()
 print ('Ha iniciado el nodo "listener"')

# Actuador

@app.route("/")
def hello():
 global i
 i += 1
 # Validacion
 print i
 print tA
 print hA
 print hR
 print lx
 print tR

 #Asignacion

 templateData = {
  'title' : 'SinglePot with Raspberry',			# Titulo de la pagina
  'tA' : tA,						# Temperatura Absoluta
  'hA' : hA,						# Humedad Absoluta
  'hR' : hR,
  'lx' : lx,
  'tR' : tR
 }

 return render_template('main.html', **templateData)

# Temperatura Absoluta
def ds18b20(a):
 global tA
 tA = a.data
 print i
 print tA

# Humedad Absoluta
def YL69(a):
 global hA
 hA = a.data
 print hA

def humedaddthsensor(a):
 global hR
 hR = a.data
 print hR

def luxometro(a):
 global lx
 lx = a.data
 print lx

def tempdthsensor(a):
 global tR
 tR = a.data
 print tR


if __name__ == "__main__":
 listener()
 app.run(host='0.0.0.0', debug=True)
 print ('end')