import socket

print("taller 7")
host = "localhost"
puerto = 9999
socket1 = socket.socket()
socket1.connect((host,puerto))
numero1 = input("Ingrese un numero: ")
numero2 = input("Ingrese un numero: ")
operation = input("Ingrese una opertation (^, +, -, *, /): ")

envio = numero1 + " " + numero2 + " " + operation
socket1.send(envio.encode('ascii'))

resultado = socket1.recv(1024)

print("Respuesta : " + resultado.decode('ascii'))
tiempo = input("presione enter para terminar")
socket1.close()
