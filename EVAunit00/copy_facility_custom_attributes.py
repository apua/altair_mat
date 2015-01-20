from __future__ import print_function
from colorprint import print
#from ConfigParser import ConfigParser
#from scripts import ....
from altair import Altair


#CFG_FILE = 'settings.cfg'
#
#conf = ConfigParser()
#conf.read(CFG_FILE)
#print({sec: dict(conf.items(sec)) for sec in conf.sections()})

# "checking configuration" section
#current = dict(conf.items('current appliance'))
#credential = dict(conf.items('credential'))
#network = dict(conf.items('network'))
#print.red(current)


# Retrieve customized data from current Altair
with Altair(appliance_ip = 'altair-dev.dev-net.local',
            username = 'administrator',
            password = 'Compaq123') as api:

    current_altair_data = {}

    # "Product Keys" and "Facility Custom Attributes"
    facility_attr = api.retrieve_facility(1)['customAttributes']
    current_altair_data['productkeys'] = {k:v
        for k,v in facility_attr.iteritems()
        if k.startswith('ProductKey_')}
    current_altair_data['customattrs'] = {k:v
        for k,v in facility_attr.iteritems()
        if not k.startswith('ProductKey_') and
           not k.startswith('__OPSW') and
           k != 'device_discovery_naming_rules'}


# Check if custom data is empty and then update
with Altair(appliance_ip = 'csi-altair.twn.hp.com',
            username = 'april',
            password = 'applianceadmin') as api:

    # Check if custom data is empty
    # =============================

    facility = api.retrieve_facility(1)
    #productkeys_are_empty = not any(k for k in facility['customAttributes']
    #                                  if k.startswith('ProductKey_'))
    #assert productkeys_are_empty
    customattrs_are_empty = not any(k for k in facility['customAttributes']
                                      if not k.startswith('ProductKey_') and
                                         not k.startswith('__OPSW') and
                                         k != 'device_discovery_naming_rules')
    assert customattrs_are_empty

    # Update
    # ======

    k = raw_input('NOTICE: update data would be hard to recover. [y/N]')
    if k.lower() not in ('y', 'yes', 'true'):
        exit()

    print.cyan(sep='\n', *sorted(facility['customAttributes'].items()))
    #facility['customAttributes'].update(current_altair_data['productkeys'])
    facility['customAttributes'].update(current_altair_data['customattrs'])
    print.green(sep='\n', *sorted(facility['customAttributes'].items()))
    api.edit_facility(1, facility)
