# 客户端发送hello,如果服务端 recv(1) ,那只能接收到 h 这一个字符，然后再recv(1) 一下，可以再接收一个 e ，
# 因为客户端发送的结果长，所以只能把其他的先缓存下来，下次recv的时候再去接收。
# 这就是粘包，即两次结果粘到一起了。
# 多次连续send小数据，也会发生黏包现象。
# 同样send一个大数据，连续 recv 小数据也会发生粘包现象

# 发生黏包现象的本质是不知道接收或者发送的数据有多大

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

# import socket
# sk = socket.socket(type=socket.SOCK_DGRAM)
# ip_port = ('127.0.0.1', 8080)
# sk.bind(ip_port)
#
# msg, addr = sk.recvfrom(1024)
# print(msg.decode('utf-8'))
# while True:
#     cmd = input('>>')
#     sk.sendto(cmd.encode('utf-8'), addr)
#     msg, addr = sk.recvfrom(10240)
#     print(msg.decode('utf-8'))
#
# sk.close()

# UDP 协议不黏包，但是会丢包


# 解决黏包方式一
# 客户端直接返回信息的长度
# 优点: 确定了接收多大的数据
# 缺点：多了一次交互
import socket
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.bind(ip_port)
sk.listen()

conn, addr = sk.accept()

while True:
    cmd = input('>>')
    conn.send(cmd.encode('gbk'))
    num = conn.recv(1024).decode('utf-8')
    msg = conn.recv(int(num)).decode('gbk')
    print(msg)

conn.close()
sk.close()
