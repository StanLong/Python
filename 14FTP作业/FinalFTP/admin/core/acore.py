import re
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
        self.admin=input("管理员账号:")
        password = input("密码:")
        crypto_password = hashlib.md5(password.encode('utf-8'))
        print(crypto_password.hexdigest())