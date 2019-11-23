def saldos(saldo):
    saldos1= saldo
    return (saldos1)
def recargo(saldo,precio):
    sal=saldo-precio
    return (sal)
import serial,time
import numpy as np
import pyttsx3
engine = pyttsx3.init() # object creation
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 200)     # setting up new voice rate
"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)                         #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

while 1:
    arduino = serial.Serial('/dev/ttyUSB0', 9600)
    cedula=0
    print ("welcome")
    precio=1800
    saldolec= arduino.readline()
    saldo=int(saldolec)
    if (saldo <= precio):
        print(saldo)
        engine.say("Hola Usuario!")
        engine.say('Su saldo es insuficiente')
        saldotar=str(recargas)+"#"
        arduino.write(saldotar.encode())
        engine.runAndWait()
        engine.stop()
    elif (saldo>=precio):
        descuento=saldo-1800
        recargas= recargo(saldo,precio)
        saldotar=str(recargas)+"#"
        arduino.write(saldotar.encode())
        time.sleep(1)
        print(recargas)
        engine.say("Hola Usuario!")
        engine.say('Su saldo es ' + str(recargas))
        engine.runAndWait()
        engine.stop()
        arduino.close()
