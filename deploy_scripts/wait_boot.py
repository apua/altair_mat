from common import *

from altair import wait_boot

if len(sys.argv)==2:
    ip = sys.argv[1]
    wait_boot(ip)
else:
    print('usage: wait_boot.py ip')
