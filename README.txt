====================
README
====================

This repository provides things below:
- An `Altair API` which can be context manager and Robot framework library.
- A `first time setup`_ recipe to export/import Altair appliance facility attributes.
- A `customized OSBP`_ recipe to export/import Altair appliance custmized OSBP.


Get the source
====================

There is a shell script `publish.sh` to publish git repo to FTP through SMB.

Users can download the archive from `ftp://csinfs.americas.hpqcorp.net/altair-recipe` with credential `csi/csi`.


Altair API
====================

The Altair API is a wrapper of the original REST API provided by Altair core team.
It provides common use methods for convenience and be low-level keywords in Robot framework.

Import API:

.. code:: python

    >>> __import__('sys').path.append('common')
    >>> from altair.api import Altair

Use Altair API login/logout manually:

.. code:: python

    >>> api = Altair("10.30.1.235")
    >>> api.login("administrator", "hpvse123")
    >>> api.is_logged_in() # api.session_id is not None
    True
    >>> api.logout()

Use Altair API as context manager:

.. code:: python

    >>> from pprint import pprint
    >>> with Altair("10.30.1.235", "administrator", "hpvse123") as api:
    ...     pprint(api.get_media_settings())
    ...
    {'file_share_host': '10.30.1.38',
     'file_share_name': '/deployment',
     'file_share_password': '......',
     'file_share_user': 'administrator',
     'http_server_host': '10.30.1.38',
     'http_server_path': '/deployment'}

Every methods in Altair API can be used as keywords in Robot framework.
First, create a Robot framework library as below:

.. code:: python

    # filename: Altair.py
    from altair.api import Altair

Then, one can write test data like this:

.. code:: robotframework

    *** Settings ***
    Library             Altair      10.30.1.235     administrator   hpvse123
    Suite Setup         Login
    Suite Teardown      Logout

    *** Test Cases ***
    Check login state
        ${logged}=          is logged in
        Should be true      ${logged}

    Show Media Settings
        ${settings}=        Get media settings
        Log to console      ${settings}


======================
Customized OSBP Recipe
======================
See:

https://rndwiki.corp.hpecorp.net/confluence/x/UbGXOw

=======================
First Time Setup Recipe
=======================
https://rndwiki.corp.hpecorp.net/confluence/display/csitestdevel/First+Time+Setup+recipe

Issues
======

[✓] Write on wiki
[✓] Improve the variable names in settings::
      __OPSW-Media-LinURI ->
          http_server_host
          http_server_path
      __OPSW-Media-WinPassword ->
          file_share_password
      __OPSW-Media-WinPath ->
          file_share_host
          file_share_name
      __OPSW-Media-WinUser ->
          file_share_user
[✓] Cleaned string::
    u'...' -> '...'
[✓] Implement upload WinPE feature and get/add SUTs features
[ ] Implement edit SUT custom attributes feature
[ ] REST API error handlers have to improve
    such as HTTP response not always have payload (JSON)
[ ] Test `export_altair_info.py`, `initiate_altair.py`, `first_time_setup.py`

=======================
Minimal Acceptance Test
=======================

These are Altair early MAT test data base on RoboGalaxy and Robot Framework.

Please refer to `<https://rndwiki.corp.hpecorp.net/confluence/x/mo2XOw>`_,
for more information about intallation and execution.


Command
=======

Dry Run:
`pybot -L trace -d reports  -i FTS -i add_suts --dryrun MAT`

Run:
`pybot -L trace -d reports  -i FTS -i add_suts MAT`





Issues
======

[✓] improve `add sut` that display progress
[✓] implement OSBP feature
[✓] improve job progress
[✓] refine `variables.py` generator
[ ] set custom attributues of SUTs
[ ] improve `wait job finish` messages
[ ] provide "run OSBPs test cases generator"




[ ] MAT - avoid user forget to set administrator password
[ ] MAT - "add user" should be idempotemt
[✓] recipe - "update administrator" feature
[ ] YAML dump can indicate newline charactor?
[ ] YAML dump with order dict


=======================================

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
[✓] Explain the requirements:
    + Python
    + Git (Finally, we just use CSINFS but Teamforge)
[✓] Support *custom attirbutes of osbps*
[✓] "export_cust_info" and "import_cust_info" are not explicit enough
    replaced with "export_custom_osbps" and "import_custom_osbps"

Altair:
[ ] 統一 naming REST API
[ ] 令訊息更明確
[ ] Add `verbose` option or logger to methods
[ ] Replace assertion error with customized Altair API exceptions
[ ] Let some REST call can be wait and retry (how to design??)

[✓] Let OSBP backup in DOS file format


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
