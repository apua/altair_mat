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


# Retrieve customized data from current Altair
with Altair(appliance_ip = current['ip'],
            username = current['username'],
            password = current['password']) as api:

    current_altair_data = {}

    # "Product Keys" and "Facility Custom Attributes"
    facility_attr = api.retrieve_facility(1)['customAttributes']
    current_altair_data['product_keys'] = {k:v
        for k,v in facility_attr.iteritems()
        if k.startswith('ProductKey_')}
    current_altair_data['custom_attr'] = {k:v
        for k,v in facility_attr.iteritems()
        if not k.startswith('ProductKey_') and
           not k.startswith('__OPSW') and
           k != 'device_discovery_naming_rules'}

    # "OSBPs", "Scripts", "Packages"
    get_customized_members = lambda category: [member['uri']
        for member in api.list_index({'category': category})['members']
        if member['attributes']['osdCustomerContent'] != 'false']
        #if member['attributes']['osdCustomerContent']]

    for category, query_category, method in (
      ('OSBPs','osdbuildplan',api.retrieve_OSBP),
      ('scripts','osdscript', api.retrieve_serverScript),
      #('packages','osdzip', ....),
      ):
        uris = get_customized_members(query_category)
        #print.green(sep='\n', *uris); continue
        for uri in uris:
            id = uri.rsplit('/')[-1]
            j = method(id)
            print.green(j)

    # Configuration Files - "osdcfgfile"
