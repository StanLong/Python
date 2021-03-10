# 基于TCP实现远程执行命令
# server端下发命令
# import socket
# sk = socket.socket()
# ip_port = ('127.0.0.1', 8080)
# sk.bind(ip_port)
# sk.listen()
#
# conn, addr = sk.accept()
#
# while True:
#     cmd = input('>>')
#     conn.send(cmd.encode('gbk'))
#     msg = conn.recv(1024).decode('gbk')
#     print(msg)
#
# conn.close()
# sk.close()

# 当向客户端发送 ipconfig 命令时，发现客户端返回的数据已经乱了
#  recv 没有接收完 或者接收多了， 这就是黏包现象


# 基于UDP实现远程执行命令

import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)
sk.bind(ip_port)

msg, addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
while True:
    cmd = input('>>')
    sk.sendto(cmd.encode('utf-8'), addr)
    msg, addr = sk.recvfrom(10240)
    print(msg.decode('utf-8'))

sk.close()

# UDP 协议不黏包，但是会丢包