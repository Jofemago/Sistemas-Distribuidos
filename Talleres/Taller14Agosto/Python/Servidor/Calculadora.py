import math


class Calculadora:

    def __init__(self, num1, num2, op):

        self.numero1 = int(num1)
        self.numero2 = int(num2)
        self.operador = op


    def suma(self):

        #assert(self.op = "+")
        return str(self.numero1 + self.numero2)

    def resta(self):

        #assert(self.op = "+")
        return str(self.numero1 - self.numero2)


    def multiplicacion(self):

        #assert(self.op = "+")
        return str(self.numero1 * self.numero2)

    def division(self):

        #assert(self.op = "+")
        return str(self.numero1 / self.numero2)

    def potenciacion(self):

        return str(self.numero1 ** self.numero2)

    def radiacion(self):

        #assert(self.op = "+")
        return str(self.numero1 ** (1 / self.numero2))

    def logaritmacion(self):

        #assert(self.op = "+")
        return str(log(self.numero1, self.numero2))
