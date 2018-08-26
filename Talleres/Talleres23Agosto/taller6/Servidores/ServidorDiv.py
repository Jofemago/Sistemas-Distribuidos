from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Calculadora import *

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

if __name__ == "__main__":

    server = SimpleXMLRPCServer(("localhost", 13000),
                            requestHandler=RequestHandler)


    server.register_introspection_functions()
    server.register_instance(Calculadora())


    # Run the server's main loop
    server.serve_forever()
