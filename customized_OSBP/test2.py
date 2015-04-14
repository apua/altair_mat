from altair import Altair
from tools import set_config

from pprint import pprint
import yaml
import os
import sys

p = lambda v: pprint(v, depth=1)

appliance_ip = '10.30.1.235'
username = 'administrator'
password = 'Compaq123'
cust_filepath = './cust-houston-20150408.yml'
data = yaml.load(open(cust_filepath))


def get_name_uri_mapping(api):
    for category in ('osdbuildplan', 'osdscript', 'osdcfgfile','osdzip'):
        print('========')
        print(category)
        print('========')
        for m in api._list_index({'category': category})['members']:
            print(m['uri'], m['name'])

    sys.exit()


def import_(data, api):
    #. get name-uri mapping
    M = get_name_uri_mapping(api)

    for script in api['script']:
        #. gen form
        #. upload and get uri
        #. update mapping
        pass

    for config in api['config']:
        #. gen form
        #. upload and get uri
        #. update mapping
        pass

    for osbp in api['osbp']:
        #. clean steps
        #. gen form
        #. upload
        pass


with Altair(appliance_ip=appliance_ip, username=username, password=password) as api:
    # let's test!!

    #api._add_cfgfile({'type':'OsdCfgFile', 'name':'Apua01', 'description':'A__a', 'text':'= =a'})
    #api._add_ogfsScript({
    #    'type': "OSDOGFSScript",
    #    'name': 'Apua06',
    #    'description': '=___=+',
    #    'source': '>///<',
    #    })
    #api._add_serverScript({
    #    'type': "OSDServerScript",
    #    'codeType': 'VBS', #"BAT", "OGFS","PY2", "SH", "VBS" 
    #    'name': 'Apua05',
    #    'description': '=___=+',
    #    'source': '>///<',
    #    'runAsSuperUser': True,
    #    "serverChanging": True,
    #    })
    #j = api._add_OSBP({
    #    'type': 'OSDBuildPlan',
    #    'modified':'0000-00-00T00:00:00.000Z',
    #    'arch': 'x64',
    #    'name': 'Apua021',
    #    'description': 'qwer',
    #    'os': 'Other', # osbp['type']
    #    'buildPlanItems': [
    #        {
    #            'parameters':'.......',
    #            'uri':'/rest/os-deployment-server-scripts/820001',
    #            'cfgFileDownload': step['type']=='configs',
    #            },
    #        ],
    #    'buildPlanCustAttrs': [{'attribute': 'xxx', 'value': 'ooo'}], #osbp['attr']
    #    })
    #print(j)

    # just upload fxxking packages....no needs

    # just upload fxxking scripts

    print('==============')
    print('import scripts')
    print('==============')

    for name, script in data['script'].items():
        while 1:
            try:
                if script['type']=='ogfs':
                    api._add_ogfsScript({
                        'type': "OSDOGFSScript",
                        'name': name,
                        'description': script['desc'],
                        'source': script['cont'],
                        })
                else:
                    api._add_serverScript({
                        'type': 'OSDServerScript',
                        'serverChanging': True,
                        'name': name,
                        'description': script['desc'],
                        'source': script['cont'],
                        'runAsSuperUser': script['sudo'],
                        'codeType': script['type'],
                        })
                break
            except:
                raw_input()


    # just upload fxxking configs

    print('==============')
    print('import configs')
    print('==============')

    for name, config in data['config'].items():
        while 1:
            try:
                api._add_cfgfile(
            {'type': 'OsdCfgFile', 'name':name, 'description':config['desc'], 'text':config['cont']}
            )
                break
            except:
                raw_input()


    # get mapping

    print('===========')
    print('get mapping')
    print('===========')

    while 1:
        try:
            P = {m['name']: m['uri'] for m in api._list_package()['members']}
            S = {m['name']: m['uri'] for m in api._list_serverScript()['members']
                                              + api._list_ogfsScript()['members']}
            C = {m['name']: m['uri'] for m in api._list_cfgfile()['members']}
            D = dict(P.items() + S.items() + C.items())
            with open('mapping.yml', 'w') as f:
                yaml.dump(D, f)
            break
        except:
            raw_input()

    # and then upload osbps

    print('============')
    print('import OSBPs')
    print('============')

    def get_uri(M, step):
        if step['type']!='packages':
            return M[step['name']]
        else:
            for i in range(len(step['name']),0,-1):
                name_ = step['name'][:i]
                try:
                    key = next(k for k in M if name_ in k)
                except:
                    continue
                return M[key]


    M = yaml.load(open('mapping.yml'))

    for name, osbp in data['osbp'].items():
        while 1:
            try:
                steps = [{'parameters': step['para'],
                          'cfgFileDownload': step['type']=='configs',
                          'uri': get_uri(M, step)}
                         for step in osbp['steps']]
                api._add_OSBP({
                    'type': 'OSDBuildPlan',
                    'modified':'0000-00-00T00:00:00.000Z',
                    'arch': 'x64',
                    'name': name,
                    'description': osbp['desc'],
                    'os': 'Other', #osbp['type'],
                    'buildPlanCustAttrs': [], #osbp['attr'],
                    'buildPlanItems': steps,
                    })
                break
            except Exception as E:
                print(name)
                print(E.message)
                print('='*30)
                if raw_input()=='pass':
                    break
                else:
                    continue
