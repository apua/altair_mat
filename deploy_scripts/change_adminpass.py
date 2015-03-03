from altair import Altair
from tools import gen_path_with_script, get_settings

SETTINGS = gen_path_with_script('settings.json')
vars().update(get_settings(SETTINGS, section='Altair'))

'''
username = ''
password = ''
default_password = ''
appliance_ip = ''
'''

with Altair(appliance_ip=appliance_ip,
            password=default_password,
            username=username) as api:
     api.change_password(password)
