import argparse

from altair import Altair
from tools import gen_path_with_script, get_settings

'''
usage: $CMD $APPLIANCE_IP $SETTINGS_FILENAME
ask administrator`s password
'''

settings = gen_path('settings.cfg', __file__)
config = get_config(settings)
username = 'administrator'
password = config[username]['password']
default_password = 'hpvse123'

with Altair(appliance_ip=appliance_ip,
            password=default_password,
            username=username) as api:

    api.change_password(old_password=default_password,
                        new_password=password)
