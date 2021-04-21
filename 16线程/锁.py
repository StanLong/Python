# 线程锁
# 保证线程安全

# 互斥锁
import threading
import time

counter = 0
lock = threading.Lock()

class LockThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self) -> None:
        global counter, lock
        time.sleep(1)
        if lock.acquire():
            counter = counter + 1
            print("I am %s, set counter %s" %(threading.Thread.getName(self), counter))
            lock.release()

if __name__ == '__main__':
    for i in range(20):
        lt = LockThread()
        lt.start()
    time.sleep(1)


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