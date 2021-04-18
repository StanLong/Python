# 线程
# 开启线程的第一种方式
# from threading import Thread
# def func():
#     print("New Thread")
#
# t = Thread(target=func)
# t.start()


# 开启线程的第二种方式
# from threading import Thread
# import time
# import os
# class MyThread(Thread):
#     def run(self) -> None:
#        time.sleep(1)
#        print('Hello word %s' %os.getpid())
#
# t = MyThread()
# t.start()

# 统计线程数
# from threading import Thread
# import time
# class MyThread(Thread):
#     count = 0
#     def run(self) -> None:
#         MyThread.count = MyThread.count + 1
#         time.sleep(1)
#         # print('Hello word %s' %os.getpid())
#
# for i in range(10):
#     t = MyThread()
#     t.start()
# print(t.count)

# 传参
from threading import Thread
import time
import os

class MyThread(Thread):
    count = 0
    def __init__(self, arg1, arg2):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self) -> None:
        MyThread.count = MyThread.count + 1
        time.sleep(1)
        # print('Hello word %s' %os.getpid())
        print('%s, %s, hello world, %s'%(self.arg1, self.arg2, os.getpid()))

for i in range(10):
    t = MyThread(i, (i+1) * '*')
    t.start()
    t.join()

