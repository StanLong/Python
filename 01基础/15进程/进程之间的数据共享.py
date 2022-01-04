# Manager 提供了多进程之间的通信机制，多个进程可以共享同一块内存
# Manager支持的类型有
# list,dict,Namespace,Lock,RLock,Semaphore,BoundedSemaphore,Condition,Event,Queue,Value和Array


from multiprocessing import Manager
from multiprocessing import Process
import time
from multiprocessing import Lock

# 使用 Manager 创建一个字典
# if __name__ == '__main__':
#     m = Manager()
#     d = m.dict()
#     d['count']=100
#     print(d)

# 验证manager是否共享内存
# def func(dic):
#     dic['count'] = dic['count']-1
#     print(dic)

# 多进程统一join, 为了数据安全加锁
def func(dic, lock):
    lock.acquire()
    dic['count'] = dic['count']-1
    lock.release()

if __name__ == '__main__':
    # 验证manager是否共享内存
    # dic={'count':100}
    # for i in range(100):
    #     p = Process(target=func, args=(dic, ))
    #     p.start()
    #     p.join()
    # 输出结果 {'count': 99}

    # 使用Manager共享内存
    # m = Manager()
    # dic = m.dict()
    # dic['count']=100
    # for i in range(100):
    #     p = Process(target=func, args=(dic, ))
    #     p.start()
    #     p.join()
    # 打印结果， count值递减

    # 多进程异步访问字典，最后统一join
    lock = Lock() # 加锁保证数据安全
    m = Manager()
    dic = m.dict()
    dic['count']=100
    lst = []
    for i in range(100):
        p = Process(target=func, args=(dic, lock))
        p.start()
        lst.append(p)
    [p.join() for p in lst]
    print(dic)
