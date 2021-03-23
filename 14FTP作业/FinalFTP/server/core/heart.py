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
        '''
        此为管理员相关功能的函数，不涉及FTP自身的功能
        :return:
        '''
        while True:
            msg='''
                    1.注册用户
                    2.删除用户
                    3.查看用户
                    4.修改配额
                    5.退出
                    '''
            self.__sendmsg(102,data=msg)
            ret_msg=self.__recvmsg()
            if ret_msg=="1" or ret_msg=="注册用户":

                wr_tag=False
                self.__sendmsg(400)#此处是为了让客户端知道下一步应该做什么，发送400 是为了让客户端进入到注册用户的界面
                sign_msg=self.__recvmsg()
                username=sign_msg.get("username")
                password=sign_msg.get("password")
                quotavalue=sign_msg.get("quotavalue")
                if os.path.exists(base_dir+"\\data\\users\\UserAuth.txt"):
                    with open(base_dir+"\\data\\users\\UserAuth.txt","r") as f_read:
                        for line in f_read:
                            usr,pad=line.strip('"').split(":")
                            if usr==username:
                                wr_tag=True
                if wr_tag==False:
                    joindir=""
                    #此处是为了预防初次操作不存在当前目录#####################
                    dirs=(base_dir+"\\data\\users\\UserAuth.txt").split("\\")
                    for i  in  range(0,len(dirs)):
                        if len(dirs)==i+1:
                            break
                        joindir=joindir+dirs[i]+"\\"
                        if os.path.exists(joindir):
                            continue
                        else:
                            os.mkdir(joindir)
                    #############################################################
                    #将用户名密码写入userauth.txt文件
                    with open(base_dir+"\\data\\users\\UserAuth.txt","a") as f:
                        f.write(json.dumps(str(username)+":"+str(password)))
                        f.write("\n")
                    #将配额值写入配额文件
                    with open(base_dir+"\\data\\users\\Quota.txt","a") as f_quota:
                        f_quota.write(json.dumps(str(username)+":"+str(quotavalue)))
                        f_quota.write("\n")
                    logging.info("管理员注册账号成功，账号名：%s，用户默认空间限额：%s"%(username,quotavalue))
                    self.__sendmsg(403)#成功
                else:#此处失败主要是因为存在相同的用户名
                    logging.error("管理员注册账号失败，账号名：%s"%username)
                    self.__sendmsg(404)#失败
                continue
            elif ret_msg=="2" or ret_msg=="删除用户":
                user_list=[]#删除用户名使用的列表
                quota_list=[]#删除配额使用的列表
                del_tag=False#表示是否需要删除用户的tag
                quota_tag=False#表示是否需要删除配额值的tag
                self.__sendmsg(405)
                del_username=self.__recvmsg()#接收需要删除的用户名
                if os.path.exists(base_dir+"\\data\\users\\UserAuth.txt"):
                    with open(base_dir+"\\data\\users\\UserAuth.txt","r") as f_delete:
                        #判断是否需要进行删除动作，若需要删除，则del_tag为True
                        for line in f_delete:
                            delusr,delpad=line.strip('"').split(":")
                            if delusr==del_username:
                                del_tag=True
                                continue
                            else:
                                user_list.append(line)
                    #判断配额值是否需要删除，若需要删除，则quota_tag为True
                    if os.path.exists(base_dir+"\\data\\users\\Quota.txt"):
                        with open(base_dir+"\\data\\users\\Quota.txt","r") as f_delquota:
                            for line2 in f_delquota:
                                delusr,delquo=line2.strip('"').split(":")
                                if delusr==del_username:
                                    quota_tag=True
                                    continue
                                else:
                                    quota_list.append(line2)
                    if del_tag and quota_tag:
                        with open(base_dir+"\\data\\users\\UserAuth.txt","w") as f_rewr:
                            for item in user_list:
                                f_rewr.write(item)
                            logging.info("完成删除用户%s"%delusr)
                        with open(base_dir+"\\data\\users\\Quota.txt","w") as f_requota:
                            for item in quota_list:
                                f_requota.write(item)
                            logging.info("完成删除用户%s磁盘配额"%delusr)
                        self.__sendmsg(401)
                    elif quota_tag==False:
                        logger.info("删除用户%s磁盘配额失败"%delusr)
                        self.__sendmsg(408)
                    else:
                        logger.error("删除用户%s失败,当前用户未注册"%delusr)
                        self.__sendmsg(402)
                else:
                    logger.info("删除用户%s失败,当前用户文件不存在"%del_username)
                    self.__sendmsg(413)
            elif ret_msg=="3" or ret_msg=="查看用户":
                seek_list=[]
                if os.path.exists(base_dir+"\\data\\users\\Quota.txt"):
                    with open(base_dir+"\\data\\users\\Quota.txt","r") as f_seek:
                        #此处发送给客户端的信息主要是配额文件内的信息
                        #格式为：  用户名：配额值
                        for line in f_seek:
                            seek_list.append(line)
                    self.__sendmsg(407,data=seek_list)

                else:
                    self.__sendmsg(407)
                logging.info("管理员查询了用户信息")
            elif ret_msg=="4" or ret_msg=="修改配额":
                self.__sendmsg(410)
                quota_msg=self.__recvmsg()
                cgqt_list=[]
                qt_value=False
                quota_name=quota_msg.get("name")
                cgqt_value=quota_msg.get("value")
                if os.path.exists(base_dir+"\\data\\users\\Quota.txt"):
                    with open(base_dir+"\\data\\users\\Quota.txt","r") as f_cgvalue:
                        for line in f_cgvalue:
                            qtname,qtvalue=line.strip("\n").strip('"').split(":")
                            if qtname==quota_name:
                                qt_value=True
                                qtline=str(qtname)+":"+str(cgqt_value)
                                cgqt_list.append(qtline)
                                continue
                            else:
                                cgqt_list.append(line.strip("\n").strip('"'))
                    if qt_value:
                        with open(base_dir+"\\data\\users\\Quota.txt","w") as f_cgvalue_write:
                            for i in range(0,len(cgqt_list)):
                                f_cgvalue_write.write('"'+cgqt_list[i]+'"')
                                f_cgvalue_write.write("\n")
                        self.__sendmsg(411)
                        logger.info("管理员修改了用户%s的配额值！"%quota_name)
                    else:
                        self.__sendmsg(412)
                        logger.info("修改配额值失败，当前要修改的用户%s不存在"%quota_name)
                else:
                    self.__sendmsg(412)
                    logger.info("修改配额值失败，当前配额文件不存在")
            elif ret_msg=="5" or ret_msg=="退出":
                self.__sendmsg(406)
                logger.info("管理员已退出")

            else:
                #103没有特殊含义，仅仅是因为其未分配提示词
                self.__sendmsg(103)
                continue
    #结束连接时
    def finish(self):
        logger.info("%s与服务器连接结束。"%self.ipaddr)
        logger.info("=============================================================")

    '''
    # 服务端接受客户端发送过来数据的
    '''
    def __recvmsg(self):
        Rsg_source=self.request.recv(1024)
        Rsg=json.loads(Rsg_source.decode())
        return Rsg

    def finish(self):
        print("finish")