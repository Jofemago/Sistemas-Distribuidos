import xmlrpclib
from Scanner import *



if __name__ == "__main__":
    s = xmlrpclib.ServerProxy('http://localhost:8005')
    sc = Scanner()

    #print s.system.listMethods()


    #cargo en la instancia todos los datos
    s.setNumero1(sc.getNro1())
    s.setNumero2(sc.getNro2())
    s.setOp(sc.getOperation())

    print("el resultado de la operacion " + sc.getOperation() + " es:" + s.makeOperacion())
