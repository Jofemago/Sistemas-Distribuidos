import SocketServer
from Calculadora import *

class miHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        self.paquete = self.request.recv(1024)


        print('se recibe: ', self.paquete)

        rec = self.paquete.split(' ')
        print(rec)
        Calc = Calculadora(rec[0], rec[1], rec[2])

        self.request.send(Calc.logaritmacion())


def main():

    print("Servidor de logaritmacion")
    host = "localhost"
    puerto = 12001

    server1 = SocketServer.TCPServer((host, puerto), miHandler)
    print("servidor corriendo")
    server1.serve_forever()

main()
