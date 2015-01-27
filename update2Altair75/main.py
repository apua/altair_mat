from __future__ import print_function

from ConfigParser import ConfigParser
import sys

from altair import Altair
from colorprint import print, pprint

if sys.version_info.major==2:
    input = raw_input


# Get attribute
# =============

CFG_FILE = 'settings.cfg'
conf = ConfigParser()
conf.read(CFG_FILE)

current = dict(conf.items('Current Appliance'))
appliance = dict(conf.items('Appliance'))


# Retrieve data
# =============

with Altair(appliance_ip = current['ip'],
            username = current['username'],
            password = current['password']) as api:

    print.reverse("-> Retrieve Data...")

    # "Product Keys" and "Facility Custom Attributes"
    facility_attr = api.retrieve_facility(1)['customAttributes']
    current_altair_data = {}
    current_altair_data['productkeys'] = {k:v
        for k,v in facility_attr.iteritems()
        if k.startswith('ProductKey_')}
    current_altair_data['customattrs'] = {k:v
        for k,v in facility_attr.iteritems()
        if not k.startswith('ProductKey_') and
           not k.startswith('__OPSW') and
           k != 'device_discovery_naming_rules'}
    current_altair_data['media'] = {k:v
        for k,v in facility_attr.iteritems()
        if k.startswith('__OPSW-Media')}

print.reverse("done\n")


# Upload data
# ===========

with Altair(appliance_ip = appliance['ip'],
            username = appliance['username'],
            password = appliance['password']) as api:

    print.reverse("-> Upload Data...")

    facility = api.retrieve_facility(1)
    current_altair_data['media']['__OPSW-Media-WinPassword'] = 'Compaq123'
    facility['customAttributes'].update(current_altair_data['productkeys'])
    facility['customAttributes'].update(current_altair_data['customattrs'])
    facility['customAttributes'].update(current_altair_data['media'])
    api.edit_facility(1, facility)


print.reverse("done\n")

print.reverse("Task is Finished Successfully~")
input("Press any key to Quit")
