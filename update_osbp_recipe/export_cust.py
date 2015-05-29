__import__('sys').path.append('../common/')

from altair import Altair
from utils import get_config, set_config

settings = get_config('settings.txt')
appliance_ip  = settings['appliance_ip']
username      = settings['username']
password      = settings['password']
cust_filepath = settings['cust_filepath']

with Altair(appliance_ip, username, password) as api:
    cust_info = api.export_cust_info()
    #cust_info = api.export_cust_info(interval=1)
    set_config(cust_info, cust_filepath)

raw_input('Press any key to continue...')
