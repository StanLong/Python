# 基于TCP实现远程执行命令
# server端下发命令
# import socket
# import subprocess
# sk = socket.socket()
# ip_port = ('127.0.0.1', 8080)
# sk.connect(ip_port)
#
# while True:
#     cmd = sk.recv(1024).decode('gbk')
#
#     result = subprocess.Popen(cmd,
#                               shell=True,
#                               stdout=subprocess.PIPE,
#                               stderr= subprocess.PIPE)
#
#     sk.send(result.stdout.read())
#     sk.send(result.stderr.read())
#
# sk.close()

# 基于UDP实现远程执行命令

# import socket
# import subprocess
#
# sk = socket.socket(type=socket.SOCK_DGRAM)
# ip_port = ('127.0.0.1', 8080)
#
# sk.sendto('Hello'.encode('utf-8'), ip_port)
#
# while True:
#     # cmd = sk.recv(10240).decode('utf-8')
#     cmd, addr = sk.recvfrom(1024)
#     cmd = cmd.decode('utf-8')
#     print(cmd)
#     result = subprocess.Popen(cmd,
#                               shell=True,
#                               stdout=subprocess.PIPE,
#                               stderr= subprocess.PIPE)
#
#     # sk.send(result.stdout.read())
#     # sk.send(result.stderr.read())
#     std_err = 'stderr :' + (result.stderr.read()).decode('gbk')
#     std_out = 'stdout :' + (result.stdout.read()).decode('gbk')
#     if len(std_out) == 8:
#         sk.sendto(std_err.encode('utf-8'), ip_port)
#     else:
#         sk.sendto(std_out.encode('utf-8'), ip_port)
#
# sk.close()


# 解决黏包方式一
# 客户端直接返回信息的长度

import socket
import subprocess
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.connect(ip_port)

while True:
    cmd = sk.recv(1024).decode('gbk')

    result = subprocess.Popen(cmd,
                              shell=True,
                              stdout=subprocess.PIPE,
                              stderr= subprocess.PIPE)

    std_out = result.stdout.read()
    std_err = result.stderr.read()
    sk.send(str(len(std_out) + len(std_err)).encode('utf-8'))
    sk.send(std_out)
    sk.send(std_err)

sk.close()