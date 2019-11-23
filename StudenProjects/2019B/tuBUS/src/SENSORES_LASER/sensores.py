##
#Libraries needed to send mail
##
import serial, time   #Libraries needed to communicate the Arduino by serial
import smtplib
import netifaces as ni
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

Arduino=serial.Serial('/dev/ttyUSB0', 9600)  #I read the data coming from the arduino using the USB cable
Arduino.flushInput()


def mail(): #Define the option that allows you to send the mail
    remitente = '2420171024@estudiantesunibague.edu.co'  #The mail sender is defined
    destinatarios = ['buscontrol357@gmail.com']     #The mail recipient is defined
    asunto = 'INFORME SOBRE LOS USUARIOS DEL BUS'   #Mail subject is defined
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
#What you want to see in the body of the message is edited in our case a detailed report of the bus system
    cuerpo = "Hola.\nEl informe de los usuarios del bus son:\n*Personas que no pagaron: "  +'%s\n'%np+  "*Entraron: "  +'%s\n'%i+ "*Salieron:  "   +'%s\n'%s+ "El producido del dia de su bus es aproximadamente:    "" $ " +'%s\n'%saldo+ "Las perdididas por concepto de personas que no pagaron el pasajes es de aproximadamente :   " " -$"  +'%s'%perdidas
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    sesion_smtp.login('2420171024@estudiantesunibague.edu.co','CONTRASEÑA') #Mail and password to login from the sender and send the message
    texto = mensaje.as_string()
    sesion_smtp.sendmail(remitente, destinatarios, texto)
    sesion_smtp.quit()  #Once you finish sending it, close the sender's email session



if __name__ == "__main__":
        i = 0
        np = 0
        s = 0
        bandera = 1
	saldo = 0
	perdidas = 0
	hora ='15:25:00'
        while 1:
	        date=time.strftime("%H:%M:%S") #24 hour format
		print(date)
		if (date==hora):
			print "In a moment the report will be sent to your mail"
			mail()
		        bandera = 0
		else:
			while 1:
		                data=Arduino.readline()
			        data= int(data)
			       	if(bandera == 1):
				     saldo=i*1800
				     perdidas=np*1800		        	           
		                     if (data==1): #Enter through the first bus door
		       		          i+=1
				     if (data==2): #Leaves by the first door of the bus
		      			  s+=1
		                     if (data==3): #Leaves through the second door of the bus
		    			  s+=1
		         	     if (data==4): #Enter through the second door of the bus and do not pay
		  			  np+=1
				     break
		               	else:
					bandera = 1
					i = 0
					s = 0
					np = 0
	           	print "No pagan:", np , "Entran:",i, "Sale:", s
			print  "Saldo:",saldo, "Perdidas:", perdidas
	
