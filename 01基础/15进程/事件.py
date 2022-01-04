# 事件
# from multiprocessing import Event
# e = Event()
# e.wait() 阻塞进程，刚实例化出来的对象默认就是阻塞进程
# e.set()  非阻塞进程
# e.clear() 将非阻塞进程变成阻塞进程
# e.is_set() 是否阻塞，True：非阻塞，False：阻塞

# 做一个红绿灯的例子
from multiprocessing import Event
from multiprocessing import Process
import time

def traffic_light(e):
    while True:
        if e.is_set():
           time.sleep(3)
           print('红灯亮')
           e.clear()
        else:
            time.sleep(3)
            print('绿灯亮')
            e.set()

def car(name, e):
    e.wait()
    print('%s车通过' %name)

if __name__ == '__main__':
    e = Event()
    p_tl = Process(target=traffic_light, args=(e,))
    p_tl.start() # 启动一个进程来控制红绿灯
    for name in ['奔驰', '宝马', '保时捷', '玛莎拉蒂', '法拉利', '劳斯莱斯', '特斯拉', '奇瑞', '悍马', '猛士']:
        time.sleep(1)
        p_car = Process(target=car, args=(name, e))
        p_car.start()