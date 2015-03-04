import argparse

from altair import Altair
from tools import gen_path, get_config, value2subconfig

'''
usage: $CMD $SETTINGS_FILENAME
'''

settings = gen_path('settings.cfg', __file__)
config = get_config(settings)
username = 'administrator'
password = config[username]['password']
appliance_ip = config['network settings']['appliance ip']

with Altair(appliance_ip=appliance_ip,
            username=username,
            password=password) as api:

    api.set_media_settings(config['media settings'])
    api.set_product_keys(config['product keys'])
    api.set_facility_attributes(config['facility attributes'])
    api.set_activation_key(config['activation key'])

    other_users = config[username]['other users']
    for section, items in value2subconfig(other_users):
        items['username'] = section
        api.add_user(items)

    # OSBPs
    # WinPE
