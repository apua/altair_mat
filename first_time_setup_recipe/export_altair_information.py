r"""
The `export_altair_information` is for exporting information of existed Altair,
including network settings, attributes, product keys, the active key, without password.

It will generate `settings.txt` in YAML format and `settings.py`, which have the same contents.

In the beginning, there should be `settings.txt` contains appliance IP, username,
password information, for connecting to Altair.
"""

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
    network_setting     = api.get_network_setting()
    activation_key      = api.get_activation_key()
    media_settings      = api.get_media_settings()
    product_keys        = api.get_product_keys()
    facility_attributes = api.get_facility_attributes()
    #pxeboot_default     = api.get_pxeboot_default()

info = {
    'basic_information':   basic_information,
    'network_setting':     network_setting,
    'media_settings':      media_settings,
    'product_keys':        product_keys,
    'facility_attributes': facility_attributes,
    #'pxeboot_default':     pxeboot_default,
    'activation_key':      activation_key,
    #'WinPE source':,
    #'SUTs':,
    #'Users':,
    }

set_config(info, config_file)

with open(variables_file, 'w') as f:
    for k, v in info.items():
        lines = pformat(v).splitlines()
        indent = ' '*(len(k)+3)
        output = ''.join((indent if ln else k+' = ')+line+'\n' for ln, line in enumerate(lines))
        f.write(output)
