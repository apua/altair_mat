__import__('sys').path.append('../common/')

from pprint import pformat

from altair.api import Altair
from altair.utils import get_config, set_config

variables_file = 'settings.py'
config_file = 'settings.txt'

settings = get_config(config_file)
basic_information = settings['basic_information']
appliance_ip  = basic_information['appliance_ip']
username      = basic_information['username']
password      = basic_information['password']

with Altair(appliance_ip, username, password) as api:
    api.setup()
    api.set_network(settings['network_setting'])
