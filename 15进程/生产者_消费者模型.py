# 生产者消费者模型
    # 解决数据的供需不平衡
# 模拟Kafka的降峰

from multiprocessing import Queue
from multiprocessing import Process
import time
def producer(q): # 生产者
    for data_log in range(100):
        q.put("数据日志_%s" %data_log)

def consumer(q): # 消费者
    for data_log in range(100):
        time.sleep(1)
        print(q.get(data_log))

if __name__ == '__main__':
    q = Queue(10) # 生成一个长度为10的队列
    p_producer = Process(target=producer, args=(q, ))
    p_producer.start()
    p_consumer1 = Process(target=consumer, args=(q, ))
    p_consumer1.start()
    p_consumer2 = Process(target=consumer, args=(q,)) # 增加消费者或者生产者来调节效率
    p_consumer2.start()