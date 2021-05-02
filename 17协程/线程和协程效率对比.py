from gevent import monkey;monkey.patch_all()
import time
import gevent

def task(args):
    time.sleep(1)
    print(args)

def sync_func():
    for i in range(10):
        task(i)

def async_func():
    g_l = []
    for i in range(10):
        g_l.append(gevent.spawn(task, i))
    gevent.joinall(g_l)

start_time = time.time()
sync_func()
print("线程消耗时间:%f" %(time.time()-start_time))
# 线程消耗时间:10.013833


start_time = time.time()
async_func()
print("协程消耗时间:%f" %(time.time()-start_time))
# 协程消耗时间:1.003006

# 在有I/O的情况下，协程的效率比线程高很多

# 爬取网页效率对比
# import requests
# import gevent
# import time
# # from gevent import monkey;monkey.patch_all()
#
# # 爬取网页
# url_list = [
#     "http://www.baidu.com",
#     "http://www.python.org",
#     "http://www.cnblogs.com",
#     "http://www.mi.com",
#     "http://www.apache.org"
# ]
#
# def get_url(url):
#     result = requests.get(url)
#     print(url, result.status_code, len(result.text))
#
# def sync_func():
#     for url in url_list:
#         get_url(url)
#
# def async_func():
#     g_l = []
#     for url in url_list:
#         g = gevent.spawn(get_url, url)
#         g_l.append(g)
#     gevent.joinall(g_l)
#
#
# start_time = time.time()
# sync_func()
# print("线程消耗时间:%f" %(time.time()-start_time))
# # 线程消耗时间:10.013833


start_time = time.time()
async_func()
print("协程消耗时间:%f" %(time.time()-start_time))


