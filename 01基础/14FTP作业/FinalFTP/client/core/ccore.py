import os
import re
import sys
import time
import json
import socket
import hashlib

class Connect:
    def startlink(self):
        while True:
            c=0
            print("欢迎使用MiniFTP文件传输系统".center(50,"-"))
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
                    if int(self.server_port)<0 or  int(self.server_port)>65535:
                        print("服务器端口必须在0-65535之间")
                        continue
                    else:
                        while True:
                            auth_res=self.__conn()#首先关联认证函数
                            if auth_res.get("standcode")==100:
                                self.server.close()
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

        data = self.server.recv(1024)
        data = json.loads(data.decode())
        return data
    def __conn(self):
        try:
            self.server=socket.socket()
            self.server.connect((self.server_ip,int(self.server_port)))
            print("寻找服务器成功!".center(50,"."))
            self.username=input("用户名：")
            password=input("密码：")
            crypto_password=hashlib.md5(password.encode("utf-8"))
            ##########此处是用来获取本机当前正在使用的地址####################
            ipaddr=[a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]
            ##################################################################
            auth_msg={
                "type":"auth",
                "ipaddr":ipaddr,
                "username":self.username,
                "password":crypto_password.hexdigest(),
                "auth_tag":"ordinary"
            }
            self.server.send(json.dumps(auth_msg).encode())
            rec_msg=self.__recvmsg()
            print(rec_msg.get("standmsg"))
            if rec_msg.get("standcode")==101:
                self.__changelink()
            elif rec_msg.get("standcode")==102 or rec_msg.get("standcode")==100:
                return rec_msg
            else:
                return  rec_msg
        except:
            print("已与服务器断开连接！".center(50,"."))
            exit()

    def __changelink(self):
         while True:
            sendmsg=input("["+self.username+"]>>")
            self.sendmsg_list=sendmsg.split()
            if len(self.sendmsg_list)==0:
                continue
            elif self.sendmsg_list[0]=="put":
                self.__put()
            elif self.sendmsg_list[0]=="get":
                self.__get()
            elif self.sendmsg_list[0]=="cd":
                self.__cd()
            elif self.sendmsg_list[0]=="ls":
                self.__ls()
            elif self.sendmsg_list[0]=="pwd":
                self.__pwd()
            elif self.sendmsg_list[0]=="mkdir":
                self.__mkdir()
                continue
            elif self.sendmsg_list[0]=="rm":
                self.__rm()
            elif self.sendmsg_list[0]=="bye":
                self.__bye()
            else:
                self.__help()


    def __help(self):
        msg={
            "Type":"help"
        }
        self.server.send(json.dumps(msg).encode())
        hsg=self.__recvmsg()
        if hsg.get("data") is not None:
            for item in hsg.get("data"):
                print("%s:%s".center(70,".")%(item,hsg.get("data")[item]))
        else:
            print("error cmd")


    def __ls(self):
        '''
        #服务器传输过来的列表只会存在文件夹和文件两个列表，即使本目录下没有文件夹或者是没有文件，也会传过来相应的空列表。
        :return:
        '''
        msg={
            "Type":"ls"
        }
        self.server.send(json.dumps(msg).encode())
        ls_list=self.__recvmsg()
        c=0#用来判断是第几次遍历
        kong_tag=False#空标志位
        #传输过来的数据格式为[[文件夹名],[文件名]]，因此需要第一遍遍历文件夹，第二遍遍历文件
        if ls_list.get("data") is not None:
            for item in ls_list.get("data"):
                if len(item)!=0:
                    #如果是第一次遍历，那么就代表了遍历结果为文件夹名，因此在得到的结果后加“/”来区分文件和文件名
                    if c==0:
                        for item2 in item:
                            if len(item2)!=0:
                                print(item2+"/")
                    #第二次遍历得到的则为文件
                    elif c==1:
                        for item2 in item:
                            if len(item2)!=0:
                                print(item2)
                    kong_tag=True
                c+=1
            #如果为空的tag是False，则代表了上面未进行遍历处理，也就代表了传过来的目录为空。
            if kong_tag==False:
                print("当前目录为空")
        else:
            print("当前目录为空")

    def __get(self):
        '''
        #此为执行下载动作的函数
        :return:
        '''
        try:
            #若传入的目标文件夹存在路径的话， 此为目标文件夹的路径
            targetfile=""
            recv_len=0
            filename=""
            #此处的3表示了输入的命令格式为get 源文件  目标文件路径，字符串经过截取以后，获得的是长度为3的sendmsg_list
            if len(self.sendmsg_list)==3:
                #此时最后一位为目标文件夹路径
                targetname=self.sendmsg_list[-1]
                if targetname.endswith("\\"):
                    print("需要输入指定存储的文件名。")
                    return False
                else:
                    #此时第二位为源文件名称
                    filename=self.sendmsg_list[-2]
                    if "\\" in targetname:
                        target_list=targetname.split("\\")
                        for i in range (0,len(target_list)):
                            if len(target_list)==i+1:
                                targetname=target_list[i]
                                break
                            #确定要存入的目标路径
                            targetfile=targetfile+target_list[i]
            elif len(self.sendmsg_list)==2:
                #此时最后以为为源文件名称
                filename=self.sendmsg_list[-1]
                if filename.endswith("\\"):
                    print("需要输入指定存储的文件名。")
                    return False
                else:
                    targetfile=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                    targetname=filename
            get_msg={
                "Type":"get",
                "filename":filename
            }
            self.server.send(json.dumps(get_msg).encode())
            #收取服务器返回的关于文件介绍的数据
            explain_list=self.__recvmsg()
            if explain_list.get("data") is not None:
                #向服务器发送信号，告知可以开启发送流程。
                size=explain_list.get("data").get("size")
                if targetfile !="":
                    try:
                        f_write=open(targetfile+"\\"+targetname,"wb")
                    except:
                        print("请确认当前指定路径是否正确,或者是是否忘记添加指定存储的文件名。")
                        return False
                self.server.send(b"121")
                while True:
                    if recv_len<int(size):
                        filedata_source=self.server.recv(1024*100)
                        f_write.write(filedata_source)
                        ################此为下载进度条的显示#########################################
                        recv_len+=len(filedata_source)
                        percent=int(recv_len)/int(size)
                        num_arrow=round(100*percent,0)
                        num_line=round(100-num_arrow,0)
                        res= '[' + '>' *int(num_arrow)  + '-' *int(num_line)  + ']'+ '%.2f' % (percent*100) + '%' + '\r'
                        sys.stdout.write(res)
                        sys.stdout.flush()
                        time.sleep(0.1)
                        ############################################################################
                    else:
                        #判断服务器发送过来的文件信息中的size跟实际收到的size是否相等， 相等则代表完成接收。
                        if size==recv_len:
                            f_write.close()
                            self.server.send(b"121")
                            #ASCII的121代表y，即为完成
                            print("\n")
                            print("文件已经下载至%s"%targetfile)
                            break
                        else:
                            #ASCII的110代表了n，即为失败
                            self.server.send(b"110")
                            print("\n")
                            print("下载失败")
                            break
            else:
                print("Error:%s,error code:%s"%(explain_list.get("standmsg"),explain_list.get("standcode")))
                print("下载失败")
        except:
            print("服务器未能回传数据。")
    def __put(self):
        '''

        :return:
        '''
        if len(self.sendmsg_list)!=1:
            if os.path.isfile(self.sendmsg_list[1]):
                base_filename=self.sendmsg_list[-1]
                ####读取文件，进行文件md5值的计算
                with open(base_filename,"rb") as f_put_read:
                    m = hashlib.md5()
                    for line in f_put_read:
                        if line is not None:
                            m.update(line)
                hash_send=m.hexdigest()
                data_msg={
                    "Type":"put",
                    "filename":base_filename,
                    "size":os.path.getsize(self.sendmsg_list[1]),
                    #最终的md5值
                    "md5":hash_send
                }
                send_len=0
                size=os.path.getsize(self.sendmsg_list[1])
                self.server.send(json.dumps(data_msg).encode())
                ret_tag=self.__recvmsg()
                if ret_tag.get("data") is not None:
                    if ret_tag.get("data") =="continue":#continue 表示继续传输
                        with open(base_filename,"rb") as f_read:
                            while True:
                                buffer=f_read.read(1024*100)
                                if not buffer:
                                    break
                                self.server.send(buffer)
                                #############此处为上传进度条显示###########################################
                                recv_len=len(buffer)
                                send_len+=recv_len
                                percent=int(send_len)/int(size)
                                num_arrow=round(100*percent,0)
                                num_line=round(100-num_arrow,0)
                                res= '[' + '>' *int(num_arrow)  + '-' *int(num_line)  + ']'+ '%.2f' % (percent*100) + '%' + '\r'
                                sys.stdout.write(res)
                                sys.stdout.flush()
                                time.sleep(0.1)
                                #######################################################################
                        print("\n")
                        finall_tag=self.__recvmsg()
                        print(finall_tag.get("standmsg"))
                    else:#此处的else目前主要针对的是传输已有文件
                        exmsg=ret_tag.get("data")
                        exsize=exmsg.get("size")
                        exmd5=exmsg.get("md5")
                        localmd5=hashlib.md5()
                        localsize=0
                        #################################################################################################
                        ###此处是为了计算将要上传的文件的size在与服务器端要求的一样大的情况下，md5值是否与服务器端的文件一致。
                        with open(base_filename,"rb") as f_exist:
                            while True:
                                ExistBuffer=f_exist.read(1024*10)
                                if localsize==exsize:
                                    break
                                ######此处是针对于被篡改以后的文件本身就小于已经上传的size，如果让其继续循环读取比较md5值，
                                ###则会使客户端陷入死循环，因此直接在开始读取文件比较之前，直接掐死。###########################
                                if ExistBuffer==b"":
                                    confirmmsg={
                                        "size":"difference",
                                        "md5":"difference",
                                        "tran":"giveup"
                                    }
                                    self.server.send(json.dumps(confirmmsg).encode())
                                    giveupmsg=self.__recvmsg()
                                    print(giveupmsg.get("standmsg"))
                                    return False#虽有返回值，但不用去接收。
                                localmd5.update(ExistBuffer)
                                localsize+=len(ExistBuffer)
                        #如果是一致的情况，那么服务器端的文件即为当前将要上传的文件的一部分，可以进行断点续传。
                        if localsize==exsize and localmd5.hexdigest()==exmd5:
                            #向服务器端发送size和md5值一致的信息,向服务器端请求数据的传输。
                            confirmmsg={
                                "size":"equally",
                                "md5":"equally",
                                "tran":"request"
                            }
                            self.server.send(json.dumps(confirmmsg).encode())
                            confirmagain=self.__recvmsg()
                            relsize=os.path.getsize(self.sendmsg_list[1])
                            #服务器端回复继续的情况下，开始文件的传输
                            if confirmagain.get("data")=="continue":
                                Transize=0
                                allsize=os.path.getsize(self.sendmsg_list[1])
                                rbuffer=1024*10
                                with open(base_filename,"rb") as f_exist:
                                    #此处需要判断当前要传输的数据是否在服务器端已经存在，若已经存在，则无需传输，若尚未存在，才
                                    #需要进行传输。
                                    while True:
                                        if Transize==exsize:
                                            rbuffer=1024*1000
                                        if Transize>exsize and Transize<=relsize:
                                            self.server.send(TranBuffer)
                                            #############此处为上传进度条显示###########################################
                                            percent=int(Transize)/int(size)
                                            num_arrow=round(100*percent,0)
                                            num_line=round(100-num_arrow,0)
                                            res= '[' + '>' *int(num_arrow)  + '-' *int(num_line)  + ']'+ '%.2f' % (percent*100) + '%' + '\r'
                                            sys.stdout.write(res)
                                            sys.stdout.flush()
                                            time.sleep(0.1)
                                            #######################################################################
                                        TranBuffer=f_exist.read(rbuffer)
                                        #当无法读取到文件内容的时候，结束读取。
                                        if len(TranBuffer)==0:
                                            break
                                        Transize+=len(TranBuffer)
                                    print("\n")
                                    finall_tag=self.__recvmsg()
                                    print(finall_tag.get("standmsg"))

                        else:#此处是客户端判断size和md5值不一致，向服务器端主动发送信息放弃传输。
                            confirmmsg={
                                "size":"difference",
                                "md5":"difference",
                                "tran":"giveup"
                            }
                            self.server.send(json.dumps(confirmmsg).encode())
                            giveupmsg=self.__recvmsg()
                            print(giveupmsg.get("standmsg"))
                else:
                     print(ret_tag.get("standmsg"))
            else:
                print("当前文件不存在，无法完成上传动作。")
    def __cd(self):
        '''
        #此为执行目录切换的函数
        :return:
        '''
        if len(self.sendmsg_list)!=1:
            msg={
                "Type":"cd",
                "dest":self.sendmsg_list[-1]
            }
            self.server.send(json.dumps(msg).encode())
            cd_res=self.__recvmsg()
            print(cd_res.get("standmsg"))


    def __pwd(self):
        '''
        #展示当前文件路径
        :return:
        '''
        msg={
            "Type":"pwd"
        }
        self.server.send(json.dumps(msg).encode())
        pwd_res=self.__recvmsg()
        if pwd_res.get("data") is not None:
            print("当前路径：%s"%pwd_res.get("data"))


    def __mkdir(self):
        '''
        #此为执行创建目录的函数
        :return:
        '''
        if len(self.sendmsg_list)!=1:
            msg={
                "Type":"mkdir",
                "mkname":self.sendmsg_list[-1]
            }
        self.server.send(json.dumps(msg).encode())
        mkres=self.__recvmsg()
        if mkres.get("standmsg") is not None:
            print(mkres.get("standmsg"))

    def __rm(self):
        '''
        此为移除目录的函数
        :return:
        '''
        if len(self.sendmsg_list)!=1:
            msg={
                "Type":"rm",
                "rmname":self.sendmsg_list[-1]
            }
        self.server.send(json.dumps(msg).encode())
        rmres=self.__recvmsg()
        if rmres.get("standmsg") is not None:
            print(rmres.get("standmsg"))

    def __bye(self):
        '''
        此为告诉服务器离开系统的指令
        :return:
        '''
        msg={
            "Type":"bye"
        }
        self.server.send(json.dumps(msg).encode())
        q=self.__recvmsg()
        if q.get("data")=="OK":
            self.server.shutdown(2)
            self.server.close()
            print("欢迎使用，再见".center(50,"-"))
            exit()