
import socket
import sys

from Scanner import *



if __name__ == "__main__":

    scan = Scanner()

    #socket
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(('localhost', 9885))


    s.send(scan.getDataToSend())


    print "---------------------------------"
    print "El resultado de la operacion " + scan.getOperation() + " es: "+ s.recv(1024)
    print "---------------------------------"
