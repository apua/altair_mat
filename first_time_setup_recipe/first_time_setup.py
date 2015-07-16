"""
Set facility & upload WinPE

Updating WinPE and adding SUTs features are not implement yet
"""

__import__('sys').path.append('../common/')

from altair.api import Altair
from altair.utils import get_config, set_config

config_file = 'settings.txt'

settings = get_config(config_file)
login_information = settings['login_information']
appliance_ip  = login_information['appliance_ip']
username      = login_information['username']
password      = login_information['password']

#api = Altair(appliance_ip)
#api.setup()
#api.set_network(settings['network_setting'])

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

    api.update_user(settings['administrator'])
    if '......'!=settings['administrator']['password']:
        api.change_password(settings['administrator']['password'])

    existed = {user['login_name'] for user in api.get_users()}
    for user in settings['users']:
        (api.update_user if user['login_name'] in existed else api.add_user)(user)
        api.change_password(user['password'], user['login_name'])

    #for sut in settings['suts']:
    #    job_uri = api.add_sut(sut) #blocking
    #    status = api.wait_job_finish(job_uri)
    #    print(status)
