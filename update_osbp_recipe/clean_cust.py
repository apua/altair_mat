from pprint import pprint
import json
import os
import sys
import time

sys.path.append('../common/')


from altair import Altair
from utils import get_config, set_config


settings = get_config('settings.txt')

appliance_ip = settings['appliance_ip']
username = settings['username']
password = settings['password']


def delete_cust(list_method, delete_method):
    for m in list_method()['members']:
        if m['isCustomerContent']:
            print(m['uri'], m['name'])
            delete_method(m['uri'].rsplit('/',1)[-1])
            print('...deleted successfully')
            time.sleep(3)


with Altair(appliance_ip=appliance_ip, username=username, password=password) as api:
    L = (
        (api._list_OSBP, api._delete_OSBP),
        (api._list_ogfsScript, api._delete_ogfsScript),
        (api._list_serverScript, api._delete_serverScript),
        (api._list_cfgfile, api._delete_cfgfile)
        )

    for lm, dm in L:
        delete_cust(lm, dm)


raw_input('Press any key to continue...')
