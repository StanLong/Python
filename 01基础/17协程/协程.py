# 对操作系统来说，线程是最小的执行单元，进程是最小的资源管理单元
# 协程，英文Coroutines，是一种比线程更加轻量级的存在。正如一个进程可以拥有多个线程一样，一个线程也可以拥有多个协程


# Greenlet是python的一个C扩展，来源于Stackless python，旨在提供可自行调度的‘微线程’， 即协程
# from greenlet import greenlet # 在单线程中切换状态的模块
#
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()

# 当创建一个greenlet时，首先初始化一个空的栈， switch到这个栈的时候，会运行在greenlet构造时传入的函数（首先在test1中打印 12），
# 如果在这个函数（test1）中switch到其他协程（到了test2 打印34），那么该协程会被挂起，等到切换回来（在test2中切换回来 打印34）。
# 当这个协程对应函数执行完毕，那么这个协程就变成dead状态

# Greenlet 不能节省IO事件，Gevent 可以

# Gevent是一个第三方库(需要额外自己安装)，可以轻松通过gevent实现并发同步或异步编程，
# 在gevent中主要用到的模式是Greenlet，它是以C扩展模块形式接入Python的轻量级协程。
# Greenlet全部运行在主程序操作系统的内部，被协作式调度
# 使用gevent库实现协程
import gevent
from gevent import monkey;monkey.patch_all() # 把出现的IO流打包成gevent能识别的I/O流
def func1():
    print("func1 running")
    gevent.sleep(2)  # 内部函数实现io操作
    print("switch func1")

def func2():
    print("func2 running")
    gevent.sleep(1)
    print("switch func2")

def func3():
    print("func3  running")
    gevent.sleep(0.5)
    print("func3 done..")

if __name__ == '__main__':
    gevent.joinall([gevent.spawn(func1),
                    gevent.spawn(func2),
                    gevent.spawn(func3),
                    ])