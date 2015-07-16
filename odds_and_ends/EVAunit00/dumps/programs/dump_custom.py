from __future__ import print_function

from altair import Altair

from colorprint import print


with Altair(appliance_ip = '10.30.1.239',
            username = 'administrator',
            password = 'Compaq123') as api:
    '''
    j = api.list_cfgfile()
    with open('cfgfile_dump.json','w') as fp:
        import json
        json.dump(j['members'], fp, indent=2)
    j = api.list_OSBP()
    with open('osbp_dump.json','w') as fp:
        import json
        json.dump(j['members'], fp, indent=2)
    j = api.list_serverScript()
    with open('serverscript_dump.json','w') as fp:
        import json
        json.dump(j['members'], fp, indent=2)
    '''

