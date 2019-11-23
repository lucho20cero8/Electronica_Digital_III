import time
import telebot
from telebot import types
import logging, sys, os

TOKEN = 'INSERT HERE YOUR BOT TOKEN'


ffx =  open("Usuarios.txt")
knownUsers = ffx.read() # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard

#teclado primario
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Profesores')
itembtn2 = types.KeyboardButton('Salones')
itembtn3 = types.KeyboardButton('Laboratorios')
itembtn4 = types.KeyboardButton('Información')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4)


#teclados secundarios
slectBloque = types.ReplyKeyboardMarkup(row_width=2)
slectBloque.add('Bloque 1', 'Bloque 2', 'Bloque 3', 'Bloque 4', 'Bloque 5', 'Bloque 6', 'Bloque 7', 'Bloque 8', 'Bloque 9')
slectTeacher = types.ReplyKeyboardMarkup(row_width=2)
slectTeacher.add('Luisa Gallo', 'Oswaldo Lopez', 'Rodolfo Gutierrez', 'Harold Murcia', 'Carlos Sandoval', 'Oscar Barrero', 'William Londoño', 'David Gonzalez')
slectInfo = types.ReplyKeyboardMarkup(row_width=2)
slectInfo.add('Electivas', 'Opciones de trabajo de grado', 'Contactar', 'Materias de semestre', 'Fechas especiales', 'Semilleros')



#teclados terciarios
slectLab = types.ReplyKeyboardMarkup(row_width=2)
slectLab.add('L1', 'L2', 'L3', 'L4', 'L5', 'L6')
slectBloque1 = types.ReplyKeyboardMarkup(row_width=2)
slectBloque1.add('11', '12', '13', '14', '15')
slectBloque2 = types.ReplyKeyboardMarkup(row_width=2)
slectBloque2.add('21', '23', '24', '25', '26')
slectBloque3 = types.ReplyKeyboardMarkup(row_width=2)
slectBloque3.add('31', '32', '33', '34', '35')
slectBloque4 = types.ReplyKeyboardMarkup(row_width=2)
slectBloque4.add('41', '42', '43', '44', '45')
slectBloque5 = types.ReplyKeyboardMarkup(row_width=2)
slectBloque5.add('51', '52', '53', '54', '55', '56')
slectBloque6 = types.ReplyKeyboardMarkup(row_width=2)
slectBloque6.add('61', '62', '63', '64', '65')
slectBloque7 = types.ReplyKeyboardMarkup(row_width=2)
slectBloque7.add('73', '74', '75')
slectBloque8 = types.ReplyKeyboardMarkup(row_width=2)
slectBloque8.add('811', '812', '813', '821', '822', '823')
slectBloque9 = types.ReplyKeyboardMarkup(row_width=2)
slectBloque9.add('914', '915', '916', '924', '925')
slectElectivas = types.ReplyKeyboardMarkup(row_width=2)
slectElectivas.add('Profesionales', 'Humanidades')
slectMaterias = types.ReplyKeyboardMarkup(row_width=2)
slectMaterias.add('Semestre 1', 'Semestre 2', 'Semestre 3', 'Semestre 4', 'Semestre 5', 'Semestre 6', 'Semestre 7', 'Semestre 8', 'Semestre 9', 'Semestre 10')
slectOpcionesGrado = types.ReplyKeyboardMarkup(row_width=2)
slectOpcionesGrado.add('Monografía', 'Asistencia de investigación', 'Trabajo de investigación', 'Opción emprendimiento')











def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0




# Historial de mensajes recibidos en la consola
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) +  " " + str(m.chat.last_name) + " [" + time.strftime("%I:%M:%S") + "] [" + str(m.chat.id) + "]: " + m.text)
            file = open("Registro.txt", "a")
            file.write(str(m.chat.first_name) +  " " + str(m.chat.last_name) + " [" + time.strftime("%I:%M:%S") + "] [" + str(m.chat.id) + "]: " + m.text + "\n")


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener





# Respuesta a comando /start de inicio del usuario
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = str(m.chat.id)
    ffx =  open("Usuarios.txt")
    knownUsers = ffx.read()
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        #ownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        #userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        file2 = open("Usuarios.txt", "a")
        file2.write(str(m.chat.first_name) +  " " + str(m.chat.last_name) + " [" + time.strftime("%I:%M:%S") + "] [" + str(m.chat.id) + "] " + "\n")

        bot.send_message(cid, "Hola {} {}!👋".format(m.chat.first_name, m.chat.last_name, ))
        bot.send_message(cid, "Mi nombre es UnibaguePocketBot 🤖 \nMi propósito es orientarte y darte información acerca de la Universidad de Ibagué 🎓📖 puedes consultar información usando las siguientes palabras:", reply_markup=markup)
        bot.send_message(cid, "👩‍🏫Profesores: Te enviaré la lista de profesores de Ingeniería electrónica\n🏠Salones: Te enviare una lista de salones que puedes consultar \n🏠Laboratorios: Te enviare la lista de laboratorios de ingeniería \n💬Información: Te brindare información general acerca de la carrera de ingeniería electrónica")
        #bot.send_message(cid, "Soy un proyecto de la asignatura Electronica Digital III y aunque estoy en fase de desarrollo mis funicones mas basicas ya estan funcionando correctamente, si no te respondo es porque estoy apagado, pero en cuando yo este encendido recibire tu mensaje y te respondere, de forma que podras envirme una solicitud")
    else:

        bot.send_message(cid, "Hola {} {}!".format(m.chat.first_name, m.chat.last_name))
        #no quitar este espacio
        bot.send_message(cid, "Mi nombre es UnibaguePocketBot 🤖 \nMi propósito es orientarte y darte información acerca de la Universidad de Ibagué 🎓📖 puedes consultar información usando las siguientes palabras:", reply_markup=markup)
        bot.send_message(cid, "👩‍🏫Profesores: Te enviaré la lista de profesores de Ingeniería electrónica\n🏠Salones: Te enviare una lista de salones que puedes consultar \n🏠Laboratorios: Te enviare la lista de laboratorios de ingeniería \n💬Información: Te brindare información general acerca de la carrera de ingeniería electrónica")
        #bot.send_message(cid, "Soy un proyecto de la asignatura Electronica Digital III y aunque estoy en fase de desarrollo mis funicones mas basicas ya estan funcionando correctamente, si no te respondo es porque estoy apagado, pero en cuando yo este encendido recibire tu mensaje y te respondere, de forma que podras envirme una solicitud")

#selecionar tipo de Electiva
@bot.message_handler(func=lambda message: message.text == "Electivas")
def command_text_opcioneselectivas(m):
    bot.send_message(m.chat.id, "¿Acerca de qué tipo de electiva quieres información?", reply_markup=slectElectivas)



# Respuesta a mensaje concreto de menu principal
@bot.message_handler(func=lambda message: message.text == "Salones")
def command_text_salones(m):
    bot.send_message(m.chat.id, "Los salones en la Universidad de Ibagué están distribuidos de la siguiente forma:\n  \n#X donde # es el número de bloque y X el número de salón  \n¿En qué bloque está ubicado el salón que buscas?", reply_markup=slectBloque)
@bot.message_handler(func=lambda message: message.text == "Información")
def command_text_info(m):
    bot.send_message(m.chat.id, "¿Que información deseas conocer?", reply_markup=slectInfo)
@bot.message_handler(func=lambda message: message.text == "Profesores")
def command_text_teacherlist(m):
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/prof.jpg', 'rb'))
    bot.send_message(m.chat.id, "Lista de profesores de la facultad de ingeniería electrónica: \nLuisa Fernanda Gallo Sanchez \nOswaldo Lopez Santos \nRodolfo Jose Gutierrez Gonzales \nHarold Fabian Murcia Moreno \nCarlos Alberto Sandoval Cardenas \nOscar Barrero Mendoza \nWilliam Londoño \nDavid Gonzalez", reply_markup=slectTeacher)
    bot.send_message(m.chat.id, "Pulsa en cualquiera de sus nombres para adquirir mas información como su correo, horario de asesorias o materias que dicta")
@bot.message_handler(func=lambda message: message.text == "Laboratorios")
def command_text_lablist(m):
    bot.send_message(m.chat.id, "¿Cual laboratorio estas buscando?", reply_markup=slectLab)




#respuesta a teclado de Electivas
@bot.message_handler(func=lambda message: message.text == "Profesionales")
def command_text_infoPro(m):
    bot.send_message(m.chat.id, "Electivas profesionales:\n🔹Inteligencia artificial \n🔹Internet: Redes y comuncaciones IP \n🔹Control de motores electricos \n🔹Convertidores de energia electrica \n🔹Mando y control electrico \n🔹Automatizacion industrial \n🔹Bioelectronica \n🔹Sistemas de telecomunicaciones", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Humanidades")
def command_text_infoHum(m):
    bot.send_message(m.chat.id, "Electivas de humanidades:\n🔹TERTULIA LITERARIA \n🔹TALLER DE ORIGAMI \n🔹TALLER DE MALABARES \n🔹ARCILLA, FUEGO Y ESPERANZA \n🔹EXPERIENCIA EN ACUARELA \n🔹TALLER DE CREACION LITERARIA \n🔹HISTORIA DEL ARTE \n🔹HISTORIA ANALITICA UNIVERSAL \n🔹HISTORIA ANALITICA DE COLOMBIA \n🔹ESCUELAS DEL PENSAMIENTO CIENTIFICO \n🔹FOTOGRAFIA BASICA \n🔹ANTROPOLOGIA GENERAL \n🔹ETICA AMBIENTAL \n🔹LITERATURA HISPANOAMERICANA \n🔹CINE Y PALABRA \n🔹VIDA COTIDIANA EN LA MODERNIDAD \n🔹ANTROPOLOGIA - SALUD Y ENFERMEDAD \n🔹ENGLISH THROUGH LITERATURE - CINEMA \n🔹GEOPOLITICA Y CULTURA POPULAR \n🔹ESTUDIOS AFROCOLOMBIANOS \n🔹EL COMER Y EL PODER \n🔹ETICA DEL CUIDADO DE SI \n🔹ALTERIDAD, GENERO Y POLITICA \n🔹FUTBOL Y LITERATURA \n🔹PSICOLOGIA Y ESPIRITUALIDAD \n🔹SUPER VILLANOS Y SUPER HEROES: L.C. \n🔹NATURALEZA Y AMBIENTE EN C.FICCION \n🔹PERSPECT. DE GENERO Y SEXUALIDAD \n🔹EL DOCUMENTAL Y SUS FORMAS NARRATIV \n🔹CIUDADES Y CULTURA: UNA EXPERIANCIA \n🔹CONSTRUC. PAZ, CIUDADAN. Y CONVIVEN  \n🔹SEMIOTICA \n🔹LOGICA \n🔹Política y sociedad \n🔹Cultura, violencia y región \n🔹Movimientos sociales \n🔹Colombia en el contexto internacional \n🔹Cultura y política \n🔹Ecologia y gestion ambiental ", reply_markup=markup)



#Respuesta a opciones de grado
@bot.message_handler(func=lambda message: message.text == "Opciones de trabajo de grado")
def command_text_infoGrado(m):
    bot.send_message(m.chat.id, "La universidad consta de 4 opciones de grado: ")
    bot.send_message(m.chat.id, "🔹Monografía  \n🔹Asistencia de investigación \n🔹Trabajo de investigación \n🔹Opción emprendimiento", reply_markup=slectOpcionesGrado)
    bot.send_message(m.chat.id, "En el plan de estudios, los estudiantes deben aprobar el 75% de los créditos totales de dicho plan, para inscribir cualquiera de las modalidades de trabajo de grado")



#Respuesta a contactar
@bot.message_handler(func=lambda message: message.text == "Contactar")
def command_text_infoContactar(m):
    bot.send_message(m.chat.id, "Numero telefónico de la Universidad: 2760010\nExtensión de la facultad de ingeniería electrónica:4251", reply_markup=markup)
    bot.send_message(m.chat.id, "Correo electrónico de la facultad de ingeniería electrónica: ingenieriaelectronica@unibague.edu.co")
    bot.send_message(m.chat.id, "Facebook del programa: https://www.facebook.com/electronica.unibague")
    bot.send_message(m.chat.id, "Micrositio del programa de Ing Electronica: https://electronica.unibague.edu.co/")


#Respuesta a Materias de semestre
@bot.message_handler(func=lambda message: message.text == "Materias de semestre")
def command_text_infoMaterias(m):
    bot.send_message(m.chat.id, "Elija el semestre en el que deseas conocer las materias", reply_markup=slectMaterias)



#Respuesta a Fechas especiales
@bot.message_handler(func=lambda message: message.text == "Fechas especiales")
def command_text_infoFechas(m):
    bot.send_message(m.chat.id, "Noviembre: \n\n15  Solicitud y trámite Validación hasta \n21 - 27  Digitación y entrega de notas - tercer reporte \n27  Entrega de listados oficiales y borradores de notas de los docentes a los programas \n27  Finalización semestre académico B/2019 \n29  Presentación examen Validación", reply_markup=markup)




#Respuesta a Semilleros
@bot.message_handler(func=lambda message: message.text == "Semilleros")
def command_text_infoSemilleros(m):
    bot.send_message(m.chat.id, "El programa de Ing Electronica consta de 7 grupo de investigación", reply_markup=markup)
    bot.send_message(m.chat.id, "Semillero D+TAP: \n\nTema de estudio: Monitoreo remoto y sistemas de navegación autónomo para la agricultura de precisión. \nCoordinador: Óscar Barrero Mendoza.")
    bot.send_message(m.chat.id, "Semillero MEC-AUTRONIC: \n\nTema de estudio: Sistemas mecatrónicos. \nCoordinador: Jorge Andrés García")
    bot.send_message(m.chat.id, "Semillero SICEP: \n\nTema de estudio: Convertidores electrónicos para sistemas de aprovechamiento de energía solar fotovoltaica. \nCoordinador: Oswaldo López Santos.")
    bot.send_message(m.chat.id, "Semillero SIRUI: \n\nTema de estudio: Móviles autónomos. \nCoordinador: William Londoño.")
    bot.send_message(m.chat.id, "Semillero GIEM: \n\nTema de estudio: Adquisición y procesamiento de señales biomédicas. \nCoordinador: Luisa Fernanda Gallo.")
    bot.send_message(m.chat.id, "Semillero SI2C: \n\nTema de estudio: Sistemas de instrumentación y control. \nCoordinador: Harold Fabián Murcia.")
    bot.send_message(m.chat.id, "Semillero LUN: \n\nTema de estudio: Procesamiento de imágenes, computación gráfica y reconocimiento de patrones. \nCoordinador: Manuel Guillermo Forero.")



#Respuesta a slectOpcionesGrado (Opciones de grado)
@bot.message_handler(func=lambda message: message.text == "Monografía")
def command_text_Monografia(m):
    bot.send_message(m.chat.id, "Monografía: Es un trabajo escrito, resultado de un proyecto de indagación dirigida, adelantado por el estudiante, quien contará con el acompañamiento comodirector, de un profesor de planta de la Universidad, de un profesor de cátedra o de un asesor externo, avalado por el Comité de Gradorespectivo.", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Asistencia de investigación")
def command_text_Asistencia(m):
    bot.send_message(m.chat.id, "Asistencia de investigación: Consiste en un trabajo que se elabora como producto de una actividad investigativa realizado por el estudiante, quien en calidad de asistente de investigación trabaja en un proyecto liderado por un docente investigador. El proyecto debe estar inscrito ante la Dirección de Investigaciones de la Universidad.", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Trabajo de investigación")
def command_text_Trabajo(m):
    bot.send_message(m.chat.id, "Trabajo de investigación: Consiste en un trabajo de investigación desarrollado por un estudiante, bajo la dirección de un profesor de planta de la Universidad, de un profesor de cátedra o de un asesor externo, avalado por el Comité de Grado respectivo.", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Opción emprendimiento")
def command_text_Emprendimiento(m):
    bot.send_message(m.chat.id, "Proyecto de emprendimiento: Los planes de negocio desarrollados por los estudiantes con el apoyo de la Unidad de Emprendimiento de la Universidad, que reciban un premio en una convocatoria regional, nacional o internacional, avalada por la Institución, serán aceptados como modalidad de trabajo de grado.", reply_markup=markup)




#Respuesta a slectMaterias (Materias de semestre)
@bot.message_handler(func=lambda message: message.text == "Semestre 1")
def command_text_Semestre1(m):
    bot.send_message(m.chat.id, "Fundamentos de matematicas \nIntroduccion a la ingeneria \nEtica y politica \nContexto y region \nEspacios de conversación \nLectura y escritura en la universidad 1", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Semestre 2")
def command_text_Semestre2(m):
    bot.send_message(m.chat.id, "Fisica y matematicas 1 \nQuimica \nAlgebra lineal \nTaller introduccion a la ingenieria \nLectura y escritura en la universidad 2", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Semestre 3")
def command_text_Semestre3(m):
    bot.send_message(m.chat.id, "Fisica y matematicas 2 \nCircuitos DC \nSemiconductores \nAPO 1", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Semestre 4")
def command_text_Semestre4(m):
    bot.send_message(m.chat.id, "Fisica y matematicas 3 \nEcuaciones diferenciales \nCircuitos AC \nElectronica 1 \nElectronica digital 1", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Semestre 5")
def command_text_Semestre5(m):
    bot.send_message(m.chat.id, "Variable compleja \nOndas y calor \nElectronica 2 \nProbabilidad y estadistica \nElectronica digital 2 \nTeoria electromagnetica", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Semestre 6")
def command_text_Semestre6(m):
    bot.send_message(m.chat.id, "Matematicas para electronica \nTeoria de señales \nMediciones e instrumentación \nElectronica de RF \nElectronica digital 3 \nComunicación e hipermedios", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Semestre 7")
def command_text_Semestre7(m):
    bot.send_message(m.chat.id, "Electiva de nucleo basico \nControl y laboratorio \nFisica cuantica \nFundamentos de comunicaciones \nElectiva general \nElectiva de humanidades 1", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Semestre 8")
def command_text_Semestre8(m):
    bot.send_message(m.chat.id, "Formación y evaluación de proyectos de ingenieria \nElectronica de potencia \nElectromedicina \nLineas y antenas \nElectiva en ingenieria \nElectiva de humanidades 2", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Semestre 9")
def command_text_Semestre9(m):
    bot.send_message(m.chat.id, "Pensamiento estrategico \nElectiva profesional 1 \nElectiva profesional 2 \nElectiva profesional 3 \nSeminario de paz y región \nElectiva de humanidades 3 \nOpcional: Trabajo de grado", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Semestre 10")
def command_text_Semestre10(m):
    bot.send_message(m.chat.id, "Trabajo de grado \nSemestre de paz y región ", reply_markup=markup)






#Respuestas teclado de profesores
@bot.message_handler(func=lambda message: message.text == "Luisa Gallo")
def command_text_infoluisa(m):
    bot.send_message(m.chat.id, "Horario de asesorias:\nMartes: 3pm - 4pm \nMiercoles: 11am - 12m \nluisa.gallo@unibague.edu.co", reply_markup=markup)
    bot.send_message(m.chat.id, "Materias:\nElectronica digital 1 \nElectromedicina \nBioelectronica \nTrabajo de grado ")
    bot.send_message(m.chat.id, "Si necesitas contactar al profesor en su horario de asesoria puedo enviarle el mensaje por ti, solo tienes que enviar el siguiente mensaje seguido de tu codigo y el texto a enviar")
    bot.send_message(m.chat.id, "Contactar Luisa Gallo")
    bot.send_message(m.chat.id, "Por ejemplo: \nContactar Luisa Gallo 2420001000 Hola, en vista de que...")
@bot.message_handler(func=lambda message: message.text == "Oswaldo Lopez")
def command_text_infooswaldo(m):
    bot.send_message(m.chat.id, "Horario de asesorias:\nMartes: 11am - 12m \nJueves: 11am - 12m \n oswaldo.lopez@unibague.edu.co", reply_markup=markup)
    bot.send_message(m.chat.id, "Materias:\nElectronica de potencia \nAutomatizacion industrial")
    bot.send_message(m.chat.id, "Si necesitas contactar al profesor en su horario de asesoria puedo enviarle el mensaje por ti, solo tienes que enviar el siguiente mensaje seguido de tu codigo y el texto a enviar")
    bot.send_message(m.chat.id, "Contactar Oswaldo Lopez")
    bot.send_message(m.chat.id, "Por ejemplo: \nContactar Oswaldo Lopez 2420001000 Hola, en vista de que...")
@bot.message_handler(func=lambda message: message.text == "Rodolfo Gutierrez")
def command_text_infofito(m):
    bot.send_message(m.chat.id, "Horario de asesorias:\nLunes: 5pm - 6pm \nMartes: 10am - 11am \nJueves: Jueves \nrodolfo.gutierrez@unibague.edu.co", reply_markup=markup)
    bot.send_message(m.chat.id, "Materias:\nElectronica 2 \nElectronica de RF \nFundamentos de comunicaciones \nLineas y antenas \nAudio y TV")
    bot.send_message(m.chat.id, "Si necesitas contactar al profesor en su horario de asesoria puedo enviarle el mensaje por ti, solo tienes que enviar el siguiente mensaje seguido de tu codigo y el texto a enviar")
    bot.send_message(m.chat.id, "Contactar Rodolfo Gutierrez")
    bot.send_message(m.chat.id, "Por ejemplo: \nContactar Rodolfo Gutierrez 2420001000 Hola, en vista de que...")
@bot.message_handler(func=lambda message: message.text == "Harold Murcia")
def command_text_infoharold(m):
    bot.send_message(m.chat.id, "Horario de asesorias:\nLunes: 11am - 12m \nViernes: 11am - 12m \nharold.murcia@unibague.edu.co", reply_markup=markup)
    bot.send_message(m.chat.id, "Materias:\nIntroduccion a la ingenieria electronica \nElectronica digital 3 \nTrabajo de grado")
    bot.send_message(m.chat.id, "Si necesitas contactar al profesor en su horario de asesoria puedo enviarle el mensaje por ti, solo tienes que enviar el siguiente mensaje seguido de tu codigo y el texto a enviar")
    bot.send_message(m.chat.id, "Contactar Harold Murcia")
    bot.send_message(m.chat.id, "Por ejemplo: \nContactar Harold Murcia 2420001000 Hola, en vista de que...")
@bot.message_handler(func=lambda message: message.text == "Carlos Sandoval")
def command_text_infosandoval(m):
    bot.send_message(m.chat.id, "Horario de asesorias:\nMartes: 8am - 11am \ncarlos.sandoval@unibague.edu.co", reply_markup=markup)
    bot.send_message(m.chat.id, "Materias:\nCircuitos DC \nCircuitos AC \nMediciones e instrumentación \nTeoria de señales \nMando y control electrico")
    bot.send_message(m.chat.id, "Si necesitas contactar al profesor en su horario de asesoria puedo enviarle el mensaje por ti, solo tienes que enviar el siguiente mensaje seguido de tu codigo y el texto a enviar")
    bot.send_message(m.chat.id, "Contactar Carlos Sandoval")
    bot.send_message(m.chat.id, "Por ejemplo: \nContactar Carlos Sandoval 2420001000 Hola, en vista de que...")
@bot.message_handler(func=lambda message: message.text == "Oscar Barrero")
def command_text_infobarrero(m):
    bot.send_message(m.chat.id, "Horario de asesorias:\nLunes: 10am - 12m \nMiercoles: 9am - 10am \nJueves: 5pm - 6pm \nViernes: 5pm - 6pm \noscar.barrero@unibague.edu.co", reply_markup=markup)
    bot.send_message(m.chat.id, "Materias:\nOndas y calor \nVariable compleja \nControl y laboratorio")
    bot.send_message(m.chat.id, "Si necesitas contactar al profesor en su horario de asesoria puedo enviarle el mensaje por ti, solo tienes que enviar el siguiente mensaje seguido de tu codigo y el texto a enviar")
    bot.send_message(m.chat.id, "Contactar Oscar Barrero")
    bot.send_message(m.chat.id, "Por ejemplo: \nContactar Oscar Barrero 2420001000 Hola, en vista de que...")
@bot.message_handler(func=lambda message: message.text == "William Londoño")
def command_text_infowilliam(m):
    bot.send_message(m.chat.id, "Horario de asesorias:\nLunes: 8am - 9:30am \nJueves: 8:30 - 10am \nViernes: 3pm - 4:30pm \nwilliam.londono@unibague.edu.co", reply_markup=markup)
    bot.send_message(m.chat.id, "Materias:\nSemiconductores \nElectronica 1")
    bot.send_message(m.chat.id, "Si necesitas contactar al profesor en su horario de asesoria puedo enviarle el mensaje por ti, solo tienes que enviar el siguiente mensaje seguido de tu codigo y el texto a enviar")
    bot.send_message(m.chat.id, "Contactar William Londoño")
    bot.send_message(m.chat.id, "Por ejemplo: \nContactar William Londoño 2420001000 Hola, en vista de que...")
@bot.message_handler(func=lambda message: message.text == "David Gonzalez")
def command_text_infowilliam(m):
    bot.send_message(m.chat.id, "Horario de asesorias:\nLunes: 6:30pm - 8:00pm \ndavid.gonzalez@unibague.edu.co", reply_markup=markup)
    #bot.send_message(m.chat.id, "Materias:\nSemiconductores \nElectronica 1")
    bot.send_message(m.chat.id, "Si necesitas contactar al profesor en su horario de asesoria puedo enviarle el mensaje por ti, solo tienes que enviar el siguiente mensaje seguido de tu codigo y el texto a enviar")
    bot.send_message(m.chat.id, "Contactar David Gonzalez")
    bot.send_message(m.chat.id, "Por ejemplo: \nContactar David Gonzalez 2420001000 Hola, en vista de que...")




#respuesta a teclado en bloques
@bot.message_handler(func=lambda message: message.text == "Bloque 1")
def command_text_b1(m):
    bot.send_message(m.chat.id, "En este bloque están ubicados los salones 11 a 15, te enviaré su ubicación y una foto del salon, te recomiendo pulsar el menu de opciones en el mapa y seleccionar la vista satelital.", reply_markup=slectBloque1)
@bot.message_handler(func=lambda message: message.text == "Bloque 2")
def command_text_b2(m):
    bot.send_message(m.chat.id, "En este bloque están ubicados los salones 21 a 24 y un poco más apartados están los salones 25 a 27, te enviaré sus ubicaciones y una foto del salon, te recomiendo pulsar el menu de opciones en el mapa y seleccionar la vista satelital.", reply_markup=slectBloque2)
@bot.message_handler(func=lambda message: message.text == "Bloque 3")
def command_text_b3(m):
    bot.send_message(m.chat.id, "En este bloque están ubicados los salones 31 a 34, te enviaré su ubicación y una foto del salon, te recomiendo pulsar el menu de opciones en el mapa y seleccionar la vista satelital.", reply_markup=slectBloque3)
@bot.message_handler(func=lambda message: message.text == "Bloque 4")
def command_text_b4(m):
    bot.send_message(m.chat.id, "En este bloque están ubicados los salones 41 a 45, te enviaré su ubicación y una foto del salon, te recomiendo pulsar el menu de opciones en el mapa y seleccionar la vista satelital.", reply_markup=slectBloque4)
@bot.message_handler(func=lambda message: message.text == "Bloque 5")
def command_text_b5(m):
    bot.send_message(m.chat.id, "En este bloque están ubicados los salones 51 a 56, te enviaré su ubicación y una foto del salon, te recomiendo pulsar el menu de opciones en el mapa y seleccionar la vista satelital.", reply_markup=slectBloque5)
@bot.message_handler(func=lambda message: message.text == "Bloque 6")
def command_text_b6(m):
    bot.send_message(m.chat.id, "En este bloque están ubicados los salones 61 a 65, te enviaré su ubicación y una foto del salon, te recomiendo pulsar el menu de opciones en el mapa y seleccionar la vista satelital.", reply_markup=slectBloque6)
@bot.message_handler(func=lambda message: message.text == "Bloque 7")
def command_text_b7(m):
    bot.send_message(m.chat.id, "En este bloque están ubicados los salones 73 a 75, te enviaré su ubicación y una foto del salon, te recomiendo pulsar el menu de opciones en el mapa y seleccionar la vista satelital.", reply_markup=slectBloque7)
@bot.message_handler(func=lambda message: message.text == "Bloque 8")
def command_text_b800(m):
    bot.send_message(m.chat.id, "En este bloque están ubicados los salones 811 a 813 en su primer piso y 821 a 823 en su segundo piso, te enviaré su ubicación y una foto del salon, te recomiendo pulsar el menu de opciones en el mapa y seleccionar la vista satelital.", reply_markup=slectBloque8)
@bot.message_handler(func=lambda message: message.text == "Bloque 9")
def command_text_b900(m):
    bot.send_message(m.chat.id, "En este bloque están ubicados los salones 914 a 916 en su primer piso y 924 a 925 en su segundo piso, te enviaré su ubicación y una foto del salon, te recomiendo pulsar el menu de opciones en el mapa y seleccionar la vista satelital.", reply_markup=slectBloque9)





#respuestas a salones especificos
#bloque 1
@bot.message_handler(func=lambda message: message.text == "11")
def command_text_s11(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 1, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/1112.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450804, -75.199318)
@bot.message_handler(func=lambda message: message.text == "12")
def command_text_s12(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 1, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/1112.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450803, -75.199330)
@bot.message_handler(func=lambda message: message.text == "13")
def command_text_s13(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 1, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/13.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450756,-75.199473)
@bot.message_handler(func=lambda message: message.text == "14")
def command_text_s14(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 1, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/14.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450725,-75.199547)
@bot.message_handler(func=lambda message: message.text == "15")
def command_text_s15(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 1, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/15.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4508131,-75.1995932)
@bot.message_handler(func=lambda message: message.text == "21")#
def command_text_s21(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 1, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/21.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4507566,-75.1994229)

@bot.message_handler(func=lambda message: message.text == "23")#
def command_text_s23(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 2, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/23.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450645,-75.199466)
@bot.message_handler(func=lambda message: message.text == "24")#
def command_text_s24(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 2, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/24.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450673,-75.199114)
@bot.message_handler(func=lambda message: message.text == "25")
def command_text_s25(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 2, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/2526.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4507118,-75.1992537)
@bot.message_handler(func=lambda message: message.text == "26")
def command_text_s26(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 2, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/2526.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4507118,-75.1992537)
@bot.message_handler(func=lambda message: message.text == "31")
def command_text_s31(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 3, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/3132.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450450,-75.199198)
@bot.message_handler(func=lambda message: message.text == "32")
def command_text_s32(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 3, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/3132.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450450,-75.199198)
@bot.message_handler(func=lambda message: message.text == "33")
def command_text_s33(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 3, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/3334.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450407,-75.199313)
@bot.message_handler(func=lambda message: message.text == "34")
def command_text_s34(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 3, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/3334.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450407,-75.199313)
@bot.message_handler(func=lambda message: message.text == "35")
def command_text_s35(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 4, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/35.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450380,-75.199387)
@bot.message_handler(func=lambda message: message.text == "41")
def command_text_s41(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 4, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/4142.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450356,-75.199177)
@bot.message_handler(func=lambda message: message.text == "42")
def command_text_s42(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 4, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/4142.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450356,-75.199177)
@bot.message_handler(func=lambda message: message.text == "43")
def command_text_s43(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 4, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/43.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450329,-75.199252)
@bot.message_handler(func=lambda message: message.text == "44")
def command_text_s44(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 4, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/44.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450319,-75.199293)
@bot.message_handler(func=lambda message: message.text == "45")
def command_text_s45(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 4, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/45.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.450303,-75.1993059)
@bot.message_handler(func=lambda message: message.text == "51")
def command_text_s51(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 5, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/5152.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4503825,-75.1992127)
@bot.message_handler(func=lambda message: message.text == "52")
def command_text_s52(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 5, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/5152.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4503825,-75.1992127)
@bot.message_handler(func=lambda message: message.text == "53")
def command_text_s53(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 5, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/5354.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4502084,-75.1991474)
@bot.message_handler(func=lambda message: message.text == "54")
def command_text_s54(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 5, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/5354.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4502084,-75.1991474)
@bot.message_handler(func=lambda message: message.text == "55")
def command_text_s55(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 5, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/5556.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4501979,-75.199147)
@bot.message_handler(func=lambda message: message.text == "56")
def command_text_s56(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 5, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/5556.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4501979,-75.199147)
@bot.message_handler(func=lambda message: message.text == "61")
def command_text_s61(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 6, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/61.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4502114,-75.1990972)
@bot.message_handler(func=lambda message: message.text == "62")
def command_text_s62(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 6, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/62.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4502114,-75.1990972)
@bot.message_handler(func=lambda message: message.text == "63")
def command_text_s63(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 6, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/63.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4501398,-75.1991727)
@bot.message_handler(func=lambda message: message.text == "64")
def command_text_s64(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 6, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/6465.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4501551,-75.1992572)
@bot.message_handler(func=lambda message: message.text == "65")
def command_text_s65(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 6, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/6465.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4501551,-75.1992572)
@bot.message_handler(func=lambda message: message.text == "73")
def command_text_s73(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 7, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/73.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4499583,-75.1988053)
@bot.message_handler(func=lambda message: message.text == "74")
def command_text_s74(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 7, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/74.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4500125,-75.1986204)
@bot.message_handler(func=lambda message: message.text == "75")
def command_text_s75(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 7, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/75.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4500125,-75.1986204)
@bot.message_handler(func=lambda message: message.text == "811")
def command_text_s811(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 8, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/811.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4498945,-75.1985045)
@bot.message_handler(func=lambda message: message.text == "812")
def command_text_s812(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 8, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/812813.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4498374,-75.1984731)
@bot.message_handler(func=lambda message: message.text == "813")
def command_text_s813(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 8, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/812813.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4498374,-75.1984731)
@bot.message_handler(func=lambda message: message.text == "821")
def command_text_s821(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 8, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/821.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4499259,-75.1984861)
@bot.message_handler(func=lambda message: message.text == "822")
def command_text_s822(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 8, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/822.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4499259,-75.1984861)
@bot.message_handler(func=lambda message: message.text == "823")
def command_text_s823(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 8, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/823.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4499259,-75.1984861)
@bot.message_handler(func=lambda message: message.text == "914")
def command_text_s914(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 9, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/914.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4497858,-75.1984635)
@bot.message_handler(func=lambda message: message.text == "915")
def command_text_s915(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 9, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/915.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4497858,-75.1984635)
@bot.message_handler(func=lambda message: message.text == "916")
def command_text_s916(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 9, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/916.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4498412,-75.1984432)
@bot.message_handler(func=lambda message: message.text == "924")
def command_text_s924(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 9, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/924.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4497859,-75.1984161)
@bot.message_handler(func=lambda message: message.text == "925")
def command_text_s925(m):
    bot.send_message(m.chat.id, "Salón ubicado en Bloque 9, te enviare su ubicación e Imagen del salón", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/925.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.4497859,-75.1984161)





#respuestas a laboratorios especificos
@bot.message_handler(func=lambda message: message.text == "L1")
def command_text_infoL1(m):
    bot.send_message(m.chat.id, "Este laboratorio está ubicado en el segundo piso del bloque de ingeniería, nombre en el cartel: Laboratorio General", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/L1.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.449283,-75.198693)
@bot.message_handler(func=lambda message: message.text == "L2")
def command_text_infoL2(m):
    bot.send_message(m.chat.id, "Este laboratorio está ubicado en el primer piso del bloque de ingeniería, nombre en el cartel: Electronica Industrial", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/L2.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.449283,-75.198693)
@bot.message_handler(func=lambda message: message.text == "L3")
def command_text_infoL3(m):
    bot.send_message(m.chat.id, "Este laboratorio está ubicado en el segundo piso del bloque de ingeniería, nombre en el cartel: Campos y Materiales", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/L3.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.449283,-75.198693)
@bot.message_handler(func=lambda message: message.text == "L4")
def command_text_infoL4(m):
    bot.send_message(m.chat.id, "Este laboratorio está ubicado en el segundo piso del bloque de ingeniería, nombre en el cartel: Electromedicina", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/L4.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.449283,-75.198693)
@bot.message_handler(func=lambda message: message.text == "L5")
def command_text_infoL5(m):
    bot.send_message(m.chat.id, "Este laboratorio está ubicado en el segundo piso del bloque de ingeniería, nombre en el cartel: Telecomunicaciones", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/L5.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.449283,-75.198693)
@bot.message_handler(func=lambda message: message.text == "L6")
def command_text_infoL6(m):
    bot.send_message(m.chat.id, "Este laboratorio está ubicado en el segundo piso del bloque de ingeniería, nombre en el cartel: Software Especializado", reply_markup=markup)
    bot.send_photo(m.chat.id, open('/home/vdesktop/Unibague/L6.jpg', 'rb'))
    bot.send_location(m.chat.id, 4.449283,-75.198693)




#Contactar Profesores
@bot.message_handler(regexp="Contactar Reinoso")
def command_text_infoL1(m):
    chatnumber=str(m.chat.id)
    bot.send_message(m.chat.id, "Le enviare tu mensaje al Ingeniero Reinoso")
    bot.send_message(628456976, "Hola ingeniero Reinoso, un estudiante me ha pedido contactarlo y le ha enviado el siguiente mensaje:")
    bot.forward_message(628456976, m.chat.id, m.message_id)
    bot.send_message(628456976, "Si desea responderle envie el siguiente mensaje seguido del texto a enviar:")
    bot.send_message(628456976, "Resp {}".format(chatnumber))
    bot.send_message(628456976, "Por ejemplo: R {} Hola, en estos momentos...".format(chatnumber))

@bot.message_handler(regexp="Contactar Richard")
def command_text_infoL1(m):
    chatnumber=str(m.chat.id)
    bot.send_message(m.chat.id, "Le enviare tu mensaje al Ingeniero Richard")
    bot.send_message(829828690, "Hola ingeniero Richard, un estudiante me ha pedido contactarlo y le ha enviado el siguiente mensaje:")
    bot.forward_message(829828690, m.chat.id, m.message_id)
    bot.send_message(829828690, "Si desea responderle envie el siguiente mensaje seguido del texto a enviar:")
    bot.send_message(829828690, "Resp {}".format(chatnumber))
    bot.send_message(829828690, "Por ejemplo: R {} Hola, en estos momentos...".format(chatnumber))

@bot.message_handler(regexp="Contactar Harold Murcia")
def command_text_infoL1(m):
    chatnumber=str(m.chat.id)
    bot.send_message(m.chat.id, "Le enviare tu mensaje al Ingeniero Harold")
    bot.send_message(891149149, "Hola ingeniero Harold, un estudiante me ha pedido contactarlo y le ha enviado el siguiente mensaje:")
    bot.forward_message(891149149, m.chat.id, m.message_id)
    bot.send_message(891149149, "Si desea responderle envie el siguiente mensaje seguido del texto a enviar:")
    bot.send_message(891149149, "Resp {}".format(chatnumber))
    bot.send_message(891149149, "Por ejemplo: R {} Hola, en estos momentos...".format(chatnumber))


#respuesta de profesores
@bot.message_handler(regexp="Resp")
def command_text_respteacher(m):
    texto=m.text
    p=texto.split()
    destino=p[1]
    if m.chat.id == 628456976:
        bot.send_message(destino, "Respuesta del Ingeniero Reinoso")
        bot.send_message(destino, m.text)
        bot.send_message(m.chat.id, "Respuesta enviada")
    if m.chat.id == 829828690:
        bot.send_message(destino, "Respuesta del Ingeniero Richard")
        bot.send_message(destino, m.text)
        bot.send_message(m.chat.id, "Respuesta enviada")
    if m.chat.id == 891149149:
        bot.send_message(destino, "Respuesta del Ingeniero Harold Murcia")
        bot.send_message(destino, m.text)
        bot.send_message(m.chat.id, "Respuesta enviada")

def solucionador():
    bot.send_message(628456976, "Error resuelto")



# Respuesta a cualquier mensaje por parte del usuario
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):

    bot.send_message(m.chat.id, "No estoy programado para entender o responder \"" + m.text + "\"\n Por favor usa uno de mis comandos predefinidos", reply_markup=markup)

def main_loop():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print("Exception occurred:", e)
            os.execv(sys.executable, ['python3'] + ['UPBn.py'])
            break
            time.sleep(2)
            sys.exit()
            pass
        else:
            break
    while 1:
        time.sleep(3)



if __name__ == '__main__':
    try:
        main_loop()

    except (ConnectionAbortedError, ConnectionResetError, ConnectionRefusedError, ConnectionError):
            print("Exception occurred:", e)
            time.sleep(2)
            os.execv(sys.executable, ['python3'] + ['UPBn.py'])
            bot.polling(none_stop=True)
            solucionador()
            pass
