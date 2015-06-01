Issues
======

- Click on Windows should run and show the state.

- Explain the data structure of YAML file.

  generating customized data::

      osbp
          $name:
              attr: ...
              desc: ...
              type: ...
              steps:
                  - name: ...
                    type: ...
                    para: ...
      script
          $name:
              desc: ...
              cont: ...
              type: ...
              sudo: ...
      config
          $name:
              desc: ...
              cont: ...

- Explain the requirements:
    + Python
    + Git

- Include Packages:
    + Requists
    + PyYAML

- Clean and import all OSBPs every time is expensive.

- Service temporarily unavailable error handling.

- Clean customized OSBPs could be force and fast.

  issues:

      #. using `api._list_index({'category': '...'})` is faster,
         but no `isCustomerContent` field,
         needs to know where is the end index of builtins

      #. delete methods are the same when using uri but id

- Export OSBP recipe can be more simple

- Let settings and customized OSBPs data as .txt file so that even notepad can open it.

- Verification:
  Given `A` is the exported.
  Import `A` to another Altair and export from the Altair as `B`.
  Check if `A` is the same with `B`.

- Remove data is not necessary; consider update just necessary part with diff feature (not implement yet)

- Need modulization.


After discussion
==============================

[✓] Merge export cust feature to API class
[✓] Use methods that fetching index and then retrieving one by one
[✓] Use imperative to rewrite fetching
[✓] Only export scripts and config files of customized OSBPs
[✓] Use index data to fast distinguish customized data
[✓] The YAML file data structure has been added `ogfsScript` and `serverScript`.
    So now it looks like that::

      osbp:
          $name:
              attr: ...
              desc: ...
              type: ...
              steps:
                  - { name: ... , type: ... , para: ... }
                  - { name: ... , type: ... , para: ... }
      ogfsScript:
          $name: { desc: ... , cont: ... , type: ... }
      serverScript:
          $name: { desc: ... , cont: ... , type: ... , sudo: ... }
      config:
          $name: { desc: ... , cont: ... }

[✓] Add "all" argument to fetch all cust even if it is not belong to any OSBP
[ ] Update usage to wiki
[ ] Write wiki to remind user that the recipes are based on *name*
[ ] If package name is a little different, think as same
[ ] Merge imporing feature and collect some useful function to API class

Altair:
[ ] 統一 naming REST API
[ ] 令訊息更明確
[ ] Add `verbose` option or logger to methods
[ ] Replace assertion error with customized Altair API exceptions
[ ] Let some REST call can be wait and retry (how to design??)


Wiki
====

Requirement
Python 2.7.x – https://www.python.org/downloads/
Git – https://git-scm.com/download/
Accessibility of recipe source code – git clone ssh://apua.juan@cgit-pro.austin.hp.com:29418/altair-recipe
Please install Python and use git clone to get Altair recipe, and enter into "altair-reciep/update_osbp_recipe".
There is a setting file "settings.txt.template". Please edit it and save as "settings.txt".


Backup
======

.. code:: Python

    # let's test!!

    api._add_cfgfile({'type':'OsdCfgFile', 'name':'Apua01', 'description':'A__a', 'text':'= =a'})
    api._add_ogfsScript({
        'type': "OSDOGFSScript",
        'name': 'Apua06',
        'description': '=___=+',
        'source': '>///<',
        })
    api._add_serverScript({
        'type': "OSDServerScript",
        'codeType': 'VBS', #"BAT", "OGFS","PY2", "SH", "VBS"
        'name': 'Apua05',
        'description': '=___=+',
        'source': '>///<',
        'runAsSuperUser': True,
        "serverChanging": True,
        })
    j = api._add_OSBP({
        'type': 'OSDBuildPlan',
        'modified':'0000-00-00T00:00:00.000Z',
        'arch': 'x64',
        'name': 'Apua021',
        'description': 'qwer',
        'os': 'Other', # osbp['type']
        'buildPlanItems': [
            {
                'parameters':'.......',
                'uri':'/rest/os-deployment-server-scripts/820001',
                'cfgFileDownload': step['type']=='configs',
                },
            ],
        'buildPlanCustAttrs': [{'attribute': 'xxx', 'value': 'ooo'}], #osbp['attr']
        })
    print(j)

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
            except Exception as E:
                raw_input(E.message)


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
                    'os': osbp['type'],
                    'buildPlanCustAttrs': [], #osbp['attr'],
                    'buildPlanItems': steps,
                    })
                print(name)
                time.sleep(3)
                break
            except Exception as E:
                print(name)
                print(E.message)
                print('='*30)
                if raw_input()=='pass':
                    break
                else:
                    continue
