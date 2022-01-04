# 验证客户端合法性

import hmac
import socket
secret_key = b'egg2'
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)

sk.connect(ip_port)
msg = sk.recv(1024)
h = hmac.new(secret_key, msg)
digest = h.digest()
sk.send(digest)
sk.close()