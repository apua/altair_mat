from __future__ import absolute_import

import time

import requests
requests.packages.urllib3.disable_warnings()

from .rest_api import RestAPI
from .utils import output


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

    from .activation_key import (get_activation_status,
                                 get_activation_key, set_activation_key)

    # OSBPs and related
    # =================

    from .osbps import export_custom_osbps, import_custom_osbps

    # WinPE
    # =====

    def upload_winpe(self, abs_path):
        def callback(monitor):
            if not callback.disable:
                show_text = '{:7.2f}%'.format(100. * monitor.bytes_read / monitor.len)
                if monitor.bytes_read != monitor.len:
                    msg = show_text + '\b'*8
                else:
                    callback.disable = True
                    msg = show_text + ' waiting Altair response... '
                output(msg, newline=False)
        callback.disable = False

        self._upload_winpe(abs_path, callback=callback)

    # users
    # =====
    from .users import (add_user,
                        update_user, change_password,
                        get_users, get_user,
                        delete_user)

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

    from .sut import get_suts, add_sut

    def wait_job_finish(self, uri, interval=10):
        while 1:
            job = self._retrieve_job(uri=uri)
            if job['running']=='false':
                return job['status']
            time.sleep(interval)
