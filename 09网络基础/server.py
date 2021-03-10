# TCP协议
import socket
sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 允许连接地址重用，避免重启时报 address already in user

# 绑定并监听地址
ip_port = ('127.0.0.1', 8080)
sk.bind(ip_port)
sk.listen()

# 接收消息
conn, addr = sk.accept()
while True:
    msg = conn.recv(1024).decode('utf-8')
    if msg == 'exit':
        break
    print(msg)

    three_body = input('>>:')
    # 发送消息
    
    conn.send(bytes(three_body, encoding='utf-8'))

# 关闭连接
conn.close()
sk.close()

# UDP协议
# udp的server不需要进行监听，也不需要建立长连接
# 在启动服务之后，只能被动的等待客户端发送信息
# 恢复消息的时候，除了要发送信息， 还需要把对方的地址发过去
import socket
sk = socket.socket(type=socket.SOCK_DGRAM) # udp协议需要指定一个 type=socket.SOCK_DGRAM
ip_port = ('127.0.0.1', 8080)
sk.bind(ip_port)

msg, addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
sk.sendto(b'Server', addr)

sk.close()