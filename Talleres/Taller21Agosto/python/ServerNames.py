
import SocketServer


def direccionamiento(operacion):

    if operacion == '+':
        return ['localhost', '8000']

    if operacion == '-':
        return ['localhost', '9000']

    if operacion == '/':
        return ['localhost', '10000']

    if operacion == '*':
        return ['localhost', '11000']

    if operacion == 'log':
        return ['localhost', '12000']

    if operacion == 'rad':
        return ['localhost', '13000']

    if operacion == 'pow':
        return ['localhost', '14000']

class miHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        self.paquete= self.request.recv(1024)


        print('se recibe: ', self.paquete)


        res = direccionamiento(self.paquete)
        print(res)
        self.request.send(res[0] + " " + res[1])


def main():

    print("Socket con direccionamiento")
    host = "localhost"
    puerto = 7006

    server1 = SocketServer.TCPServer((host, puerto), miHandler)
    print("servidor corriendo")
    server1.serve_forever()

main()
