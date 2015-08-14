"""
Set facility & upload WinPE

Updating WinPE and adding SUTs features are not implement yet
"""

def _():
    """
    Add "../common/" to search path
    """
    import os, sys
    prog_dir = os.path.dirname(sys.argv[0]) or os.curdir
    relpath = os.path.join(prog_dir, os.path.normpath('../common/'))
    abspath = os.path.abspath(relpath)
    sys.path.append(abspath)
_()

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

    print("set media settings...")
    api.set_media_settings(settings['media_settings'])

    print("set product keys...")
    api.set_product_keys(settings['product_keys'])

    print("set facility attributes...")
    api.set_facility_attributes(settings['facility_attributes'])

    print("enter activation key...")
    if api.get_activation_status()!="activated":
        api.set_activation_key(settings['activation_key'])
    else:
        pass #print(api.get_activation_key(), settings['activation_key'])

    print("set other facility settings...")
    api.set_pxeboot_default(settings['pxeboot_default'])
    not_upload_winpe = True
    if settings['winpe_source']:
        Not_Upload_WinPE = False
        api.upload_winpe(settings['winpe_source'])

    print("update administrator information and password...")
    api.update_user(settings['administrator'])
    if settings['administrator']['password'] not in ('......', password):
        print("...(NOTE: administrator password has been changed)")
        api.change_password(settings['administrator']['password'])

    print("set users...")
    existed = {user['login_name'] for user in api.get_users()}
    for user in settings['users']:
        (api.update_user if user['login_name'] in existed else api.add_user)(user)
        api.change_password(user['password'], user['login_name'])

    #for sut in settings['suts']:
    #    job_uri = api.add_sut(sut) #blocking
    #    status = api.wait_job_finish(job_uri)
    #    print(status)


print("""
first time setup is completed, the works below not be executed:
- change network settings
- adding SUTs
- import customized OSBPs
""".format("- upload WinPE\n" if not_upload_winpe else ""))
