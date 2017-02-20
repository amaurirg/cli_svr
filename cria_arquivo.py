import platform, os


os.system("WMIC /output:C:\\temp\pro.txt product get name, version, installdate")
with open("C:\\temp\\pro.txt") as f:
        file = f.read()

message = """
Nome do computador: {0}
Sistema: {1}
Versão: {2}
Plataforma: {3}
Máquina: {4}
Arquitetura: {5}
Processador: {6}\n
Programas Instalados: \n{7}
""".format(
platform.node(),
platform.system(),
platform.release(),
platform.platform(),
platform.machine(),
platform.architecture(),
platform.processor(),
file)

if not os.path.exists('C:\\teste'):
	os.makedirs("c:\\teste")
with open("c:\\teste\\relatorio.txt", "w") as w:
	w.write(message)

