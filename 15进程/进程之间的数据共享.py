# Manager 提供了可以进行数据共享的机制
from multiprocessing import Manager
from multiprocessing import Process
import time

def func(dic):
    while True:
        print(dic)
        dic['name'] = '沈万三'
        time.sleep(3)


if __name__ == '__main__':
    # m = Manager()
    # d = m.dict()
    # print(d)
    # d['name'] = 'stanlong'
    # print(d)

    m = Manager()
    dic = m.dict()
    dic['name'] = 'stanlong'
    p = Process(target=func, args=(dic, ))
    p.start()
    p.join()
