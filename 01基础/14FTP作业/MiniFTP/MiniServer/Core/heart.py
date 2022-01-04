# -*- coding:utf-8 -*-



import json,os,sys,time,shutil,timer
import socketserver
import logging
import hashlib

#MiniServer文件夹
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)
from Core.Record import record
from Data.Conf.configure import HomeDocs,admin,password


Stand_msg={
    100:"认证失败，用户名或者密码错误",
    101:"认证成功",
    102:"尚未存在注册用户，请先注册",
    103:None,#随机配置
    104:"",
    105:"Format Error:认证文件格式已被更改",
    106:"客户端强制结束会话",
    107:"Read failed: 服务端未能找到相应的文件",
    108:"指定的文件目录不存在",
    109:"目录切换成功。",
    110:"已返回指定上级目录。",
    111:"指定文件夹越权，无法完成切换",
    112:"指定创建的目录已存在，无法再次创建。",
    113:"创建目录成功",
    114:"目录删除成功",
    115:"目录删除失败，当前目录不存在",
    116:"文件删除成功",
    117:"文件删除失败，当前文件不存在",
    118:"删除动作执行失败，是否存在其余账号读取文件？",
    119:"文件已存在，请勿重复传入。",
    120:"传输完成！文件已上传至服务器.",
    121:"传输存在问题，文件md5有异",
    122:"文件已经存在，但是与传输的数据大小不同，请求计算在当前大小的前提下文件的MD5值",
    123:"两次传入文件MD5值不相同，无法断点续传文件",
    400:"与管理员注册新用户时输入用户名和密码有关的提示",
    401:"删除用户成功",
    402:"删除用户失败,当前用户未注册",
    403:"注册用户成功",
    404:"注册用户失败，当前用户已存在",
    405:"与管理员删除用户时输入用户名有关的提示",
    406:"用户退出系统",
    407:"展示当前存在的用户",
    408:"磁盘配额",
    409:"用户信息不存在，需要先进行注册",
    410:"修改配额",
    411:"修改成功",
    412:"修改失败,不存在用户名",
    413:"删除用户失败,当前用户文件不存在",
    414:"所上传的文件大于当前可用空间，无法上传"
}

#初始化log日志
timer=time.strftime("%Y-%m-%d")
logger=record(Base_dir+"\\Data\\Log\\"+timer+".txt")
class MyTCPHandler(socketserver.BaseRequestHandler):
    #开始连接时
    def setup(self):
        auth_msg_source=self.request.recv(1024).strip()
        self.auth_msg=json.loads(auth_msg_source.decode())
        if self.auth_msg.get("Type")=="auth":
            self.username=self.auth_msg["username"]
            self.md5_password=self.auth_msg["password"]
            self.ipaddr=self.auth_msg["ipaddr"]
            self.role=self.auth_msg["auth_tag"]
            logger.info("用户名：%s尝试从终端 %s 登录到服务器"%(self.username,self.ipaddr))




    def handle(self):
        '''
        此函数为MyTCPhandle进行主链接使用的
        :return:
        '''
        if self.auth_msg.get("Type")=="auth":
            auth_tag=self.__auth()
            if auth_tag==101:
                logger.info("用户 %s 从终端 %s 登录成功！"%(self.username,self.ipaddr))
                #此处定义的是当前登录用户的目标文件夹，此处也是函数self.dest初始化的位置
                self.dest=HomeDocs+"\\"+self.username
                ##########此处执行的动作是创建以用户名命名的文件夹，防止后续操作出现问题###############
                dirs=self.dest.split("\\")
                res_item=""
                for item in  dirs:
                    res_item=res_item+item+"\\"
                    if os.path.exists(res_item):
                        pass
                    else:
                        os.mkdir(res_item)
                ########################################################################################
                ###################读取当前用户的空间使用值#############################################
                with open(Base_dir+"\\Data\\Users\\Quota.txt","r") as f_qtread:
                    for qt in f_qtread:
                        qtusr,qtvl=qt.strip("\n").strip('"').split(":")
                        if qtusr==self.username:
                            self.qtvl=qtvl
                            self.qtvl=int(self.qtvl)*1024*1024
                            break
                #########################################################################################
                ####################读取当前用户名下的文件大小###########################################
                self.allsize=0
                for size_path,size_dirs,size_files in os.walk(HomeDocs+"\\"+self.username):
                    for  item in size_files:
                        self.allsize=self.allsize+int(os.path.getsize(os.path.join(size_path,item)))
                self.__changemsg()
            elif auth_tag==102:
                logger.error("用户名 %s 未注册。"%self.username)
            elif auth_tag==100:
                logger.error("用户登录失败，用户名或密码发送错误。")

    def __sendmsg(self,stand_code,data=None):
        '''
        此函数是服务端用来向客户端发送数据的
        :param stand_code: 标准信息码
        :param data: 附带数据，若存在则可填入，若不存在默认为None
        :return: 无值
        '''
        sendmsg={
            "standcode":stand_code,
            "standmsg":Stand_msg[stand_code],
            "data":data
        }
        self.request.send(json.dumps(sendmsg).encode())

    def __recvmsg(self):
        '''
        此函数是服务端接受客户端发送过来数据的
        :return: 返回的是接收到的数据
        '''
        Rsg_source=self.request.recv(1024)
        Rsg=json.loads(Rsg_source.decode())
        return Rsg


    def __walk(self):
        '''
        #此处遍历当前目录，找出所在文件夹的子文件夹和文件列表，并返回相应的列表，格式为  [[文件夹列表]，[文件列表]]
        :return: 返回的是当前文件夹下存在的文件夹名和文件名的列表
        '''
        c=0
        search_list=[]
        ls_list=os.walk(self.dest)
        for item in ls_list:
            for item2 in item:
                if c==0:
                    c+=1
                    continue
                search_list.append(item2)
            if c==1:
                break
        return search_list

    def __auth(self):
        '''
        此为用户认证函数，用户是否能够登录到系统由此函数判断
        :return:
        '''
        if self.role=="ordinary":
            auth_tag=False
            if os.path.exists(Base_dir+"\\Data\\Users\\UserAuth.txt"):
                with open(Base_dir+"\\Data\\Users\\UserAuth.txt","r") as f_read:
                    for line in f_read:
                        usr,pad=line.strip('\n').strip('"').split(":")
                        if usr==self.username and pad ==self.md5_password:
                            auth_tag=True
                            self.__sendmsg(101)
                            return 101
                if auth_tag==False:
                    self.__sendmsg(100)
                    return 100
            else:
                self.__sendmsg(102)
                return 102
        elif self.role=="mgr":
            m=hashlib.md5(password.encode("utf-8"))
            passwdvalue=m.hexdigest()
            if self.username==admin and self.md5_password==passwdvalue:
                self.__sendmsg(101,data="True")
                logger.info("用户 %s 从终端 %s 登录成功！"%(self.username,self.ipaddr))
                try:
                    self.__mgr()
                except:
                    logger.info("%s的管理员已断开连接。"%self.ipaddr)
            else:
                self.__sendmsg(100)

    def __changemsg(self):
        '''
        此函数为登录成功后客户端与服务器相互交互的函数，客户端发送相关指令给服务器，服务器根据指令分配相应函数完成。
        :return:
        '''
        while True:
            try:
                self.chmsg=self.__recvmsg()
                if self.chmsg.get("Type")=="pwd":
                    #运行pwd函数
                    self.__pwd()
                elif self.chmsg.get("Type")=="cd":
                    self.__cd()
                elif self.chmsg.get("Type")=="ls":
                    self.__ls()
                elif self.chmsg.get("Type")=="put":
                    self.__put()
                elif self.chmsg.get("Type")=="get":
                    self.__get()
                elif self.chmsg.get("Type")=="mkdir":
                    self.__mkdir()
                elif self.chmsg.get("Type")=="rm":
                    self.__rm()
                elif self.chmsg.get("Type")=="bye":
                    self.__bye()
                else:
                    self.__help()
            except:
                logger.info("客户端%s已断开连接"%self.ipaddr)
                break

    def __countsize(self):
        '''
        计算当前用户目录下的文件总大小
        :return: 返回文件总大小的值
        '''
        countallsize=0
        for size_path,size_dirs,size_files in os.walk(HomeDocs+"\\"+self.username):
            for  item in size_files:
                countallsize=countallsize+int(os.path.getsize(os.path.join(size_path,item)))
        return countallsize

    def __help(self):
        hsg={
            "put":"作用：上传文件，格式：put 文件名",
            "get":"作用：下载文件，格式：get 原文件名 目标文件路径",
            "ls":"作用：展示当前文件夹内容，格式： ls",
            "pwd":"作用：展示当前文件夹路径，格式：pwd",
            "cd":"作用：切换文件夹，格式：cd 目标文件夹",
            "mkdir":"作用：创建文件夹，格式： mkdir 文件夹名称",
            "rm":"作用：移除文件夹，格式：rm 文件夹名称",
            "bye":"作用：离开， 格式：bye"
        }
        self.__sendmsg(102,data=hsg)


    def __get(self):
        '''
        #执行下载动作的函数#
        :return:
        '''
        if self.chmsg.get("Type") is not None:
            try:
                #此处只考虑文件存在的情况，不存在的情况直接触发try except。
                filename=self.chmsg["filename"]
                size=os.path.getsize(self.dest+"\\"+filename)
                file_msg={
                    "filename":filename,
                    "size":size
                }
                ####发送下载该文件的相关信息
                self.__sendmsg(103,data=file_msg)
                start_tag=self.request.recv(1024)
                #客户端接受到相应的文件信息，并同意服务器开始发送数据。
                if start_tag==b"121":
                    ###########执行发送文件的动作########################
                    recv_len=0#已经发送的长度
                    with open(self.dest+"\\"+filename,"rb") as f_read:
                        while True:
                            if recv_len<int(size):
                                filedata_source=f_read.read(1024*100)
                                self.request.send(filedata_source)
                                recv_len=recv_len+len(filedata_source)
                            else:
                                break
                    ##########接收客户端的反馈###########################
                    return_tag=self.request.recv(1024)
                    if return_tag==b"121":
                        logger.info("传输完成，文件(%s)已下载至客户端。"%filename)
                    else:
                        logger.error("文件下载失败.")
                else:
                    pass
            except:
                logger.error("用户%s请求下载的文件未查询到"%self.username)
                self.__sendmsg(107)
    def __ls(self):
        '''
        #此处为遍历当前目录下所有的文件夹和文件，然后返回。
        #若当前目录为空，则不会返回data数据，客户端可据此进行判断“当前目录为空”
        :return:
        '''
        ls_send_list=[]
        if self.chmsg.get("Type") is not None:
            ls_send_list=self.__walk()
            logger.info("用户%s遍历了目录,目录名为%s"%(self.username,self.dest.strip("").split("\\")[-1]))
        self.__sendmsg(103,data=ls_send_list)

    def __cd(self):
        '''
        #执行目录切换动作的函数
        :return:
        '''
        if self.chmsg.get("Type") is not None:
            dest=self.chmsg["dest"]
            #将全局的self.dest赋值到本函数内的this_dest,确保调用。
            this_dest=self.dest
            # this_tag=False
            #此处只是获取search_walk返回的文件夹列表##
            floder_list=(self.__walk())#[0]
            file_list=floder_list[0]
            ###########################################
            if dest in file_list:
                self.dest=this_dest+"\\"+dest
                self.__sendmsg(109)
                logger.info("用户%s已将目录切换至%s"%(self.username,self.dest))
            #若使用“..”进行文件夹切换，可返回至上层目录。
            #此处会进行判断是否切换的目录超过权限，若超过，则维持原目录，即最高可切换至以用户名命名的文件夹。
            elif dest=="..":
                #如果切换越权，维持原目录
                if self.dest==HomeDocs+"\\"+self.username+"\\" or self.username not in self.dest.split("\\"):
                    self.dest=HomeDocs+"\\"+self.username
                    logger.error("用户%s指定切换的目录越权，无法完成切换。"%self.username)
                    self.__sendmsg(111)
                #如果没有越权，则执行切换，将字符串切割以后舍弃最后一个。
                # elif HomeDocs+"\\"+self.username in self.dest:
                else:
                    dest_list=self.dest.split("\\")
                    new_dest=""
                    for i in range(0,len(dest_list)):
                        if len(dest_list)==i+1:
                            break
                        new_dest=new_dest+dest_list[i]+"\\"
                    #执行完成切换以后，将已经变动的当前文件路径重新赋值给全局的self.dest，算是告知所有协同工作的函数
                    self.dest=new_dest.strip("\\")
                    logger.info("用户%s切换目录至上一级%s"%(self.username,self.dest))
                    self.__sendmsg(110)
            else:
                logger.error("用户%s切换目录至%s失败，服务器不存在此目录"%(self.username,dest))
                self.__sendmsg(108)
    def __put(self):
        '''
        ##执行上传动作的函数#
        :return:
        '''
        recv_len=0#已经收到的长度
        tag=False#tag 是用来判断是否有必要执行下一步的，如果此文件名存在于服务器，那么不接受再次传入。
        filename=self.chmsg["filename"]#取得发送过来的文件名
        if "\\" in filename:#此处是为了判断发送过来的文件是否携带路径，若携带路径，则对字符串进行切割提取。
            filename=(filename.split("\\"))[-1]
        size=self.chmsg["size"]#取得发送过来的文件大小
        md5=self.chmsg["md5"]#取得文件发送过来的md5值
        exist_list=self.__walk()
        #md5值的计算
        file_md5 = hashlib.md5()
        ##################
        for existname in exist_list:
            if len(existname)!=0:
                if filename in existname:
                    tag=True#tag为真，证明文件存在，若还需要传输，则需要进行md5值的比较。
        ########################此处计算已经存在文件的size加上需要上传的文件的size###########
        self.allsize=int(self.allsize)+int(size)
        #存在的文件加要上传的文件如果没超过限定值，开始接受传输。
        if self.qtvl>=self.allsize:
            #如果tag为Flase， 则证明服务器端原本就没有此文件，那么此文件就以新文件形式处理。
            if tag==False:
                #服务器向客户端发出继续发送的指令。
                self.__sendmsg(102,data="continue")
                filename_stream=open(self.dest+"\\"+filename,"wb")
                while True:
                    ############循环接受数据传输##################
                    try:
                        if recv_len<int(size):
                            filedata_source=self.request.recv(1024*100)
                            #此处进行判断是因为在客户端断开后，可能会传输空字符串，从而导出出现问题。
                            if filedata_source ==b"":
                                errsize3=os.path.getsize(self.dest+"\\"+filename)
                                errvalue2=eval("(errsize3/size)*100")
                                logger.error("目标已传入：百分之%.2f"%errvalue2)
                                return False
                            file_md5.update(filedata_source)
                            filename_stream.write(filedata_source)
                            recv_len+=len(filedata_source)
                    #############################################
                        #若接受的字节长度与传过来的文件大小相等，则代表接收完成。
                        else:
                            if size==recv_len:
                                filename_stream.close()
                                hash_recv=file_md5.hexdigest()
                                if md5==hash_recv:
                                    logger.info("传输完成！文件（%s）已上传至服务器"%filename)
                                    self.__sendmsg(120)
                                else:
                                    #此处是在传输最后比较md5值，不一样的话则证明文件出现问题，直接将此文件删除。
                                    os.remove(self.dest+"\\"+filename)
                                    logger.info("传输存在问题，文件（%s）md5有异,已被删除"%filename)
                                    self.__sendmsg(121)
                                break
                    #此处是用来表明链接出现问题的情况，一般为客户端被强行终端，从而导致传输没能完成。
                    except:
                        errsize=os.path.getsize(self.dest+"\\"+filename)
                        errvalue=eval("(errsize/size)*100")
                        logger.error("链接中断，目标已传入：百分之%.2f"%errvalue)
                        break
            #此处是标明了tag为True的情况，这证明了此文件名之前是存在的，那么现在就需要进行断点续传。
            else:
                #获取服务器端当前存在的文件大小。
                exist_size=os.path.getsize(self.dest+"\\"+filename)
                #获取服务器端当前存在的文件的MD5值
                exist_md5=hashlib.md5()
                with open(self.dest+"\\"+filename,"rb") as f_exist:
                    for line in f_exist:
                        exist_md5.update(line)
                #对比前期传过来的文件size，若size一样，则证明了之前文件已经传输完成，在此情况下就不需要进行断点续传了。
                if self.chmsg.get("size")==exist_size:
                    logger.error("文件%s已存在，拒绝重复传入。"%filename)
                    self.__sendmsg(119)
                #若文件的size大小不一样，那么就需要对比文件的md5值，看上传的文件与当前服务器存在的文件是否一致
                #将文件名一致但内容不一致的情况去除。
                else:
                    #传送服务器端已经存在的文件size和md5值，以便客户端进行校对。
                    exist_msg={
                        "size":exist_size,
                        "md5":exist_md5.hexdigest()
                    }
                    self.__sendmsg(122,data=exist_msg)
                    #收到客户端返回的信息，返回的信息中包含了校对的size和md5值是否一致。
                    #一致则皆为equally  不一致则为difference
                    exmsg=self.__recvmsg()
                    #一致的情况下进行文件接收，此处的文件接收是经过客户端过滤，即是从已经接受了多少的情况下继续接收，而不是
                    #从头开始接收。
                    if exmsg.get("size")=="equally" and exmsg.get("md5")=="equally":
                        #发送信号告知客户端开始进行传输。
                        self.__sendmsg(103,data="continue")
                        exist_filename_stream=open(self.dest+"\\"+filename,"ab")
                        while True:
                            ############循环接受数据传输##################
                            try:
                                if exist_size<int(size):
                                    filedata_source=self.request.recv(1024*1000)
                                    if filedata_source ==b"":
                                        errsize3=os.path.getsize(self.dest+"\\"+filename)
                                        errvalue2=eval("(errsize3/size)*100")
                                        logger.error("目标已传入：百分之%.2f"%errvalue2)
                                        break
                                    exist_md5.update(filedata_source)
                                    exist_filename_stream.write(filedata_source)
                                    exist_size+=len(filedata_source)
                            #############################################
                                #若接受的字节长度与传过来的文件大小相等，则代表接收完成。
                                elif exist_size==int(size):
                                    exist_filename_stream.close()
                                    hash_recv=exist_md5.hexdigest()
                                    if md5==hash_recv:
                                        logger.info("传输完成！文件（%s）已上传至服务器"%filename)
                                        self.__sendmsg(120)
                                    else:
                                        os.remove(self.dest+"\\"+filename)
                                        logger.info("传输存在问题，文件（%s）md5有异,已被删除"%filename)
                                        self.__sendmsg(121)
                                    break
                            #此处是为了防止出现客户端断开链接的情况
                            except:
                                errsize2=os.path.getsize(self.dest+"\\"+filename)
                                errvalue2=eval("(errsize2/size)*100")
                                logger.error("链接中断，目标已传入：百分之%.2f"%errvalue2)
                                break
                    #此处是在校对了文件以后，size和md5值不一致的情况下，结束文件接受。
                    elif exmsg.get("size")=="difference" and exmsg.get("md5")=="difference":
                        logger.error("两次传入文件MD5值不相同，无法断点续传文件。")
                        self.__sendmsg(123)
        #超过限额值则直接返回不满足上传条件。
        elif self.qtvl<self.allsize:
            self.allsize=self.__countsize()
            self.__sendmsg(414)
            logger.info("用户%s上传的文件大于当前可用空间，无法完成上传。"%self.username)

    def __pwd(self):
        '''
        #此为查看当前所在位置的函数
        :return:
        '''
        send_list=""
        send_tag=False
        if self.chmsg.get("Type") is not None:
            dest_list=self.dest.split("\\")
            for item in dest_list:
                if item!="":
                    if item==self.username:
                        send_tag=True
                    if send_tag==True:
                        send_list=send_list+item+"\\"
            logger.info("用户：%s查询了当前所在目录：%s"%(self.username,send_list))
            self.__sendmsg(103,data=send_list)


    def __mkdir(self):
        '''
        #此为执行创建目录的函数
        :return:
        '''
        if self.chmsg.get("Type") is not None:
            mkname=self.chmsg.get("mkname")
            if os.path.exists(self.dest+"\\"+mkname):
                logger.error("指定创建的目录已存在，无法创建")
                self.__sendmsg(112)
            else:
                #在创建目录的过程中，此处判断是否存在路径上没有的目录，若目录上没有，则会一块创建。
                dirs=self.dest.split("\\")
                dirs.append(mkname)
                res_item=""
                for item in  dirs:
                    res_item=res_item+item+"\\"
                    if os.path.exists(res_item):
                        pass
                    else:
                        os.mkdir(res_item)
                self.__sendmsg(113)
                logger.info("用户%s创建文件夹%s成功"%(self.username,self.chmsg.get("mkname")))


    def __rm(self):
        '''
        #此为执行移除文件或者文件夹的函数
        #需要判断移除的是文件还是文件夹，第一遍循环的是文件夹，第二遍循环的是文件
        #在删除文件夹的时候，若文件夹内有文件，使用os.rmdir()无法移除文件夹，会直接报错
        #使用shutil.rmtree则可以直接全部删除
        :return:
        '''
        if self.chmsg.get("Type") is not None:
            c=0
            tag=False
            rmname=self.chmsg.get("rmname")
            file_list=self.__walk()
            for item in file_list:
                if rmname in item and c==0:
                    if os.path.exists(self.dest+"\\"+rmname):
                        try:
                            shutil.rmtree(self.dest+"\\"+rmname)
                            logger.info("文件夹%s已被用户%s删除"%(rmname,self.username))
                            self.__sendmsg(114)
                        except:
                            logger.error("文件夹%s删除异常，未能成功处理"%rmname)
                            self.__sendmsg(118)
                    else:
                        logger.error("指定删除的文件夹不存在，无法完成删除")
                        self.__sendmsg(115)
                    tag=True
                #在循环第一遍的时候，因为c=0，因此无法执行此函数，只有在循环的第二遍的时候，才会进入此判断
                elif  rmname in item and c==1:
                    if os.path.isfile(self.dest+"\\"+rmname):
                        try:
                            os.remove(self.dest+"\\"+rmname)
                            self.__sendmsg(116)
                            logger.error("文件%s已被用户%s删除"%(rmname,self.username))
                        except:
                            logger.error("文件%s删除异常，未能成功处理"%rmname)
                            self.__sendmsg(118)
                    else:
                        logger.error("指定删除的文件不存在，无法完成删除")
                        self.__sendmsg(117)
                    tag=True
                c+=1
            if tag==False:
                logger.error("指定删除的文件不存在，无法完成删除")
                self.__sendmsg(117)
            #################执行删除动作以后，重新计算当前用户目录下的文件大小####################
            self.allsize=0
            for size_path,size_dirs,size_files in os.walk(HomeDocs+"\\"+self.username):
                for  item in size_files:
                    self.allsize=self.allsize+int(os.path.getsize(os.path.join(size_path,item)))
            ########################################################################################


    def __bye(self):
        '''
        #此为告知客户端关闭通知的函数
        :return:
        '''
        if self.chmsg.get("Type") is not None:
            action=self.chmsg.get("Type")
            if action=="bye":
                logger.info("用户%s已退出"%self.username)
                self.__sendmsg(103,data="OK")


    #此处的函数主要是用管理员功能，因只涉及管理员功能，故而不对函数进行拆分
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
                if os.path.exists(Base_dir+"\\Data\\Users\\UserAuth.txt"):
                    with open(Base_dir+"\\Data\\Users\\UserAuth.txt","r") as f_read:
                        for line in f_read:
                            usr,pad=line.strip('"').split(":")
                            if usr==username:
                                wr_tag=True
                if wr_tag==False:
                    joindir=""
                    #此处是为了预防初次操作不存在当前目录#####################
                    dirs=(Base_dir+"\\Data\\Users\\UserAuth.txt").split("\\")
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
                    with open(Base_dir+"\\Data\\Users\\UserAuth.txt","a") as f:
                        f.write(json.dumps(str(username)+":"+str(password)))
                        f.write("\n")
                    #将配额值写入配额文件
                    with open(Base_dir+"\\Data\\Users\\Quota.txt","a") as f_quota:
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
                if os.path.exists(Base_dir+"\\Data\\Users\\UserAuth.txt"):
                    with open(Base_dir+"\\Data\\Users\\UserAuth.txt","r") as f_delete:
                        #判断是否需要进行删除动作，若需要删除，则del_tag为True
                        for line in f_delete:
                            delusr,delpad=line.strip('"').split(":")
                            if delusr==del_username:
                                del_tag=True
                                continue
                            else:
                                user_list.append(line)
                    #判断配额值是否需要删除，若需要删除，则quota_tag为True
                    if os.path.exists(Base_dir+"\\Data\\Users\\Quota.txt"):
                        with open(Base_dir+"\\Data\\Users\\Quota.txt","r") as f_delquota:
                            for line2 in f_delquota:
                                delusr,delquo=line2.strip('"').split(":")
                                if delusr==del_username:
                                    quota_tag=True
                                    continue
                                else:
                                    quota_list.append(line2)
                    if del_tag and quota_tag:
                        with open(Base_dir+"\\Data\\Users\\UserAuth.txt","w") as f_rewr:
                            for item in user_list:
                                f_rewr.write(item)
                            logging.info("完成删除用户%s"%delusr)
                        with open(Base_dir+"\\Data\\Users\\Quota.txt","w") as f_requota:
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
                if os.path.exists(Base_dir+"\\Data\\Users\\Quota.txt"):
                    with open(Base_dir+"\\Data\\Users\\Quota.txt","r") as f_seek:
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
                if os.path.exists(Base_dir+"\\Data\\Users\\Quota.txt"):
                    with open(Base_dir+"\\Data\\Users\\Quota.txt","r") as f_cgvalue:
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
                        with open(Base_dir+"\\Data\\Users\\Quota.txt","w") as f_cgvalue_write:
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
