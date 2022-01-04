# 队列

# from multiprocessing import Queue
# q = Queue() 实例化一个队列， 可在实例化队列的时候指定队列的长度。如实例化一个长度为3的队列 q=Quene(3)
# q.put()  # 往队列中放一个元素， 如果队列已满再put元素，队列会阻塞
# q.get()  # 从队列中取出一个元素， 如果队列已空再get元素，队列会阻塞
# q.qsize() # 队列大小

# 通过队列实现进程通信

from multiprocessing import Process
from multiprocessing import Queue

def q_put(q):
    q.put('hello')

def q_get(q):
    print(q.get())

if __name__ == '__main__':
    q = Queue()
    p_put = Process(target=q_put, args=(q, ))
    p_put.start()
    p_get = Process(target=q_get, args=(q, ))
    p_get.start()
