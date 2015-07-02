vsphere = {
    'vcenter':       '10.30.1.33',
    'username':      'administrator@vsphere.local',
    'password':      'Compaq123',
    'host':          '10.30.1.14',
    'resource_pool': 'Resources',
    'network':       'Dev_Net',
    'datastore':     'apua',
    }

basic_information = {
    'appliance_ip': '10.30.1.235',
    'password': 'hpvse123',
    'username': 'administrator',
    }

product_keys = {
    'ProductKey_Win2008-DC-x64': '9G777-PNWH4-3FMJT-C7VTR-GXT9Y',
    'ProductKey_Win2008-Ent-x64': 'C6DCB-VPXCT-MBB8B-WXPX9-TWV9M',
    'ProductKey_Win2008-Std-x64': 'C6DCB-VPXCT-MBB8B-WXPX9-TWV9M',
    'ProductKey_Win2008-Web-x64': 'HPXKY-B3479-B97V9-PGY3T-Q84HT',
    'ProductKey_Win2008R2-DC-x64': 'VX7GH-78HYP-PPWBG-DC3C4-MYBCD',
    'ProductKey_Win2008R2-Ent-x64': 'C6DCB-VPXCT-MBB8B-WXPX9-TWV9M',
    'ProductKey_Win2008R2-Fnd-x64': 'Q8T9W-4QMV6-GT9CX-TVR3T-2YCR4',
    'ProductKey_Win2008R2-HPC-x64': 'GF8KJ-9P8MD-6BKRF-MW7G3-WGXXT',
    'ProductKey_Win2008R2-Std-x64': 'CYPHP-RJ7XK-T8FQ4-V9XYB-HDB3H',
    'ProductKey_Win2008R2-Web-x64': 'GF8KJ-9P8MD-6BKRF-MW7G3-WGXXT',
    'ProductKey_Win2012-DC-x64': '9G777-PNWH4-3FMJT-C7VTR-GXT9Y',
    'ProductKey_Win2012-Std-x64': 'NHTXG-4Y82Y-CPJFW-RMYPV-T2763',
    'ProductKey_Win2012R2-DC-x64': 'YJQK4-VNR69-QGGY4-86FQQ-2WDW8',
    'ProductKey_Win2012R2-Std-x64': 'N4CM4-V7WVF-BB26H-QHBYP-DC9CJ',
    }

facility_attributes = {
    'EncryptedAdminPassword': 'QwBvAG0AcABhAHEAMQAyADMAQQBkAG0AaQBuAGkAcwB0AHIAYQB0AG8AcgBQAGEAcwBzAHcAbwByAGQA',
    '__apuatest': 'qwer',
    'encrypted_root_password': '$1$p2BVE2fU$IQv1Mski3vvSUsgEdQcMW1',
    }


winpe_source = '/ovf/icsp-winpe4.zip'

pxeboot_default = 'linux6-64-ogfs'

network_setting = {
    'appliance': {'gateway': '10.30.1.254',
                  'ip_address': '10.30.1.235',
                  'subnet': '255.255.0.0'},
    'deployment': {'ip_address': '10.30.1.236'},
    'dns': ['16.110.135.51', '16.110.135.52'],
    'hostname': 'ci-0050569322e9.dns.hp',
    }

media_settings = {
    'file_share_host': '10.30.1.38',
    'file_share_name': '/deployment',
    'file_share_password': 'Compaq123',
    'file_share_user': 'administrator',
    'http_server_host': '10.30.1.38',
    'http_server_path': '/deployment',
    }

suts = [
    {'custom_attributes': {},
     'ilo_ip_address': '16.153.112.91',
     'password': 'Compaq123',
     'username': 'administrator'},
    #{'custom_attributes': {},
    # 'ilo_ip_address': '10.30.1.54',
    # 'password': 'Compaq123',
    # 'username': 'administrator'},
    ]

activation_key = 'MzVWTlotSjJDSkMtNTdER1QtWjVWSlItWlI4Qzc='

users = [
    {'email': 'HPSCSISWTAIPEI@hp.com',
     'full_name': 'CSI User',
     'login_name': 'csi',
     'mobile_phone': '',
     'office_phone': '',
     'password': 'Hp@taipei',
     'roles': ['Server administrator']},
    {'email': '',
     'full_name': 'Default appliance administrator',
     'login_name': 'administrator',
     'mobile_phone': '',
     'office_phone': '',
     'password': 'Compaq123',
     'roles': ['Infrastructure administrator']},
    ]
