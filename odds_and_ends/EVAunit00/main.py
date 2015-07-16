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
credential = dict(conf.items('credential'))
network = dict(conf.items('network'))
print.red(current)


# Retrieve customized data from current Altair
with Altair(appliance_ip = current['ip'],
            username = current['username'],
            password = current['password']) as api:

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
    '''

    # "OSBPs", "Scripts", "Packages"
    get_customized_members = lambda category: [member['uri']
        for member in api.list_index({'category': category})['members']
        if member['attributes']['osdCustomerContent'] != 'false']
        #if member['attributes']['osdCustomerContent']]

    for category, query_category, fetch_method in (
      ('osbps','osdbuildplan',api.retrieve_OSBP),
      ('scripts','osdscript', api.retrieve_serverScript),
      #('packages','osdzip', ....),
      ):
        print('fetching {}, it might take a long time'.format(category))
        uris = get_customized_members(query_category)
        #print.green(sep='\n', len(uris), *uris); continue
        current_altair_data[category] = [fetch_method(uri.rsplit('/',1)[-1]) for uri in uris]
    '''

    # Configuration Files - "osdcfgfile"

    # Servers - "osdserver"


# Check if custom data is empty and then update
with Altair(appliance_ip = network['appliance_ip'],
            username = credential['username'],
            password = credential['password']) as api:

    # Check if custom data is empty
    # =============================

    facility = api.retrieve_facility(1)
    productkeys_are_empty = not any(k for k in facility['customAttributes']
                                      if k.startswith('ProductKey_'))
    assert productkeys_are_empty
    customattrs_are_empty = not any(k for k in facility['customAttributes']
                                      if not k.startswith('ProductKey_') and
                                         not k.startswith('__OPSW') and
                                         k != 'device_discovery_naming_rules')
    assert customattrs_are_empty
    '''

    get_customized_members = lambda category: [member['uri']
        for member in api.list_index({'category': category})['members']
        if member['attributes']['osdCustomerContent'] != 'false']
        #if member['attributes']['osdCustomerContent']]

    osbps_are_empty = not get_customized_members('osdbuildplan')
    assert osbps_are_empty

    scripts_are_empty = not get_customized_members('osdscript')
    assert scripts_are_empty
    '''

    # Update
    # ======

    k = raw_input('NOTICE: update data would be hard to recover. [y/N]')
    if k.lower() not in ('y', 'yes', 'true'):
        exit()

    print.cyan(sep='\n', *sorted(facility['customAttributes'].items()))
    facility['customAttributes'].update(current_altair_data['productkeys'])
    facility['customAttributes'].update(current_altair_data['customattrs'])
    print.green(sep='\n', *sorted(facility['customAttributes'].items()))
    api.edit_facility(1, facility)

    '''
    for osbp in current_altair_data['osbps']:
        #print.purple(sep='\n', *osbp.items())
        #api.add_OSBP(osbp)
        api.add_OSBP( {
            "name": "Apua",#osbp["name"],
            "description": osbp["description"],
            #"os": osbp["os"],
            "buildPlanItems": [],#osbp["buildPlanItems"],
            "buildPlanCustAttrs": osbp["buildPlanCustAttrs"],
            "isCustomerContent": osbp["isCustomerContent"],
            "type": osbp["type"],
            "arch": osbp["arch"],
            "created": osbp["created"],
            "modified": osbp["modified"],
            } )
        #api.add_OSBP( {"name":"Apua","description":"asdf","os":"Other","buildPlanItems":[],"buildPlanCustAttrs":[],"isCustomerContent":True,"type":"OSDBuildPlan","arch":"x64","created":"2015-01-15T08:16:05.699Z","modified":"2015-01-15T08:16:05.699Z"} )

    for script in current_altair_data['scripts']:
        if script['type']=='os-deployment-server-scripts':
            # 'os-deployment-server-scripts' is for Altair 7.3.x
            # for Altair 7.5.x , use 'OSDServerScript'
            script['type'] = 'OSDServerScript'
            api.add_serverScript(script)
        else:
            # os-deployment-ogfs-scripts
            api.add_ogfsScript(script)
    '''
