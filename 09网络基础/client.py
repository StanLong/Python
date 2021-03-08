import socket
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.connect(ip_port)
while True:
    info = input('>>')
    sk.send(bytes(info, encoding='utf-8'))
    msg = sk.recv(1024)
    print(msg.decode('utf-8'))

sk.close()