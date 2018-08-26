

import xmlrpclib


class Direccionador:

    def makeOperacion(self):

        if(self.op == "+"):
            s = xmlrpclib.ServerProxy('http://localhost:10000')

            #enviamos los atributos que trae el direccionador a la clase almacenada en el servidor
            s.setNumero1(self.getNumero1())
            s.setNumero2(self.getNumero2())
            s.setOp(self.getOp())
            return s.suma()

        elif(self.op == "-"):
            s = xmlrpclib.ServerProxy('http://localhost:11003')

            #enviamos los atributos que trae el direccionador a la clase almacenada en el servidor
            s.setNumero1(self.getNumero1())
            s.setNumero2(self.getNumero2())
            s.setOp(self.getOp())
            return s.resta()

        elif(self.op == "*"):
            s = xmlrpclib.ServerProxy('http://localhost:12001')

            #enviamos los atributos que trae el direccionador a la clase almacenada en el servidor
            s.setNumero1(self.getNumero1())
            s.setNumero2(self.getNumero2())
            s.setOp(self.getOp())
            return s.multiplicacion()

        elif(self.op == "/"):
            s = xmlrpclib.ServerProxy('http://localhost:13000')

            #enviamos los atributos que trae el direccionador a la clase almacenada en el servidor
            s.setNumero1(self.getNumero1())
            s.setNumero2(self.getNumero2())
            s.setOp(self.getOp())
            return s.division()

        elif(self.op == "rad"):
            s = xmlrpclib.ServerProxy('http://localhost:14000')

            #enviamos los atributos que trae el direccionador a la clase almacenada en el servidor
            s.setNumero1(self.getNumero1())
            s.setNumero2(self.getNumero2())
            s.setOp(self.getOp())
            return s.radiacion()

        elif(self.op == "log"):
            s = xmlrpclib.ServerProxy('http://localhost:15000')

            #enviamos los atributos que trae el direccionador a la clase almacenada en el servidor
            s.setNumero1(self.getNumero1())
            s.setNumero2(self.getNumero2())
            s.setOp(self.getOp())
            return s.logaritmacion()

        elif(self.op == "pow"):
            s = xmlrpclib.ServerProxy('http://localhost:16001')

            #enviamos los atributos que trae el direccionador a la clase almacenada en el servidor
            s.setNumero1(self.getNumero1())
            s.setNumero2(self.getNumero2())
            s.setOp(self.getOp())
            return s.potenciacion()



    def setNumero1(self, nro1):
        self.numero1 = nro1
        return True

    def setNumero2(self, nro2):
        self.numero2 = nro2
        return True

    def setOp(self, op):
        self.op = op
        return True


    def getNumero1(self):

        return self.numero1

    def getNumero2(self):

        return self.numero2

    def getOp(self):

        return self.op
