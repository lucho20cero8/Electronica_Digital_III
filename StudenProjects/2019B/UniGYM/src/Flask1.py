from flask import Flask, escape, request, redirect, url_for, session, flash, request
from flask import render_template

from PromedioSemana import grafica

from doc_exportar import login
from doc_exportar import calificacion
from doc_exportar import correo
from doc_exportar import promedio
from doc_exportar import guardar

app = Flask(__name__)

@app.route('/')
def PPusuario():
    return render_template('/usuario/PPusuario.html')

@app.route('/SDusuario')
def SDusuario():
    return render_template('/usuario/SDusuario.html')

@app.route('/HOusuario')
def HOusuario():
    x1=grafica()
    print ("funciona la grafica",x1)
    return render_template('/usuario/HOusuario.html')

# administrador

@app.route('/PPadministrador')
def PPadministrador():
    return render_template('/AD/PPadministrador.html')

@app.route('/SDadministrador')
def SDadministrador():
    return render_template('/AD/SDadministrador.html')

@app.route('/HOadministrador')
def HOadministrador():
    x1=grafica()
    print ("funciona la grafica",x1)
    return render_template('/AD/HOadministrador.html')

### opciones
#  log
@app.route('/LOG')
def LOG():
    return render_template('/log/LOG.html')

@app.route('/CODLOG')
def CODLOG():

    verdad=2
    userr = request.args.get('userr')
    contrasenaa = request.args.get('contrasenaa')

    print (userr,"=",contrasenaa)

    if userr=='' or contrasenaa=='':
        return redirect(url_for('LOG'))
    else:
        verdad=login(userr,contrasenaa)

        if verdad==1:
            return redirect(url_for('PPadministrador'))

        elif verdad==0:
            return render_template('/log/RES0LOG.html')
###
# Calificar
@app.route('/ADcalificar')
def ADcalificar():
    return render_template('/calificar/ADcalificar.html')

@app.route('/CODcalificar',methods=['GET'])
def CODcalificar():

    verdad=2
    codigo = request.args.get('codigo')
    nota = request.args.get('nota')

    print (codigo,"=",nota)

    respuesta =[{'ya':'porfavor'}]

    if codigo=='' or nota=='':
        return redirect(url_for('ADcalificar'))
    else:
        verdad=calificacion(codigo,nota)
        if verdad==1:
            #return redirect(url_for('ADcalificar',respuesta=respuesta ))
            return render_template('/calificar/RES1calificar.html',respuesta=respuesta )
        elif verdad==0:
            #return redirect(url_for('ADcalificar',respuesta=respuesta ))
            return render_template('/calificar/RES0calificar.html',respuesta=respuesta )
###
# promedio
@app.route('/ADpromedio')
def ADpromedio():
    return render_template('/promedio/ADpromedio.html')

@app.route('/CODpromedio',methods=['GET'])
def CODpromedio():

    verdad=2
    codigo = request.args.get('codigo')

    print (codigo,"=")

    if codigo=='':
        return redirect(url_for('ADpromedio'))
    else:
        verdad=promedio(codigo)
        print(verdad[0])
        print(verdad[1])

        if verdad[1]==1:
            return render_template('/promedio/RES1promedio.html',verdad = verdad[0])
        elif verdad[1]==0:
            return render_template('/promedio/RES0promedio.html')
###
# correo
@app.route('/ADcorreo')
def ADcorreo():
    return render_template('/correo/ADcorreo.html')

@app.route('/CODcorreo',methods=['GET'])
def CODcorreo():

    #destinatario = request.args.get('destinatario')
    asunto = request.args.get('asunto')
    mensajee = request.args.get('mensajee')

    print ("=",asunto,"=",mensajee)

    #if destinatario=='':
    #    return redirect(url_for('ADcorreo'))
    #else:
    correo(asunto,mensajee)
    return render_template('/correo/RES1correo.html')
###

#  registro
@app.route('/ADregistro')
def ADregistro():
    return render_template('/registro/ADregistro.html')

@app.route('/CODregistro')
def CODregistro():
    verdad=0

    codigo      = request.args.get('codigo')
    nombre      = request.args.get('nombre')
    cedula      = request.args.get('cedula')
    EPS         = request.args.get('EPS')
    Nemergencia = request.args.get('Nemergencia')
    RH          = request.args.get('RH')
    carrera     = request.args.get('carrera')
    correo      = request.args.get('correo')

    if codigo=='' or nombre=='' or cedula=='' or EPS=='' or Nemergencia=='' or RH=='' or carrera=='' or correo=='':
        return render_template('/registro/RES0registro.html')
    else:
        verdad=guardar(codigo,nombre,cedula,EPS,Nemergencia,RH,carrera,correo)
        if verdad==1:
                return render_template('/registro/RES1registro.html')
        elif verdad==2:
                return render_template('/registro/RES2registro.html')
###

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
