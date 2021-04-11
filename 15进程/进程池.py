# 获取计算机核数
# from multiprocessing import cpu_count
# print(cpu_count())

# 进程池
# from multiprocessing import Pool
# import time
# import os

# def func(i):
#     print(i, os.getpid())
#     time.sleep(1)
#
# def func_async(i):
#     time.sleep(1)
#     return i

# if __name__ == '__main__':
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
    # p = Pool(5)
    # lst = []
    # for i in range(20):
    #     result = p.apply_async(func_async, args=(i,)) # apply_async 异步提交任务
    #     # print(result.get()) # result.get() 阻塞
    #     # 阻塞，等待任务结果, 现象为同步
    #     lst.append(result)
    # p.close() # close 必须加在join之前，不允许再添加新的任务了
    # p.join() # 等待子进程结束再往下执行
    # [print(res.get()) for res in lst] # 异步调用获取函数的返回值


# 回调函数
# def func(i):
#     return i * '*'
#
# def call(arg): # 回调函数是在主进程中完成的，不能传参，只能接收多进程中函数的返回值
#     print(arg)
#
# if __name__ == '__main__':
#     p = Pool(5)
#     for i in range(10):
#         p.apply_async(func, args=(i,), callback=call)
#     p.close()
#     p.join()

# 回调函数练习
# 请求多个网页
from multiprocessing import Pool
import requests

def get_url(url):
    result = requests.get(url)
    return {
            'url':url,
            'status_code':result.status_code,
            'content':result.text
            }

def parser(dic):
    print(dic['url'], dic['status_code'], len(dic['content']))

if __name__ == '__main__':
    url_l = [
        'http://www.baidu.com',
        'http://www.sogou.com',
        'http://hao123.com',
        'http://python.org',
        'http://taobao.com'
    ]
    p = Pool(5)
    for url in url_l:
        p.apply_async(get_url, args=(url, ), callback=parser)
    p.close()
    p.join()