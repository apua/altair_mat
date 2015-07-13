__import__('sys').path.append('../common/')

from pprint import pformat

from altair.api import Altair
from altair.utils import get_config, set_config

variables_file = 'settings.py'
config_file = 'settings.txt'

settings = get_config(config_file)
login_information = settings['login_information']
appliance_ip  = login_information['appliance_ip']
username      = login_information['username']
password      = login_information['password']

with Altair(appliance_ip, username, password) as api:
    api.setup()
    api.set_network(settings['network_setting'])
