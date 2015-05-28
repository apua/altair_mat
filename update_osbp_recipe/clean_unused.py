__import__('sys').path.append('../common/')

from common import *

from altair import Altair
from utils import get_config, set_config

settings = get_config('settings.txt')
appliance_ip  = settings['appliance_ip']
username      = settings['username']
password      = settings['password']
cust_filepath = settings['cust_filepath']

def get_uri_mapping(self):
    uri_mapping = {}
    for cate in ('osdscript', 'osdcfgfile', 'osdzip'):
        for member in self._list_index({'category': cate})['members']:
            uri_mapping[member['name']] = member['uri']
    return uri_mapping

def find_cust_scrpit(self):
    return {m['name']:m['uri'] for m in self._list_index({'category': 'osdscript'})['members']
                               if m['attributes']['osdCustomerContent']=='true'}

def find_cust_config(self):
    return {m['name']:m['uri'] for m in self._list_cfgfile()['members']
                               if m['isCustomerContent']}
            

with Altair(appliance_ip, username, password) as api:
    cust_info = api.get_cust_info()
    #p(get_uri_mapping(api)
    #p(find_cust_scrpit(api))
    #p(find_cust_config(api))
    cust_scripts = find_cust_scrpit(api)
    cust_configs = find_cust_config(api)
    cust_script_names = cust_scripts.keys()
    cust_config_names = cust_configs.keys()

    # just double check
    assert set(cust_config_names).issuperset(cust_info['config'].keys())
    assert set(cust_script_names).issuperset(cust_info['serverScript'].keys()+ cust_info['ogfsScript'].keys())
    
    # compute diff
    r_config_names = set(cust_config_names) - cust_info['config'].viewkeys()
    r_script_names = set(cust_script_names) - cust_info['serverScript'].viewkeys() - cust_info['ogfsScript'].viewkeys()
    p(r_config_names)
    p(r_script_names)

    # clean
    print('====> Start clean unused config')
    for name in r_config_names:
        print('delete', name)
        api._delete_cfgfile(uri=cust_configs[name])
    print('====> Start clean unused script')
    for name in r_script_names:
        print('delete', name)
        uri = cust_scripts[name]
        (api._delete_serverScript if 'server-script' in uri else api._delete_ogfsScript)(uri=uri)

raw_input('Press any key to continue...')

