__import__('sys').path.append('../common/')

from altair.api import Altair
from altair.utils import get_config, set_config

settings = get_config('settings.txt')
login_information = settings['login_information']
appliance_ip  = login_information['appliance_ip']
username      = login_information['username']
password      = login_information['password']
cust_filepath = settings['cust_filepath']

try:
    get_config(cust_filepath)
    mesg = '"{}" already exists, replace it? (Y/N) '.format(cust_filepath)
    if raw_input(mesg).lower()[0]!='y':
        print('Stop to export customized OSBPs')
        raw_input('Press any key to continue...')
        exit()
except IOError:
    pass

with Altair(appliance_ip, username, password) as api:
    cust_info = api.export_custom_osbps()
    #cust_info = api.export_custom_osbps(interval=1)
    set_config(cust_info, cust_filepath)

raw_input('Press any key to continue...')
