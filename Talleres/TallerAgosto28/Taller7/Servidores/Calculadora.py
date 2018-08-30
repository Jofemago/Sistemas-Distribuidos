from math import *


class Calculadora:

    def __init__(self, num1, num2, op):

        self.numero1 = int(num1)
        self.numero2 = int(num2)
        self.op = op


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
        return str(self.numero1 ** float(1 / self.numero2))

    def logaritmacion(self):

        assert(self.op == "log")
        return str(log(self.numero1, self.numero2))
