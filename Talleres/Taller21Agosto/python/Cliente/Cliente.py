import socket
from Scanner import *


def HacerConsulta(host, puerto, mensaje, imprimir = ""):

    socket1 = socket.socket()
    socket1.connect((host, puerto))
    #necesito temporizador????
    socket1.send(mensaje)


    #tiempo = raw_input(imprimir +", presione enter para terminar")
    #posible temporizador
    res = socket1.recv(1024)


    socket1.close()

    return res

if __name__ == "__main__":

    print("taller 3")
    host = "localhost"
    puerto = 7003


    #Obtengo los numeros
    sc = Scanner()
    direccion =  HacerConsulta(host,puerto, sc.getOperation(), "Obteniendo direccionamiento")
    #socket1.send(sc.getOperation())
    dirr = direccion.split(' ')

    print("direccionado a:", dirr)
    resultado = HacerConsulta(dirr[0],int(dirr[1]), sc.getDataToSend(), "realizando operacion: " + sc.getOperation() )

    print("el resultado es: " + resultado)
