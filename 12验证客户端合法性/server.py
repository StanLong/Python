# 验证客户端合法性

# import hmac
# h = hmac.new() # 需要两个参数 参数一：盐， 参数二，要加密的字节
# h.digest() # 生成密文
# hmac.compare_digest() # 比较密文是否一致


import os
import hmac
import socket
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.bind(ip_port)
sk.listen()

conn, addr = sk.accept()

secret_key = b'egg2'

def check_conn(conn):
    msg = os.urandom(32) # 返回一个有32个byte那么长的一个string，然后很适合用于加密
    conn.send(msg)
    h = hmac.new(secret_key, msg)
    digest = h.digest()
    client_digest = conn.recv(1024)
    return hmac.compare_digest(digest, client_digest)
res = check_conn(conn)
if res:
    print('合法的客户端')
    conn.close()
else:
    print('非法的客户端')
    conn.close()
sk.close()
