# 管道
    # 双向通信
    # 如果管道的端点没有被使用，那就应该关闭管道的端点。如在生产者消费者模型中，生产者要关闭管道的输出端，消费者要关闭管道的输入端
    # 如果没有执行关闭操作，程序可能在消费者中的 recv() 操作上挂起
    # 管道用在进程之间会发生数据冲突的情况，数据不安全
    # 在主进程中关闭管道不会影响管道在子进程中的使用
# 队列=管道+锁
from multiprocessing import Pipe
from multiprocessing import Process

def func(p):
    father, son = p
    #father.close()
    print(son.recv())
    print(son.recv())

if __name__ == '__main__':
    father, son = Pipe()
    p = Process(target=func, args=((father, son),))
    p.start()
    father.send('hello')
    father.close()
