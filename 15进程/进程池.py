from multiprocessing import Pool
import time
import os

def func(i):
    i = i+1
    print(i, os.getpid())

if __name__ == '__main__':
    p = Pool(5)
    start_time = time.time()
    p.map(func, range(10))
    p.close() # 不允许向进程池中添加任务
    p.join()
    print('<===>')
    print(time.time() - start_time)