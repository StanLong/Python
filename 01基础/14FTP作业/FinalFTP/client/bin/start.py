
import os
import sys

BaseDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)
from  core.ccore import Connect

if __name__ == '__main__':
    client=Connect()
    client.startlink()