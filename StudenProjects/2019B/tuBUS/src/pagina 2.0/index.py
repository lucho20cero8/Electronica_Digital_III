from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
import serial, time,sys
import smtplib
import datetime
import netifaces as ni
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

ser=serial.Serial('/dev/ttyUSB1', 9600)
#saldoact=int(LECTURA)
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2420151002'
app.config['MYSQL_DB'] = 'unibague'
mysql = MySQL(app)
app.secret_key='mysecretkey'
caja=int(0)
def recargo(saldo,recarga):
    saldonu=saldo+recarga
    return (saldonu)
@app.route('/correo')
def correo():
    remitente = '2420171024@estudiantesunibague.edu.co'
    destinatarios = ['gildar9909@gmail.com','buscontrol357@gmail.com','2420151002@estudiantesunibague.edu.co']
    asunto = 'INFORME SALDO EN CAJA'
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    cuerpo = "Hola.\nEl informe de saldo en caja del dia de hoy es: "  +'%s\n'%caja
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    sesion_smtp.login('2420171024@estudiantesunibague.edu.co','GILDARDO99')
    texto = mensaje.as_string()
    sesion_smtp.sendmail(remitente, destinatarios, texto)
    sesion_smtp.quit()

    return redirect(url_for('home'))
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT*FROM Usuario')
    data = cur.fetchall()
    cur.close()
    return render_template("index.html", usuarios=data)

@app.route('/recargas')
def recargas_usuario():
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM Usuario')
    data = cur.fetchall()
    cur.close()
    return render_template('indexrecargas.html', usuarios=data)


# @app.route('/Buscar/<id>', methods = ['POST', 'GET'])
# def Buscar(id):
#     cur= mysql.connection.cursor()
#     cur.execute('SELECT * FROM Usuario Usuario WHERE id = %s', (id))
#     data = cur.fetchall()
#     cur.close()
#     return render_template('indexbuscar.html', usuarios=data)

@app.route('/Buscando', methods = ['POST', 'GET'])
def Buscar():
    if request.method=='POST':
        id = request.form['Busqueda']
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM Usuario WHERE id = %s', (id))
        data = cur.fetchall()
        cur.close()
        return render_template('indexbuscar.html', usuarios=data)

@app.route('/contacto_nuevo', methods=['POST'])
def contacto_nuevo():
    if request.method=='POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        saldo = request.form['saldo']
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO Usuario (cedula, nombre, telefono, saldo) VALUES (%s,%s,%s,%s)",(cedula,nombre,telefono,saldo))
        mysql.connection.commit()
        flash('Usuario registrado')
        return redirect(url_for('home'))

@app.route('/Editar/<id>', methods = ['POST', 'GET'])
def editar_usuario(id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM Usuario WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    return render_template('editar-usuario.html', usuario=data[0])

@app.route('/editar_saldo/<id>',methods = ['POST','GET'])
def editar_saldo(id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM Usuario WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    return render_template('recargas.html', usuario=data[0])

@app.route('/Recargar/<id>', methods = ['POST','GET'])
def recargar_usuario(id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM Usuario WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    return render_template('editar-recarga.html', usuario=data[0])

app.route('/Busqueda/<id>', methods = ['POST','GET'])
def buscar_usuario(id):
    if request.method=='POST':
        id= request.form['id']
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM Usuario WHERE id = %s', (id))
        data = cur.fetchall()
        cur.close()
        return render_template('editar-recarga.html', usuario=data[0])

@app.route('/actualizar_saldo/<id>', methods = ['POST'])
def actualizar_saldo(id):
    if request.method=='POST':

        cedula = request.form['cedula']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        lectura= ser.readline()
        saldo = int(lectura)
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Usuario
            SET cedula = %s,
                nombre = %s,
                telefono = %s,
                saldo= %s
            WHERE id =%s
        """, (cedula, nombre, telefono, saldo,id))
        flash('Usuario actualizado')
        mysql.connection.commit()
        return redirect(url_for('home'))

@app.route('/actualizar/<id>', methods = ['POST'])
def actualizar_usuario(id):
    if request.method=='POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        saldo = request.form['saldo']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Usuario
            SET cedula = %s,
                nombre = %s,
                telefono = %s,
                saldo= %s
            WHERE id =%s
        """, (cedula, nombre, telefono, saldo,id))
        flash('Usuario actualizado')
        mysql.connection.commit()
        return redirect(url_for('home'))

@app.route('/actualizarrecarga/<id>',methods = ['POST'])
def actualizar_recarga(id):
    if request.method=='POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        saldo = request.form['saldo']
        recarga=request.form['recarga']
        saldonu=int(saldo)+int(recarga)
        saldotar=str(saldonu)+"#"
        global caja
        caja= int(caja) + int(recarga)
        print(caja)
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Usuario
            SET cedula = %s,
                nombre = %s,
                telefono = %s,
                saldo= %s
            WHERE id =%s
        """, (cedula, nombre, telefono, saldonu ,id))
        #val=raw_input("Introduzca recarga:")
        ser.write(saldotar.encode())
        flash('Recarga realizada')
        mysql.connection.commit()
        return redirect(url_for('home'))

@app.route('/Eliminar/<string:id>',methods = ['POST','GET'])
def Eliminar_usuario(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Usuario WHERE id ={0}'.format(id))
    mysql.connection.commit()
    flash('Usuario Eliminado')
    return redirect(url_for('home'))

# Make sure this we are executing this file
if __name__ == '__main__':
    caja=0
    app.run(host= '0.0.0.0', port=3000, debug=True)
    # while 1:
    #     datetime.datetime.now()
    #     print(datetime.datetime.now())
    #     date=time.strftime("%H:%M")
    #
    #     if (date=='15:46'):
    #         print ("fun")
    #         correo()
    #         caja=0
    #         print ("funy")
    #     else:
    #         app.run(host= '0.0.0.0', port=3000, debug=True)
    #         app.stop()
