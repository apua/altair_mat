from common import *


if len(sys.argv)==2:
    given_ip = sys.argv[1]
    config = get_config(script_related(__file__, ALTAIR_SETTINGS))
elif len(sys.argv)==3:
    given_ip = sys.argv[1]
    config = get_config(sys.argv[2])
else:
    exit('usage: ./initiate.py ip [altair_settings]')


print('\nWait for booting:')
A.wait_boot(given_ip)

print('\nAccept EULA and disable support access')
if A.retrieve_eula(given_ip) is True:
    A.accept_eula(given_ip, supportAccess='no')

print('\nReset Administrator Password')
try:
    A.change_default_adminpass(given_ip, {
        'newPassword':  config['login user']['password'],
        'oldPassword' : 'admin',
        'userName' :    'administrator',
        })
except:
    pass

print('\nSet Appliance IP to %s' % config['network settings'][0]['app1Ipv4Addr'])
with Altair(appliance_ip=given_ip,
            username=config['login user']['userName'],
            password=config['login user']['password']) as api:
    J = api._retrieve_network()

    Networks = J['applianceNetworks']
    Time = J['time']


    # Now I only consider deployment network is same as appliance network
    Networks[0].update(config['network settings'][0])
    Networks[0]['ipv4Type'] = 'STATIC'
    ####


    api._set_network({
        'type': 'ApplianceServerConfiguration',
        'applianceNetworks': Networks, 
        'time': Time,
        })

