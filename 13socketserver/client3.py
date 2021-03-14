# socketserver
# SocketServer模块简化了编写网络服务程序的任务, 是对socket的封装

import socket
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.connect(ip_port)
while True:
    msg = input('>>')
    sk.send(('client3' + msg).encode('utf-8'))
    ret = sk.recv(1024).decode('utf-8')
    print(ret)
sk.close()