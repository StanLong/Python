from gevent import monkey
monkey.patch_all()  # 有了该猴子补丁后，当任务发生IO事件时，协程任务就会切换
import gevent
import socket


def DealMautual(conn):
    '''
    协程任务
    与client的会话
    :return:
    '''
    conn.send(b'hello')
    msg = conn.recv(1024).decode('utf-8')
    print(msg)
    conn.close()


if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8080))
    sk.listen()
    while 1:
        conn, addr = sk.accept()    # 阻塞等待客户端连接上来
        gevent.spawn(DealMautual, conn) # 当有一个客户端连上来后则异步创建一个协程任务，异步运行协程任务，当协程任务遇到IO后，则会发生协程的任务切换
