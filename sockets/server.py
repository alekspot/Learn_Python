import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

server_socket.bind(('localhost', 9090))
server_socket.listen(1)

client_socket, addr = server_socket.accept()
client_socket.sendall(b'Server says hello =)')

while True: 
    data = client_socket.recv(1024)
    
    if not data:
        break
    print(data.decode('utf-8'))

    msg = input()

    client_socket.sendall(bytes(msg.encode('utf-8')))

client_socket.close()

input()

