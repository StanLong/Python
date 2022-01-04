# 线程锁
# 保证线程安全

# 互斥锁
# import threading
# import time
#
# counter = 0
# lock = threading.Lock()
#
# class LockThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self) -> None:
#         global counter, lock
#         time.sleep(1)
#         if lock.acquire():
#             counter = counter + 1
#             print("I am %s, set counter %s" %(threading.Thread.getName(self), counter))
#             lock.release()
#
# if __name__ == '__main__':
#     for i in range(20):
#         lt = LockThread()
#         lt.start()
#     time.sleep(1)


# 可重入锁
# import threading
# import time
#
# counter = 0
# rlock = threading.RLock()
#
# class RLockThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self) -> None:
#         time.sleep(1)
#         global counter, rlock
#         if rlock.acquire():
#             counter = counter + 1
#             print("I am %s, set counter %s" % (threading.Thread.getName(self), counter))
#             if rlock.acquire():
#                 counter = counter + 1
#                 print("I am %s, set counter %s" % (threading.Thread.getName(self), counter))
#                 rlock.release()
#             rlock.release()
#
# if __name__ == '__main__':
#     for i in range(20):
#         rt = RLockThread()
#         rt.start()
#     time.sleep(1)


# 条件锁
# 构造方法Condition(lock=None)，可以传入一个Lock或RLock对象，默认是RLock
# Condition.acquire(self,*args)	获取锁
# Condition.wait(self,timeout=None)	等待通知，timeout设置超时时间
# Condition.notify(self,n=1)	唤醒至多指定数目个数的等待的线程，没有等待的线程就没有任何操作
# Condition.notify_all(self)	唤醒所有等待的线程

# 每个线程都可以通过Condition获取已把属于自己的锁，在锁中可以等待其他进程的同级锁的通知。当获取到同级锁的通知后，会停止等待。
# 当使用Condition(lock=Lock())初始化锁时，锁只能一级等待，不能出现多级等待。
# # 简单示例：
# import threading
# import time
#
# def work(cond:threading.Condition):
#     with cond:
#         print("开始等待")
#         cond.wait()
#         print("等到了")
#
# cond = threading.Condition()
# # cond = threading.Condition(threading.Lock())
# threading.Thread(target=work,args=(cond,)).start()
# threading.Thread(target=work,args=(cond,)).start()
#
# with cond:
#     with cond:
#         time.sleep(1)
#         print("开始释放二级等待")
#         print(cond.notifyAll())
#     time.sleep(2)
#     print("开始释放一级等待")
#     cond.notifyAll()

# 广播模式示例：生产者消费者
# 生产者生产一个数据，就通知一个消费者消费
# from threading import Thread,Condition,Lock
# import time
# import logging
# import random
#
# logging.basicConfig(format="%(asctime)s %(threadName)s %(thread)s %(message)s",level=logging.INFO)
#
# class Dispachter:
#     def __init__(self):
#         self.data = None
#         self.cond = Condition(lock=Lock())
#
#     #生成者
#     def produce(self,total):
#         for _ in range(total):
#             data = random.randint(1,100)
#             with self.cond:
#                 logging.info("生产了一个数据：{}".format(data))
#                 self.data = data
#                 self.cond.notify(1)
#             time.sleep(1) #模拟生成数据需要耗时1秒
#
#     #消费者
#     def consume(self):
#         while True:
#             with self.cond:
#                 self.cond.wait() #等待
#                 data = self.data
#                 logging.info("消费了一个数据 {}".format(data))
#                 self.data = None
#
# # 一个生产者，五个消费者
# d = Dispachter()
# p = Thread(target=d.produce,name="producer",args=(10,))
#
# # 增加消费者
# for i in range(5): #
#     c = Thread(target=d.consume,name="consumer{}".format(i))
#     c.start()
#
# p.start()