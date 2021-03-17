import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def setup(self):
        print("setup")
    def handle(self):
        print("handle")
    def finish(self):
        print("finish")