#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:22:53 2019

@author: juan
"""

import pandas as pd
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import numpy as np

def login(userr,contrasenaa):

    try:
        user=int(userr)

        datos_estudiantes = pd.read_csv('User_contra.csv')
        usuario = datos_estudiantes.loc[(datos_estudiantes)['USUARIO'] == user]
        contra = datos_estudiantes.loc[(datos_estudiantes)['CONTRASENA'] == contrasenaa]
        """
        print('')
        print "", 'ACCESO CONFIRMADO', '\n USUARIO:', usuario.iloc[0,0],  '\n CONTRASENA:',contra.iloc[0,1],
        print('')
        """
        return 1

    except:
        """
        print('')
        print('vuelve a ingresar el codigo, posiblemente no se encuentra en la base de datos')
        """
        return 0



def entrada_alumno(codigoentradaa):

    try:
        codigoentrada=int(codigoentradaa)

        datos_estudiantes = pd.read_csv('datos_usuarios.csv')
        alumno = datos_estudiantes.loc[(datos_estudiantes)['CODIGO'] == codigoentrada]
        fecha = time.strftime("%c")
        Fecha = pd.DataFrame({'':[''],'FECHA':[fecha]})
        Nombre = pd.DataFrame({'':[''],'NOMBRE':[alumno.iloc[0,1]]})
        Codigo = pd.DataFrame({'':[''],'CODIGO':[alumno.iloc[0,0]]})
        Vector_info = pd.concat([Codigo,Nombre,Fecha ], axis=1)
        Vector_info.reset_index(drop = True).to_csv('Historial.csv',header=False, index=False, mode='a')
        """
        print('')
        print "", 'Ingresó el dia: ' + time.strftime('%x'), '\n Hora: ' + time.strftime('%X'), '\n Codigo:', alumno.iloc[0,0],  '\n Nombre:',alumno.iloc[0,1], '\n Eps:',alumno.iloc[0,3], '\n Número de emergencia:', alumno.iloc[0,4]
        print('')
        """
        return 1

    except:
        """
        print('')
        print('vuelve a ingresar el codigo, posiblemente no se encuentra en la base de datos')
        """
        return 0


def calificacion(codigo_del_calificantee, notaa):

    try:
       nota=int(notaa)
       codigo_del_calicante = int(codigo_del_calificantee)

       datos_estudiantes = pd.read_csv('datos_usuarios.csv')
       alumno = datos_estudiantes.loc[(datos_estudiantes)['CODIGO'] == codigo_del_calicante]
       Nota = pd.DataFrame({'':[''],'NOTA':[nota]})
       Nombre = pd.DataFrame({'':[''],'NOMBRE':[alumno.iloc[0,1]]})
       Codigo = pd.DataFrame({'':[''],'CODIGO':[alumno.iloc[0,0]]})
       Vector_info = pd.concat([Codigo,Nombre,Nota], axis=1)
       Vector_info.reset_index (drop = True).to_csv('calificar.csv',header=False, index=False, mode='a')
       """
       print "", '\n Codigo:', alumno.iloc[0,0],  '\n Nombre:', alumno.iloc[0,1], "\n Nota:",nota
       print('')
       """
       p1 = str(codigo_del_calificantee)
       p2 = '@estudiantesunibague.edu.co'
       total = p1+p2

       z1 = str(notaa)
       z2 = 'su nota es'
       z3 = 'por mal comportamiento'
       men = z2+' '+z1+' '+z3

       #print ("=",total,"=",p1,"=",z1,"=",men)

       v=int(notaa)
       #print ("=",v)

       if v<3:
           destinatario=total
           asunto='calificacion'
           mensajee=men

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

           print("correo:",destinatario)

           message = mensajee
           mensaje = MIMEText(message)
           correo.attach(mensaje)

           nombreImagen = "logo-actual-01.png"
           picture = open(nombreImagen, "rb")
           imagen = MIMEImage(picture.read())
           imagen.add_header('Content-Disposition', 'attachment', filename = nombreImagen)
           correo.attach(imagen)

           servidor.sendmail(direccionDe,destinatario,correo.as_string())

       return 1

    except:
        """
        print('')
        print('vuelve a ingresar el codigo, posiblemente no se encuentra en la base de datos')
        """
        return 0


def promedio(codigo_del_promediadoo):

    codigo_del_promediado=int(codigo_del_promediadoo)

    try:
        datos = pd.read_csv('calificar.csv')
        df = pd.DataFrame(datos)
        lop=df[df['CODIGO'] == codigo_del_promediado]['NOTA']

        datos_estudiantes = pd.read_csv('datos_usuarios.csv')
        alumno = datos_estudiantes.loc[(datos_estudiantes)['CODIGO'] == codigo_del_promediado]

        Nombre = pd.DataFrame({'':[''],'NOMBRE':[alumno.iloc[0,1]]})
        Codigo = pd.DataFrame({'':[''],'CODIGO':[alumno.iloc[0,0]]})# #       print ("=",todo)

        a=np.array(lop)
        promedio=np.mean(a)

        print("=",promedio)
        todo= ["{0:.2f}".format(promedio),1]
        print ("=",todo)
        return todo

    except:
        todo= [0,0]
        #print ("=",todo)
        return todo
###

def correo(asunto, mensajee):

    datos_estudiantes = pd.read_csv('datos_usuarios.csv')
    p0 = datos_estudiantes['CODIGO']

    for x in p0:
        p1 = str(x)
        p2 = '@estudiantesunibague.edu.co'
        total = p1+p2
        print ("=",total)

        destinatario=total

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


def  guardar(cod_registro,nombre,cedula,EPS,Nemergencia,RH,carrera,correo):

    cod_registro= int(cod_registro)
    nombre      = str(nombre)
    cedula      = int(cedula)
    EPS         = str(EPS)
    Nemergencia = int(Nemergencia)
    RH          = str(RH)
    carrera     = str(carrera)
    correo      = str(correo)
    # revisar si el codigo esta registro
    a=0
    datos = pd.read_csv('datos_usuarios.csv', header=0)
    C = datos['CODIGO']
    for x in C:
        if x==cod_registro:
            a=1
    ###
    # envia el estado
    if a==1:
        return 1

    else:

        cod_registroo= pd.DataFrame({'CODIGO':[cod_registro]})
        nombree      = pd.DataFrame({'NOMBRE':[nombre]})
        cedulaa      = pd.DataFrame({'CEDULA':[cedula]})
        EPSS         = pd.DataFrame({'EPS':[EPS]})
        Nemergenciaa = pd.DataFrame({'EN CASO DE EMERGENCIA LLAMAR A:':[cod_registro]})
        RHH          = pd.DataFrame({'RH':[RH]})
        carreraa     = pd.DataFrame({'CARRERA':[carrera]})
        correoo      = pd.DataFrame({'CORREO':[correo]})

        Vector_info = pd.concat([cod_registroo,nombree,cedulaa,EPSS,Nemergenciaa,RHH,carreraa,correoo], axis=1)
        Vector_info.reset_index (drop = True).to_csv('datos_usuarios.csv',header=False, index=False, mode='a')

        return 2
