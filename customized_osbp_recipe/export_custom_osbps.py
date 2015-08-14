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

settings = get_config('settings.txt')
login_information = settings['login_information']
appliance_ip  = login_information['appliance_ip']
username      = login_information['username']
password      = login_information['password']
cust_filepath = settings['cust_filepath']

try:
    get_config(cust_filepath)
    mesg = '"{}" already exists, replace it? (Y/N) '.format(cust_filepath)
    if raw_input(mesg).lower()[0]!='y':
        print('Stop to export customized OSBPs')
        exit()
except IOError:
    pass

with Altair(appliance_ip, username, password) as api:
    cust_info = api.export_custom_osbps()
    #cust_info = api.export_custom_osbps(interval=1)
    set_config(cust_info, cust_filepath)

print("""
export customized OSBPs successfully
""")
