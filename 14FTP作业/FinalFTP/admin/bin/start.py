import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core.acore import Manager

'''
# 管理端入口程序
'''
if __name__ == '__main__':
    StartLink = Manager()
    StartLink.link_server()