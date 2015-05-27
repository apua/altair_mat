import time

type_mapping = {
    'os-deployment-install-cfgfiles': 'configs',
    'os-deployment-ogfs-scripts':     'ogfsScripts',
    'os-deployment-server-scripts':   'serverScripts',
    'os-deployment-install-zips':     'packages',
    }


def get_cust_info(self, interval=0):
    print('================================\n'
          'fetch id of osbp, script, config\n'
          '================================')
    osbp_ids   = [m['uri'].rsplit('/', 1)[-1] for m in self._list_index({'category':'osdbuildplan'})['members']]
    ogfsScript_ids = [m['uri'].rsplit('/', 1)[-1] for m in self._list_index({'category':'osdscript'})['members']
                                              if 'os-deployment-ogfs-scripts' in m['uri']]
    serverScript_ids = [m['uri'].rsplit('/', 1)[-1] for m in self._list_index({'category':'osdscript'})['members']
                                              if 'os-deployment-server-scripts' in m['uri']]
    config_ids = [m['uri'].rsplit('/', 1)[-1] for m in self._list_index({'category':'osdcfgfile'})['members']]
    print('....done')

    print('====================\n'
          'get osbp information\n'
          '====================')
    cust_osbp_info = {}
    for id in osbp_ids:
        osbp = self._retrieve_OSBP(id)
        time.sleep(interval)
        print(osbp['name'])
        if not osbp['isCustomerContent']:
            continue
        cust_osbp_info[osbp['name']] = {
            'attr': osbp['buildPlanCustAttrs'],
            'desc': osbp['description'],
            'type': osbp['os'],
            'steps': [
                {'name': step['name'],
                 'type': type_mapping[step['type']],
                 'para': step['parameters']}
                for step in osbp['buildPlanItems']
                ]
            }

    print('===========================\n'
          'get ogfs script information\n'
          '===========================')
    cust_ogfsScript_info = {}
    for id in ogfsScript_ids:
        ogfsScript = self._retrieve_ogfsScript(id)
        time.sleep(interval)
        print(ogfsScript['name'])
        if not ogfsScript['isCustomerContent']:
            continue
        cust_ogfsScript_info[ogfsScript['name']] = {
            'desc': ogfsScript['deogfsScription'],
            'cont': ogfsScript['source'],
            'type': ogfsScript['codeType'],
            #'sudo': ogfsScript['runAsSuperUser'],
            }

    print('=============================\n'
          'get server script information\n'
          '=============================')
    cust_serverScript_info = {}
    for id in serverScript_ids:
        serverScript = self._retrieve_serverScript(id)
        time.sleep(interval)
        print(serverScript['name'])
        if not serverScript['isCustomerContent']:
            continue
        cust_serverScript_info[serverScript['name']] = {
            'desc': serverScript['deserverScription'],
            'cont': serverScript['source'],
            'type': serverScript['codeType'],
            'sudo': serverScript['runAsSuperUser'],
            }

    print('======================\n'
          'get config information\n'
          '======================')
    cust_config_info = {}
    for id in config_ids:
        config = self._retrieve_cfgfile(id)
        time.sleep(0); print(config['name'])
        if not config['isCustomerContent']:
            continue
        cust_config_info[config['name']] = {
            'desc': config['description'],
            'cont': config['text'],
            }

    return {
        'osbp': cust_osbp_info,
        'ogfsScript': cust_ogfsScript_info,
        'serverScript': cust_serverScript_info,
        'config': cust_config_info,
        }
