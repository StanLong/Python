# -*- coding:utf-8 -*-


import sys,os,json
#目录为MiniFTP\Miniserver
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)

from Core.ACore import Manager


if __name__=="__main__":
    StartLink=Manager()
    StartLink.link_server()