import os
import xlwt
from datetime import datetime
c=1

fh=1


#################posicion archivo##################
carpeta=os.getcwd()
carpeta=carpeta.split("code")
tabla=carpeta[0]+"data/tabla_mapa.xls"
carpeta=carpeta[0]+"data/archivos.txt"

###############################################
texto = open(carpeta, "r")
Palabras1 = texto.read()
texto.close()
palabras = Palabras1.splitlines()
######################################################
style0 = xlwt.easyxf('font: name Times New Roman, colour red, bold on')
style1 = xlwt.easyxf('',num_format_str='DD-MMM-YY')
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet',cell_overwrite_ok=True)
###############################################organizar textos###########################
ws.write(0, 0, 'humedad', style0)
ws.write(0, 1, 'temperatura', style0)
ws.write(0, 2, 'aire', style0)
ws.write(0, 3, 'monoxido', style0)
ws.write(0, 4, 'latitude		', style0)
ws.write(0, 5, 'longitude	', style0)


##############################humedad########################################
while True:

	try:
		linea=palabras[c]
		linea=linea.split(" ")
		ws.write(fh, 0, linea[0])
		ws.write(fh, 1, linea[1])
		ws.write(fh, 2, linea[2])
		ws.write(fh, 3, linea[3])
		ws.write(fh, 4, linea[4])
		ws.write(fh, 5, linea[5])
		c=c+1
		fh=fh+1
		

		
	except:	
		print "tabla terminada subir a google maps....."
		break	
#########################################temperatura################################





wb.save(tabla)
