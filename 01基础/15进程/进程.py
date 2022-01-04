import os
from multiprocessing import Process

# def func():
#     print('子进程', os.getpid())
#     print('父进程', os.getppid())
#     print('123')
#
# if __name__ == '__main__':
#     p = Process(target=func) # 创建一个进程对象
#     print('主进程', os.getpid())
#     p.start()                # 开启一个进程, 进程是异步执行的
#     print('主进程', os.getpid())

# 主进程 3856
# 主进程 3856
# 子进程 3452
# 父进程 3856
# 123


# def func(money):
#     print('money: %d' %money)
#
# if __name__ == '__main__':
#     p = Process(target=func, args=(100,)) # 进程传参，参数必须是一个元组类型
#     p.start()                # 开启一个进程, 进程是异步执行的
# money: 100


# def func(money):
#     print('money: %d' %money)
#
# if __name__ == '__main__':
#     p = Process(target=func, args=(100,)) # 进程传参，参数必须是一个元组类型
#     p.start()                # 开启一个进程, 进程是异步执行的
#     p.join()                 # 开启一个阻塞，子进程执行完毕后才会继续往下执行
#     print('取完钱了')
#
# money: 100
# 取完钱了


# 开启多个子进程
# def func():
#     print('子进程: ', os.getpid(), '父进程', os.getppid())
#
# if __name__ == '__main__':
#     p1 = Process(target=func) # 进程传参，参数必须是一个元组类型
#     p2 = Process(target=func)  # 进程传参，参数必须是一个元组类型
#     p1.start()                # 开启第一个进程
#     p2.start()                # 开启第二个进程
#     print('主进程', os.getpid())
# 主进程 8680
# 子进程:  7344 父进程 8680
# 子进程:  1084 父进程 8680


# 循环开启进程
# def func():
#     print('子进程: ', os.getpid(), '父进程', os.getppid())
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(10):
#         p = Process(target=func)
#         p.start()
#         p_list.append(p)
#     for p in p_list:   # 多个子进程阻塞
#         p.join()
#     print('主进程', os.getpid())

# 数据隔离
# 进程与进程之间数据是隔离的
# n = 10
# def func():
#     global n
#     n = n -1
#     print(n)
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=func)
#         p.start()
#         # p.join()
#     print('主进程', os.getpid())
# 主进程 6876
# 9
# 9
# 9
# 9
# 9
# 9
# 9
# 9
# 9
# 9




# 使用类继承方式创建进程
#   这个类必须继承 Process
#   必须实现 run 方法

# class MyProcess(Process):
#     def run(self) -> None:
#         print('子进程: ', os.getpid(), '父进程', os.getppid())
#
# if __name__ == '__main__':
#     p = MyProcess()
#     p.start()   # start 默认调用run方法
#     print('主进程', os.getpid())

# 主进程 1920
# 子进程:  980 父进程 1920

# 使用类继承方式创建进程，传参
class MyProcess(Process):
    def __init__(self, arg1, arg2, arg3):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def run(self) -> None:
        print('子进程: ', os.getpid(), '父进程', os.getppid(), self.arg1, self.arg2, self.arg3)
        self.walk(1) # walk 方法在子进程中调用

    @staticmethod
    def walk(self):
        print('walk 方法', os.getpid())

if __name__ == '__main__':
    p = MyProcess(1,2,3)
    p.start()   # start 默认调用run方法
    # p.walk(1)   # walk 方法在主进程中调用
    print('主进程', os.getpid())

# walk 方法 7596
# 主进程 7596
# 子进程:  3328 父进程 7596 1 2 3


# 进程的其他方法
# p.terminate()
# p.pid
# p.is_alive()