from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time
from Direccionador import *


class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self, puerto):
         threading.Thread.__init__(self)
         self.localServer = SimpleThreadedXMLRPCServer(("localhost",puerto))
         #self.localServer.register_function(div)
         self.localServer.register_instance(Direccionador())

    def run(self):
         self.localServer.serve_forever()





server = ServerThread(9995)
#server = ServerThread(9993)
#server = ServerThread(9994)
server.start() # The server is now running
print "Listo servidor."
