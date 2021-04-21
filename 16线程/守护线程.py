# 守护线程
# 守护线程，程序结束时，线程跟着结束

import threading
import time
import sys

def install():
    print("开始安装")
    time.sleep(10)
    print()
    print("安装完成")

def until():
    while True:
        sys.stdout.write("###")
        time.sleep(0.5)
        sys.stdout.flush()

t_install = threading.Thread(target=install)
t_install.start()
time.sleep(0.01)
t_until = threading.Thread(target=until, daemon=True) # 开启守护线程
t_until.start()