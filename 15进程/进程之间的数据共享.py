# Manager 提供了进程之间可以进行数据共享的机制
from multiprocessing import Manager
from multiprocessing import Process
import time
import os

def func(dic):
    while True:
        dic['count'] = dic['count'] -1
        print(dic, os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    # m = Manager()
    # d = m.dict()
    # print(d)
    # d['name'] = 'stanlong'
    # print(d)

    m = Manager()
    dic = m.dict()
    dic['count'] = 100
    lst = []
    for i in range(10):
        p = Process(target=func, args=(dic, ))
        p.start()
        p.join()
