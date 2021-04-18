import socket
from threading import Thread

def func(conn):
    conn.send(b'hello')
    ret = conn.recv(1024)
    print(ret.decode('utf-8'))
    conn.close()

sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.bind(ip_port)
sk.listen()

while True:
    conn, addr = sk.accept()
    Thread(target=func, args=(conn, )).start()

sk.close()