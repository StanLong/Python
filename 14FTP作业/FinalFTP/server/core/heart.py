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

    def finish(self):
        print("finish")