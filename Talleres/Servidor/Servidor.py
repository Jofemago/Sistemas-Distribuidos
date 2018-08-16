
import SocketServer


class miHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        self.paquete= self.request.recv(1024)
        #se reciben datos de 1024 bits

        print(self.paquete)

        #print("los numeros son :" , self.numero1 , " y " , self.numero2 , " y la suma es :" , self.suman)
        mensaje = "respuesta"
        self.request.send(mensaje)


def main():

    print("Taller sockets")
    host = "localhost"
    puerto = 9996

    server1 = SocketServer.TCPServer((host, puerto), miHandler)
    print("servidor corriendo")
    server1.serve_forever()

main()
