# 生产者消费者模型
    # 解决数据的供需不平衡

# 模拟Kafka的降峰
# from multiprocessing import Queue
# from multiprocessing import Process
# import time
# def producer(q): # 生产者
#     for data_log in range(50):
#         q.put("数据日志_%s" %data_log)
#         print("生产者生产了数据日志_%s" %data_log)
#
# def consumer(q): # 消费者
#     for data_log in range(50):
#         time.sleep(1)    # 降峰
#         print('消费者消费了' + q.get(data_log))
#
# # 一个生产者，两个消费者
# if __name__ == '__main__':
#     q = Queue(10) # 生成一个长度为10的队列
#     p_producer = Process(target=producer, args=(q, ))
#     p_producer.start()
#     p_consumer1 = Process(target=consumer, args=(q, ))
#     p_consumer1.start()
#     p_consumer2 = Process(target=consumer, args=(q,)) # 增加消费者或者生产者来调节效率
#     p_consumer2.start()


# 生产者生产的数据全部被消费--》生产者进程结束--》主进程代码执行结束--》消费者守护进程结束
# from multiprocessing import JoinableQueue
# from multiprocessing import Process
# import time
# import random
#
# def producer(q, name): # 生产者
#     for data_log in range(10):
#         q.put("%s_业务数据日志_%s" %(name, data_log))
#         print("%s_业务产生数据日志_%s" %(name, data_log))
#         time.sleep(random.randint(1,3))
#     q.join() # 等待消费者把所有的数据都处理完
#
# def consumer(q): # 消费者
#     while True:
#         print('kafka消费' + q.get())
#         q.task_done() # 数据消费结束
#
# # 多个生产者，多个消费者
# if __name__ == '__main__':
#     q = JoinableQueue() # 生成一个长度为10的队列
#     p_producer1 = Process(target=producer, args=(q, '阅读'))
#     p_producer1.start()
#     p_producer2 = Process(target=producer, args=(q, '视频'))
#     p_producer2.start()
#
#     p_consumer1 = Process(target=consumer, args=(q, ))
#     p_consumer1.daemon = True
#     p_consumer1.start()
#
#     p_consumer2 = Process(target=consumer, args=(q,))
#     p_consumer2.daemon = True
#     p_consumer2.start()
#
#     p_producer1.join() # 等待 p_producer1 生产结束
#     p_producer2.join() # 等待 p_producer2 生产结束