import os
import sys
import socketserver
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)


from data.conf.configure import Host,Port
from core.heart import MyTCPHandler

'''
# 服务端入口程序
'''
if __name__ == '__main__':
    try:
        server = socketserver.ThreadingTCPServer((Host, Port), MyTCPHandler)
        print("Server is Running".center(50, "-"))
        print("Server地址：%s，端口号：%s".center(32, " ") % (Host, Port))
        server.serve_forever()
    except:
        print("当前server所需端口已被占用,请检查！")
