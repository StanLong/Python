# 守护进程
# 守护进程会随着主进程代码执行结束而结束
# 正常的子进程没有执行完的时候，主进程要一直等值
# 守护进程中不能再开启子进程

import time
from multiprocessing import Process

def cal_time():
    while True:
        time.sleep(1)
        print("过去了1秒")

if __name__ == '__main__':
    p = Process(target=cal_time)
    p.daemon = True # 开启守护进程，这行代码一定要写在 p.start() 之前
    p.start()
    for i in range(100): # 开启守护进程后，父进程执行完，子进程也跟着一起结束
        time.sleep(0.1)
        print('*' * i)