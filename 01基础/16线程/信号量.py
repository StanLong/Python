# 信号量
# 信号量对象内部维护一个倒计数器，每一次acquire都会减1，
# 当acquire方法发现计数为0就阻塞请求 的线程，直到其它线程对信号量release后，计数大于0，恢复阻塞的线程

# Semaphore(value=1)	构造方法。value为初始信号量。value小于0，抛出ValueError异常
# Semaphore.acquire(self,blocking=True,timeout=None)	获取信号量，技术器减1，即_value的值减少1。如果_value的值为0会变成阻塞状态。获取成功返回True
# Semaphore.release(self)	释放信号量，计数器加1。即_value的值加1
# Semaphore._value	信号量，当前信号量
# 注意：
# 计数器永远不会低于0，因为acquire的时候，发现是0，都会被阻塞。
# 信号量没有做超界限制

# 信号量实例
# from threading import Semaphore
#
# s =Semaphore(3)
# print(s._value)
# s.release() #会增加信号量
# print(s._value) #可以看出没有做信号量上线控制
# print("----------------")
# print(s.acquire())
# print(s._value)
# print(s.acquire())
# print(s._value)
# print(s.acquire())
# print(s._value)
# print(s.acquire())
# print(s._value)
# print(s.acquire()) #当信号量为0再次acquire会被阻塞
# print("~~~~~~阻塞了吗？")
# print(s._value)

# 跨线程使用演示
# from threading import Thread,Semaphore
# import time
# import logging
#
# logging.basicConfig(format="%(asctime)s %(threadName)s %(thread)s %(message)s",level=logging.INFO)
#
# #定义获取信号量
# def worker(s:Semaphore):
#     while s.acquire():
#         logging.info("被执行了一次，获取一个信号量 _value={}".format(s._value))
#
# #释放信号量
# def cunn(s:Semaphore):
#     while True:
#         logging.info("释放一个信号量")
#         s.release()
#         time.sleep(1)
#
# s = Semaphore(3)
# #创建3个线程获取信号量
# for i in range(3):
#     Thread(target=worker,args=(s,),name="w{}".format(i)).start()
#
# #开启一个线程释放信号量
# Thread(target=cunn,args=(s,)).start()


# 有界信号量
# 有界信号量，不允许使用release超出初始值的范围，否则，抛出ValueError异常
# BoundedSemaphore(value=1)	构造方法。value为初始信号量。value小于0，抛出ValueError异常
# BoundedSemaphore.acquire(self,blocking=True,timeout=None)	获取信号量，技术器减1，即_value的值减少1。如果_value的值为0会变成阻塞状态。获取成功返回True
# BoundedSemaphore.release(self)	释放信号量，计数器加1。即_value的值加1，超过初始化值会抛出异常ValueError。
# BoundedSemaphore._value	信号量，当前信号量
# 应用实例
# from threading import BoundedSemaphore
#
# bs = BoundedSemaphore(3)
# print(bs._value)
# bs.acquire()
# bs.acquire()
# bs.acquire()
# print(bs._value)
# bs.release()
# bs.release()
# bs.release()
# print(bs._value)
# bs.release() release超出初始值的范围，会抛出ValueError异常
# raise ValueError("Semaphore released too many times")
# ValueError: Semaphore released too many times

# 应用举例：连接池
# 因为资源有限，且开启一个连接成本高，所以，使用连接池。
# 一个简单的连接池：连接池应该有容量（总数），有一个工厂方法可以获取连接，能够把不用的连接返回，供其他调用者使用
from threading import Thread,BoundedSemaphore
import time
import logging
import random

logging.basicConfig(format="%(asctime)s %(threadName)s %(thread)s %(message)s",level=logging.INFO)

#链接类
class Conn:
    def __init__(self,name):
        self.name = name

class Pool:
    def __init__(self,count:int):
        self.count = count
        #池中放着链接备用
        self.pool = [self._connect("conn-{}".format(i)) for i in range(count)]
        self.bsemaphore = BoundedSemaphore(count)

    #创建连接方法，返回一个连接对象
    def _connect(self,conn_name):
        return Conn(conn_name)

    #获取一个链接
    def get_conn(self):
        self.bsemaphore.acquire()
        self.pool.pop()
        logging.info("从连接池拿走了一个连接~~~~~~~")

    #归还一个连接
    def return_conn(self,conn:Conn):
        logging.info("归还了一个连接----------")
        self.pool.append(conn)
        self.bsemaphore.release()

def worker(pool:Pool):
    conn = pool.get_conn()
    logging.info(conn)
    #模拟使用了一段时间
    time.sleep(random.randint(1,5))
    pool.return_conn(conn)

pool = Pool(3)
for i in range(6):
    Thread(target=worker,name="worker-{}".format(i),args=(pool,)).start()