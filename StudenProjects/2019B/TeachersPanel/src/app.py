#
# Created by:
# Jhon Mendoza
# Camilo Leon
# Julian Alcala
#

import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import xlrd

#configurations PINS
SERVO_PIN = 12
WOW = 21
LED_PIN2 = 20
# Initialize GPIO for LED and button. 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(SERVO_PIN, GPIO.OUT) 
GPIO.output(SERVO_PIN, GPIO.LOW)
GPIO.setup(LED_PIN2, GPIO.LOW) 
GPIO.output(LED_PIN2, GPIO.LOW) 
GPIO.setup(WOW, GPIO.LOW)
GPIO.output(WOW, GPIO.LOW)

#Iniciar Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))

   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   client.subscribe("/profesor1/puerta")
   client.subscribe("/profesor1/estado")
   client.subscribe("/profesor2/puerta")
   client.subscribe("/profesor2/estado")

# The callback for when a PUBLISH message is received from the ESP8266.
def on_message(client, userdata, message):
   GPIO.output(WOW, GPIO.HIGH)
   if message.topic == "/profesor1/puerta":
      # Look at the message data and perform the appropriate action.
      socketio.emit('var_puerta', {'data': message.payload})
      hol=message.payload
      print("valor 1: ")
      print(hol)
      if hol == b'Abierta':
          var=1
          p.ChangeDutyCycle(7.5)
          time.sleep(2)
          print("el var es: ")
          print var
      elif hol == b'Cerrada':
          p.ChangeDutyCycle(12.5)
          time.sleep(2)
          print("el var es: ")
          print var
   if message.topic == "/profesor2/puerta":
      # Look at the message data and perform the appropriate action.
      socketio.emit('var_puerta2', {'data': message.payload})
      hol=message.payload
      print("valor 1: ")
      print(hol)
      if hol == b'Abierta':
          var=1
          p.ChangeDutyCycle(7.5)
          time.sleep(2)
          print("el var es: ")
          print var
      elif hol == b'Cerrada':
          p.ChangeDutyCycle(12.5)
          time.sleep(2)
          print("el var es: ")
          print var
   if message.topic == "/profesor1/estado":
      # Look at the message data and perform the appropriate action. 
      socketio.emit('var_estado', {'data': message.payload})
      hol2=message.payload
      print("valor 2: ")
      print(hol2)
      if hol2 == b'Ocupado':
          GPIO.output(LED_PIN2, GPIO.HIGH) 
      elif hol2 == b'Disponible': 
          GPIO.output(LED_PIN2, GPIO.LOW) 
      elif hol2 == b'TOGGLE': 
          GPIO.output(LED_PIN2, not GPIO.input(LED_PIN2))
   if message.topic == "/profesor2/estado":
      # Look at the message data and perform the appropriate action. 
      socketio.emit('var_estado2', {'data': message.payload})
      hol2=message.payload
      print("valor 2: ")
      print(hol2)
      if hol2 == b'Ocupado':
          GPIO.output(LED_PIN2, GPIO.HIGH) 
      elif hol2 == b'Disponible': 
          GPIO.output(LED_PIN2, GPIO.LOW) 
      elif hol2 == b'TOGGLE': 
          GPIO.output(LED_PIN2, not GPIO.input(LED_PIN2))

mqttc=mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("localhost",1883,60)
mqttc.loop_start()

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   4 : {'name' : 'GPIO 4', 'board' : 'esp8266', 'topic' : 'profesor1/4', 'state' : 'False'},
   5 : {'name' : 'GPIO 5', 'board' : 'esp8266', 'topic' : 'profesor2/5', 'state' : 'False'}
   }

# Put the pin dictionary into the template data dictionary:
templateData = {
   'pins' : pins
   }

@app.route("/")
def main():
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', async_mode=socketio.async_mode, **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<board>/<changePin>/<action>")
def action(board, changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   devicePin = pins[changePin]['name']
   # If the action part of the URL is "1" execute the code indented below:
   global globvar
   if action == "1" and board == 'profesor1':
      mqttc.publish(pins[changePin]['topic'],"1")
      pins[changePin]['state'] = 'True'
   if action == "1" and board == 'profesor2':
      mqttc.publish(pins[changePin]['topic'],"1")
      pins[changePin]['state'] = 'True'
   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }
   return render_template('main.html', **templateData)
@app.route("/horarios")
def horarios():
   filepath = "/home/pi/Desktop/web/Horarios.xlsx"
   openFile = xlrd.open_workbook(filepath)
   sheet = openFile.sheet_by_name("Hoja1")
   print(sheet.nrows)
   #for i in range(sheet.nrows):
   #   print(sheet.cell_value(i,0),"   ",sheet.cell_value(i,1))
   pos00= sheet.cell_value(0,0)
   pos01= sheet.cell_value(0,1)
   pos05= sheet.cell_value(0,5)
   pos10= sheet.cell_value(1,0)
   pos11= sheet.cell_value(1,1)
   pos12= sheet.cell_value(1,2)
   pos14= sheet.cell_value(1,4)
   pos20= sheet.cell_value(2,0)
   pos22= sheet.cell_value(2,2)
   pos23= sheet.cell_value(2,3)
   pos30= sheet.cell_value(3,0)
   pos32= sheet.cell_value(3,2)
   return render_template('horarios.html',pos00=pos00, pos01=pos01, pos05=pos05, pos10=pos10, pos11=pos11, pos12=pos12, pos14=pos14, pos20=pos20, pos22=pos22, pos23=pos23, pos30=pos30, pos32=pos32, **templateData)
@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json data here: ' + str(json))

if __name__ == "__main__":
   socketio.run(app, host='0.0.0.0', port=8001, debug=True)
