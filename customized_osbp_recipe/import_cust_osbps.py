__import__('sys').path.append('../common/')

from altair.api import Altair
from altair.utils import get_config, set_config

settings = get_config('settings.txt')
appliance_ip  = settings['appliance_ip']
username      = settings['username']
password      = settings['password']
cust_filepath = settings['cust_filepath']

with Altair(appliance_ip, username, password) as api:
    api.import_custom_osbps(cust_filepath))

raw_input('Press any key to continue...')
