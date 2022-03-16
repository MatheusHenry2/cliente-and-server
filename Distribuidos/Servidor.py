import socket

HOST = '192.168.56.1'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen()

print('Aguardando conexão de um cliente')
conn, ender = s.accept()

print('Conectado em', ender)

while True:
    data = conn.recv(1024) # recebe informação
    print(data)
    if not data:
        print('Fechando a conexao')
        conn.close()
        break;
    conn.sendall(data)


