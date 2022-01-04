# IO 模型

## IO模型简介

```
内存分为内核缓冲区和用户缓冲区(网络下载的资源，硬盘加载的资源，先放到内核缓冲区---->copy到应用程序的缓冲区，应用程序才能用这个数据)

我们这里研究的IO模型都是针对网络IO的
五种IO Model:
    * blocking IO           阻塞IO
    * nonblocking IO        非阻塞IO
    * IO multiplexing       IO多路复用  select(windows支持，windows不支持epoll，官方不提供redis的window版本)，poll，epoll(linux支持)
    * signal driven IO      信号驱动IO
    * asynchronous IO       异步IO
    由于signal driven IO(信号驱动IO)在实际中并不常用，所以主要介绍其余四种IO Model
    
1) 等待数据准备 (Waiting for the data to be ready)
2) 将数据从内核拷贝到进程中(Copying the data from the kernel to the process)

同步异步
阻塞非阻塞
常见的网络阻塞状态:
  	accept
    recv
    recvfrom
    
    send虽然它也有io行为 但是不在我们的考虑范围
```

## 阻塞IO

```
我们之前写的都是阻塞IO模型  协程除外
    
在服务端开设多进程或者多线程 进程池线程池 其实还是没有解决IO问题	
该等的地方还是得等 没有规避
只不过多个人等待彼此互不干扰

import socket

server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn, addr = server.accept()
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0:break
            print(data)
            conn.send(data.upper())
        except ConnectionResetError as e:
            break
    conn.close()
```

## 非阻塞IO

```python
import socket
import time

server = socket.socket()
server.bind(('127.0.0.1', 8081))
server.listen(5)
server.setblocking(False)
# 将所有的网络阻塞变为非阻塞
r_list = []
del_list = []
while True:
    try:
        conn, addr = server.accept()
        r_list.append(conn)
    except BlockingIOError:
        # time.sleep(0.1)
        # print('列表的长度:',len(r_list))
        # print('做其他事')
        for conn in r_list:
            try:
                data = conn.recv(1024)  # 没有消息 报错
                if len(data) == 0:  # 客户端断开链接
                    conn.close()  # 关闭conn
                    # 将无用的conn从r_list删除
                    del_list.append(conn)
                    continue
                conn.send(data.upper())
            except BlockingIOError:
                continue
            except ConnectionResetError:
                conn.close()
                del_list.append(conn)
        # 挥手无用的链接
        for conn in del_list:
            r_list.remove(conn)
        del_list.clear()

# 客户端
import socket

client = socket.socket()
client.connect(('127.0.0.1',8081))

while True:
    client.send(b'hello world')
    data = client.recv(1024)
    print(data)
```

总结：
虽然非阻塞IO给你的感觉非常的厉害
但是该模型会长时间占用着CPU并且不干活 让CPU不停的空转
我们实际应用中也不会考虑使用非阻塞IO模型
任何的技术点都有它存在的意义
实际应用或者是思想借鉴

## IO多路复用

```python
当监管的对象只有一个的时候 其实IO多路复用连阻塞IO都比不上！！！
但是IO多路复用可以一次性监管很多个对象
server = socket.socket()
conn,addr = server.accept()
监管机制是操作系统本身就有的 如果你想要用该监管机制(select)
需要你导入对应的select模块

import socket
import select

server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)
server.setblocking(False)
read_list = [server]

while True:
    r_list, w_list, x_list = select.select(read_list, [], [])
    """
    帮你监管
    一旦有人来了 立刻给你返回对应的监管对象
    """
    # print(res)  # ([<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080)>], [], [])
    # print(server)
    # print(r_list)
    for i in r_list:  #
        """针对不同的对象做不同的处理"""
        if i is server:
            conn, addr = i.accept()
            # 也应该添加到监管的队列中
            read_list.append(conn)
        else:
            res = i.recv(1024)
            if len(res) == 0:
                i.close()
                # 将无效的监管对象 移除
                read_list.remove(i)
                continue
            print(res)
            i.send(b'hello python')

 # 客户端
import socket

client = socket.socket()
client.connect(('127.0.0.1',8080))

while True:

    client.send(b'hello world')
    data = client.recv(1024)
    print(data)
```

总结：
监管机制其实有很多
select机制windows linux都有
poll机制只在linux有 poll和select都可以监管多个对象 但是poll监管的数量更多
上述select和poll机制其实都不是很完美 当监管的对象特别多的时候
可能会出现极其大的延时响应
epoll机制只在linux有
它给每一个监管对象都绑定一个回调机制
一旦有响应 回调机制立刻发起提醒
针对不同的操作系统还需要考虑不同检测机制 书写代码太多繁琐
有一个人能够根据你跑的平台的不同自动帮你选择对应的监管机制
selectors模块

## 异步IO

asyncio

```python
"""
异步IO模型是所有模型中效率最高的 也是使用最广泛的
相关的模块和框架
	模块: asyncio模块
	异步框架:sanic tronado twisted
		速度快！！！
"""
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('hello world %s'%threading.current_thread())
    yield from asyncio.sleep(1)  # 换成真正的IO操作
    print('hello world %s' % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```

