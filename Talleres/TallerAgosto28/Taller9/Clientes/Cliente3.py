import socket
import sys

from Scanner import *


if __name__ == "__main__":


    scan = Scanner()
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(('localhost', 3005))

    s.send(scan.getOperation())
    #sevidor = s.recv(1024)
    direccion = s.recv(1024)
    ip, puerto = direccion.split()

    s2 = socket.socket()
    s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s2.connect((ip, int(puerto)))

    s2.send(scan.getDataToSend())


    print "---------------------------------"
    print "El resultado de la operacion " + scan.getOperation() + " es: "+ s2.recv(1024)
    print "---------------------------------"
