#Librerias
import serial,math,smtplib,time,threading,itertools,urllib.request
import os.path as op
from datetime import date,timedelta,datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from time import time,clock
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import pink, green, brown, white

#Serial
Arduino=serial.Serial("/dev/ttyACM1",baudrate=9600,timeout=10)

#Main
if __name__ =="__main__":

	#Variables Corriente
	sumatoria=0
	sumatoria1=0
	sumatoria2=0
	sumatoria3=0
	bandera=0
	bandera1=0
	bandera2=0
	bandera3=0
	corriente_negativa=0

	#Variables Voltaje
	sumatoria4=0
	sumatoria5=0
	sumatoria6=0
	sumatoria7=0
	bandera4=0
	bandera5=0
	bandera6=0
	bandera7=0
	voltaje_negativo=0

	#Variables Potencia
	potencia1=0
	potencia2=0
	potencia3=0
	potencia4=0
	potencia5=0
	potencia6=0
	potencia7=0
	potencia8=0
	potencia9=0
	potencia10=0
	potencia_filtrada=0
	bandera_potencia_hora=0
	potencia_hora=0
	potencia_kwh=0
	potencia_actual=0
	potencia_anterior=0

	#Otras Constantes
	cont=0
	b=0
	d=0
	f=0

	while(True):

		##Lectura Arduino##
		data= str(Arduino.readline())
		separado= str.split(data,":")
		separado_2= str.split(separado[0],"'")
		separado_3= str.split(separado[1],"\\")
		#separado_4= str.split(separado[2],"\\")
		A= float(separado_2[1])
		B= float(separado_3[0])
		C= float(separado_4[0])


		##Factor de potencia##
		cosenofi= math.cos(C)
		cosenofi= round(cosenofi,3)
		cosenofi= abs(cosenofi)


		##Corriente##
		data1= A - 2.5
		corriente= data1*12
		if(corriente_negativa<corriente):
			corriente_negativa= corriente
			bandera= bandera + 1
			cont= cont + 1
			sumatoria= sumatoria + (corriente_negativa**2)
		elif(corriente_negativa>corriente):
			corriente_negativa= corriente
			bandera1= bandera1 + 1
			sumatoria1=sumatoria1 + (corriente_negativa**2)
		elif(corriente_negativa<corriente):
			corriente_negativa= corriente
			bandera2= bandera2 + 1
			sumatoria2= sumatoria2 + (corriente_negativa**2)
		elif(corriente_negativa>corriente):
			corriente_negativa= corriente
			bandera3= bandera3 + 1
			sumatoria3= sumatoria3 + (corriente_negativa**2)
		elif(corriente==0):
			corriente=0
			sumatoria=0
			sumatoria1=0
			sumatoria2=0
			sumatoria3=0

		if(bandera!=0 or bandera1!=0 or bandera2!=0 or bandera3!=0):
			corriente= sumatoria + sumatoria1
			banderax= bandera + bandera1 + bandera2 + bandera3
			corriente= math.sqrt(corriente / banderax)
			corriente= round(corriente,3)


		##Voltaje##
		data2= B - 2.5
		voltaje= data2*(115/12)*(24/5)
		if(voltaje_negativo<voltaje):
			voltaje_negativo= voltaje
			bandera4= bandera4 + 1
			sumatoria4= sumatoria4 + (voltaje_negativo**2)
		elif(voltaje_negativo>voltaje):
			voltaje_negativo= voltaje
			bandera5= bandera5 + 1
			sumatoria5= sumatoria5 + (voltaje_negativo**2)
		elif(voltaje_negativo<voltaje):
			voltaje_negativo= voltaje
			bandera6= bandera6 + 1
			sumatoria6= sumatoria6 + (voltaje_negativo**2)
		elif(voltaje_negativo>voltaje):
			voltaje_negativo= voltaje
			bandera7= bandera7 + 1
			sumatoria7= sumatoria7 + (voltaje_negativo**2)
		elif(voltaje==0):
			voltaje=0
			sumatoria4=0
			sumatoria5=0
			sumatoria6=0
			sumatoria7=0

		if(bandera4!=0 or bandera5!=0 or bandera6!=0 or bandera7!=0):
			voltaje= sumatoria4 + sumatoria5 
			banderay= bandera4 + bandera5 + bandera6+ bandera7
			voltaje= math.sqrt(2*voltaje / banderay)
			voltaje= round(voltaje,3)


		##Inicio Calculo potencia##

		#Potencia Promedio
		potencia= corriente*voltaje

		potencia10=potencia9
		potencia9=potencia8
		potencia8=potencia7
		potencia7=potencia6
		potencia6=potencia5
		potencia5=potencia4
		potencia4=potencia3
		potencia3=potencia2
		potencia2=potencia1
		potencia1=potencia

		potencia_filtrada= (potencia + potencia1 + potencia2 + potencia3 + potencia4 + potencia5 + potencia6 + potencia7 + potencia8 + potencia9 + potencia10) / 11
		potencia_filtrada= round(potencia_filtrada,3)

		bandera_potencia_hora= bandera_potencia_hora + 1
		potencia_hora= potencia_hora + potencia_filtrada
		potencia_hora= potencia_hora / bandera_potencia_hora

		#Potencia Hora
		a=clock()
		if(a-b > 1):#60
			potencia_kwh= (potencia_hora*1)/1000
			potencia_kwh= round(potencia_kwh,3)
			b=a

		potencia_anterior= potencia_actual
		potencia_actual= potencia_kwh

		#Impresion Potencia
		if(cont==30):
			print("I:     "+"V:     "+"P:     ")
			print(corriente , voltaje , potencia_filtrada)
			cont=0


		##Correo##
		c=clock()
		if(c-d > 30):#180
			#Estructura
			anfitrion = "smtp.gmail.com"
			puerto = 587
			direccionDe = "2420171047@estudiantesunibague.edu.co"
			contrasenaDe = "camilo900613"
			direccionPara = "2420171040@estudiantesunibague.edu.co"
			servidor = smtplib.SMTP(anfitrion,puerto)
			servidor.starttls()
			servidor.login(direccionDe,contrasenaDe)
			print("")
			print("Enviando Factura...")
			print("")
			asunto = "Medielectric"
			correo = MIMEMultipart()
			correo['From'] = direccionDe
			correo['To'] = direccionPara
			correo['Subject'] = asunto
			#Logo
			file = open("logo.png", "rb")
			attach_image = MIMEImage(file.read())
			attach_image.add_header('Content-Disposition', 'attachment; filename = "logo.png"')
			correo.attach(attach_image)
			#Mensaje
			message = """Estimado usuario, Juan Camilo Buitrago Diaz
Como está acordado en el contrato de mensualidad de pago se le anexa el recibo eléctrico para su cancelación.

Su fiel y eficiente servicio Medielectric estará atento y dipuesto a servirlo en lo que podamos.

Número de contacto #1: 272 56 47
Número de contacto #2: 312 313 02 07

                                        Fan page:
								www.facebook.com/Medielectric
							  	   www.Medielectric.com
 """
			#Archivo adjundo
			part = MIMEBase('application', "octet-stream")
			part.set_payload(open("reciboPdf_tablas_si.pdf", "rb").read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition',
                        'attachment; filename="Recibo electrico"')
			correo.attach(part)

			mensaje = MIMEText(message)
			correo.attach(mensaje)
			servidor.sendmail(direccionDe,direccionPara,correo.as_string())
			d=c


		##ThingSpeak##
		e=clock()
		if(e-f > 10):#90
			val=potencia_filtrada
			val1=corriente
			val2=voltaje
			URL='https://api.thingspeak.com/update?api_key='
			KEY='R13A4I1DK051F8TV'
			HEADER='&field1={}&field2={}&field3={}'.format(val,val1,val2)
			new_URL=URL+KEY+HEADER
			print("")
			print("Subiendo Informormacion al ThingSpeak...")
			print("")
			datos=urllib.request.urlopen(new_URL)
			f=e


		##Documento pdf##
		Titulo= 'Recibo Eléctrico'
		#potencia_actual=potencia_kwh
		#potencia_anterior=potencia_anterior
		factor_potencia=cosenofi
		c=canvas.Canvas("reciboPdf_tablas_si.pdf")
		hoy=date.today()
		mes_actual=hoy.month
		mes_pasado=hoy-timedelta(days=31)
		mes_pasado=mes_pasado.month
		valor_kwh=550

		#Ancho de linea
		c.setLineWidth(.3)

		#Fuente y tamano
		c.setFont('Helvetica',14)

		#Dibuja texto en posicion X y Y por puntos. 1pt= 1/72 pulgadas
		c.drawString(400,630,"Fecha:  " + str(hoy))
		c.drawString(100,630,"Titular:    Juan Camilo Buitrago Diaz ")
		c.drawString(100,600,"Dirección:  Avenida Ferrocarril")
		c.drawString(100,570,"Manzana 29, Casa 16")
		c.drawString(195,492,"Medición de consumo")
		c.drawString(148,472,"Mes")
		c.drawString(150,452,str(mes_actual))
		c.drawString(150,432,str(mes_pasado))
		c.drawString(262,472,"Kwh")
		c.drawString(262,452,str(potencia_filtrada))
		c.drawString(262,432,str(potencia_anterior))
		c.drawString(360,472,"Valor a pagar")
		c.drawString(378,452,"$"+str(round(valor_kwh*potencia_filtrada,2)))
		c.drawString(378,432,"$"+str(round(valor_kwh*potencia_anterior,2)))
		c.drawString(220,300,"Desplazamiento de fase ",2)
		c.drawString(285,270,str(factor_potencia))
		c.drawString(104,402,"Valor Kwh")
		c.drawString(262,402,"$"+str(valor_kwh))
		#Posicion X1 Y1 X2 Y2
		c.line(150,628,330,628)
		c.line(167,598,297,598)
		c.line(450,628,525,628)

		#Imagen
		c.drawImage("logo.png", 420, 725,width=150, height=100)
		c.drawImage("logo2.png", 450, 415,width=150, height=100)
		c.drawImage("frame.png", 210, 30,width=180, height=180)

		#Tabla
		c.setFillColorRGB(255, 0,0 )
		c.setFont("Courier-Bold", 25)
		c.drawCentredString(290,700, Titulo)

		#Rectangulo (cx,cy,ancho,alto)
		c.rect(100,490,360,20)
		c.rect(100,470,120,20)
		c.rect(220,470,120,20)
		c.rect(340,470,120,20)
		c.rect(100,450,120,20)
		c.rect(220,450,120,20)
		c.rect(340,450,120,20)
		c.rect(100,430,120,20)
		c.rect(220,430,120,20)
		c.rect(340,430,120,20)
		c.rect(100,400,120,20)
		c.rect(220,400,120,20)

		#Circulo (cx,cy,ancho,alto)
		c.circle(300,300,90,1)

		#Escribe y guarda el documento
		c.showPage()
		c.save()
