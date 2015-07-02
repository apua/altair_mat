from __future__ import absolute_import

from sys import stdout

import requests
from .rest_api import RestAPI
from .utils import generate_uri, failure_information

class Altair(RestAPI):
    r"""
    Usage
    =====

    1.  with Altair(appliance_ip, username, password) as api:
            ...

    2.  api = Altair(appliance_ip, username, password)
        with api:
            ...

    3.  api = Altair(appliance_ip, username, password)
        api.login()
        try:
            ...
        finally:
            api.logout()
    """
    def __init__(self, appliance_ip, username=None, password=None, trust_env=False):
        r"""
        api = Altair(appliance_ip)
        api = Altair(appliance_ip, username, password)
        """
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
        self.login()
        return self

    def __exit__(self, type, value, traceback):
        self.logout()

    def login(self, username=None, password=None):
        r"""
        api.login()
        api.login(username, password)
        """
        if username is None and password is None:
            self.session_id = self._authenticate(self.username, self.password)['sessionID']
        elif username is not None and password is not None:
            self.session_id = self._authenticate(username, password)['sessionID']
            self.username = username
            self.password = password
        else:
            raise Exception('Should set username and password')

    def logout(self):
        self._remove_session()
        self.session_id = None

    # media settings, product keys, facility attributes, pxeboot default
    # ==================================================================

    from .facility import (get_media_settings,
                           get_product_keys,
                           get_facility_attributes,
                           get_pxeboot_default,
                           set_media_settings,
                           set_product_keys,
                           set_facility_attributes,
                           set_pxeboot_default)

    # the activation key
    # ==================

    from .activation_key import get_activation_key, set_activation_key

    # OSBPs and related
    # =================

    from .export_cust import export_cust_info
    from .import_cust import import_cust_info

    # WinPE
    # =====

    def upload_winpe(self, abs_path, write=None):
        if write is None:
            def write(s):
                stdout.write(s)
                stdout.flush()

        def callback(monitor):
            if not callback.disable:
                show_text = '{:7.2f}%'.format(100. * monitor.bytes_read / monitor.len)
                if monitor.bytes_read != monitor.len:
                    write(show_text + '\b'*8)
                else:
                    callback.disable = True
                    write(show_text + ' waiting Altair response... ')
        callback.disable = False

        self._upload_winpe(abs_path, callback=callback)

    # users
    # =====
    from .users import (get_users, add_user, delete_user,
                        get_user_info, update_user_info,
                        change_own_password)

    # network
    # =======

    from .network import get_network_setting, set_network

    # first time setup
    # ================

    def setup(self):
        passwd_info = {'newPassword':self.password,
                       'oldPassword':'admin',
                       'userName':'administrator'}
    
        supportAccess, version = self._accept_Eula(supportAccess='no')
        self._change_default_adminpass(passwd_info)

    # SUTs
    # ====

    from .sut import get_suts, add_sut, set_sut

requests.packages.urllib3.disable_warnings()
