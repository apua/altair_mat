from __future__ import print_function
from colorprint import print
from ConfigParser import ConfigParser
#from scripts import ....
from altair import Altair


#CFG_FILE = 'settings.cfg'
#
#conf = ConfigParser()
#conf.read(CFG_FILE)
#pprint({sec: dict(conf.items(sec)) for sec in conf.sections()})


with Altair(appliance_ip = '10.30.1.235',
            username = 'april',
            password = 'applianceadmin') as api:
    # product keys
    # facility attributes
    custom_attr = api.retrieve_facility(1)['customAttributes']
    product_keys = {k:v for k,v in custom_attr.iteritems()
                        if k.startswith('ProductKey_')}
    print.yellow(sep='\n', *sorted(custom_attr.iteritems()))


    # OSBPs    - osdbuildplan
    # scripts  - osdscript
    # packages - osdzip
    get_customized_members = lambda category: [member['uri']
        for member in api.list_index({'category': category})['members']
        if member['attributes']['osdCustomerContent'] != 'false']
        #if member['attributes']['osdCustomerContent']]

    for cate in ('osdbuildplan', 'osdscript', 'osdzip'):
        print.green(sep='\n', *get_customized_members(cate))

    # configuration files - osdcfgfile
    # it has no 'osdCustomerContent' attribute in searching result....damn

