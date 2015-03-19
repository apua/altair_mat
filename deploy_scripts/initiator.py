from altair import Altair
from altair import retrieve_Eula, accept_Eula, reset_administrator_password
from pprint import pprint as p


'True'
p(
retrieve_Eula(appliance_ip='10.30.1.37')
)

'''
{u'supportAccess': u'yes',
 u'version': u'7.5.0-105696,2015-03-14T00:36:10-0600'}
'''
p(
accept_Eula(appliance_ip='10.30.1.37', supportAccess='yes')
)

'''
use `POST` but `PUT` = =+...
'''
reset_administrator_password('10.30.1.37', {
        "newPassword" : "qwer1234",
        "oldPassword" : "admin",
        "userName" : "administrator"
        })

with Altair(appliance_ip='10.30.1.37',
            username='administrator',
            password='qwer1234') as api:
    api._set_network({
        'type': 'ApplianceServerConfiguration',
        'applianceNetworks': [{
            'activeNode': 1,
            'aliasDisabled': False,
            'app1Ipv4Addr': '10.30.1.235',
            'app1Ipv4Alias': '10.30.1.236',
            'hostname': 'ci-005056986789',
            'interfaceName': 'Deployment',
            'ipv4Gateway': '10.30.1.254',
            'ipv4NameServers': [],
            'ipv4Subnet': '255.255.0.0',
            'ipv4Type': 'STATIC',
            'macAddress': '00:50:56:98:67:89',

            'app1Ipv6Addr': '',
            'app1Ipv6Alias': '',
            'app2Ipv4Addr': None,
            'app2Ipv4Alias': None,
            'app2Ipv6Addr': None,
            'app2Ipv6Alias': None,
            'bondedTo': None,
            'configurePostgresSslListener': False,
            'configureRabbitMqSslListener': False,
            'confOneNode': True,
            'device': 'eth0',
            'domainName': '',
            'ipv6Gateway': '',
            'ipv6NameServers': [],
            'ipv6Subnet': '',
            'ipv6Type': 'UNCONFIGURE',
            'overrideIpv4DhcpDnsServers': False,
            'overrideIpv6DhcpDnsServers': False,
            'searchDomains': None,
            'unconfigure': False,
            'virtIpv4Addr': None,
            'virtIpv6Addr': None,
            'webServerCertificateChain': None,
            'webServerCertificateKey': None,
            'webServerCertificate': None,
        }],
        'time': {
            'dateTime': None,
            'ntpServers': [],
            'pollingInterval': None,
            'timezone': 'UTC',
            },
    })
