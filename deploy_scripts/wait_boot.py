from common import *


if len(sys.argv)==2:
    ip = sys.argv[1]
    A.wait_boot(ip)
else:
    print('usage: wait_boot.py ip')
