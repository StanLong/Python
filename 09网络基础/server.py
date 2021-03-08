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