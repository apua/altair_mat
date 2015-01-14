from __future__ import print_function
from colorprint import print
from ConfigParser import ConfigParser
#from scripts import ....
from altair import Altair


CFG_FILE = 'settings.cfg'

conf = ConfigParser()
conf.read(CFG_FILE)
#print({sec: dict(conf.items(sec)) for sec in conf.sections()})

# "checking configuration" section
current = dict(conf.items('current appliance'))
print.red(current)


with Altair(appliance_ip = current['ip'],
            username = current['username'],
            password = current['password']) as api:
    # product keys
    # facility attributes
    custom_attr = api.retrieve_facility(1)['customAttributes']
    product_keys = {k:v for k,v in custom_attr.iteritems()
                        if k.startswith('ProductKey_')}
    customized_attr = {k:v for k,v in custom_attr.iteritems()
                           if not k.startswith('ProductKey_') and
                              not k.startswith('__OPSW') and
                              k != 'device_discovery_naming_rules'}
                    
    print.yellow(sep='\n', *sorted(product_keys.iteritems()))
    print.yellow(sep='\n', *sorted(customized_attr.iteritems()))


    # OSBPs    - osdbuildplan
    # scripts  - osdscript
    # packages - osdzip
    get_customized_members = lambda category: [member['name']#uri']
        for member in api.list_index({'category': category})['members']
        if member['attributes']['osdCustomerContent'] != 'false']
        #if member['attributes']['osdCustomerContent']]

    for cate in ('osdbuildplan', 'osdscript', 'osdzip'):
        print.green(sep='\n', *get_customized_members(cate))

    # configuration files - osdcfgfile
    # it has no 'osdCustomerContent' attribute in searching result....damn

