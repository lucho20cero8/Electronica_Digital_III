from flask import Flask, render_template, request
import serial
import pandas as pd
import RPi.GPIO as GPIO

arduino = serial.Serial("/dev/ttyUSB0",baudrate = 9600)
app = Flask(__name__)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)	# GPIO

email = ""
mode = ""
estRiego = ""
estCubierta = ""
lMin = 0
lMax = 0
hMin = 0.0
hMax = 0.0

@app.route("/")
def principal():
	return render_template("principal.html")
@app.route("/correo",methods=["get"])
def correo():
		global email
		email = request.args.get("correo")
		datos()
		print(email)
		return render_template("principal.html",email = email)
@app.route("/modo/<string:modo>")
def estado(modo):
	global mode
	mode = modo
	datos()
	print(mode)
	if modo == "manual":
		return render_template("manual.html")
	else:
		return render_template("automatico.html")
@app.route("/activacion/<string:opcion>")
def activacion(opcion):
	global estRiego,estCubierta
	if opcion == "Activado" or opcion == "Desactivado":
		estRiego = opcion
		datos()
		if opcion == "Activado":
			print(estRiego)
			GPIO.output(7,GPIO.HIGH)
		elif opcion == "Desactivado":
			print(estRiego)
			GPIO.output(7,GPIO.LOW)
	elif opcion == "Desplegada" or opcion == "Plegada":
		estCubierta = opcion
		datos()
		if opcion == "Desplegada" :
			print(estCubierta)
			arduino.write("0".encode())
		elif opcion == "Plegada":
			print(estCubierta)
			arduino.write("1".encode())
	return render_template("manual.html",estRiego = estRiego,estCubierta = estCubierta)
@app.route("/limites",methods=["get"])
def limites():
	global lMin,lMax,hMin,hMax
	lMin = request.args.get("lmin")
	lMax = request.args.get("lmax")
	hMin = request.args.get("hmin")
	hMax = request.args.get("hmax")
	datos()
	print(lMin+"-"+lMax+"-"+hMin+"-"+hMax)
	return render_template("automatico.html",lMin = lMin,lMax = lMax,hMin = hMin,hMax = hMax)

def datos():
	global email,mode,estRiego,estCubierta,lMin,lMax,hMin,hMax
	correo = str(email)
	modo = str(mode)
	estadoRiego = str(estRiego)
	estadoCubierta = str(estCubierta)
	ilMin = int(lMin)
	ilMax = int(lMax)
	phMin = float(hMin)
	phMax = float(hMax)
	datos = {"Correo":[correo],"Modo":[modo],"Sistema de Riego":[estadoRiego],"Cubierta":[estadoCubierta],"Intensidad de Luz Minima":[ilMin],"Intensidad de Luz Maxima":[ilMax],"Porcentaje de Humedad Minimo":[phMin],"Porcentaje de Humedad Maximo":[phMax]}
	informacion = pd.DataFrame(datos)
	informacion.to_csv("datos.csv")

while 1:
	app.run(host = "0.0.0.0", port = 8000, debug = True)
