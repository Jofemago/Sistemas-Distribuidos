



class Direccionador:

    def getServer(self,op):

        if(op == "+"):
            return 'http://localhost:10000'

        elif(op == "-"):
            return 'http://localhost:11000'

        elif(op == "*"):
            return 'http://localhost:12000'

        elif(op == "/"):
            return 'http://localhost:13000'

        elif(op == "rad"):
            return 'http://localhost:14000'

        elif(op == "log"):
            return 'http://localhost:15000'

        elif(op == "pow"):
            return 'http://localhost:16000'
