import urllib2, serial, time, smtplib, netifaces
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd
import RPi.GPIO as GPIO

time.sleep(10)

arduino = serial.Serial("/dev/ttyUSB0",baudrate = 9600)
direccion = "https://api.thingspeak.com/update?api_key=5WF21AVEQHWJSC6E"
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)	# GPIO

modo = "automatico"
bdCorreo = 0
usPromL = 0
usPromH = 0.0
contador = 0

def thingspeak():
	field = "&field1={}&field2={}&field3={}".format(intLuz,prHumedad,prTanque)
	graficar = urllib2.urlopen(direccion+field)
	print(graficar)

def notificaciones():
	global bdCorreo
	if bdCorreo == 0:
		if modo == "automatico":
			prePromL = 1000
			prePromH = 30.0
			if prTanque == "15":
				asunto = "SelFARMING: Tanque en nivel bajo"
				mensaje = """Estimado usuario, el nivel de agua del tanque es menor o igual al 15%, se solicita vertir agua al tanque lo mas pronto posible."""
				rutaImagen = "/home/pi/Desktop/SELFARMING/15.png"
				correo(asunto,mensaje,rutaImagen)
				bdCorreo = 1
			elif prTanque == "50":
				asunto = "SelFARMING: Tanque en nivel medio"
				mensaje = """Estimado usuario, el nivel de agua del tanque es menor o igual al 50%, se recomienda vertir agua."""
				rutaImagen = "/home/pi/Desktop/SELFARMING/50.png"
				correo(asunto,mensaje,rutaImagen)
				bdCorreo = 1
			if bool(usPromL) == False and bool(usPromH) == False:
				if intLuz <= prePromL:
					arduino.write("1".encode())
					asunto = "SelFARMING: Cubierta plegada"
					mensaje = """Estimado usuario, la intensidad luz captada por el cultivo es menor a los {} lux preestablecidos en el sistema. Por tanto, se plego la cubierta para favorecer los procesos nutricionales del cultivo.""".format(prePromL)
					rutaImagen = "/home/pi/Desktop/SELFARMING/cubierta.jpg"
					correo(asunto,mensaje,rutaImagen)
					bdCorreo = 1
				elif intLuz > prePromL:
					arduino.write("0".encode())
					asunto = "SelFARMING: Cubierta desplegada"
					mensaje = """Estimado usuario, la intensidad de luz captada por el cultivo ha superado los {} lux preestablecidos en el sistema. Por tanto, se desplego la cubierta para proteger el cultivo de resecamiento.""".format(prePromL)
					rutaImagen = "/home/pi/Desktop/SELFARMING/cubierta.jpg"
					correo(asunto,mensaje,rutaImagen)
					bdCorreo = 1
				if prHumedad <= prePromH:
					GPIO.output(7,GPIO.HIGH)
					asunto = "SelFARMING: Sistema de riego activado"
					mensaje = """Estimado usuario, la humedad del suelo en el cultivo es menor al {}% preestablecido por el sistema. Por tanto, se activo el sistema de riego para mantener correctamente hidratado al cultivo.""".format(prePromH)
					rutaImagen = "/home/pi/Desktop/SELFARMING/gota.png"
					correo(asunto,mensaje,rutaImagen)
					bdCorreo = 1
				elif prHumead > prePromH:
					GPIO.output(7,GPIO.LOW)
					asunto = "SelFARMING: Sistema de riego desactivado"
					mensaje = """Estimado usuario, la humedad del suelo en el cultivo ha superado al {}% preestablecido por el sistema. Por tanto, se desactivo el sistema de riego para no sobre-hidratar al cultivo.""".format(prePromH)
					rutaImagen = "/home/pi/Desktop/SELFARMING/gota.png"
					correo(asunto,mensaje,rutaImagen)
					bdCorreo = 1
			else:
				if intLuz <= usPromL:
					arduino.write("1".encode())
					asunto = "SelFARMING: Cubierta plegada"
					mensaje = """Estimado usuario, la intensidad de luz captada por el cultivo es menor a los {} lux promediados con sus limites. Por tanto, se plego la cubierta para favorecer los procesos nutricionales del cultivo.""".format(usPromL)
					rutaImagen = "/home/pi/Desktop/SELFARMING/cubierta.jpg"
					correo(asunto,mensaje,rutaImagen)
					bdCorreo = 1
				elif intLuz > usPromL:
					arduino.write("0".encode())
					asunto = "SelFARMING: Cubierta desplegada"
					mensaje = """Estimado usuario, la intensidad de luz captada por el cultivo ha superado los {} lux promediados con sus limites. Por tanto, se desplego la cubierta para proteger el cultivo de resecamiento.""".format(usPromL)
					rutaImagen = "/home/pi/Desktop/SELFARMING/cubierta.jpg"
					correo(asunto,mensaje,rutaImagen)
					bdCorreo = 1
				if prHumedad == 1:
					GPIO.output(7,GPIO.HIGH)
					asunto = "SelFARMING: Sistema de riego activado"
					mensaje = """Estimado usuario, la humedad del suelo en el cultivo es menor al {}% promediado con sus limites. Por tanto, se activo el sistema de riego para mantener correctamente hidratado al cultivo.""".format(usPromH)
					rutaImagen = "/home/pi/Desktop/SELFARMING/gota.png"
					correo(asunto,mensaje,rutaImagen)
					bdCorreo = 1
				elif prHumedad == 0:
					GPIO.output(7,GPIO.LOW)
					asunto = "SelFARMING: Sistema de riego desactivado"
					mensaje = """Estimado usuario, la humedad del suelo en el cultivo es menor al {}% promediado con sus limites. Por tanto, se desactivo el sistema de riego para no sobre-hidratar al cultivo.""".format(usPromH)
					rutaImagen = "/home/pi/Desktop/SELFARMING/gota.png"
					correo(asunto,mensaje,rutaImagen)
					bdCorreo = 1
		else:
			if estRiego == "Activado":
				asunto = "SelFARMING: Sistema de riego activado"
				mensaje = """Estimado usuario, se activo manualmente el sistema de riego."""
				rutaImagen = "/home/pi/Desktop/SELFARMING/gota.png"
				correo(asunto,mensaje,rutaImagen)
				bdCorreo = 1
			elif estRiego == "Desactivado":
				asunto = "SelFARMING: Sistema de riego desactivado"
				mensaje = """Estimado usuario, se desactivo manualmente el sistema de riego."""
				rutaImagen = "/home/pi/Desktop/SELFARMING/gota.png"
				correo(asunto,mensaje,rutaImagen)
				bdCorreo = 1
			if estCubierta == "Desplegada":
				asunto = "SelFARMING: Cubierta desplegada"
				mensaje = """Estimado usuario, se desplego manualmente la cubierta."""
				rutaImagen = "/home/pi/Desktop/SELFARMING/cubierta.jpg"
				correo(asunto,mensaje,rutaImagen)
				bdCorreo = 1
			elif estRiego == "Plegada":
				asunto = "SelFARMING: Cubierta plegada"
				mensaje = """Estimado usuario, se plego manualmente la cubierta."""
				rutaImagen = "/home/pi/Desktop/SELFARMING/cubierta.jpg"
				correo(asunto,mensaje,rutaImagen)
				bdCorreo = 1
	else:
		global contador
		contador = contador+1
		if contador == 2:
			bdCorreo = 0
			contador = 0

def correo(asunto,mensaje,rutaImagen):
	proveedor = "smtp.gmail.com"
	puerto = 587
	dRemitente = "selfarming@gmail.com"
	cRemitente = "jsm040867"
	dDestinatario = "selfarming@gmail.com"

	servidor = smtplib.SMTP(proveedor,puerto)
	servidor.starttls()
	servidor.login(dRemitente,cRemitente)
	print(servidor.ehlo())

	correo = MIMEMultipart()
	correo["From"] = dRemitente
	correo["To"] = dDestinatario
	correo["Subject"] = asunto

	netifaces.ifaddresses("eth0")

	message = MIMEText(mensaje)
	correo.attach(message)

	picture = open(rutaImagen,"rb")
	imagen = MIMEImage(picture.read())
	particion = rutaImagen.split("/")
	nombreImagen = particion[4]
	imagen.add_header("Content-Disposition","attachment",filename = nombreImagen)
	correo.attach(imagen)

	servidor.sendmail(dRemitente,dDestinatario,correo.as_string())
	servidor.quit()

while 1:
	dSensores = arduino.readline()
	dtSensores = dSensores.decode()
	sensores = dtSensores.split(",")

	intLuz = sensores[0]
	prHumedad = sensores[1]
	nivTanque = sensores[2].replace("\r\n","")
	if nivTanque == "00":
		prTanque = "15"
	elif nivTanque == "01":
		prTanque = "50"
	elif nivTanque == "10":
		pass
	elif nivTanque == "11":
		prTanque = "100"

	thingspeak()

	datos = pd.read_csv("datos.csv")

	email = str(datos.iloc[0][1])
	estCubierta = str(datos.iloc[0][2])
	usLMax = int(datos.iloc[0][3])
	usLMin = int(datos.iloc[0][4])
	modo = str(datos.iloc[0][5])
	usHMax = float(datos.iloc[0][6])
	usHMin = float(datos.iloc[0][7])
	estRiego = str(datos.iloc[0][8])

	usPromL = (usLMax+usLMin)/2
	usPromH = (usHMax+usHMin)/2.0

	if prHumedad <= usPromH:
		prHumedad = 1
	elif prHumedad > usPromH:
		prHumedad = 0

	dDestinatario = email

	notificaciones()

	time.sleep(15)
