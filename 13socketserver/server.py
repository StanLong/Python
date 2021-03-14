# socketserver
# SocketServer模块简化了编写网络服务程序的任务, 是对socket的封装, 可以同时和多个客户端通信

import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self): # 定义了如何处理每一个连接
        while True:
            # self.client_address
            msg = self.request.recv(1024).decode('utf-8')
            print(msg)
            info = input('>>')
            self.request.send(info.encode('utf-8'))


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)
    server.serve_forever() # 即使一个连接报错了，但不会导致程序停止，而是会持续运行，与其他客户端通信