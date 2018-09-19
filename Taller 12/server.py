from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import xmlrpclib
import threading

server_list = {
	"+": "8000",
	"-": "8001",
	"/": "8002",
	"*": "8003",
	"**": "8004",
	"log": "8005",
	"-/": "8006"
}

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
	pass

def getPort(op):
	return server_list[op]

# Run the server's main loop
class ServerThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.localServer = SimpleThreadedXMLRPCServer(("localhost",9997))
		self.localServer.register_function(getPort)

	def run(self):
		self.localServer.serve_forever()

server = ServerThread()
server.start() # The server is now running
print "Server ready."