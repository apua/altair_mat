'''
usage: command appliance_ip [config_path]
'''

import getpass
import os
import sys

from altair import Altair
from tools import set_config


if   len(sys.argv)==2:
    appliance_ip = sys.argv[1]
    config_path = os.path.join(os.path.dirname(__file__), 'settings.cfg')
elif len(sys.argv)==3:
    appliance_ip = sys.argv[1]
    config_path = sys.argv[2]
else:
    exit(__doc__.strip())


if os.path.isfile(config_path):
    templ = '"%s" exists. Recover it? [Y/n]'
    choice = raw_input(templ % config_path).lower()[0]
    if choice == 'n':
        exit(2)


username = 'administrator'
password = getpass.getpass('Administrator`s Password: ')

with Altair(appliance_ip=appliance_ip,
            username=username,
            password=password) as api:

    config = {
        'media settings': api.get_media_settings(),
        'product keys': api.get_product_keys(),
        'facility attributes': api.get_facility_attributes(),
        'activation key': api.get_activation_key(),
        'pxeboot default': api.get_pxeboot_default(),
        'network settings': api.get_network_settings(),
        }

    users = api.get_users()
    config['login user'] = next(user for user in users if user['userName'].lower()==username)
    config['other users'] = [user for user in users if user['userName'].lower()!=username]

# OSBPs

# WinPE

# hypervisor
#config['hypervisor'] = {
#    'host_ip': '',
#    'username': '',
#    'password': '',
#    }

set_config(config, config_path)
