from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from math import *
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time


def suma(a, b):
    return a + b

def mult(a, b):
     return a * b

def div(a, b):
     return a / b

def rest(a, b):
     return a - b

def poten(a, b):
     return a ** b

def rad(a,b):

     return a ** (1/b)

def loga(a,b):

     return log(a,b)


class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self, puerto, foperacion):
         threading.Thread.__init__(self)
         self.localServer = SimpleThreadedXMLRPCServer(("localhost",puerto))
         #self.localServer.register_function(div)
         self.localServer.register_function(foperacion,  "op")

    def run(self):
         self.localServer.serve_forever()





server = ServerThread(10003,suma)
server1 = ServerThread(11001,rest)
server2 = ServerThread(12001,mult)
server3 = ServerThread(13001,div)
server4 = ServerThread(14001,rad)
server5 = ServerThread(15001,loga)
server6 = ServerThread(16001,poten)
#server = ServerThread(9993)
#server = ServerThread(9994)
server.start() # The server is now running
server1.start()
server2.start()
server3.start()
server4.start()
server5.start()
server6.start()
print "Listo servidores."
