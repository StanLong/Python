# 守护线程
import time
import threading
def func():
    print("开始执行子进程 %s" %threading.currentThread().getName())
    time.sleep(1)
    print("子进程执行结束 %s" %threading.currentThread().getName())

t1 = threading.Thread(target=func)
t1.setDaemon(True)
t1.start()

t2 = threading.Thread(target=func)
t2.start()
t2.join()


