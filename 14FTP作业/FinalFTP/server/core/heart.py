import os
import sys
import json
import time
import timer
import hashlib
import logging
import socketserver

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core.record import record
from data.conf.configure import HomeDocs, username, password
from data.dict.dict import Stand_msg

'''
# 拼接文件日志，格式为 %Y-%m-%d.txt
'''
timer = time.strftime("%Y-%m-%d")
logger = record(base_dir + "\\data\\log\\" + timer + ".txt")

class MyTCPHandler(socketserver.BaseRequestHandler):
    '''
    # 解析连接请求参数
    '''
    def setup(self):
        auth_msg_source = self.request.recv(1024).strip()
        self.auth_msg = json.loads(auth_msg_source)
        if(self.auth_msg.get('type')) == 'auth':
            self.username = self.auth_msg['username']
            self.md5_password = self.auth_msg['password']
            self.ipaddr = self.auth_msg['ipaddr']
            self.role = self.auth_msg['auth_tag']
            logger.info("用户名: %s尝试从终端 %s 登录服务器"%(self.username, self.ipaddr))

    '''
    # 处理连接
    '''
    def handle(self):
        if self.auth_msg.get('type') == 'auth':
            auth_tag = self.__auth()

    '''
    # 服务端用户加密认证
    '''
    def __auth(self):
        if self.role == 'ordinary': # 普通用户身份登录
            pass
        elif self.role == 'mgr': # 管理员身份登录
            m = hashlib.md5(password.encode('utf-8'))
            passwd_value = m.hexdigest()
            if self.username == username and self.md5_password == passwd_value:
                self.__sendmsg(101, data = 'True')
                logger.info("用户 %s 从终端 %s 登录成功！" % (self.username, self.ipaddr))
                try:
                    self.__mgr()
                except:
                    logger.info("%s的管理员已断开连接。" % self.ipaddr)
            else:
                self.__sendmsg(100)

    '''
    # 发送处理结果给请求端
    '''
    def __sendmsg(self, stand_code, data=None):
        sendmsg = {
            'standcode':stand_code,
            'standmsg':Stand_msg[stand_code],
            'data':data
        }
        self.request.send(json.dumps(sendmsg).encode())

    '''
    # 此为管理员相关功能的函数，不涉及FTP自身的功能
    '''
    def __mgr(self):
        while True:
            msg='''
                    1.注册用户
                    2.删除用户
                    3.查看用户
                    4.修改配额
                    5.退出
                    '''
            self.__sendmsg(102,data=msg)
            ret_msg = self.__recvmsg()
            if ret_msg=="1" or ret_msg=="注册用户":
                wr_tag = False
                self.__sendmsg(400)
                sign_msg = self.__recvmsg()
                username = sign_msg.get("username")
                password = sign_msg.get("password")
                quotavalue = sign_msg.get("quotavalue")
                if os.path.exists(base_dir + "\\data\\users\\UserAuth.txt"):
                    with open(Base_dir + "\\data\\users\\UserAuth.txt", "r") as f_read:
                        for line in f_read:
                            usr, pad = line.strip('"').split(":")
                            if usr == username:
                                wr_tag = True
                                pass

    '''
    # 服务端接受客户端发送过来数据的
    '''
    def __recvmsg(self):
        Rsg_source=self.request.recv(1024)
        Rsg=json.loads(Rsg_source.decode())
        return Rsg

    def finish(self):
        print("finish")