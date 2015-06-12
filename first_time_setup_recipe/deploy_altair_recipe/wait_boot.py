from common import *


if len(sys.argv)==2:
    ip = sys.argv[1]
    A.wait_boot(ip)
else:
    exit('usage: wait_boot.py ip')
