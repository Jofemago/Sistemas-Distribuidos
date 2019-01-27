from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time
from Scanner import Scanner



class ClientThread(threading.Thread):
    def __init__(self):
    	self.sc=Scanner()
    	threading.Thread.__init__(self)
    	self.s = xmlrpclib.ServerProxy('http://localhost:9995')
        self.sop = None #servidor que realiza las operaciones



    def toString(self):
    	x= "La operacion "+str(self.sc.getNro1())+" "+self.sc.getOperation()+" "+str(self.sc.getNro2())+" = "+str(mekeOperation(self.sc,self.s))
    	return x

    def run(self):
		#time.sleep(3)
		print "Llamada cliente1 "
		url = self.s.getServer(self.sc.getOperation())
		serverop = xmlrpclib.ServerProxy(url)
		print(serverop.op(int(self.sc.getNro1()), int(self.sc.getNro2())))
		#print self.toString()
		#print  "La operacion ",self.sc.getNro1()," ",self.sc.getOperation()," ",self.sc.getNro2()," = ",mekeOperation(self.sc,self.s)
		#print "Esto da: ",self.s.div(5,2)  # Returns 5//2 = 2
		#print self.s.add(7,2)




client = ClientThread()
#client2 = ClientThread2()
client.start() # The server is now running
#client2.start()
