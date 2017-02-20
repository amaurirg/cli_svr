# coding: utf-8

import sys, platform
from socket import *


serverhost = '10.0.0.13'
serverport = 50006

# message = ["Olá Mundo!"]
message = """
Nome do computador: {0}
Sistema: {1}
Versão: {2}
Plataforma: {3}
Máquina: {4}
Arquitetura: {5}
Processador: {6}
================================================================================""" \
.format(
platform.node(),
platform.system(),
platform.release(),
platform.platform(),
platform.machine(),
platform.architecture(),
platform.processor())

# if len(sys.argv)>1:
# 	serverhost = sys.argv[1]
# 	if len(sys.argv)>2:
# 		message = sys.argv[2:]

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverhost, serverport))

msg = ''

for line in message:
	sockobj.send(line)
	data = sockobj.recv(1024)
	msg += data
	#print ("Client Recebeu: ", repr(data))
print msg
sockobj.close()