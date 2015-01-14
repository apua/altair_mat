from __future__ import print_function
from pprint import pprint
from ConfigParser import ConfigParser
#from scripts import ....
from altair import Altair


#CFG_FILE = 'settings.cfg'
#
#conf = ConfigParser()
#conf.read(CFG_FILE)
#pprint({sec: dict(conf.items(sec)) for sec in conf.sections()})
#
#
#with Altair(appliance_ip = network['appliance_ip'],
#            username = credential['username'],
#            password = credential['password']) as api:
#    session = api.retrieve_session()

with Altair(appliance_ip = '10.30.1.235',
            username = 'april',
            password = 'applianceadmin') as api:
    print("I am in block")
    print(api)
    print(api.retrieve_session())
    print("would go out block")

print("I am outside block")
print(api)
print(api.retrieve_session())
