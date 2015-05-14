altair_ip = "10.30.1.235"
altair_admin_username = "Administrator"
altair_admin_password = "hpvse123"

Validate_MediaServer = "ProLiant SW - Validate Media Server Settings"

SUTs = [
    {'ip':'16.153.112.91', 'account':'administrator', 'password':'Compaq123','serialno':'CN72050134'},
    {'ip': '10.30.1.6',     'account': 'administrator', 'password': 'Compaq123', 'serialno':'CN745108FZ'},
    #{'ip':'16.153.112.173', 'account':'administrator', 'password':'Compaq123','serialno':'CN731403Z0'},
    #{'ip':'10.20.2.9', 'account':'administrator', 'password':'Compaq123','serialno':'MX233800TB'},
    ]

vSphere = {
    'vcenter': '10.30.1.33',
    'vc_username': 'administrator@vsphere.local',
    'vc_password': 'Compaq123',
    'network': 'Dev_Net',
    'datastore': 'apua',
    'host': '10.30.1.14',
    'resource_pool': 'Resources',
    }
