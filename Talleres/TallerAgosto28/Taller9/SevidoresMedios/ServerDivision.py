
import socket
import sys
import thread

from Calculadora import *


def operar(sc, addr):


    data1,data2,opcionMenu = sc.recv(1024).split()
    print "recibido", data1, data2, opcionMenu


    c = Calculadora(data1, data2, opcionMenu)
    enviar = c.division()

    sc.send(enviar)


if __name__ == "__main__":

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('', 13000))
    s.listen(10)


    print "respondiendo..."

    while 1:

        sc, addr = s.accept()
        print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
        print "\n"
        thread.start_new_thread(operar,(sc,addr))


    sc.close()
    s.close()
