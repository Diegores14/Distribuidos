import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:9997')

print "Envie una operacion con el siguiente formato:"
print "Numero_1 Operador Numero_2"
print "Operadores permitidos:"
print "suma -> +"
print "resta -> -"
print "division -> /"
print "multiplicacion -> *"
print "potenciacion -> **"
print "radicacion -> -/"
print "logaritmacion -> log"

numeros = raw_input("> ")
a, op, b = numeros.split(" ")
port = s.getPort(op)
s2 = xmlrpclib.ServerProxy('http://localhost:' + port)
print s2.calc(a, b)