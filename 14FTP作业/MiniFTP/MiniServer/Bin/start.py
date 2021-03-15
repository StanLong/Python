# -*- coding:utf-8 -*-



import socket,socketserver
import sys,os,json
#目录为MiniFTP\MiniServer
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)


from Data.Conf.configure import Host,Port
from Core.heart import MyTCPHandler


if __name__=="__main__":
    try:
        server=socketserver.ThreadingTCPServer((Host,Port),MyTCPHandler)
        print("Server is Running".center(50,"-"))
        print("Server地址：%s，端口号：%s".center(32," ")%(Host,Port))
        server.serve_forever()
    except:
        print("当前server所需端口已被占用,请检查！")
