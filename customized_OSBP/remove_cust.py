'''
issues:
    #. using `api._list_index({'category': '...'})` is faster,
       but no `isCustomerContent` field,
       needs to know where is the end index of builtins
    #. delete methods are the same when using uri but id
'''

from altair import Altair
from tools import set_config

from pprint import pprint
import json
import os
import sys

p = lambda v: pprint(v, depth=1)

if len(sys.argv)!=4:
    sys.exit('usage: cmd appliance_ip username password')
else:
    appliance_ip, username, password = sys.argv[1:]


def delete_cust(list_method, delete_method):
    for m in list_method()['members']:
        if m['isCustomerContent']:
            print(m['uri'], m['name'])
            delete_method(m['uri'].rsplit('/',1)[-1])


with Altair(appliance_ip=appliance_ip, username=username, password=password) as api:
    L = (
        (api._list_OSBP, api._delete_OSBP),
        (api._list_ogfsScript, api._delete_ogfsScript),
        (api._list_serverScript, api._delete_serverScript),
        (api._list_cfgfile, api._delete_cfgfile)
        )
    
    for lm, dm in L:
        delete_cust(lm, dm)
    

