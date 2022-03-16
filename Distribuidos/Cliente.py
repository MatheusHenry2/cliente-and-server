import socket

HOST = '192.168.56.1'
PORT = 50000
respostas = ['V', 'F', 'V', 'F', 'V']

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode('Bom dia Boson'))
data = s.recv(1024)

print ('Mensagem ecoada:', data.decode())




