#! python3
import socket
import sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

server_socket.bind((host, port))
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    print('连接地址：%s'% str(addr))
    msg = '欢迎\n'
    client_socket.send(msg.encode('utf-8'))
    client_socket.close()