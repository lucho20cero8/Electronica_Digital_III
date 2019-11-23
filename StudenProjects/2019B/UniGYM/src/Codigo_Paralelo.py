#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:19:38 2019

@author: juan
"""


import pandas as pd
import time
import numpy as np
import serial


def entrada_alumno(codigoentrada):

    try:
        #parte 1 guardar entrada
        datos_estudiantes = pd.read_csv('datos_usuarios.csv')
        #print (datos_estudiantes)['CODIGO']
        #print ( (datos_estudiantes)['CORREO'],"A")
        alumno = datos_estudiantes.loc[(datos_estudiantes)['CODIGO'] == codigoentrada]

        Nombre = pd.DataFrame({'':[''],'NOMBRE':[alumno.iloc[0,1]]})
        Codigo = pd.DataFrame({'':[''],'CODIGO':[alumno.iloc[0,0]]})

        # parte 2 buscar promedio
        datos = pd.read_csv('calificar.csv')
        df = pd.DataFrame(datos)
        lop=df[df['CODIGO'] == codigoentrada]['NOTA']

        a=np.array(lop)
        promedio=np.mean(a)

        #print(promedio)
        todo= [promedio,1]
        #print (todo)

        if promedio>=3:

            fecha = time.strftime("%c")
            Fecha = pd.DataFrame({'FECHA':[fecha]})
            Nombre = pd.DataFrame({'NOMBRE':[alumno.iloc[0,1]]})
            Codigo = pd.DataFrame({'CODIGO':[alumno.iloc[0,0]]})
            Vector_info = pd.concat([Codigo,Nombre,Fecha ], axis=1)
            Vector_info.reset_index(drop = True).to_csv('Historial.csv',header=False, index=False, mode='a')

            #print('')
            #print "", 'Ingresó el dia: ' + time.strftime('%x'), '\n Hora: ' + time.strftime('%X'), '\n Codigo:', alumno.iloc[0,0],  '\n Nombre:',alumno.iloc[0,1], '\n Eps:',alumno.iloc[0,3], '\n Número de emergencia:', alumno.iloc[0,4]
            #print('')

        return todo

    except:
        todo= [0,0]
        #print ("=",todo)
        return todo
#######################################3

ser=serial.Serial('/dev/ttyUSB0', 9600)
c=2

while 1:
    val=raw_input('codigo:')[:11]
    val=int(val)
    print("codigo",val)
    a = entrada_alumno(val)

    if a[0] < 3 :
        c=0
    else:
        c=1

    ser.write(str(c).encode())
    print("He enviado: " + str(c) )
    print("promedio",a)
