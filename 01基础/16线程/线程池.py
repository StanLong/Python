# 用来做池（进程池，线程池）操作的新模块
# from concurrent import futures
# futures.ThreadPoolExecutor # 线程池
# futures.ProcessPoolExecutor # 进程池


# from concurrent import futures
# import time
# import random
# def func(n):
#     time.sleep(random.randint(1,3))
#     print(n)
# # 线程池线程的个数：CPU个数 * 5
# thread_pool = futures.ThreadPoolExecutor(5)
# for i in range(10):
#     thread_pool.submit(func, i) # submit 合并了创建线程对象和start的功能

# 返回值
# from concurrent import futures
# import time
# import random
# def func(n):
#     time.sleep(random.randint(1,3))
#     print(n)
#     return n * '*'
# # 线程池线程的个数：CPU个数 * 5
# thread_pool = futures.ThreadPoolExecutor(5)
# for i in range(10):
#     tp = thread_pool.submit(func, i) # submit 合并了创建线程对象和start的功能
#     print(tp.result()) # 同步

# shutdown
# from concurrent import futures
# import time
# import random
# def func(n):
#     time.sleep(random.randint(1,3))
#     print(n)
#     return n * '*'
# # 线程池线程的个数：CPU个数 * 5
# thread_pool = futures.ThreadPoolExecutor(5)
#
# for i in range(10):
#     tp = thread_pool.submit(func, i) # submit 合并了创建线程对象和start的功能
#     print(tp.result())
# thread_pool.shutdown()  # shutdown合并了 close() join()


# map
# from concurrent import futures
# import time
# import random
# def func(n):
#     time.sleep(random.randint(1,3))
#     print(n)
#     return n * '*'
# # 线程池线程的个数：CPU个数 * 5
# thread_pool = futures.ThreadPoolExecutor(5)
# thread_pool.map(func, range(10)) # map 异步，接受可迭代对象的数据，不支持返回值

# 回调函数
from concurrent import futures
import time
import random
def func(n):
    time.sleep(random.randint(1,3))
    print(n)
    return n * '*'

def call(args):
    print(args.result())
# 线程池线程的个数：CPU个数 * 5
thread_pool = futures.ThreadPoolExecutor(5)

thread_pool.submit(func, 1).add_done_callback(call)
