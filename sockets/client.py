import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 9090))


client_socket.sendall(b'Client say hi =(')
while True: 
    data = client_socket.recv(1024)
    
    if not data:
        break
    print(data.decode('utf-8'))

    msg = input()

    client_socket.sendall(bytes(msg.encode('utf-8')))

client_socket.close()

input()