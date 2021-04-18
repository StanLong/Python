import socket
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.connect(ip_port)

ret = sk.recv(1024)
print(ret)
msg = input(">>")
sk.send(msg.encode('utf-8'))
sk.close()
