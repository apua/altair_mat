__import__('sys').path.append('../common/')

from common import *

from altair import Altair
from utils import get_config, set_config

def compare_cust(older, newer):
    diff = {'uploads':{}, 'updates':{}, 'removes':{}}
    for category in ('osbp','ogfsScript','serverScript','config'):
        # Altair compares name **in lowercase** !?

        #ncate = newer[category]
        #ocate = older[category]
        ncate = {name.lower(): data for name,data in newer[category].items()}
        ocate = {name.lower(): data for name,data in older[category].items()}

        realnames = {name.lower(): name for name in newer[category].viewkeys()|older[category].viewkeys()}

        # dict.viewkeys is Python2.x only
        added_names     = ncate.viewkeys() - ocate.viewkeys()
        deprecate_names = ocate.viewkeys() - ncate.viewkeys()
        same_names      = ncate.viewkeys() & ocate.viewkeys()

        #diff['uploads'][category] = {name: ncate[name] for name in added_names}
        #diff['removes'][category] = {name: ocate[name] for name in deprecate_names}
        #diff['updates'][category] = {name: ncate[name] for name in same_names if ncate[name]!=ocate[name]}
        diff['uploads'][category] = {realnames[name]: ncate[name] for name in added_names}
        diff['removes'][category] = {realnames[name]: ocate[name] for name in deprecate_names}
        diff['updates'][category] = {realnames[name]: ncate[name] for name in same_names if ncate[name]!=ocate[name]}

    return diff

def get_uri_mapping(self):
    return {
        member['name']: member['uri']
        for cate in ('osdbuildplan', 'osdscript', 'osdcfgfile', 'osdzip')
        for member in self._list_index({'category': cate})['members']
        }

def upload_cust_items(self, uploads):
    for name, script in uploads['serverScript'].items():
        print('upload', name)
        self._add_serverScript({
            'type': 'OSDServerScript',
            'serverChanging': True,
            'name': name,
            'description': script['desc'],
            'source': script['cont'],
            'runAsSuperUser': script['sudo'],
            'codeType': script['type'],
            })
    for name, script in uploads['ogfsScript'].items():
        print('upload', name)
        self._add_ogfsScript({
            'type': "OSDOGFSScript",
            'name': name,
            'description': script['desc'],
            'source': script['cont'],
            })
    for name, config in uploads['config'].items():
        print('upload', name)
        self._add_cfgfile({
            'type': 'OsdCfgFile',
            'name':name,
            'description':config['desc'],
            'text':config['cont'],
            })

def upload_cust_osbps(self, uploads):
    def gen_step_data(step):
        """
        It is also strange,
        such as duplicated information and process non-exist package name,
        thus collect to a single function.
        """
        if step['name'] in uri_mapping:
            name = step['name']
        elif step['type']=='packages':
            try:
                name = next(n for i in reversed(range(len(step['name'])))
                              for n in uri_mapping
                              if n.startswith(step['name'][:i]) )
                print('Choose package "{}" but "{}"'.format(name, step['name']))
            except StopIteration:
                raise Exception('Cannot find suitable package for "{name}"'.format(**step))
            except:
                raise Exception('Unknown Error...')
        else:
            raise Exception('Cannot find step "{type}" "{name}"'.format(**step))

        return {
            # every type of step has key 'cfgFileDownload' and it is necessary
            'cfgFileDownload': step['type']=='configs',
            'parameters': step['para'],
            'uri': uri_mapping[name],
            }

    uri_mapping = get_uri_mapping(self)
    for name, osbp in uploads['osbp'].items():
        print('upload OSBP', name)
        api._add_OSBP({
            'type': 'OSDBuildPlan',
            'modified':'0000-00-00T00:00:00.000Z',
            'arch': 'x64',
            'name': name,
            'description': osbp['desc'],
            'os': osbp['type'],
            'buildPlanCustAttrs': osbp['attr'],
            'buildPlanItems': tuple(map(gen_step_data, osbp['steps'])),
            })

def remove_cust(self, removes):
    uri_mapping = get_uri_mapping(self)
    # OSBPs have to be removed first
    for name in removes['osbp']:
        print('remove osbp', name)
        self._delete_OSBP(uri=uri_mapping[name])
    for name in removes['serverScript']:
        print('remove script', name)
        self._delete_serverScript(uri=uri_mapping[name])
    for name in removes['ogfsScript']:
        print('remove script', name)
        self._delete_ogfsScript(uri=uri_mapping[name])
    for name in removes['config']:
        print('remove config', name)
        self._delete_cfgfile(uri=uri_mapping[name])

settings = get_config('settings.txt')
appliance_ip  = settings['appliance_ip']
username      = settings['username']
password      = settings['password']
cust_filepath = settings['cust_filepath']

with Altair(appliance_ip, username, password) as api:
    older = api.get_cust_info(fetch_all=True)
newer = get_config(cust_filepath)

diff = compare_cust(older, newer)
with Altair(appliance_ip, username, password) as api:
    #upload_cust_items(api, uploads=diff['uploads'])
    #upload_cust_osbps(api, uploads=diff['uploads'])

    #update_cust_items(api, updates=diff['updates'])
    #update_cust_osbps(api, updates=diff['updates'])

    pprint(diff['removes'], depth=2)
    remove_cust(api, removes=diff['removes'])
