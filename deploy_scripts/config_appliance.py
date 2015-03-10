'''
usage: command appliance_ip [config_path]
'''

import argparse
import os
import sys

from altair import Altair
from tools import get_config


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

from pprint import pprint as p
p(vars())
exit()

with Altair(appliance_ip=appliance_ip,
            username=username,
            password=password) as api:

    api.set_media_settings(config['media settings'])
    api.set_product_keys(config['product keys'])
    api.set_facility_attributes(config['facility attributes'])
    api.set_activation_key(config['activation key'])

    for user in config['other users']:
        api.add_user(user)

    # OSBPs
    # WinPE
