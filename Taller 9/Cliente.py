import socket

print("taller 8")
host = "localhost"
puerto = 9999
socket1 = socket.socket()
socket1.connect((host,puerto))
numero1 = input("Ingrese un numero: ")
numero2 = input("Ingrese un numero: ")
operation = input("Ingrese una opertation (^, +, -, *, /): ")

envio = numero1 + " " + numero2
socket1.send(operation.encode('ascii'))

resultado = socket1.recv(1024).decode('ascii')
IPPUERTO = resultado.split(" ")
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2.connect((IPPUERTO[0], int(IPPUERTO[1])))
socket2.send(envio.encode('ascii'))
resultado = socket2.recv(1024)

print("Respuesta : " + resultado.decode('ascii'))
tiempo = input("presione enter para terminar")
socket1.close()
