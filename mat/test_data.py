altair_ip = "10.30.1.235"
altair_admin_username = "Administrator"
altair_admin_password = "Compaq123"

Validate_MediaServer = "ProLiant SW - Validate Media Server Settings"

SUTs = [
    #{'ip': '10.30.1.6',     'account': 'administrator', 'password': 'Compaq123'},
    #{'ip':'16.153.112.91', 'account':'administrator', 'password':'Compaq123','serialno':'CN72050134'},
    {'ip':'16.153.112.173', 'account':'administrator', 'password':'Compaq123','serialno':'CN731403Z0'},
    ]

OSBPs = [
    "ProLiant OS - Windows 2012 R2 Standard x64 Scripted Install",
    "ProLiant OS - Windows 2012 Standard x64 Scripted Install",
    "ProLiant OS - Windows 2008 R2 SP1 Standard x64 Scripted Install",
    "ProLiant OS - Windows 2008 SP2 Standard x64 Scripted Install",
    "ProLiant OS - RHEL 7.1 x64 Scripted Install",
    "ProLiant OS - RHEL 7.0 x64 Scripted Install",
    "ProLiant OS - RHEL 6.6 x64 Scripted Install",
    "ProLiant OS - RHEL 6.5 x64 Scripted Install",
    "ProLiant OS - RHEL 6.4 x64 Scripted Install",
    "ProLiant OS - RHEL 5.11 x64 Scripted Install",
    "ProLiant OS - RHEL 5.9 x64 Scripted Install",
    "ProLiant OS - SLES 12 x64 Scripted Install",
    "ProLiant OS - SLES 11 SP3 x64 Scripted Install",
    "ProLiant OS - ESXi 5.5 Scripted Install",
    "ProLiant OS - ESXi 5.1 U3 Scripted Install",
    "ProLiant OS - ESXi 5.0 U2 Scripted Install",
    ]

MAT_pairs = [(s, o) for s in range(len(SUTs)) for o in range(len(OSBPs))]

vSphere = {
    'vcenter': '10.30.1.33',
    'vc_username': 'administrator@vsphere.local',
    'vc_password': 'Compaq123',
    'network': 'Dev_Net',
    'datastore': 'apua',
    'host': '10.30.1.14',
    'resource_pool': 'Resources',
    }
