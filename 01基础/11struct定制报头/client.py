# struct 自定义报头
# 实现一个大文件的上传下载
# 发送端

# https://btsow.cam/
# https://btsow.shop/
# https://btsow.one
# https://btsow.com
import os
import json
import struct
import socket
# 定制文件信息字典
header = {
    'filepath':r'D:\下载',
    'filename':r'[电影天堂www.dy2018.net]新铁血战士BD中英双字.rmvb',
    'filesize':None
}
file_path = os.path.join(header['filepath'], header['filename'])
filesize = os.path.getsize(file_path)
header['filesize'] = filesize

# 字典序列化
json_head = json.dumps(header)
# 字符串转bytes
bytes_head = json_head.encode('utf-8')

# struct 打包
head_len = len(bytes_head)
pack_len = struct.pack("i", head_len)

# 创建socket
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.connect(ip_port)

# 发送数据
sk.send(pack_len) # 先发送长度
sk.send(bytes_head) # 在发送报头

buffer = 1024 # 读数缓冲，每次读 1024 个字节
with open(file_path, 'rb') as f:
    while filesize:
        if filesize >= buffer:
            content = f.read(buffer)
            sk.send(content)
            filesize = filesize - buffer
        else:
            content = f.read(buffer)
            sk.send(content)
            break
sk.close()


