# -*- coding:utf-8 -*-

import os
import sys

BaseDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)
from  Core.CCore import Connect


client=Connect()
client.startlink()