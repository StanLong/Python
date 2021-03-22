import socket
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.connect(ip_port)
msg = sk.recv(1024)
print(msg)
info = input(">>")
sk.send(info.encode('utf-8'))
sk.close()