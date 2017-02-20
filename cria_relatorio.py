import platform, os


if not os.path.exists('C:\\temprel'):
	os.makedirs("c:\\temprel")

if platform.release() == "XP":
	os.system("WMIC /output:C:\\temprel\pro.txt product get name, version, installdate")
else:
	os.system("Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, InstallDate | Sort-Object -Property DisplayName -Unique | Format-Table -AutoSize > c:\\temprel\pro.txt")


with open("C:\\temprel\\pro.txt") as f:
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

if not os.path.exists('C:\\relpc'):
	os.makedirs("c:\\relpc")
with open("c:\\relpc\\relatorio.txt", "w") as w:
	w.write(message)

