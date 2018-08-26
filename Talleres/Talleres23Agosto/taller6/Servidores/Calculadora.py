from math import *


class Calculadora:

    def __init__(self, num1 = None, num2 = None , op = None):

        self.numero1 = num1
        self.numero2 = num2
        self.op = op

    def makeOperacion(self):

        if(self.op == "+"):
            return self.suma()

        elif(self.op == "-"):
            return self.resta()

        elif(self.op == "*"):
            return self.multiplicacion()

        elif(self.op == "/"):
            return self.division()

        elif(self.op == "rad"):
            return self.radiacion()

        elif(self.op == "log"):
            return self.logaritmacion()

        elif(self.op == "pow"):
            return self.potenciacion()



    def setNumero1(self, nro1):
        self.numero1 = nro1
        return False

    def setNumero2(self, nro2):
        self.numero2 = nro2
        return False

    def setOp(self, op):
        self.op = op
        return False

    def suma(self):

        assert(self.op == "+")
        return str(self.numero1 + self.numero2)

    def resta(self):

        assert(self.op == "-")
        return str(self.numero1 - self.numero2)


    def multiplicacion(self):

        assert(self.op == "*")
        return str(self.numero1 * self.numero2)

    def division(self):

        assert(self.op == "/")
        try:
            return str(self.numero1 / self.numero2)
        except Exception as e:
            return 'infinito'


    def potenciacion(self):
        assert(self.op == "pow")
        return str(self.numero1 ** self.numero2)


    #error en opercion siempre retorna 1
    def radiacion(self):

        assert(self.op == "rad")
        return str(self.numero1 ** (1 / self.numero2))

    def logaritmacion(self):

        assert(self.op == "log")
        return str(log(self.numero1, self.numero2))
