# 事件
# Event事件，是线程间通信机制中最简单的实现，使用一个内部的标记flag,通过flag的True或False的变化 来进行操作
# event.set()	标记设置为True
# event.clear()	标记设置为False
# event.is_set()	标记是否为True
# event.wait(timeout=None)	设置等待标记为True的时长，None为无限等待。等到返回True,未等到超时了返回False

# 实例：老板雇佣了一个工人，让他生产杯子，老板一直等着这个工人，直到生产了10个杯子
# import threading
# import time
# import logging
#
# logging.basicConfig(format="%(asctime)s %(threadName)s %(thread)s %(message)s",level=logging.INFO)
#
# def worker(event:threading.Event,count = 10):
#     logging.info("我是worker工作线程")
#     cups = []
#     while True:
#         logging.info("制作了一个 cup")
#         time.sleep(0.2)
#         cups.append(1)
#         if len(cups)>=count:
#             event.set()
#             break
#     logging.info("制作完成：{}".format(cups))
#
# def boss(event:threading.Event):
#     logging.info("我是boss")
#     event.wait()
#     logging.info("Good Job")
#
# event = threading.Event()
# b = threading.Thread(target=boss,args=(event,))
# w = threading.Thread(target=worker,args=(event,))
# b.start()
# w.start()

# wait的使用
# 谁wait就是等到ﬂag变为True，或等到超时返回False。不限制等待的个数。

from threading import Thread,Event
import logging

logging.basicConfig(format="%(asctime)s %(threadName)s %(thread)s %(message)s",level=logging.INFO)

def worker(event:Event,interval:int):
    while not event.wait(interval):
        logging.info("没有等到。。")

e = Event()
Thread(target=worker,args=(e,1)).start()

e.wait(5)
e.set()

print("======end========")