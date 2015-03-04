import argparse

from altair import Altair
from tools import gen_path, set_config, subconfig2value

'''
usage: $CMD $APPLIANCE_IP $SETTINGS_FILENAME
ask administrator`s password
'''

settings = gen_path('settings.cfg', __file__)
username = 'administrator'

with Altair(appliance_ip=appliance_ip,
            username=username,
            password=password) as api:

    config = {
        'media settings': api.get_media_settings(),
        'product keys': api.get_product_keys(),
        'facility attributes': api.get_facility_attributes(),
        'activation key': api.get_activation_key(),
        'network settings': api.get_network_settings(),
        }

    users = api.get_users()
    other_users = ...
    login_user = ...
    login_user['other users'] = subconfig2value(other_users)
    config[username] = login_user

    # OSBPs
    # WinPE

config['hypervisor'] = {
    'ip': '',
    'username': '',
    'password': '',
    'vmname': '',
    }

set_config(settings, config)
