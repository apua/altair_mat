from __future__ import print_function, absolute_import

from .utils import generate_uri, failure_information as _failure_information
from . import requests


class Altair(object):
    """
    support context manager
    """

    def __init__(self, appliance_ip, username, password, trust_env=False):
        # build HTTP connection session
        self.conn = requests.Session()
        self.conn.trust_env = trust_env
        self.conn.verify = False
        # set target appliance and authenticate
        self.appliance_ip = appliance_ip
        self.session_id = self.authenticate(
             username=username,
             password=password,
             )['sessionID']

    def __enter__(self):
        # if session is outdate, it would raise assertion error
        # refer `retrieve_session` method
        self.retrieve_session()
        return self

    def __exit__(self, type, value, traceback):
        self.remove_session()


    # DEPLOYMENT
    # ==========

    # Configuration Files
    # -------------------

    def list_cfgfile(self):
        """
        basic usage:
            sessionID -> members
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-install-cfgfiles",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def add_cfgfile(self, properties):
        """
        basic usage:
            sessionID, properties -> uri, name, description, text
        """
        response = self.conn.post(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-install-cfgfiles",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==201, _failure_information(response)
        return response.json()


    def retrieve_cfgfile(self, cfgfileID):
        """
        basic usage:
            sessionID, cfgfileID -> uri, name, description, text
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def edit_cfgfile(self, cfgfileID, properties):
        """
        basic usage:
            sessionID, cfgfileID, properties -> uri, name, description, text
        """
        response = self.conn.put(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def delete_cfgfile(self, cfgfileID):
        """
        basic usage:
            sessionID, cfgfileID -> None
        """
        response = self.conn.delete(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==204, _failure_information(response)
        return None


    # Deployment Settings
    # -------------------

    def list_deployment_settings(self):
        """
        basic usage:
            sessionID -> members (DHCP and FTS)
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-settings",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def retrieve_deployment_settings(self, uri):
        """
        basic usage:
            sessionID, uri -> JSON
        uri := (FTS, OsdDhcpConfig, WinPE, activation, MatrixPassword)
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-settings/{uri}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def edit_deployment_settings(self, uri, data):
        """
        basic usage:
            sessionID, uri, data -> JSON
        uri := (FTS, OsdDhcpConfig, WinPE, activation, MatrixPassword)
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-settings/{uri}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = data,
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def export_userDefined_content(self, *args, **kwargs):
        """export all user-defined content such as OSBP, script,..."""

    def import_userDefined_content(self, *args, **kwargs):
        """import all user-defined content such as OSBP, script,..."""

    def reconcileindex(self, *args, **kwargs):
        """sync items between webUI and Altair database"""

    def retrieve_file(self, *args, **kwargs):
        """retrieve files such as Media Server Tool and WinPE Tool"""


    # The four methods below are reference.


    def retrieve_FTS(self):
        """
        basic usage:
            sessionID -> ftsTasks
        FTS := first time setup
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-settings/FTS",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def edit_FTS(self, ftsTasks):
        """
        basic usage:
            sessionID -> ftsTasks
        """
        response = self.conn.put(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-settings/FTS",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {
                "ftsTasks": ftsTasks,
                },
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def retrieve_DHCP(self):
        """
        basic usage:
            sessionID -> value
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-settings/OsdDhcpConfig",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def edit_DHCP(self, dhcpState, subnetList):
        """
        basic usage:
            sessionID -> JSON
        """
        response = self.conn.put(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-settings/OsdDhcpConfig",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {
                "dhcpState": dhcpState,
                "subnetList": subnetList,
                },
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    # Device Groups
    # -------------

    # Facility
    # --------

    def list_facility(self):
        """
        basic usage:
            sessionID -> members
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-facility",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def retrieve_facility(self, facilityID):
        """
        basic usage:
            sessionID, facilityID -> customAttributes
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-facility/{facilityID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 1,#02,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def edit_facility(self, facilityID, properties):
        """
        basic usage:
            sessionID, facilityID, properties -> customAttributes
        """
        response = self.conn.put(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-facility/{facilityID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    # HP OneView Appliances
    # ---------------------

    # Jobs
    # ----

    # OGFS Scripts
    # ------------

    def list_ogfsScript(self):
        """
        basic usage:
            sessionID -> members
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-ogfs-scripts",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def add_ogfsScript(self, properties):
        """
        basic usage:
            sessionID, properties -> uri, name, codeType, description, source
        """
        response = self.conn.post(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-ogfs-scripts",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==201, _failure_information(response)
        return response.json()


    def retrieve_ogfsScript(self, ogfsScriptID):
        """
        basic usage:
            sessionID, ogfsScriptID -> uri, name, codeType, description, source
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-ogfs-scripts/{ogfsScriptID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def edit_ogfsScript(self, ogfsScriptID, properties):
        """
        basic usage:
            sessionID, ogfsScriptID, properties -> uri, name, codeType, description, source
        """
        response = self.conn.put(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-ogfs-scripts/{ogfsScriptID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def delete_ogfsScript(self, ogfsScriptID):
        """
        basic usage:
            sessionID, cfgfileID -> None
        """
        response = self.conn.delete(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==204, _failure_information(response)
        return None


    # OS Build Plans
    # --------------

    def list_OSBP(self):
        """
        basic usage: sessionID -> members
        ** never use it....it wil also list detail of every OSBPs **
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-build-plans",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def add_OSBP(self, properties, parentTask=None):
        """
        basic usage:
            sessionID, properties -> uri, name, description, os,
                                     buildPlanItems, buildPlanCustAttrs
        """
        response = self.conn.post(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-build-plans",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==201, _failure_information(response)
        return response.json()


    def retrieve_OSBP(self, buildPlanID):
        """
        basic usage:
            sessionID, buildPlanID -> uri, name, description, os,
                                      buildPlanItems, buildPlanCustAttrs
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-build-plans/{buildPlanID}".format(**locals()),
                ),
            headers = {
                #"X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def edit_OSBP(self, buildPlanID, properties):
        """
        basic usage:
            sessionID, buildPlanID, properties -> uri, name, description, os,
                                                  buildPlanItems, buildPlanCustAttrs
        """
        response = self.conn.put(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-build-plans/{buildPlanID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def delete_OSBP(self, buildPlanID):
        """
        basic usage:
            sessionID, buildPlanID -> None
        """
        response = self.conn.delete(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-build-plans/{buildPlanID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==204, _failure_information(response)
        return None


    # Packages
    # --------

    # Server Scripts
    # --------------

    def list_serverScript(self):
        """
        basic usage:
            sessionID -> members
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-server-scripts",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def add_serverScript(self, properties):
        """
        basic usage:
            sessionID, properties -> uri, name, codeType, runAsSuperUser, description, source

        """
        response = self.conn.post(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-server-scripts",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==201, _failure_information(response)
        return response.json()


    def retrieve_serverScript(self, serverScriptID):
        """
        basic usage:
            sessionID, serverScriptID -> uri, name, codeType, runAsSuperUser, description, source

        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-server-scripts/{serverScriptID}".format(**locals()),
                ),
            headers = {
                #"X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def edit_serverScript(self, serverScriptID, properties):
        """
        basic usage:
            sessionID, serverScriptID, properties -> uri, name, codeType, runAsSuperUser, description, source

        """
        response = self.conn.put(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-server-scripts/{serverScriptID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def delete_serverScript(self, serverScriptID):
        """
        basic usage:
            sessionID, cfgfileID -> None
        """
        response = self.conn.delete(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==204, _failure_information(response)
        return None


    # Servers
    # -------

    def list_server(self):
        """
        basic usage:
            sessionID -> members
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-servers",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def add_server(self, properties):
        """
        basic usage:
            sessionID, properties -> uri, name, description, customAttributes

        """
        response = self.conn.post(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-servers",
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==201, _failure_information(response)
        return response.json()


    def retrieve_server(self, serverID):
        """
        basic usage:
            sessionID, serverID -> uri, name, description, customAttributes

        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-servers/{serverID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def edit_server(self, serverID, properties):
        """
        basic usage:
            sessionID, serverID, properties -> uri, name, description, customAttributes

        """
        response = self.conn.put(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-servers/{serverID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = properties,
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def delete_server(self, serverID):
        """
        basic usage:
            sessionID, cfgfileID -> None
        """
        response = self.conn.delete(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
                ),
            headers = {
                "X-API-Version": 102,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==204, _failure_information(response)
        return None





    # SETTINGS
    # ========

    # Appliance Eula
    # --------------

    def accept_Eula(self, supportAccess):
        """
        basic usage:
            supportAccess ("yes"/"no") -> supportAccess, version
        """
        response = self.conn.post(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/appliance/eula/save",
            ),
            headers = {
                "X-API-Version": 1,
                "Accept-Language": "en_US",
                },
            json = {
                "supportAccess": supportAccess,
            },
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def retrieve_Eula(self, ):
        """
        basic usage:
            None -> Boolean
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/appliance/eula/status",
                ),
            headers = {
                "X-API-Version": 1,
                "Accept-Language": "en_US",
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    # Appliance Factory Reset
    # -----------------------

    def reset_factory(self, mode):
        """
        basic usage:
            sessionID, mode -> Location
        """
        #assert (mode in ("BEFORE_RESTORE", "FAILED_RESTORE", "FULL", "PRESERVE_NETWORK", "RECOVERY"))
        #assert (mode in ("FULL", "PRESERVE_NETWORK", "RECOVERY"))
        response = self.conn.delete(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/appliance",
                Query = {
                    "mode": mode,
                    },
                ),
            headers = {
                "X-API-Version": 100,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==202, _failure_information(response)
        return response.json()


    # Appliance Firmware
    # ------------------

    # Appliance Health-status
    # -----------------------

    # Appliance Network Interfaces
    # ----------------------------

    # Appliance Node Information
    # --------------------------

    # Appliance Shutdown
    # ------------------

    # Appliance Support Dumps
    # -----------------------

    # Backups
    # -------

    # Email notification
    # ------------------

    # Global Settings
    # ---------------

    # Licenses
    # --------

    # Restores
    # --------

    # Service Access
    # --------------

    def enable_service_access(self, enable):
        """
        basic usage:
            .. enable (Boolean) -> status ("Enabled"/"Disabled")
            enable (Boolean) -> True # it looks like the method not implemented as document said

        Authorization:
            Category: appliance
            Action: Update
        """
        response = self.conn.put(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/appliance/settings/enableServiceAccess",
            ),
            headers = {
                "X-API-Version": 1,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = enable,
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def retrieve_service_access(self):
        """
        basic usage:
            None -> Boolean
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/appliance/settings/serviceaccess",
            ),
            headers = {
                "X-API-Version": 1,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    # Startup Progress
    # ----------------

    def get_startup_status(self, ):
        """
        basic usage:
            None -> complete, total
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/appliance/progress",
                ),
            headers = {
                "X-API-Version": 100,
                "Accept-Language": "en_US",
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    # Version
    # -------

    def get_supported_API_version(self, ):
        """
        basic usage:
            None -> currentVersion, minimumVersion
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/version",
                ),
            headers = {},
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()





    # SECURITY
    # ========

    # Active User Sessions
    # --------------------

    # Authorizations
    # --------------

    def list_categories_and_actions(self):
        """
        basic usage:
            sessionID -> ??
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/authz/category-actions",
                ),
            headers = {
                "X-Api-Version": 1,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                "If-None-Match": None,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def list_roles_and_associated(self):
        """
        basic usage:
            sessionID -> ??
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/authz/role-category-actions",
                ),
            headers = {
                "X-Api-Version": 1,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def check_user_permission(self, actionDto, categoryDto):
        """
        basic usage:
            sessionID, actionDto, categoryDto -> Boolean
        """
        response = self.conn.post(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/authz/validator",
                ),
            headers = {
                "X-Api-Version": 1,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {
                "actionDto": actionDto,
                "categoryDto": categoryDto,
            },
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    # Certificate Authority
    # ---------------------

    # Certificates Client RabbitMq
    # ----------------------------

    # Client Certificates
    # -------------------

    # Login Domains
    # -------------

    # Login Domains Global Settings
    # -----------------------------

    # Login Domains Group To Role Mapping
    # -----------------------------------

    # Login Sessions
    # --------------

    def authenticate(self, username, password):
        """
        basic usage:
            username, password -> sessionID
        """
        response = self.conn.post(
   #     response = self.conn.post(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/login-sessions",
                ),
            headers = {
                "X-API-Version": 3,
                "Accept-Language": "en_US",
                },
            json = {
                "userName": username,
                "password": password,
                "authLoginDomain": None,
                "authnHost": None,
                },
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def reconnect_session(self):
        """
        Basic Usage:
            sessionID -> sessionID

        It looks like useless....?
        """
        response = self.conn.put(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/login-sessions",
                ),
            headers = {
                "X-API-Version": 3,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    def remove_session(self):
        """
        Basic Usage:
            sessionID -> None

        It is explict logout.
        """
        response = self.conn.delete(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/login-sessions",
                ),
            headers = {
                "X-API-Version": 3,
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==204, _failure_information(response)
        return None


    # Roles
    # -----

    # Sessions
    # --------

    def retrieve_session(self):
        """
        basic usage:
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/sessions",
                ),
            headers = {
                "X-API-Version": 1,
                "Accept-Language": "en_US",
                "Session-Keepalive": True,
                "Session-Id": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()

    def list_sessions(self):
        """
        basic usage:
        ** This feature can not be used. **
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/sessions/users",
                ),
            headers = {
                "X-API-Version": 1,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()

    # Users
    # -----

    # Web Server Certificates
    # -----------------------




    # ACTIVITY
    # ========

    # Alerts
    # ------

    # Audit Logs
    # ----------

    # Events
    # ------

    # Reports
    # -------

    # Tasks
    # -----

    def get_tasks(self):
        """
        basic usage:
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/tasks",
                ),
            headers = {
                "X-API-Version": 100,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    # SEARCH
    # ======

    # Index Associations
    # ------------------

    # Index Resources
    # ---------------

    def list_index(self, query):
        """
        basic usage:
        """
        response = self.conn.get(
            generate_uri(
                netloc = self.appliance_ip,
                path = "/rest/index/resources",
                Query = query,
                ),
            headers = {
                #"X-API-Version": 100,
                "Accept-Language": "en_US",
                "Auth": self.session_id,
                },
            json = {},
            )
        assert response.status_code==200, _failure_information(response)
        return response.json()


    # Index Search Suggestions
    # ------------------------

    # Index Trees
    # -----------


