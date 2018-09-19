from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import xmlrpclib
import threading

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
	pass

def calc(numbers):
	a, op, b = numbers.split(" ")
	if op == '+':
		port = "8000"
	elif op == '-':
		port = "8001"
	elif op == '*':
		port = "8002"
	elif op == '/':
		port = "8003"
	elif op == '**':
		port = "8004"
	elif op == "-/":
		port = "8005"
	else:
		port = "8006"

	class ClientThread(threading.Thread):
		def __init__(self):
			threading.Thread.__init__(self)
			self.s = xmlrpclib.ServerProxy("http://localhost:" + port)

		def run(self):
			return self.s.calc(a, b)

	client = ClientThread()
	return client.run()

# Run the server's main loop
class ServerThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.localServer = SimpleThreadedXMLRPCServer(("localhost",9997))
		self.localServer.register_function(calc)

	def run(self):
		self.localServer.serve_forever()

server = ServerThread()
server.start() # The server is now running
print "Server ready."