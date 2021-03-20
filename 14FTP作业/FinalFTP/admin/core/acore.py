import re
import os
import json
import socket
import hashlib

pattern = re.compile("^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$")

class Manager:

    '''
    # 连接服务器
    '''
    def link_server(self):
        c = 0 # 作为计数器，统计登录次数
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
                        auth_res = self.__AuthenticationName() # 用户认证
                        if auth_res.get('standcode') == 100:
                            self.sock.close()
                            c = c + 1
                            if c>= 3:
                                print("累次错误三次，程序退出")
                                exit()
                else:
                    print("服务端口必须为数字，请重新填写")
            else:
                print("服务器格式必须为IPv4地址，请重新填写。")
                continue

    '''
    # 登录服务器，服务器端认证用户名和密码
    '''
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
            self.__Admin_manager()
        elif rec_msg.get('standcode') == 102 or rec_msg.get('standcode') == 100:
            return rec_msg
        else:
            return rec_msg

    '''
    # 从服务起端接收消息
    '''
    def __recvmsg(self):
        data = self.sock.recv(1024)
        data = json.loads(data.decode('utf-8'))
        return data

    '''
    # 管理员登录成功后，展示操作界面
    '''
    def __Admin_manager(self):
        while True:
            msg = self.__recvmsg()
            if msg.get('data') is not None:
                msg_data = msg.get('data')

                while True:
                    print(msg_data)
                    select = input("请选择:")
                    if select != "":
                        self.sock.send(json.dumps(select).encode('utf-8'))
                        ret_slt = self.__recvmsg()
                        # 添加用户
                        if ret_slt.get("standcode") == 400:
                            self.__admin_add()
                            break
                        # 删除用户
                        elif ret_slt.get("standcode") == 405:
                            self.__admin_delete()
                            break

                        # 退出系统
                        elif ret_slt.get("standcode") == 406:
                            self.__admin_exit()
                            break
                        # 查看当前存在的用户
                        elif ret_slt.get("standcode") == 407:
                            self.__skmsg(ret_slt)
                            break
                        # 修改配额
                        elif ret_slt.get("standcode") == 410:
                            self.__cgmsg()
                            break
                        elif ret_slt.get("standcode") == 102:
                            continue
                    else:
                        continue

    def __admin_add(self):
        reg_user = input("注册的用户名：").strip()
        reg_passwd = input("注册的密码:").strip()
        reg_passwd = (hashlib.md5(reg_passwd.encode("utf-8"))).hexdigest()
        ret_msg = {
            "username": reg_user,
            "password": reg_passwd,
            "quotavalue": "30"
        }
        self.sock.send(json.dumps(ret_msg).encode())
        tag = self.__recvmsg()
        print(str(tag.get("standcode")) + ":" + tag.get("standmsg"))
