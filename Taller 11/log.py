from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", 8006), requestHandler = RequestHandler)
server.register_introspection_functions()


class MyFuncs:
	def calc(self, x, y):
		return int(x) ** (1.0 / int(y))

server.register_instance(MyFuncs())

server.serve_forever()