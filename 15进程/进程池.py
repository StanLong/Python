# 获取计算机核数
# from multiprocessing import cpu_count
# print(cpu_count())

# 进程池
from multiprocessing import Pool
import time
import os

def func(i):
    print(i, os.getpid())
    time.sleep(1)

def func_async(i):
    time.sleep(1)
    return i


if __name__ == '__main__':
    # p = Pool(5)
    # p.map(func, range(20)) # 开5个进程执行 func

    # apply 同步提交任务
    # p = Pool(5)
    # for i in range(20):
    #     p.apply(func, args=(i, )) # apply 同步提交任务

    # apply_async 异步提交任务
    # p = Pool(5)
    # for i in range(20):
    #     p.apply_async(func, args=(i,)) # apply_async 异步提交任务
    # p.close() # close 必须加在join之前，不允许再添加新的任务了
    # p.join() # 等待子进程结束再往下执行

    # 异步提交任务接收返回结果
    p = Pool(5)
    for i in range(20):
        result = p.apply_async(func_async, args=(i,)) # apply_async 异步提交任务
        print(result.get()) # result.get() 发生
        # 阻塞，等待任务结果, 现象为同步
    p.close() # close 必须加在join之前，不允许再添加新的任务了
    p.join() # 等待子进程结束再往下执行
