import socket
from multiprocessing import Process

def talk(conn):
    conn.send(b'connected')
    msg = conn.recv(1024)
    print(msg)

if __name__ == '__main__':
    sk = socket.socket()
    ip_port = ('127.0.0.1', 8080)
    sk.bind(ip_port)
    sk.listen()
    while True:
        conn, addr = sk.accept()
        p = Process(target=talk, args=(conn,))
        p.start()
    conn.close()
    sk.close()