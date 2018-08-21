import socket

print("taller 1")


host = "localhost"
puerto = 7006
socket1 = socket.socket()

socket1.connect((host, puerto))
numero1 = raw_input("ingrese un numero: ")
#socket1.send(numero1)

numero2 = raw_input("ingrese un numero: ")
#socket1.send(numero2)

operacion = numero2 = raw_input("ingrese operacion: ")


envio = numero1 +" "+numero2+" "+operacion


socket1.send(operacion)

resultado = socket1.recv(1024)

print("Respuesta: " + resultado )
tiempo = raw_input("presione enter para terminar")
socket1.close()
