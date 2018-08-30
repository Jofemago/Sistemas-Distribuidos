

import socket
import sys
import thread


from Direccionador import *


def direccionar(sc,addr):

    d = Direccionador()
    dirr = d.getServer(sc.recv(1024))
    sc.send(dirr)


if __name__ == "__main__":


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('', 3005))
    s.listen(10)


    print "respondiendo..."
    while 1:
        sc, addr = s.accept()
        print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
        print "\n"
        thread.start_new_thread(direccionar,(sc,addr))

    sc.close()
    s.close()
