

import xmlrpclib
from Scanner import *



if __name__ == "__main__":

    s = xmlrpclib.ServerProxy('http://localhost:5000')
    sc = Scanner()

    opera = xmlrpclib.ServerProxy(s.getServer(sc.getOperation()))


    opera.setNumero1(sc.getNro1())
    opera.setNumero2(sc.getNro2())
    opera.setOp(sc.getOperation())


    print("el resultado de la operacion " + sc.getOperation() + " es:" + opera.makeOperacion())
