#!/user/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import time
import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class base_datos():

    def __init__(self):
        self.alumno = ''
        self.equipo = ''
        self.x = 0
        print('\n\t\tkyselite')
        print('______________________________________________\n')
        while True:
            self.inteligencia()
            pass
        print('final ERROR')

    def inteligencia(self):
        self.menu()
        if self.x == 0:
            self.x = 0

        elif self.x == 1:
            self.registro_alumno()
            if self.x != 0:
                self.registro_equipo()
                self.registrando()
                self.x = 1

        elif self.x == 2:
            self.devolucion()

        elif self.x == 3:
            self.correo()

        else:
            print('¡¡¡ Opcion no valida !!!')
            self.x = 0

    def menu(self):
        if self.x == 0:
            print('\n\t ****   MENU  ****')
            print('\nElija una opcion: ')
            print(' 1 > Prestamo')
            print(' 2 > Devolucion')
            print(' 3 > Solicitar equipo')
            print(' Doble enter para salir')
            self.x = input('\nOpcion: ')
            print('')

    def registro_alumno(self):
        print ("\n\t****   PRESTAMO   ****")
        print('\n( Atras = 0)')
        try:
            codigo = input('\n~~Ingrese el codigo de barras del estudiante: ')
            if codigo != 0:
                datos_estudiantes = pd.read_csv('Estudiantes.csv')
                self.alumno = datos_estudiantes.loc[(datos_estudiantes)['CODIGO'] == codigo]
                print('')
                print "\t", self.alumno.iloc[0,0], self.alumno.iloc[0,1] #[:,0:2]
                print('')
            else:
                self.x = 0
        except:
            print "ERROR: codigo mal ingresado o no existente"

    def registro_equipo(self):
        try:
            datos_equipos = pd.read_csv('Base equipos.csv')
            codigo = raw_input('\n~~Ingrese el codigo de barras del equipo: ')
            self.equipo = datos_equipos.loc[(datos_equipos)['ACTIVO NUEVO'] == codigo]
            print('')
            print "\t", self.equipo.iloc[0,1], self.equipo.iloc[0,4] #[:,1:3]
            print('')
        except:
            print "ERROR: codigo mal ingresado o no existente"

    def registrando(self):
        fecha = time.strftime("%c")
        #espacio2=pd.DataFrame({'':['']})
        estado = pd.DataFrame({'':[''],'FECHA':[fecha]})
        estadoo = pd.DataFrame({'':[''],'ESTADO':['Prestado']})
        informacion = pd.merge(self.alumno, self.equipo, on="ja", how="outer")
        informacion_con_estado = pd.concat([informacion, estadoo, estado], axis=1)
        informacion_sin_fecha = pd.concat([informacion, estadoo], axis=1)
        guardar = raw_input("\n~~Guardar registro? (enter=si / n=no):  ")
        if guardar == "":
            try:
                print('')
                print "\t", self.alumno.iloc[0,0],'saco:',self.equipo.iloc[0,1]
                informacion_con_estado.reset_index(drop = True).to_csv('Historial.csv',header=False, index=False, mode='a')
                #espacio2.reset_index(drop = True).to_csv('Historial.csv',header=False, index=False, mode='a')
                informacion_sin_fecha.reset_index(drop = True).to_csv('Prestamos.csv',header=False, index=False, mode='a')
                print("\n Registro guardado\n")
            except:
                print"\n\n!!!!!ERROR: datos mal ingresados"
                print "por favor intente de nuevo!!!"
        elif guardar=="n":
            print("\n Registro no guardado\n")

    def devolucion(self):
        fecha = time.strftime("%c")
        estado=pd.DataFrame({'':[''],'FECHA':[fecha]})
        #espacio2=pd.DataFrame({'':['']})
        print ("\n\t****   DEVOLUCION   ****")
        print'\n(x = atras)'
        equipo= raw_input('\n~~Ingrese el codigo de barras del equipo: ')
        if equipo!='x':
            try:
                datos_prestamos=pd.read_csv('Prestamos.csv')
                equipo_en_prestamo=datos_prestamos.loc[(datos_prestamos)['ACTIVO NUEVO']==equipo]
                informacion_cambio_estado=equipo_en_prestamo.replace({'ESTADO': "Prestado"}, "Entregado")
                informacion_con_estado = pd.concat([informacion_cambio_estado,estado], axis=1,)###########################
                sacar=datos_prestamos.loc[(datos_prestamos)['ACTIVO NUEVO']!=equipo]
                print "\t", informacion_con_estado.iloc[0,1],'tiene:',informacion_con_estado.iloc[0,4]
                guardar=raw_input("\n~~Realizar devolucion? (enter=si / n=no):  ")
                if guardar=="":
                    informacion_con_estado.reset_index(drop = True).to_csv('Historial.csv',header=False, index=False, mode='a')
                    #espacio2.reset_index(drop = True).to_csv('Historial.csv',header=False, index=False, mode='a')
                    sacar.reset_index(drop = True).to_csv('Prestamos.csv',header=True, index=False)
                    print "\t", informacion_con_estado.iloc[0,1],'entrego:',informacion_con_estado.iloc[0,4]
                    print("\n Devolucion realizada\n")
                elif guardar=="n":
                    print("\n Devolucion no realizada\n")

            except:
                print "ERROR: el equipo no esta en prestamo"

        else:
            self.x=0

    def correo(self):
        print ("\n\n\t\t********************************\n") #encabezado
        print ("\t\t*    Enviar email con Gmail    *\n")
        print ("\t\t********************************\n")
        print'\n(x = atras)'
        user = raw_input("\nCuenta de gmail: ")     #cuenta donde se enviara el correo
        if user!='x':
            password = getpass.getpass("Password")      #password de la cuenta
            remitente = user  #cuenta de quien enviara el correo, generalmente la misma con la que se ingreso
            codg=raw_input('\n~~Ingrese el codigo de barras del equipo a solicitar: ')
            datos_prestamos=pd.read_csv('Prestamos.csv')
            try:
                equipo_prestado=datos_prestamos.loc[(datos_prestamos)['ACTIVO NUEVO']==codg]
                direc_correo = equipo_prestado['CORREO']
                print('')
                print(equipo_prestado.iloc[0,4])
                print('')
                destinatario = direc_correo.item() #raw_input("Para: (ejemplo: codigo@estudiantesunibague.edu.co): ")     #cuenta de quien recibira el correo
                asunto =(" Devolucion urgente del equipo de laboratorio")#Subject, asunto del mensaje
                eq=equipo_prestado['EQUIPO']
                eq = eq.item()
                mensaje = ("Cordial saludo estimado alumno, se le solicita la DEVOLUCION INMEDIATA del equipo "+ str(eq)+ " codigo: "+ str(codg) +".")
                print "Asunto: ", asunto
                print "\nMensaje HTML: ",mensaje
                print ("\n")
                # host y puertos SMTP de gmail
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                #protocolo de cifrado de datos utilizado por gmail
                gmail.starttls()
                try:
                    #credenciales
                    gmail.login(user, password)
                    #muestra la depuracion de la operacion de envio 1=true
                    gmail.set_debuglevel(1)
                    header = MIMEMultipart()    #parametros del correo de quien envia y recibe y el asunto
                    header ['Subject'] = asunto
                    header ['From'] = remitente
                    header ['To'] = destinatario
                    mensaje = MIMEText(mensaje, 'html') # 'text' en un archivo de texto o 'html' en el correo
                    header.attach(mensaje)
                    #enviar email
                    gmail.sendmail(remitente, destinatario, header.as_string())
                    #cerrar la conexion SMTP
                    gmail.quit()
                    print"\n-------Correo enviado--------"
                except:
                    print"!!!!!!ERROR: usuario o contraseña incorrecta"
                    print "por favor intente de nuevo¡¡¡¡¡¡¡¡¡¡"
            except:
                print"!!ERROR: codigo no existentete¡¡"
        else:
            self.x=0

if __name__ == '__main__':
    base_datos()
