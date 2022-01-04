# 定时器
# threading.Timer继承自Thread,这个类用来定义延迟多久后执行一个函数
# Timer.cancel()	取消定时器，(定时器为执行函数时可以取消，在函数执行中无法取消)
# Time.start()	启动定时器

# start方法执行之后，Timer对象会处于等待状态，等待了interval秒之后，开始执行function函数的。
# Timer是线程Thread的子类，Timer实例内部提供了一个ﬁnished属性，该属性是Event对象。
# cancel方法，本质上 是在worker函数执行前对ﬁnished属性set方法操作，从而跳过了worker函数执行，达到了取消的效果

from threading import Timer
import logging
import time

logging.basicConfig(format="%(asctime)s %(threadName)s %(thread)s %(message)s",level=logging.INFO)

def worker():
    logging.info("in worker")
    time.sleep(5)
    logging.info("end in worker")

t = Timer(2,worker)
t.setName("timer1") #设置线程名称
# t.cancel() #取消定时器后，定时器不在执行
t.start()
# t.cancel() #取消定时器后，定时器不在执行
time.sleep(3) #等待3秒后，定时器已经开始执行 # in worker打印过后一秒打印 ======end========
t.cancel() #当定时器执行后，无法取消

print("======end========")