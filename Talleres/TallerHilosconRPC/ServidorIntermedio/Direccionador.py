



class Direccionador:

    def getServer(self,op):

        if(op == "+"):
            return 'http://localhost:10003'

        elif(op == "-"):
            return 'http://localhost:11001'

        elif(op == "*"):
            return 'http://localhost:12001'

        elif(op == "/"):
            return 'http://localhost:13001'

        elif(op == "rad"):
            return 'http://localhost:14001'

        elif(op == "log"):
            return 'http://localhost:15001'

        elif(op == "pow"):
            return 'http://localhost:16001'
