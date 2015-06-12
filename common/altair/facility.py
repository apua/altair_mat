from .utils import clean_unicode as clean

def retrieve_custom_attributes(api, key_filter=lambda x:True):
    """
    Get custom attributes, filter, and clean unicode
    """
    return clean({k:v for k,v in api._retrieve_facility(1)['customAttributes'].items() if key_filter(k)})

def update_custom_attributes(api, settings):
    """
    Update custom attributes by given settings
    """
    facility = api._retrieve_facility(1)
    facility['customAttributes'].update(settings)
    api._edit_facility(1, facility)

# Get
# ===

def get_media_settings(api):
    M = retrieve_custom_attributes(api, lambda k: k.startswith('__OPSW-Media'))
    return {'file_share_host': M['__OPSW-Media-WinPath'].split('/',1)[0][1:],
            'file_share_name': '/'+M['__OPSW-Media-WinPath'].split('/',1)[1],
            'file_share_user': M['__OPSW-Media-WinUser'].split('/',2)[2][:-1],
            'file_share_password': M['__OPSW-Media-WinPassword'],
            'http_server_host': M['__OPSW-Media-LinURI'].split('/',3)[2],
            'http_server_path': '/'+M['__OPSW-Media-LinURI'].split('/',3)[3]}

def get_product_keys(api):
    return retrieve_custom_attributes(api, lambda k: k.startswith('ProductKey_'))

def get_facility_attributes(api):
    return retrieve_custom_attributes(api, lambda k: not k.startswith('ProductKey_') and
                                                     not k.startswith('__OPSW') and
                                                     k != 'device_discovery_naming_rules')

def get_pxeboot_default(api):
    return retrieve_custom_attributes(api)['__OPSWpxeboot_default']

# Set
# ===

def set_media_settings(api, S):
    update_custom_attributes(api, {'__OPSW-Media-WinPath': '@'+S['file_share_host']+S['file_share_name'],
                                   '__OPSW-Media-WinUser': 'smb://'+S['file_share_user']+':',
                                   '__OPSW-Media-WinPassword': S['file_share_password'],
                                   '__OPSW-Media-LinURI': 'http://'+S['http_server_host']+S['http_server_path']})

def set_product_keys(api, keys):
    update_custom_attributes(api, keys)

def set_facility_attributes(api, attributes):
    update_custom_attributes(api, attributes)

def set_pxeboot_default(api, default):
    update_custom_attributes(api, {'__OPSWpxeboot_default': default})
