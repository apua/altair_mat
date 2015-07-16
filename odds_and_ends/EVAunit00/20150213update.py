from altair import Altair


'''
with Altair(appliance_ip = '10.30.1.233',
            username = 'administrator',
            password = 'Compaq123') as api:

    facility_attr = api.retrieve_facility(1)['customAttributes']
    del facility_attr['device_discovery_naming_rules']
    facility_attr['__OPSW-Media-WinPassword'] = 'Compaq123'

    activation = {'activationCode': api.retrieve_activation()['activationCode']}

    data = {
        'facility_attr': facility_attr,
        'activation': activation,
        }
'''

'''
with Altair(appliance_ip = '10.30.1.235',#3',
            username = 'administrator',
            password = 'hpvse123') as api:#Compaq123') as api:

    facility = api.retrieve_facility(1)
    facility['customAttributes'].update(data['facility_attr'])
    api.edit_facility(1, facility)

    activation = api.retrieve_activation()
    activation.update(data['activation'])
    result = api.send_activation(activation)

    api.update_user({
        'currentPassword': 'hpvse123',
        'password': 'Compaq123',
        'userName': 'administrator',
        })
'''

'''
with Altair(appliance_ip = '10.30.1.235',
            username = 'administrator',
            password = 'Compaq123') as api:

    api.add_server({
        'ipAddress': '10.30.1.6',
        'password': 'Compaq123',
        'username': 'administrator',
        })
'''

with Altair(appliance_ip = '10.30.1.235',
            username = 'administrator',
            password = 'Compaq123') as api:
    pass
