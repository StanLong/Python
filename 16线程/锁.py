# from threading import  Thread
# from threading import Lock
# import time
# def func():
#     # 锁没起作用
#     # global n
#     # time.sleep(0.01)
#     # lock.acquire()
#     # n = n -1
#     # lock.release()
#
#     # 锁也没起作用
#     global n
#     time.sleep(0.01)
#     lock.acquire()
#     temp= n
#     time.sleep(0.01)
#     n = temp -1
#     lock.release()
#
# n = 100
# t_list = []
# lock = Lock()
# for i in range(90):
#     t = Thread(target=func)
#     t.start()
#     t_list.append(t)
# [t.join() for i in t_list]
# print(n)