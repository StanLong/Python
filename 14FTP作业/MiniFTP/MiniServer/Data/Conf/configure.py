# -*- coding:utf-8 -*-


import os
#最终定位到的是Data文件夹
ServerData=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#用户存放文件的目录
HomeDocs="%s\\Docs"%ServerData
#最终定位到MiniServer\Data\Docs


###################################
#当前服务器的地址
Host="127.0.0.1"
#当前服务器需要监听的端口
Port=8808
###################################


#管理员账号
admin="admin"
password="password"

Account="%s\Conf\\accounts.cfg"%ServerData