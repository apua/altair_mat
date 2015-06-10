def import_cust_info(api, new_info, remove_unused=False):
    """
    Given the newer customized info. Diff and upload/update/remove

    Return Nonthing
    """
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
    
    def get_uri_mapping(api):
        return {
            member['name']: member['uri']
            for cate in ('osdbuildplan', 'osdscript', 'osdcfgfile', 'osdzip')
            for member in api._list_index({'category': cate})['members']
            }
    
    def get_modified_mapping(api):
        return {
            member['name']: member['modified']
            for cate in ('osdbuildplan', 'osdscript', 'osdcfgfile', 'osdzip')
            for member in api._list_index({'category': cate})['members']
            }
    
    def gen_step_data(step, uri_mapping):
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
    
    def upload_cust_items(api, uploads):
        for name, script in uploads['serverScript'].items():
            print('upload', name)
            api._add_serverScript({
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
            api._add_ogfsScript({
                'type': "OSDOGFSScript",
                'name': name,
                'description': script['desc'],
                'source': script['cont'],
                })
        for name, config in uploads['config'].items():
            print('upload', name)
            api._add_cfgfile({
                'type': 'OsdCfgFile',
                'name':name,
                'description':config['desc'],
                'text':config['cont'],
                })
    
    def upload_cust_osbps(api, uploads):
        uri_mapping = get_uri_mapping(api)
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
                'buildPlanItems': [gen_step_data(s, uri_mapping) for s in osbp['steps']],
                })
    
    def upload_cust(api, uploads):
        upload_cust_items(api, uploads)
        upload_cust_osbps(api, uploads)
    
    def update_cust(api, updates):
        uri_mapping = get_uri_mapping(api)
        modified_mapping = get_modified_mapping(api)
    
        for name, osbp in updates['osbp'].items():
            print('update OSBP', name)
            api._edit_OSBP(uri=uri_mapping[name], properties={
                'type': 'OSDBuildPlan',
                'lifeCycle': 'AVAILABLE',
                'arch': 'x64',
                'name': name,
                'buildPlanCustAttrs': osbp['attr'],
                'description': osbp['desc'],
                'os': osbp['type'],
                'buildPlanItems': [gen_step_data(s, uri_mapping) for s in osbp['steps']],
                'modified': modified_mapping[name],
                'uri': uri_mapping[name],
                })
    
        for name, config in updates['config'].items():
            print('update config', name)
            api._edit_cfgfile(uri=uri_mapping[name], properties={
                'type': 'OsdCfgFile',
                'name': name,
                'description': config['desc'],
                'text': config['cont'],
                'modified': modified_mapping[name],
                'uri': uri_mapping[name],
                })
    
        for name, script in updates['serverScript'].items():
            print('update script', name)
            api._edit_serverScript(uri=uri_mapping[name], properties={
                'type': 'OSDServerScript',
                'serverChanging': True,
                'name': name,
                'description': script['desc'],
                'source': script['cont'],
                'runAsSuperUser': script['sudo'],
                'codeType': script['type'],
                'modified': modified_mapping[name],
                'uri': uri_mapping[name],
                })
    
        for name, script in updates['ogfsScript'].items():
            print('update script', name)
            api._edit_ogfsScript(uri=uri_mapping[name], properties={
                'type': "OSDOGFSScript",
                'name': name,
                'description': script['desc'],
                'source': script['cont'],
                'modified': modified_mapping[name],
                'uri': uri_mapping[name],
                })
    
    def remove_cust(api, removes):
        uri_mapping = get_uri_mapping(api)
        # OSBPs have to be removed first
        for name in removes['osbp']:
            print('remove osbp', name)
            api._delete_OSBP(uri=uri_mapping[name])
        for name in removes['serverScript']:
            print('remove script', name)
            api._delete_serverScript(uri=uri_mapping[name])
        for name in removes['ogfsScript']:
            print('remove script', name)
            api._delete_ogfsScript(uri=uri_mapping[name])
        for name in removes['config']:
            print('remove config', name)
            api._delete_cfgfile(uri=uri_mapping[name])
    
    diff = compare_cust(api.export_cust_info(fetch_all=True), new_info)
    
    if remove_unused:
        remove_cust(api, removes=diff['removes'])
    upload_cust(api, uploads=diff['uploads'])
    update_cust(api, updates=diff['updates'])
