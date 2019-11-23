
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot

def grafica():
    # importar datos por semana :
    datos = pd.read_csv('PromedioSemana.csv', header=0)
    # importar datos semana1
    lunes1 = datos['lunes1']
    martes1 = datos['martes1']
    miercoles1 = datos['miercoles1']
    jueves1 = datos['jueves1']
    viernes1 = datos ['viernes1']
    sabado1 = datos ['sabado1']
    domingo1 = datos ['domingo1']
    # importar datos semana2
    lunes2 = datos['lunes2']
    martes2 = datos['martes2']
    miercoles2 = datos['miercoles2']
    jueves2 = datos['jueves2']
    viernes2 = datos ['viernes2']
    sabado2 = datos ['sabado2']
    domingo2 = datos ['domingo2']
    # importar datos semana3
    lunes3 = datos['lunes3']
    martes3 = datos['martes3']
    miercoles3 = datos['miercoles3']
    jueves3 = datos['jueves3']
    viernes3 = datos ['viernes3']
    sabado3 = datos ['sabado3']
    domingo3 = datos ['domingo3']
    # PromedioSemanas
    total=[]
    # promedio por semanas y dia
    promedio1=0
    primedio2=0
    promedio3=0
    promedio4=0
    primedio5=0
    promedio6=0
    promedio7=0
    #prueba de eje x y
    ejex = []
    ejey = []
    for x in range(1,7):
        for y in range(1,14):
            ejex.append(x)
            ejey.append(y)
    # llamar dastos por dia y semana
    # adicionar datos a total
    # lunes
    for x1 in range(0,13):
        promedio1 = lunes1[x1]+lunes2[x1]+lunes3[x1]
        total.append(promedio1/3)
    # martes
    for x2 in range(0,13):
        promedio2 = martes1[x2]+martes2[x2]+martes3[x2]
        total.append(promedio2/3)
    # miercoles
    for x3 in range(0,13):
        promedio3 = miercoles1[x3]+miercoles2[x3]+miercoles3[x3]
        total.append(promedio3/3)
    # jueves
    for x4 in range(0,13):
        promedio4 = jueves1[x4]+jueves2[x4]+jueves3[x4]
        total.append(promedio4/3)
    # viernes
    for x5 in range(0,13):
        promedio5 = viernes1[x5]+viernes2[x5]+viernes3[x5]
        total.append(promedio5/3)
    # sabado
    for x6 in range(0,13):
        promedio6 = sabado1[x6]+sabado2[x6]+sabado3[x6]
        total.append(promedio6/3)
    # domingo
    #for x7 in range(0,13):
    #    promedio7 = domingo1[x7]+domingo2[x7]+domingo3[x7]
    #    total.append(promedio7/3)

    """
    print  ( ejex ,"=",len (ejex) )
    print  ( ejey ,"=",len (ejey) )
    print ( total,"=",len(total) )
    print ( lunes1,"=",len(lunes1) )
    print ( lunes2,"=",len(lunes2) )
    print ( lunes3,"=",len(lunes3) )
    """
    """
    plt.plot (ejex, total, 'ro')
    plt.xlabel('Edad')
    plt.ylabel('Semestre')
    plt.show()
    """

    """
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.scatter3D(ejex,total,ejey, c=ejex, cmap='Set1')
    ax.plot_wireframe(ejex,total,ejey)
    """

    # nombres en el eje x
    c = ["0","lun","mar","mier","jue","vie","sab"]#,"dom"]
    h = ["0","10 am","12 am","2 pm","4 pm","6 pm","8 pm"]
    #fig=plt.figure()
    fig, ax = plt.subplots()
    plt.scatter(ejex,ejey,s=250,c=total,cmap='jet',marker='o')

    plt.xlim(0,7)
    plt.ylim(0,14)
    plt.title('flujo de semana')
    plt.xlabel('Dias')
    plt.ylabel('horas')
    ax.set_xticklabels(c)
    ax.set_yticklabels(h)

    cbar = plt.colorbar()
    cbar.set_label('cantidad de personas')
    # comado para tomar foto
    pyplot.savefig('static/PruebaFoto.png')
    # para ver la grafica
    # plt.show()
    x1=1
    return x1
#grafica()
