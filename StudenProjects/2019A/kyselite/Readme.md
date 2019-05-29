# KYSELITE

A software that allows to manage the assignation in the electronic engineering laboratory at the University of Ibagué by using bar codes. [see Youtube-Link](https://www.youtube.com/watch?v=MOrEAkXgoRY)

The contents of this repository:
  - Source code
  - Python development scripts
  - Database

## Hardware requirements:
- Bar code reading gun

## Software requirements:
- Ubuntu 16.04
- Python 2.7 (pandas, time, smtplib, getpass, MIMEMultipart, MIMEText)
- Databases

### Installation of pandas library

It's necessary to install the pandas library which will create and modify the software databases. To install use * pip *
```sh
pip install pandas
```
### Kyseslite functions
- Prestamos
- Devolucion
- Solicitar equipo
###  Prestamos
In the option of * Prestamos * the bar code of the student card and the equipment to be requested is requested, the software looks for the information of these codes in the database of the students and the laboratory equipment respectively:
```sh
datos_estudiantes = pd.read_csv('Estudiantes.csv')
self.alumno = datos_estudiantes.loc[(datos_estudiantes)['CODIGO'] == codigo]
    
datos_equipos = pd.read_csv('Base equipos.csv')
self.equipo = datos_equipos.loc[(datos_equipos)['ACTIVO NUEVO'] == codigo]
```
Finally, the loan information is stored in a database of current loans and another with the loan history:
```sh
informacion_con_estado.reset_index(drop = True).to_csv('Historial.csv',header=False, index=False, mode='a')

informacion_sin_fecha.reset_index(drop = True).to_csv('Prestamos.csv',header=False, index=False, mode='a')
```

### Devolucion
In the option of * Devolucion * the barcode of the equipment to be returned is requested, the software looks for the information of the code in the database of the current loans:
```sh
datos_prestamos=pd.read_csv('Prestamos.csv')
equipo_en_prestamo=datos_prestamos.loc[(datos_prestamos)['ACTIVO NUEVO']==equipo]
```
Finally the information of the registry in the database of the current loans is eliminated and in the data base of the history the delivery of the equipment is registered:
```sh
informacion_con_estado.reset_index(drop = True).to_csv('Historial.csv',header=False, index=False, mode='a')
```

### Solicitar equipo
In the option of * Solicitar equipo * the email and password of the administrator or manager of the laboratory is requested, then the bar code of the equipment to be requested is requested and the software automatically searches for the necessary information of the person in the loan database to send an email, finally the software writes and sends the email:
```sh
gmail = smtplib.SMTP('smtp.gmail.com', 587)
gmail.starttls()
gmail.login(user, password)
gmail.set_debuglevel(1)
header.attach(mensaje)
gmail.sendmail(remitente, destinatario, header.as_string())
```
## *Important*
For the correct operation of the software, the following points must be taken into account:
- The databases are .csv files.
- You can not modify the names of the databases.
- Can not modify the database headers.
- The source code and the databases have to be in the same folder.

***

## Authors
#### Universidad de Ibagué
#### Programa de Electrónica
#### Electrónica Digial III 2019A

- [Bryan F. Fandiño] - (2420162019@estudiantesunibague.edu.co)
- [Andres L. Castillo] - (2420172019@estudiantesunibague.edu.co)
- [Laura V. Gonzalez] - (2420161037@estudiantesunibague.edu.co)
- [Harold F MURCIA](www.haroldmurcia.com) - Tutor

***

