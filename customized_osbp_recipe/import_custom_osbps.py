def _():
    """
    Add "../common/" to search path
    """
    import os, sys
    prog_dir = os.path.dirname(__file__)
    relpath = os.path.join(prog_dir, os.path.normpath('../common/'))
    abspath = os.path.abspath(relpath)
    sys.path.append(abspath)
_()

from altair.api import Altair
from altair.utils import get_config, set_config

settings = get_config('settings.txt')
login_information = settings['login_information']
appliance_ip  = login_information['appliance_ip']
username      = login_information['username']
password      = login_information['password']
cust_filepath = settings['cust_filepath']

with Altair(appliance_ip, username, password) as api:
    api.import_custom_osbps(get_config(cust_filepath))

print("""
import customized OSBPs successfully
""")
