#!/user/bin/env python
# -*- coding: utf-8 -*-

import os
import secrets
from PIL import Image
from flask import render_template, request, url_for, redirect, flash, abort
from flaskblog import app, db, bcrypt, mail
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

import pandas as pd
from IPython.display import HTML
import time
from datetime import datetime

@app.route('/')
@app.route('/Fastpel')
def Fastpel():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("Fastpel.html", posts=posts)

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('Fastpel'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Tu cuenta ha sido creada! Ahora puede iniciar sesion','success') # flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Fastpel'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Fastpel'))
        else:
            flash('Inicio de sesion fallido, verifique el correo electronico y el password','danger') # flash(f'Account created for {form.username.data}!', 'success')
    return render_template("login.html", title='Inicio de sesion', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Fastpel'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # random_hex = str(os.urandom(8))
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Su cuenta ha sido actualizada!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Cuenta', image_file=image_file, form=form)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Tu publicacion ha sido creada!', 'success')
        return redirect(url_for('Fastpel'))
    return render_template('create_post.html', title='Nueva publicacion', form=form, legend='Nueva publicacion')

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Tu publicacion ha sido actualizada!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Actualizar publicacion', form=form, legend='Actualizar publicacion')

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Tu publicacion ha sido eliminada!', 'success')
    return redirect(url_for('Fastpel'))

@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Solicitud de restablecimiento de password',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = '''Para restablecer su password, visite el siguiente enlace:
'{}',
Si no realizo esta solicitud, simplemente ignore este correo electronico y no se realizaran cambios.'''.format(url_for('reset_token', token=token, _external=True))
    mail.send(msg)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('Fastpel'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Se ha enviado un correo electronico con instrucciones para restablecer su password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Restablecer el Password', form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('Fastpel'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Ese es un token no valido o caducado', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Su password ha sido actualizada! Ahora puede iniciar sesion', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Restablecer el Password', form=form)

###########################################################################
#                   OPCIONES FASTPEL
###########################################################################
@app.route('/Prestamos', methods=['GET','POST'])
@login_required
def Prestamos():

    if request.method == 'POST':
        nombre = int(request.form.get('cestudiante'))
        datos_estudiantes = pd.read_csv('../bases de datos/Estudiantes v2.csv')
        alumno = datos_estudiantes.loc[(datos_estudiantes)['CODIGO'] == nombre]

        eq = str(request.form.get('cequipo'))
        datos_equipos = pd.read_csv('../bases de datos/Base equipos v2.csv')
        equipo = datos_equipos.loc[(datos_equipos)['ACTIVO NUEVO'] == eq]

        datos_prestamos=pd.read_csv('../bases de datos/Prestamos v2.csv')
        bequipo=datos_prestamos.loc[(datos_prestamos)['ACTIVO NUEVO'] == eq]

        fecha = time.strftime("%c")
        estado = pd.DataFrame({'':[''],'FECHA':[fecha]})
        estadoo = pd.DataFrame({'':[''],'ESTADO':['Prestado']})

        informacion = pd.merge(alumno, equipo, on="ja", how="outer")
        informacion_con_estado = pd.concat([informacion, estadoo, estado], axis=1)
        informacion_sin_fecha = pd.concat([informacion, estadoo], axis=1)

        try:        # VERIFICAR SI NO ESTA PRESTADO EL EQUIPO
            vequipo=bequipo['ACTIVO NUEVO']
            vequipo = vequipo.item()
            flash('El equipo ya esta prestado, por favor intenta de nuevo', 'warning') # info  success warning
            info= "ERROR: El equipo ya esta prestado, por favor intenta de nuevo"
            print ("\n\n!!!!!ERROR: El equipo ya esta prestado, por favor intenta de nuevo")
        except:
            try:            # VERIFICAR SI EL ALUMNO EXISTE
                valumno=alumno['CODIGO']
                valumno = valumno.item()
                try:        # VERIFICAR SI EL EQUIPO EXISTE
                    vqq=equipo['ACTIVO NUEVO']
                    vqq = vqq.item()
                    try:
                        print('')
                        print ("\t", alumno.iloc[0,0],'saco:',equipo.iloc[0,1])

                        informacion_con_estado.reset_index(drop = True).to_csv('../bases de datos/Historial v2.csv',header=False, index=False, mode='a')
                        informacion_sin_fecha.reset_index(drop = True).to_csv('../bases de datos/Prestamos v2.csv',header=False, index=False, mode='a')

                        flash('Registro guardado', 'success') # info  success warning
                        info= "Registro guardado"
                        print("\n Registro guardado\n")

                    except:
                        flash('Datos mal ingresados, por favor intente de nuevo', 'warning') # info  success warning
                        info= "ERROR: Datos mal ingresados, por favor intente de nuevo"
                        print ("\n\n!!!!!ERROR: datos mal ingresados")
                        print ("por favor intente de nuevo!!!")
                except:
                    flash('El equipo ingresado no existe, por favor intenta de nuevo', 'warning') # info  success warning
                    info= "ERROR: El equipo ingresado no existe, por favor intenta de nuevo"
                    print ("\n\n!!!!!ERROR: El equipo no existe, por favor intenta de nuevo")
            except:
                flash('El alumno ingresado no existe, por favor intenta de nuevo', 'warning') # info  success warning
                info= "ERROR: El alumno ingresado no existe, por favor intenta de nuevo"
                print ("\n\n!!!!!ERROR: El alumno no existe, por favor intenta de nuevo")

        return render_template("prestamo.html", info=info, title='Prestamos')

    return render_template("prestamo.html", title='Prestamos')


@app.route('/Devoluciones', methods=['GET','POST'])
@login_required
def Devoluciones():
 
    if request.method == 'POST':
        eqd = str(request.form.get('ceqdeb'))
        datos_prestamos=pd.read_csv('../bases de datos/Prestamos v2.csv')
        equipo_en_prestamo=datos_prestamos.loc[(datos_prestamos)['ACTIVO NUEVO'] == eqd]

        obss = str(request.form.get('obser')) #.decode('utf-8')
        observacion=pd.DataFrame({'':[''],'OBSERVACION':[obss]})

        fecha = time.strftime("%c")
        estado=pd.DataFrame({'':[''],'FECHA':[fecha]})

        informacion_cambio_estado=equipo_en_prestamo.replace({'ESTADO': "Prestado"}, "Entregado")
        informacion_con_estado = pd.concat([informacion_cambio_estado,estado], axis=1,)
        informacion_con_estado_y_observacion = pd.concat([informacion_con_estado, observacion], axis=1,)

        try:
            eq=equipo_en_prestamo['ACTIVO NUEVO']
            eq = eq.item()      # para generar error y no guardar espacio vacio si no existe el codigo
            sacar=datos_prestamos.loc[(datos_prestamos)['ACTIVO NUEVO']!=eqd]
            print ("\n\t", informacion_con_estado.iloc[0,1],'tiene:',informacion_con_estado.iloc[0,4])

            informacion_con_estado_y_observacion.reset_index(drop = True).to_csv('../bases de datos/Historial v2.csv',header=False, index=False, mode='a')
            sacar.reset_index(drop = True).to_csv('../bases de datos/Prestamos v2.csv',header=True, index=False)
            print ("\t", informacion_con_estado.iloc[0,1],'entrego:',informacion_con_estado.iloc[0,4])

            flash('Devolucion realizada', 'success') # info  success warning
            info= "Devolucion realizada"
            print("\n Devolucion realizada\n")

        except:
            flash('Codigo mal ingresado o el equipo no esta en prestamo', 'warning') # info  success warning
            info= "ERROR: Codigo mal ingresado o el equipo no esta en prestamo"
            print ("\nERROR: Codigo mal ingresado o el equipo no esta en prestamo\n")

        return render_template("devolucion.html", info=info, title='Devoluciones')

    return render_template("devolucion.html", title='Devoluciones')

@app.route('/Solicitar_equipo', methods=['GET','POST'])
@login_required
def Solicitar_equipo():

    if request.method == 'POST':
        print ("\n\n\t\t********************************\n") #encabezado
        print ("\t\t*    Enviar email con Gmail    *\n")
        print ("\t\t********************************\n")

        codg=str(request.form.get('ccequipo'))
        datos_prestamos=pd.read_csv('../bases de datos/Prestamos v2.csv')
        equipo_prestado=datos_prestamos.loc[(datos_prestamos)['ACTIVO NUEVO']==codg]
        direc_correo = equipo_prestado['CORREO']
        try:
            print(equipo_prestado.iloc[0,4])  #      genera error si no existe el codigo, si no esta prestado el equipo
            destinatario = direc_correo.item()
            msg = Message('Devolucion urgente del equipo de laboratorio',
                          sender='noreply@demo.com',
                          recipients=[destinatario])

            eq=equipo_prestado['EQUIPO']
            eq = eq.item()
            msg.body = "Cordial saludo estimado alumno, se le solicita la DEVOLUCION INMEDIATA del equipo "+ str(eq)+ " codigo: "+ str(codg) +"."
            mail.send(msg)

            flash('Correo enviado', 'success') # info  success warning
            info="Correo enviado"
            print("\n-------Correo enviado--------")

        except:
            flash('Codigo no existentete', 'warning') # info  success warning
            info="ERROR: codigo no existentete"
            print("!!ERROR: codigo no existentete¡¡")

        return render_template("solicitar_equipo.html", info=info, title='Solicitar equipo')

    datos_prestamos=pd.read_csv('../bases de datos/Prestamos v2.csv') #roloooooo
    df1 = datos_prestamos[['CODIGO','NOMBRE','EQUIPO','ACTIVO NUEVO']]
    tabla_prestamos = HTML(df1.to_html(classes = 'table table- border table-striped table-hover table-condensed' )) 
    print "\n\t", tabla_prestamos

    return render_template("solicitar_equipo.html", title='Solicitar equipo', tabla_prestamos=tabla_prestamos)

@app.route('/Laboratorios', methods=['GET','POST'])
@login_required
def Laboratorios():
    
    cupp1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
    cup1 = len(cupp1.index)
    cdis1 = 22 - cup1

    cupp2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
    cup2 = len(cupp2.index)
    cdis2 = 26 - cup2

    cupp3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
    cup3 = len(cupp3.index)
    cdis3 = 14 - cup3

    return render_template("laboratorios.html", title='Laboratorios', cdis1=cdis1, cdis2=cdis2, cdis3=cdis3)

@app.route('/lab1', methods=['GET','POST'])
@login_required
def lab1():
    hora1 = datetime.strptime("6:00:00", "%X").time()
    hora2 = datetime.strptime("11:00:00", "%X").time()
    hora_act = datetime.now().time()
    if hora1 < hora_act and hora_act < hora2:
        lab_cerrar = "abierto"
        if request.method == 'POST':
            toppe=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
            tope = len(toppe.index)
            if tope < 22:
                dnom = str(request.form.get('dnom')) #.decode('utf-8')
                nombre=pd.DataFrame({'NOMBRE':[dnom]})
                dced = str(request.form.get('dced')) #.decode('utf-8')
                cedula=pd.DataFrame({'CEDULA':[dced]})
                dcel = str(request.form.get('dcel')) #.decode('utf-8')
                celular=pd.DataFrame({'CELULAR':[dcel]})
                deps = str(request.form.get('deps')) #.decode('utf-8')
                eps=pd.DataFrame({'EPS':[deps]})
                dcod = int(request.form.get('dcod')) #.decode('utf-8')
                codigo=pd.DataFrame({'CODIGO':[dcod]})
                dcorreo = str(request.form.get('dcorreo')) #.decode('utf-8')
                correo=pd.DataFrame({'CORREO':[dcorreo]})
                dequipo = str(request.form.get('dequipo')) #.decode('utf-8')
                equipo=pd.DataFrame({'EQUIPO':[dequipo]})

                datos_estudiantes_lab = pd.concat([codigo, nombre, cedula, celular, eps, correo, equipo], axis=1,)
                datos_estudiantes_lab.reset_index(drop = True).to_csv('../bases de datos/lab2 estudiantes v2.csv',header=False, index=False, mode='a')

                llen=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                lleno = len(llen.index)
                if lleno == 22:
                    ue=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                    uee=ue.iloc[0:1]
                    direc_correo_lab = uee['CORREO']
                    user_email_lab = direc_correo_lab.item()
                    msg = Message('Solicitud de prestamo de laboratorio',
                                  sender='noreply@demo.com',
                                  recipients=[user_email_lab])
                    msg.body = "Para solicitar el laboratorio descargue el formato, llenelo respectivamente y entregelo al administrador. Si no realizo esta solicitud, simplemente ignore este correo electronico."
                    with open("../bases de datos/lab2 estudiantes v2.csv") as fp:
                        msg.attach("lab2 formato.csv", "lab2 formato/csv", fp.read())

                    mail.send(msg)

                    flash('Estudiante registrado y formulario enviado al primero de la lista', 'success') # info  success warning
                    
                    cupp1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                    cup1 = len(cupp1.index)
                    cdis1 = 22 - cup1
                    cupp2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                    cup2 = len(cupp2.index)
                    cdis2 = 26 - cup2
                    cupp3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                    cup3 = len(cupp3.index)
                    cdis3 = 14 - cup3
                    return render_template("laboratorios.html", title='Laboratorio',cdis1=cdis1, cdis2=cdis2, cdis3=cdis3, lab_cerrar = lab_cerrar)


                flash('Estudiante registrado', 'success') # info  success warning
              
                cupp1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                cup1 = len(cupp1.index)
                cdis1 = 22 - cup1
                cupp2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                cup2 = len(cupp2.index)
                cdis2 = 26 - cup2
                cupp3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                cup3 = len(cupp3.index)
                cdis3 = 14 - cup3
                return render_template("laboratorios.html", title='Laboratorio', cdis1=cdis1, cdis2=cdis2, cdis3=cdis3, lab_cerrar = lab_cerrar)

            else:
                flash('Este Laboratorio se encuentra lleno, intenta en otro', 'warning') # info  success warning
              
                cupp1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                cup1 = len(cupp1.index)
                cdis1 = 22 - cup1
                cupp2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                cup2 = len(cupp2.index)
                cdis2 = 26 - cup2
                cupp3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                cup3 = len(cupp3.index)
                cdis3 = 14 - cup3
                return render_template("laboratorios.html", title='Laboratorio', cdis1=cdis1, cdis2=cdis2, cdis3=cdis3, slab_cerrar = lab_cerrar)

        datos_estudiantes_lab1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
        df1 = datos_estudiantes_lab1[['CODIGO','NOMBRE', 'CEDULA', 'CELULAR','EPS','CORREO','EQUIPO']]
        tabla_estu_lab = HTML(df1.to_html(classes = 'table table- border table-striped table-hover table-condensed' )) 

        return render_template("lab1.html", title='Laboratorio2', tabla_estu_lab=tabla_estu_lab, lab_cerrar=lab_cerrar)

    else:
        lab_cerrar = "cerrado"
        hora3 = datetime.strptime("11:00:00", "%X").time()
        hora4 = datetime.strptime("20:30:00", "%X").time()
        hora_actual = datetime.now().time()
        if hora3 < hora_actual and hora_actual < hora4:
            print "borrado"
            dfborrar=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
            filas = len(dfborrar.index)
            dfborrar.drop(dfborrar.index[[range(0, filas, 1)]], inplace = True)
            dfborrar.reset_index(drop = True).to_csv('../bases de datos/lab2 estudiantes v2.csv',index=False)

            flash('Base de datos reseteada exitosamente', 'success') # info  success warning
            flash('Registro de laboratorios actualmente cerrados, tenga en cuenta los horarios', 'info')
    
            return render_template("lab1.html", title='Laboratorio2', lab_cerrar=lab_cerrar)

        flash('Registro de laboratorios actualmente cerrados, tenga en cuenta los horarios', 'info') # info  success warning

        return render_template("lab1.html", title='Laboratorio2', lab_cerrar=lab_cerrar)

    return render_template("lab1.html", title='Laboratorio2')



@app.route('/lab2', methods=['GET','POST'])
@login_required
def lab2():
    hora1 = datetime.strptime("6:00:00", "%X").time()
    hora2 = datetime.strptime("21:00:00", "%X").time()
    hora_act = datetime.now().time()
    if hora1 < hora_act and hora_act < hora2:
        lab_cerrar = "abierto"
        if request.method == 'POST':
            toppe=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
            tope = len(toppe.index)

            if tope < 26:
                dnom = str(request.form.get('dnom')) #.decode('utf-8')
                nombre=pd.DataFrame({'NOMBRE':[dnom]})
                dced = str(request.form.get('dced')) #.decode('utf-8')
                cedula=pd.DataFrame({'CEDULA':[dced]})
                dcel = str(request.form.get('dcel')) #.decode('utf-8')
                celular=pd.DataFrame({'CELULAR':[dcel]})
                deps = str(request.form.get('deps')) #.decode('utf-8')
                eps=pd.DataFrame({'EPS':[deps]})
                dcod = int(request.form.get('dcod')) #.decode('utf-8')
                codigo=pd.DataFrame({'CODIGO':[dcod]})
                dcorreo = str(request.form.get('dcorreo')) #.decode('utf-8')
                correo=pd.DataFrame({'CORREO':[dcorreo]})
                dequipo = str(request.form.get('dequipo')) #.decode('utf-8')
                equipo=pd.DataFrame({'EQUIPO':[dequipo]})

                datos_estudiantes_lab = pd.concat([codigo, nombre, cedula, celular, eps, correo, equipo], axis=1,)
                datos_estudiantes_lab.reset_index(drop = True).to_csv('../bases de datos/lab5 estudiantes v2.csv',header=False, index=False, mode='a')

                llen=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                lleno = len(llen.index)
                if lleno == 26:
                    ue=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                    uee=ue.iloc[0:1]
                    direc_correo_lab = uee['CORREO']
                    user_email_lab = direc_correo_lab.item()
                    msg = Message('Solicitud de prestamo de laboratorio',
                                  sender='noreply@demo.com',
                                  recipients=[user_email_lab])
                    msg.body = "Para solicitar el laboratorio descargue el formato, llenelo respectivamente y entregelo al administrador. Si no realizo esta solicitud, simplemente ignore este correo electronico."
                    with open("../bases de datos/lab5 estudiantes v2.csv") as fp:
                        msg.attach("lab5 formato.csv", "lab5 formato/csv", fp.read())
                    mail.send(msg)

                    flash('Estudiante registrado y formulario enviado al primero de la lista', 'success') # info  success warning
                   
                    cupp1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                    cup1 = len(cupp1.index)
                    cdis1 = 22 - cup1
                    cupp2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                    cup2 = len(cupp2.index)
                    cdis2 = 26 - cup2
                    cupp3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                    cup3 = len(cupp3.index)
                    cdis3 = 14 - cup3
                    return render_template("laboratorios.html", title='Laboratorio', cdis1=cdis1, cdis2=cdis2, cdis3=cdis3, lab_cerrar = lab_cerrar)

                flash('Estudiante registrado', 'success') # info  success warning
                
                cupp1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                cup1 = len(cupp1.index)
                cdis1 = 22 - cup1
                cupp2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                cup2 = len(cupp2.index)
                cdis2 = 26 - cup2
                cupp3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                cup3 = len(cupp3.index)
                cdis3 = 14 - cup3
                return render_template("laboratorios.html", title='Laboratorio', cdis1=cdis1, cdis2=cdis2, cdis3=cdis3, lab_cerrar = lab_cerrar)

            else:
                flash('Este Laboratorio se encuentra lleno, intenta en otro', 'warning') # info  success warning
                
                cupp1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                cup1 = len(cupp1.index)
                cdis1 = 22 - cup1
                cupp2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                cup2 = len(cupp2.index)
                cdis2 = 26 - cup2
                cupp3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                cup3 = len(cupp3.index)
                cdis3 = 14 - cup3
                return render_template("laboratorios.html", title='Laboratorio', cdis1=cdis1, cdis2=cdis2, cdis3=cdis3, lab_cerrar = lab_cerrar)

        datos_estudiantes_lab2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv') #roloooooo
        df2 = datos_estudiantes_lab2[['CODIGO','NOMBRE', 'CEDULA', 'CELULAR','EPS','CORREO','EQUIPO']]
        tabla_estu_lab2 = HTML(df2.to_html(classes = 'table table- border table-striped table-hover table-condensed' )) 

        return render_template("lab2.html", title='Laboratorio5', tabla_estu_lab2=tabla_estu_lab2, lab_cerrar = lab_cerrar)

    else:
        lab_cerrar = "cerrado"
        hora3 = datetime.strptime("11:00:00", "%X").time()
        hora4 = datetime.strptime("20:30:00", "%X").time()
        hora_actual = datetime.now().time()
        if hora3 < hora_actual and hora_actual < hora4:
            print "borrado"
            dfborrar=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
            filas = len(dfborrar.index)
            dfborrar.drop(dfborrar.index[[range(0, filas, 1)]], inplace = True)
            dfborrar.reset_index(drop = True).to_csv('../bases de datos/lab5 estudiantes v2.csv',index=False)

            flash('Base de datos reseteada exitosamente', 'success') # info  success warning
            flash('Registro de laboratorios actualmente cerrados, tenga en cuenta los horarios', 'info')
            
            return render_template("lab2.html", title='Laboratorio5', lab_cerrar=lab_cerrar)

        flash('Registro de laboratorios actualmente cerrados, tenga en cuenta los horarios', 'info') # info  success warning
       
        return render_template("lab2.html", title='Laboratorio5', lab_cerrar=lab_cerrar)

    return render_template("lab2.html", title='Laboratorio5')

@app.route('/lab3', methods=['GET','POST'])
@login_required
def lab3():
    hora1 = datetime.strptime("06:00:00", "%X").time()
    hora2 = datetime.strptime("21:00:00", "%X").time()
    hora_act = datetime.now().time()
    if hora1 < hora_act and hora_act < hora2:
        lab_cerrar = "abierto"
        if request.method == 'POST':
            toppe=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
            tope = len(toppe.index)

            if tope < 14:
                dnom = str(request.form.get('dnom')) #.decode('utf-8')
                nombre=pd.DataFrame({'NOMBRE':[dnom]})
                dced = str(request.form.get('dced')) #.decode('utf-8')
                cedula=pd.DataFrame({'CEDULA':[dced]})
                dcel = str(request.form.get('dcel')) #.decode('utf-8')
                celular=pd.DataFrame({'CELULAR':[dcel]})
                deps = str(request.form.get('deps')) #.decode('utf-8')
                eps=pd.DataFrame({'EPS':[deps]})
                dcod = int(request.form.get('dcod')) #.decode('utf-8')
                codigo=pd.DataFrame({'CODIGO':[dcod]})
                dcorreo = str(request.form.get('dcorreo')) #.decode('utf-8')
                correo=pd.DataFrame({'CORREO':[dcorreo]})
                dequipo = str(request.form.get('dequipo')) #.decode('utf-8')
                equipo=pd.DataFrame({'EQUIPO':[dequipo]})

                datos_estudiantes_lab = pd.concat([codigo, nombre, cedula, celular, eps, correo, equipo], axis=1,)
                datos_estudiantes_lab.reset_index(drop = True).to_csv('../bases de datos/lab4 estudiantes v2.csv',header=False, index=False, mode='a')

                llen=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                lleno = len(llen.index)
                if lleno == 14:
                    ue=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                    uee=ue.iloc[0:1]
                    direc_correo_lab = uee['CORREO']
                    user_email_lab = direc_correo_lab.item()
                    msg = Message('Solicitud de prestamo de laboratorio',
                                  sender='noreply@demo.com',
                                  recipients=[user_email_lab])
                    msg.body = "Para solicitar el laboratorio descargue el formato, llenelo respectivamente y entregelo al administrador. Si no realizo esta solicitud, simplemente ignore este correo electronico."
                    with open("../bases de datos/lab4 estudiantes v2.csv") as fp:
                        msg.attach("lab4 formato.csv", "lab4 formato/csv", fp.read())
                    mail.send(msg)

                    flash('Estudiante registrado y formulario enviado al primero de la lista', 'success') # info  success warning
               
                    cupp1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                    cup1 = len(cupp1.index)
                    cdis1 = 22 - cup1
                    cupp2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                    cup2 = len(cupp2.index)
                    cdis2 = 26 - cup2
                    cupp3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                    cup3 = len(cupp3.index)
                    cdis3 = 14 - cup3
                    return render_template("laboratorios.html", title='Laboratorio',cdis1=cdis1, cdis2=cdis2, cdis3=cdis3, lab_cerrar = lab_cerrar)

                flash('Estudiante registrado', 'success') # info  success warning
        
                cupp1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                cup1 = len(cupp1.index)
                cdis1 = 22 - cup1
                cupp2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                cup2 = len(cupp2.index)
                cdis2 = 26 - cup2
                cupp3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                cup3 = len(cupp3.index)
                cdis3 = 14 - cup3
                return render_template("laboratorios.html", title='Laboratorio',cdis1=cdis1, cdis2=cdis2, cdis3=cdis3, lab_cerrar = lab_cerrar)

            else:
                flash('Este Laboratorio se encuentra lleno, intenta en otro', 'warning') # info  success warning
                
                cupp1=pd.read_csv('../bases de datos/lab2 estudiantes v2.csv')
                cup1 = len(cupp1.index)
                cdis1 = 22 - cup1
                cupp2=pd.read_csv('../bases de datos/lab5 estudiantes v2.csv')
                cup2 = len(cupp2.index)
                cdis2 = 26 - cup2
                cupp3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
                cup3 = len(cupp3.index)
                cdis3 = 14 - cup3
                return render_template("laboratorios.html", title='Laboratorio',cdis1=cdis1, cdis2=cdis2, cdis3=cdis3, lab_cerrar = lab_cerrar)

        datos_estudiantes_lab3=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
        df3 = datos_estudiantes_lab3[['CODIGO','NOMBRE', 'CEDULA','CELULAR','EPS','CORREO','EQUIPO']]
        tabla_estu_lab3 = HTML(df3.to_html(classes = 'table table- border table-striped table-hover table-condensed' )) 

        return render_template("lab3.html", title='Laboratorio4', tabla_estu_lab3=tabla_estu_lab3, lab_cerrar = lab_cerrar)

    else:
        lab_cerrar = "cerrado"
        hora3 = datetime.strptime("11:00:00", "%X").time()
        hora4 = datetime.strptime("20:30:00", "%X").time()
        hora_actual = datetime.now().time()
        if hora3 < hora_actual and hora_actual < hora4:
            print "borrado"
            dfborrar=pd.read_csv('../bases de datos/lab4 estudiantes v2.csv')
            filas = len(dfborrar.index)
            dfborrar.drop(dfborrar.index[[range(0, filas, 1)]], inplace = True)
            dfborrar.reset_index(drop = True).to_csv('../bases de datos/lab4 estudiantes v2.csv',index=False)

            flash('Base de datos reseteada exitosamente', 'success') # info  success warning
            flash('Registro de laboratorios actualmente cerrados, tenga en cuenta los horarios', 'info')
           
            return render_template("lab3.html", title='Laboratorio4', lab_cerrar=lab_cerrar)

        flash('Registro de laboratorios actualmente cerrados, tenga en cuenta los horarios', 'info') # info  success warning
     
        return render_template("lab3.html", title='Laboratorio4', lab_cerrar=lab_cerrar)

    return render_template("lab3.html", title='Laboratorio4')
