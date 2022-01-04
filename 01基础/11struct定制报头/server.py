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
            # 实现下载进度条展示功能
            print('\r下载进度 %.2f%%' %((head['filesize']-filesize)/head['filesize']*100), end='') # \r表示回车但是不换行，利用这个原理进行百分比的刷新
            f.flush()
        else:
            content = conn.recv(buffer)
            f.write(content)
            break
print('\n', '传输完成')
conn.close()
sk.close()

