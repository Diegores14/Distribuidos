from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import threading

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
	pass

def calc(numbers):
	a, op, b = numbers.split(" ")
	if op == '+':
		return int(a) + int(b)
	elif op == '-':
		return int(a) - int(b)
	elif op == '*':
		return int(a) * int(b)
	elif op == '/':
		return float(a) / float(b)
	elif (op == '**'):
		return int(a) ** int(b)
	else:
		return float(b) ** (1 / float(a))

# Run the server's main loop
class ServerThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.localServer = SimpleThreadedXMLRPCServer(("localhost",8000))
		self.localServer.register_function(calc)

	def run(self):
		self.localServer.serve_forever()

server = ServerThread()
server.start() # The server is now running
print "Server ready."