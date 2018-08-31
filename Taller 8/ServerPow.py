import socket
import math
import sys
import _thread
                                                  
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket1.bind(('', 8005))
socket1.listen(10)
print("Taller 8 socket con hilos")                           
print("server corriendo")
		
def program(sc, addr):
	mensaje = sc.recv(1024).decode('ascii')
	numero1, numero2 = mensaje.split(" ")
	envio = str(pow(int(numero1), int(numero2)))
	print("los numeros recibidos son: ", numero1,"y", numero2, "y el resultado es: ", envio)
	sc.send(envio.encode('ascii'))

def main():
	while 1:
		sc, addr = socket1.accept()
		print("recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1]))
		_thread.start_new_thread(program,(sc,addr))



main()
sc.close()
socket1.close()