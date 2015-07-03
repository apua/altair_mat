from ..utils import output

osbp_steps_type_mapping = {
    'os-deployment-install-cfgfiles': 'configs',
    'os-deployment-ogfs-scripts':     'ogfsScripts',
    'os-deployment-server-scripts':   'serverScripts',
    'os-deployment-install-zips':     'packages',
    }

def export_custom_osbps(api, interval=0, fetch_all=True):
    """
    Fetch osbp, config, ogfsScript, serverScript, and then return the necessary data.

    It uses fetching Altair index now.

    You can set :param:`interval` (second) to wait after retrieve data everytime.

    You can set :param:`fetch_all` (bool) `False` to fetch config/script only related to customized OSBPs,
    it will be faster since checking if config is customized or not cannot use index.
    """
    import time

    info = {'osbp':{}, 'ogfsScript':{}, 'serverScript':{}, 'config':{}}

    # used to fast check if ogfsScript/serverScript is custom or not
    cust_script_names = {member['name']: member['uri']
                         for member in api._list_index({'category':'osdscript'})['members']
                         if member['attributes']['osdCustomerContent']=='true'}

    for member in api._list_index({'category':'osdbuildplan'})['members']:
        if member['attributes']['osdCustomerContent']=='false':
            continue
        osbp = api._retrieve_OSBP(uri=member['uri'])

        time.sleep(interval)
        output("osbp -- {}".format(osbp['name']))

        info['osbp'][osbp['name']] = {
            'attr': osbp['buildPlanCustAttrs'],
            'desc': osbp['description'],
            'type': osbp['os'],
            'steps': [
                {'name': step['name'],
                 'type': osbp_steps_type_mapping[step['type']],
                 'para': step['parameters']}
                for step in osbp['buildPlanItems']
                ]
            }

        if fetch_all:
            continue

        # retrieve customized items of the OSBP
        for item in osbp['buildPlanItems']:
            if   item['type']=='os-deployment-install-cfgfiles':
                # there is no way to check if it is customized or not from fetched data
                config = api._retrieve_cfgfile(item['id'])
                if config['isCustomerContent']:
                    info['config'][config['name']] = {
                        'desc': config['description'],
                        'cont': config['text'],
                        }
            elif item['type']=='os-deployment-ogfs-scripts' and item['name'] in cust_script_names:
                ogfsScript = api._retrieve_ogfsScript(item['id'])
                info['ogfsScript'][ogfsScript['name']] = {
                    'desc': ogfsScript['description'],
                    'cont': ogfsScript['source'],
                    'type': ogfsScript['codeType'],
                    }
            elif item['type']=='os-deployment-server-scripts' and item['name'] in cust_script_names:
                serverScript = api._retrieve_serverScript(item['id'])
                info['serverScript'][serverScript['name']] = {
                    'desc': serverScript['description'],
                    'cont': serverScript['source'],
                    'type': serverScript['codeType'],
                    'sudo': serverScript['runAsSuperUser'],
                    }
            else: #os-deployment-install-zips
                pass

            #time.sleep(interval)
            #print(item['name'])

    if fetch_all:
        for name, uri in cust_script_names.items():
            output("script -- {}".format(member['name']))
            if 'os-deployment-ogfs-scripts' in uri:
                ogfsScript = api._retrieve_ogfsScript(uri=uri)
                info['ogfsScript'][ogfsScript['name']] = {
                    'desc': ogfsScript['description'],
                    'cont': ogfsScript['source'],
                    'type': ogfsScript['codeType'],
                    }
            elif 'os-deployment-server-scripts' in uri:
                serverScript = api._retrieve_serverScript(uri=uri)
                info['serverScript'][serverScript['name']] = {
                    'desc': serverScript['description'],
                    'cont': serverScript['source'],
                    'type': serverScript['codeType'],
                    'sudo': serverScript['runAsSuperUser'],
                    }
        for member in api._list_index({'category':'osdcfgfile'})['members']:
            output("config -- {}".format(member['name']))
            config = api._retrieve_cfgfile(uri=member['uri'])
            if config['isCustomerContent']:
                info['config'][config['name']] = {
                    'desc': config['description'],
                    'cont': config['text'],
                    }

    return info
