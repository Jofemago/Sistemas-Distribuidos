
import SocketServer


def direccionamiento(operacion):

    if operacion == '+':
        return 'localhost' + " "  + '8004'

    elif operacion == '-':
        return 'localhost' + " "  + '9000'

    elif operacion == '/':
        return 'localhost' + " "  + '10000'

    elif operacion == '*':
        return 'localhost' + " "  + '11000'

    elif operacion == 'log':
        return 'localhost' + " "  + '12001'

    elif operacion == 'rad':
        return 'localhost' + " "  + '13000'

    elif operacion == 'pow':
        return 'localhost' + " "  + '14000'

class miHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        self.paquete= self.request.recv(1024)


        print('se recibe: ', self.paquete)


        res = direccionamiento(self.paquete)
        print(res)
        self.request.send(res)


def main():

    print("Socket con direccionamiento")
    host = "localhost"
    puerto = 7003

    server1 = SocketServer.TCPServer((host, puerto), miHandler)
    print("servidor corriendo")
    server1.serve_forever()

main()
