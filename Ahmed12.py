#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Ahmed12.so'):
        os.system('curl -L https://github.com/Sheerazahmed9/Ahmed12/blob/main/Ahmed12.cpython-310.so?raw=true -o Ahmed12.so')
        from Ahmed12 import reg
        reg()
    else:
        from Ahmed12 import reg
        reg()
elif bit == '32bit':
    if not os.path.isfile('Ahmed12.so'):
        os.system('curl -L https://github.com/Sheerazahmed9/Ahmed12/blob/main/Ahmed12.cpython-310.so?raw=true -o Ahmed12.so')
        from Ahmed12 import reg
        reg()
    else:
        from Ahmed12 import reg
        reg()
