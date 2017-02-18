# coding: utf-8

from socket import *


myhost =''
myport = 50006

msg = ''

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myhost, myport))
sockobj.listen(5)


while True:
	connection, address = sockobj.accept()
	print ("Servidor conectado por: ", address)
	while True:
		data = connection.recv(1024)
		#print (data)
		msg += data
		if not data:
			break
		connection.send(data)
	print msg
	connection.close()