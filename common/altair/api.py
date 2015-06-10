import requests
from rest_api import RestAPI


class Altair(RestAPI):

    def __init__(self, appliance_ip, username=None, password=None, trust_env=False):
        # given both username and password or not
        assert (username is None)==(password is None)

        # build HTTP connection session
        self._conn = requests.Session()
        self._conn.trust_env = trust_env
        self._conn.verify = False

        # set target appliance and authenticate
        self.appliance_ip = appliance_ip
        self.username = username
        self.password = password
        self.session_id = None

    def __enter__(self):
        # must set username and password already
        assert self.username is not None and self.password is not None
        self.login(self.username, self.password)
        return self

    def __exit__(self, type, value, traceback):
        self.logout()

    def login(self, username, password):
        self.session_id = self._authenticate(username, password)['sessionID']
        self.username = username
        self.password = password

    def logout(self):
        self._remove_session()
        self.session_id = None

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

    from export_cust import export_cust_info
    from import_cust import import_cust_info

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

    def change_password(self, new_password):
        self._update_user({'userName': self.username,
                           'password': new_password,
                           'currentPassword': self.password})

    # network
    # =======

    def get_network_settings(self):
        '''
        include DHCP server
        '''
        return {}

requests.packages.urllib3.disable_warnings()
