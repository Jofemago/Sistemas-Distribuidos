



class Direccionador:

    def getServer(self,op):

        if(op == "+"):
            return '127.0.0.1 10000'

        elif(op == "-"):
            return '127.0.0.1 11000'

        elif(op == "*"):
            return '127.0.0.1 12000'

        elif(op == "/"):
            return '127.0.0.1 13000'

        elif(op == "rad"):
            return '127.0.0.1 14000'

        elif(op == "log"):
            return '127.0.0.1 15000'

        elif(op == "pow"):
            return '127.0.0.1 16000'
