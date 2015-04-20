import argparse

from altair import Altair
from tools import gen_path, get_config

'''
usage: $CMD $SETTINGS_FILENAME

it can be implemented by turning off vm
'''

settings = gen_path('settings.cfg', __file__)
config = get_config(settings)
username = 'administrator'
password = config[username]['password']
appliance_ip = config['network settings']['appliance ip']

with Altair(appliance_ip=appliance_ip,
            username=username,
            password=password) as api:

    api.shutdown()
