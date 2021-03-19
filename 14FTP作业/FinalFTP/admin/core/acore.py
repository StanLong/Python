import re
import os
import json
import socket
import hashlib

pattern = re.compile("^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$")

class Manager:
    def link_server(self):
        while True:
            print("欢迎登录FinalFTP管理系统".center(50, '-'))
            self.server_ip = input("服务器地址:")
            if self.server_ip == "":
                print("服务器地址不能为空，请重新填写")
                continue
            elif pattern.match(self.server_ip):
                self.server_port = input("服务端口:")
                if self.server_port == "":
                    print("服务器端口不能为空，请重新填写")
                    continue
                elif self.server_port.isdigit():
                    while True:
                        auth_res = self.__AuthenticationName()
                        pass

    def __AuthenticationName(self):
        self.sock = socket.socket()
        self.sock.connect((self.server_ip, int(self.server_port)))
        print("寻找服务器成功".center(50,"-"))
        self.username=input("管理员账号:")
        password = input("密码:")
        crypto_password = hashlib.md5(password.encode('utf-8'))
        ##########此处是用来获取本机当前正在使用的地址####################
        # ipaddr = [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]
        ipaddr = [a for a in os.popen('ipconfig').readlines() if 'IPv4 地址' in a][0].split(':')[1].split()[0]
        ##################################################################
        auth_msg = {
            'type':'auth',
            'ipaddr':ipaddr,
            'username':self.username,
            'password':crypto_password.hexdigest(),
            'auth_tag':'mgr'
        }
        self.sock.send(json.dumps(auth_msg).encode('utf-8'))
        rec_msg = self.__recvmsg()
        if rec_msg.get('standcode') == 101:
            print(rec_msg.get('standmsg'))
            print(('%s, 欢迎进入FinalFTP管理界面' %self.username).center(50,'-'))

    def __recvmsg(self):
        data = self.sock.recv(1024)
        data = json.loads(data.decode('utf-8'))
        return data
