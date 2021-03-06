'''
usage: command appliance_ip [config_path]
'''

import argparse
import os
import sys

from altair.api import Altair
from altair.utils import get_config


if   len(sys.argv)==1:
    config_path = os.path.join(os.path.dirname(__file__), 'settings.cfg')
elif len(sys.argv)==2:
    config_path = sys.argv[1]
else:
    exit(__doc__.strip())


if not os.path.isfile(config_path):
    templ = '"%s" doesn`t exist.'
    print(templ % config_path)
    exit(2)


try:
    config = get_config(config_path)
except Exception as e:
    print(e.message)
    exit(2)


username = config['login user']['userName']
password = config['login user']['password']
appliance_ip = config['network settings']['appliance_ip']

with Altair(appliance_ip=appliance_ip,
            username=username,
            password=password) as api:

    api.set_media_settings(config['media settings'])
    api.set_product_keys(config['product keys'])
    api.set_facility_attributes(config['facility attributes'])

    # bwlow is not idempotent
    api.set_activation_key(config['activation key'])

    api.update_user_info(config['login user'])

    # below is not idempotent
    for user in config['other users']:
        api.add_user(user)

    # OSBPs
    # WinPE
