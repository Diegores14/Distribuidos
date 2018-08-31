import socket
import math
import sys
import _thread

server_list = [8000,8001,8002,8003,8004,8005,8006]
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket1.bind(('', 9999))
socket1.listen(10)
print("Taller 8 socket con hilos")                           
print("server corriendo")
		
def program(sc, addr):
	operation = sc.recv(1024).decode('ascii')
	envio = "Error"	
	if "+"==operation:
		envio = "localhost" + " " + str(server_list[0])
	elif "-"==operation:
		envio = "localhost" + " " + str(server_list[1])
	elif "*"==operation:
		envio = "localhost" + " " + str(server_list[2])
	elif "/"==operation:
		envio = "localhost" + " " + str(server_list[3])
	elif "sqrt"==operation:
		envio = "localhost" + " " + str(server_list[4])
	elif "^"==operation:
		envio = "localhost" + " " + str(server_list[5])
	sc.send(envio.encode('ascii'))

def main():
	while 1:
		sc, addr = socket1.accept()
		print("recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1]))
		_thread.start_new_thread(program,(sc,addr))



main()
sc.close()
socket1.close()