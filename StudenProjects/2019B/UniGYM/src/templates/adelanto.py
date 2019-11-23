# correo
@app.route('/ADcorreo')
def ADcorreo():
    return render_template('/correo/ADcorreo.html')

@app.route('/CODcorreo',methods=['GET'])
def CODcorreo():

    asunto = request.args.get('asunto')
    mensajee = request.args.get('mensajee')

    print (asunto,"=",mensajee)

    correo(asunto,mensajee)
    return render_template('/correo/RES1correo.html')
###

def correo(destinatario, asunto, mensajee):

    anfitrion = "smtp.gmail.com"
    puerto = 587
    direccionDe = "gymunibague@gmail.com"
    contrasenaDe = "Unibague123"

    servidor = smtplib.SMTP(anfitrion,puerto)
    servidor.starttls()
    servidor.login(direccionDe,contrasenaDe)
    print(servidor.ehlo())

    correo = MIMEMultipart()
    correo['From'] = direccionDe
    correo['To'] = destinatario
    correo['Subject'] = asunto

    message = mensajee
    mensaje = MIMEText(message)
    correo.attach(mensaje)

    nombreImagen = "logo-actual-01.png"
    picture = open(nombreImagen, "rb")
    imagen = MIMEImage(picture.read())
    imagen.add_header('Content-Disposition', 'attachment', filename = nombreImagen)
    correo.attach(imagen)

    servidor.sendmail(direccionDe,destinatario,correo.as_string())

###
import pandas as pd
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import numpy as np

datos_estudiantes = pd.read_csv('datos_usuarios.csv')
p0 = datos_estudiantes['CODIGO']

#p0 = [2420171062,2420171051,2420162033]

for x in p0:
    p1 = str(x)
    p2 = '@estudiantesunibague.edu.co'
    total = p1+p2
    print ("=",total)

    destinatario=total
    asunto='hola'
    mensajee='ya'

    anfitrion = "smtp.gmail.com"
    puerto = 587
    direccionDe = "gymunibague@gmail.com"
    contrasenaDe = "Unibague123"

    servidor = smtplib.SMTP(anfitrion,puerto)
    servidor.starttls()
    servidor.login(direccionDe,contrasenaDe)
    print(servidor.ehlo())

    correo = MIMEMultipart()
    correo['From'] = direccionDe
    correo['To'] = destinatario
    correo['Subject'] = asunto

    message = mensajee
    mensaje = MIMEText(message)
    correo.attach(mensaje)

    nombreImagen = "logo-actual-01.png"
    picture = open(nombreImagen, "rb")
    imagen = MIMEImage(picture.read())
    imagen.add_header('Content-Disposition', 'attachment', filename = nombreImagen)
    correo.attach(imagen)

    servidor.sendmail(direccionDe,destinatario,correo.as_string())

###
