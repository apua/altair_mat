from __future__ import print_function
from colorprint import print
from altair import Altair


# Retrieve customized data from current Altair
with Altair(appliance_ip = 'csi-altair.twn.hp.com',
            username = 'administrator',
            password = 'Compaq123') as api:

    user_data = {
        "emailAddress": 'HPSCSISWTAIPEI@hp.com',
        "enabled": True,
        "fullName": 'CSI User',
        "mobilePhone": "",
        "officePhone": "",
        "password": 'Hp@taipei',
        "userName": 'csi',
        #"roles": ["Server administrator"],
        }
    
    #api.add_users(user_data)
    api.update_user_role(user='csi', roles=['Server administrator']) 

    #api.delete_user(user='qwer')

    #print(api.retrieve_network())

    media_server = {
        u'__OPSW-Media-WinPath': u'@10.20.7.14/deployment',
        u'__OPSW-Media-WinPassword': u'Compaq123',
        u'__OPSW-Media-LinURI': u'http://10.20.7.14/deployment',
        u'__OPSW-Media-WinUser': u'smb://administrator:'
        }

    facility = api.retrieve_facility(1)
    facility['customAttributes'].update(media_server)
    api.edit_facility(1, facility)
