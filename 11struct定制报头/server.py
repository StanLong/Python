# struct 自定义报头
# 实现一个大文件的上传下载
# 接收端
# 文件保存到当前目录，文件名与上传的文件名相同

import json
import socket
import struct

sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.bind(ip_port)
sk.listen()

conn, addr = sk.accept()

head_len = conn.recv(4)
print(head_len)
head_len = struct.unpack("i", head_len)[0]
json_head = conn.recv(head_len).decode('utf-8')
print(json_head)
head = json.loads(json_head)
filesize = head['filesize']
buffer = 1024

with open(head['filename'], 'wb') as f:
    while filesize:
        if filesize >= buffer:
            content = conn.recv(buffer)
            f.write(content)
            filesize = filesize - buffer
            # TODO
            # 实现下载进度条展示功能
        else:
            content = conn.recv(buffer)
            f.write(content)
            break
print('传输完成')
conn.close()
sk.close()

