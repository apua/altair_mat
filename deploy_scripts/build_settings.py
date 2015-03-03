import argparse
import sys

#from altair import Altair
from tools import gen_path, IP

'''
usage: $CMD $APPLIANCE_IP $SETTINGS_FILENAME

content of settings.cfg::

  [administrator]
  password = 'hpvse123'
  
  [activation key]
  [prodyct keys]
  [facility attributes]
  [network]
  [media server]
  username
  password
  
  appliance_ip = ''
  info_filename = ''
'''

settings = gen_path('settings.cfg', __file__)


with Altair(appliance_ip=appliance_ip,
            username=username,
            password=password) as api:

    info = api.get_info()
    '''
    info = {
        'facility_attr': {
            'ProductKey_*': '',
            '__OPSW-Media-*: '',
            ...,
            },
        'activation': ...,
        # 'users': ...,
        # 'osbps': ...,
        }
    '''
