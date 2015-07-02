"""
Set facility & upload WinPE

Updating WinPE and adding SUTs features are not implement yet
"""

__import__('sys').path.append('../common/')

from altair.api import Altair
from altair.utils import get_config, set_config

config_file = 'settings.txt'

settings = get_config(config_file)
basic_information = settings['basic_information']
appliance_ip  = basic_information['appliance_ip']
username      = basic_information['username']
password      = basic_information['password']

with Altair(appliance_ip, username, password) as api:
    api.set_media_settings(settings['media_settings'])
    api.set_product_keys(settings['product_keys'])
    api.set_facility_attributes(settings['facility_attributes'])

    if api.get_activation_status()!="activated":
        api.set_activation_key(settings['activation_key'])
    else:
        print(api.get_activation_key(), settings['activation_key'])

    api.set_pxeboot_default(settings['pxeboot_default'])

    api.upload_winpe(settings['winpe_source'])

    for user in settings['users']:
        if user['login_name']==username:
            # will not change password and modify admin roles
            api.update_user_info(user)
        else:
            api.add_user(user)

    for sut in settings['suts']:
        job = api.add_sut(sut) #async
