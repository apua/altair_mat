from __future__ import print_function

import requests


class Altair(object):

    def __init__(self, appliance_ip, username, password, trust_env=False):

        # build HTTP connection session
        self.conn = requests.Session()
        self.conn.trust_env = trust_env
        self.conn.verify = False

        # set target appliance and authenticate
        self.appliance_ip = appliance_ip
        self.username = username
        self.session_id = self._authenticate(
             username=username,
             password=password,
             )['sessionID']

    def __enter__(self):
        '''
        test if session is outdated
        '''
        self._retrieve_session()
        return self

    def __exit__(self, type, value, traceback):
        self._remove_session()
        self.conn.close()

    # media settings, product keys, facility attributes, pxeboot default
    # ==================================================================

    def get_media_settings(self):
        customAttributes = self._retrieve_facility(1)['customAttributes']
        media_settings = {k: v for k, v in customAttributes.items()
                               if k.startswith('__OPSW-Media')}
        media_settings['__OPSW-Media-WinPassword'] = ''
        return media_settings

    def get_product_keys(self):
        customAttributes = self._retrieve_facility(1)['customAttributes']
        product_keys = {k: v for k, v in customAttributes.items()
                             if k.startswith('ProductKey_')}
        return product_keys

    def get_facility_attributes(self):
        customAttributes = self._retrieve_facility(1)['customAttributes']
        product_keys = {k: v for k, v in customAttributes.items()
                             if not k.startswith('ProductKey_') and
                                not k.startswith('__OPSW') and
                                k != 'device_discovery_naming_rules'}
        return product_keys

    def get_pxeboot_default(self):
        customAttributes = self._retrieve_facility(1)['customAttributes']
        attr_name = '__OPSWpxeboot_default'
        return {attr_name: customAttributes[attr_name]}

    def set_media_settings(self, settings):
        facility = self._retrieve_facility(1)
        facility['customAttributes'].update(settings)
        self._edit_facility(1, facility)

    def set_product_keys(self, keys):
        facility = self._retrieve_facility(1)
        facility['customAttributes'].update(keys)
        self._edit_facility(1, facility)

    def set_facility_attributes(self, attributes):
        facility = self._retrieve_facility(1)
        facility['customAttributes'].update(attributes)
        self._edit_facility(1, facility)

    def set_pxeboot_default(self, default):
        facility = self._retrieve_facility(1)
        facility['customAttributes'].update(default)
        self._edit_facility(1, facility)

    # the activation key
    # ==================

    def get_activation_key(self):
        from base64 import b64encode
        key = self._retrieve_activation()['activationCode']
        return b64encode(key)

    def set_activation_key(self, key_):
        from base64 import b64decode
        activation = self._retrieve_activation()
        activation['activationCode'] =  b64decode(key_)
        self._send_activation(activation)

    # OSBPs and related
    # =================

    def get_cust_info(self, *args, **kwargs):
        pass

    def upload_osbps(self, osbps):
        pass

    # WinPE
    # =====

    def upload_winpe(self, abs_path):
        pass

    # users
    # =====

    def get_users(self):
        def get_role(user):
            members = self._retrieve_user_role(user)['members']
            return (mem['roleName'] for mem in members)

        # Don`t know how to treat those special users yet,
        # since they invisible at first, visible after modified,
        # and no options talk about that.
        # So, just ignore them now.
        builtin_usernames = ('paul','ralph','april','rheid')
        users = [user for user in self._list_users()['members']
                      if user['userName'] not in builtin_usernames]
        for user in users:
            user['password'] = ''
            user['role'] = ', '.join(get_role(user['userName']))
        return users

    def add_user(self, user_data):
        def clean(user_data):
            from re import split
            keys = ('emailAddress', 'enabled', 'fullName', 'userName',
                    'mobilePhone', 'officePhone', 'password')
            cleaned_data = {k.lower(): v for k,v in user_data.items()}
            user_data = {k: cleaned_data[k.lower()] for k in keys}
            role = split(r',\s*', cleaned_data['role'])
            return user_data, role

        cleaned_user_data, role = clean(user_data)
        self._add_users(cleaned_user_data)
        self._update_user_role(cleaned_user_data['userName'], role)

    def update_user_info(self, user_data):
        def clean(user_data):
            from re import split
            keys = ('emailAddress', 'enabled', 'fullName', 'userName',
                    'mobilePhone', 'officePhone')
            cleaned_data = {k.lower(): v for k,v in user_data.items()}
            user_data = {k: cleaned_data[k.lower()] for k in keys}
            return user_data

        cleaned_user_data = clean(user_data)
        self._update_user(cleaned_user_data)

    def change_password(self, old_password, new_password):
        self._update_user({'userName': self.username,
                           'password': new_password,
                           'currentPassword': old_password})

    # network
    # =======

    def get_network_settings(self):
        '''
        include DHCP server
        '''
        return {}


def collect_members(*module_names):
    from importlib import import_module

    for module_name in module_names:
        module = import_module('.'+module_name, package=__package__)
        for attr_name in dir(module):
            if not attr_name.startswith('_'):
                attr_value = getattr(module, attr_name)
                yield attr_name, attr_value


for name, member in collect_members('rest_api'):
    setattr(Altair, '_'+name, member)

for name, member in collect_members('export_cust'):
    setattr(Altair, name, member)

for name, member in collect_members('init'):
    globals()[name] = member

requests.packages.urllib3.disable_warnings()
