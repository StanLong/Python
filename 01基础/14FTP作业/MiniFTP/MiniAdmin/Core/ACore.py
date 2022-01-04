# -*- coding:utf-8 -*-

import hashlib
import os,json,re,socket
Base_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"\\MiniServer"
#此处定位到MiniServer目录下

class Manager():

    def link_server(self):
        c=0
        while True:
            print("欢迎使用MiniFTP管理系统".center(50,"-"))
            self.server_ip=input("服务器地址:")
            if self.server_ip =="":
                print("服务器地址不能为空，请重新填写")
                continue
            elif re.match("^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$",self.server_ip):
                self.server_port=input("服务端口：")
                if self.server_port =="":
                    print("服务器端口不能为空，请重新填写")
                    continue
                elif self.server_port.isdigit():
                    while True:
                        auth_res=self.__AuthenticationName()#首先关联认证函数
                        if auth_res.get("standcode")==100:
                            self.sock.close()
                            c+=1
                            if c>=3:#三次以后程序关闭
                                print("错误次数达到上限。")
                                exit()
                else:
                    print("服务器端口必须为数字，请重新填写")
                    continue
            else:
                print("服务器格式必须为IPv4地址，请重新填写。")
                continue

    def __recvmsg(self):
        '''
        #此为客户端得到服务器回复的信息后执行相应解析的函数，对应的是服务端__sendmsg函数
        :return: 返回的是接收后经过处理的数据
        '''

        data = self.sock.recv(1024)
        data = json.loads(data.decode())
        return data


    def  __AuthenticationName(self):
         # try:
        self.sock=socket.socket()
        self.sock.connect((self.server_ip,int(self.server_port)))
        print("寻找服务器成功!".center(50,"."))
        self.admin=input("管理员账号：")
        password=input("密码：")
        crypto_password=hashlib.md5(password.encode("utf-8"))
        ##########此处是用来获取本机当前正在使用的地址####################
        ipaddr=[a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]
        ##################################################################
        auth_msg={
            "Type":"auth",
            "ipaddr":ipaddr,
            "username":self.admin,
            "password":crypto_password.hexdigest(),
            "auth_tag":"mgr"
        }
        self.sock.send(json.dumps(auth_msg).encode())
        rec_msg=self.__recvmsg()

        if rec_msg.get("standcode")==101:
            print(rec_msg.get("standmsg"))
            print(("%s，欢迎进入MiniFTP管理界面"%self.admin).center(50,"-"))
            self.__Adminmanager()
        elif rec_msg.get("standcode")==102 or rec_msg.get("standcode")==100:
            return rec_msg
        else:
            return  rec_msg
        # except:
        #     print("连接失败！".center(50,"."))




    def  __Adminmanager(self):
        while True:
            msg=self.__recvmsg()
            if msg.get("data") is not None:
                msg_data= msg.get("data")

                while True:
                    print(msg_data)
                    select=input("请选择：")
                    if select !="" :
                        self.sock.send(json.dumps(select).encode())
                        ret_slt=self.__recvmsg()
                        #添加用户
                        if ret_slt.get("standcode") == 400:
                            self.__admin_add()
                            break
                        #删除用户
                        elif ret_slt.get("standcode")==405:
                            self.__admin_delete()
                            break

                        #退出系统
                        elif ret_slt.get("standcode")==406:
                            self.__admin_exit()
                            break
                        #查看当前存在的用户
                        elif ret_slt.get("standcode")==407:
                            self.__skmsg(ret_slt)
                            break
                        #修改配额
                        elif ret_slt.get("standcode")==410:
                            self.__cgmsg()
                            break
                        elif ret_slt.get("standcode")==102:
                            continue
                    else:
                        continue


    def __admin_add(self):
        reg_user=input("注册的用户名：").strip()
        reg_passwd=input("注册的密码").strip()
        reg_passwd=(hashlib.md5(reg_passwd.encode("utf-8"))).hexdigest()
        ret_msg={
            "username":reg_user,
            "password":reg_passwd,
            "quotavalue":"30"
        }
        self.sock.send(json.dumps(ret_msg).encode())
        tag=self.__recvmsg()
        print(str(tag.get("standcode"))+":"+tag.get("standmsg"))



    def __admin_delete(self):
        del_name=input("要删除的用户名：")
        self.sock.send(json.dumps(del_name).encode())
        tag=self.__recvmsg()
        print(str(tag.get("standcode"))+":"+tag.get("standmsg"))



    def __skmsg(self,ret_slt):
        seek_list=ret_slt.get("data")
        if seek_list is not None:
            if len(seek_list)!=0:
                for item in seek_list:
                    try:
                        skuser,skvalue=item.strip("\n").strip('"').split(":")
                        print("用户名：%s，当前服务器空间限额：%sM"%(skuser,skvalue))
                    except:
                        break
        else:
            print("当前尚未存在用户")
    def __cgmsg(self):
        while True:
            qtname=input("用户名:")
            qtvalue=input("修改后的配额值：")
            if qtvalue.isdigit():
                qtmsg={
                    "name":qtname,
                    "value":qtvalue
                }
                self.sock.send(json.dumps(qtmsg).encode())
                qt_res=self.__recvmsg()
                if qt_res.get("standcode")==411:
                    print("修改成功！")
                    break
                else:
                    print("修改失败！")
                    break
            else:
                print("输入的配额值必须是数字！")
    def __admin_exit(self):
        self.sock.shutdown(2)
        self.sock.close()
        print("欢迎使用，再见".center(50,"-"))
        exit()

