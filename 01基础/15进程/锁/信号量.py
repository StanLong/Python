# 信号量
# Semaphore  n.	信号标; 旗语;

# 模拟10个人上卫生间，但是卫生间只有四个坑
from multiprocessing import Semaphore
from multiprocessing import Process
import random
import time

def toilet(name, sem):
    sem.acquire()
    print('%s : 进入卫生间' %name)
    time.sleep(random.randint(1,10))
    print('%s : 离开卫生间' %name)
    sem.release()

if __name__ == '__main__':
    sem = Semaphore(4)
    for name in ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']:
        process = Process(target=toilet, args=(name, sem))
        process.start()