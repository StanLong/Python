# 锁, 在并发编程中保证数据安全
# 模拟抢票

from multiprocessing import Lock
from multiprocessing import Process
import json
import time
import random

# 查询余票
def search(name):
    with open('ticket.txt', 'r', encoding='utf-8') as f_r:
        print('%s 查询剩余票数 %s' %(name, json.load(f_r)['count']))

# 购票
def get(name):
    with open('ticket.txt', 'r', encoding='utf-8') as f_r:
        ticket_count = json.load(f_r)['count']
    time.sleep(random.random()) # 模拟网络延迟
    if ticket_count > 0:
        with open('ticket.txt', 'w', encoding='utf-8') as f_w:
            json.dump({'count':ticket_count-1}, f_w)
        print('%s买到票了' %name)
    else:
        print('没票了')


def task(name, lock):
    search(name)
    lock.acquire()
    get(name)  # 给购票函数加锁，当一个进程购票时，其他进程等待
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for name in ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']:
        p = Process(target=task, args=(name, lock))
        p.start()