M = mapping = {
    'hostname':   'hostname',
    'ip_address': 'app1Ipv4Addr',
    'subnet':     'ipv4Subnet',
    'gateway':    'ipv4Gateway',
    'dns':        'ipv4NameServers',
    'alias':      'app1Ipv4Alias',
    }

def get_network_setting(api):
    N = api._retrieve_network_interface()['applianceNetworks']

    if len(N)==1:
        setting = {'hostname':   N[-1][M['hostname']],
                   'dns':        N[-1][M['dns']],
                   'appliance':  {'ip_address': N[-1][M['ip_address']],
                                  'gateway':    N[-1][M['gateway']],
                                  'subnet':     N[-1][M['subnet']]},
                   'deployment': {'ip_address': N[-1][M['alias']]}}
    elif len(N)==2:
        setting = {'hostname':   N[-1][M['hostname']],
                   'dns':        N[-1][M['dns']],
                   'appliance':  {'ip_address': N[-1][M['ip_address']],
                                  'subnet':     N[-1][M['subnet']],
                                  'gateway':    N[-1][M['gateway']]},
                   'deployment': {'ip_address': N[-2][M['ip_address']],
                                  'subnet':     N[-2][M['subnet']]}}
    return setting


def set_network(api, setting):
    r"""
    This method is not perfect because it always shows error in "Activity" page
    on Altair webUI without any hint even if it sent exactly same thing through
    HTTP POST with setting network manually on Altair webUI.

    The document of REST API is not clear, so that all of things below has been
    tested many times.
    """
    J = api._retrieve_network_interface()
    N = J['applianceNetworks']

    # Notice:
    #     building a new dict object and updating it is for
    #     avoiding side-effect which might cause disaster

    # Notice:
    #     since the Altair is just a single node cluster,
    #     "confOneNode" is always "True" and "activeNode" is always "1"
    #     so that no need to change

    # shared
    if not setting['deployment'].has_key('subnet'):
        app_nic = {}
        app_nic.update(N[-1])
        app_nic.update({'ipv4Type': 'STATIC', 'aliasDisabled': False})

        # The information which users care below
        app_nic.update({M['hostname']:   setting['hostname'],
                        M['dns']:        setting['dns'],
                        M['ip_address']: setting['appliance']['ip_address'],
                        M['gateway']:    setting['appliance']['gateway'],
                        M['subnet']:     setting['appliance']['subnet'],
                        M['alias']:      setting['deployment']['ip_address']})

        nics = [app_nic]

    # independent
    else:
        app_nic, dep_nic = {}, {}
        if len(N)==1:
            # When the setting is not with "independent" in last time,
            # it is necessary to "aliasDisabled" and correct "device".
            # It is also possible that it is in first time setup,
            # so that "ipv4Type" has to set "STATIC" to replace "DHCP".
            app_nic.update(N[-1])
            app_nic.update({'ipv4Type': 'STATIC', 'aliasDisabled': True, 'device': 'eth0'})
            dep_nic.update(N[-1])
            dep_nic.update({'ipv4Type': 'STATIC', 'aliasDisabled': True, 'device': 'eth1',
                            'macAddress': api._retrieve_macs()['members'][0]['macAddress'],
                            'interfaceName': 'Deployment'})
        elif len(N)==2:
            app_nic.update(N[-1])
            dep_nic.update(N[-2])

        # The information which users care below
        app_nic.update({M['hostname']:   setting['hostname'],
                        M['dns']:        setting['dns'],
                        M['ip_address']: setting['appliance']['ip_address'],
                        M['gateway']:    setting['appliance']['gateway'],
                        M['subnet']:     setting['appliance']['subnet'],
                        M['alias']:      None})

        dep_nic.update({M['hostname']:   'sa1', # Set it manually
                        M['dns']:        [],
                        M['ip_address']: setting['deployment']['ip_address'],
                        M['gateway']:    setting['appliance']['gateway'],
                        M['subnet']:     setting['deployment']['subnet'],
                        M['alias']:      None})

        nics = [dep_nic, app_nic]

    J['applianceNetworks'] = nics
    api._configure_network_interface(J)
