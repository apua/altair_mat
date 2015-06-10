from .utils import (generate_uri as _generate_uri,
                    failure_information as _failure_information)


# ===
# API
# ===

# DEPLOYMENT
# ==========

# Configuration Files
# -------------------

def list_cfgfile(self):
    """
    basic usage:
        sessionID -> members
    """
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.post(
        _generate_uri(
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


def retrieve_cfgfile(self, cfgfileID=None, uri=None):
    """
    basic usage:
        sessionID, cfgfileID -> uri, name, description, text
    """
    assert (cfgfileID is None)+(uri is None)==1
    path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()) if uri is None else uri
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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


def edit_cfgfile(self, properties, cfgfileID=None, uri=None):
    """
    basic usage:
        sessionID, cfgfileID, properties -> uri, name, description, text
    """
    assert (cfgfileID is None)+(uri is None)==1
    path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()) if uri is None else uri
    response = self._conn.put(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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


def delete_cfgfile(self, cfgfileID=None, uri=None):
    """
    basic usage:
        sessionID, cfgfileID -> None
    """
    assert (cfgfileID is None)+(uri is None)==1
    path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()) if uri is None else uri
    response = self._conn.delete(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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

def export_content(self):
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = "/rest/os-deployment-settings/exportContent",
            ),
        headers = {
            "X-API-Version": 108,
            "Accept-Language": "en_US",
            "Auth": self.session_id,
            },
        json = {},
        )
    assert response.status_code==200, _failure_information(response)
    return response


def list_deployment_settings(self):
    """
    basic usage:
        sessionID -> members (DHCP and FTS)
    """
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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


def retrieve_activation(self):
    """
    """
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = "/rest/os-deployment-settings/activation",
            ),
        headers = {
            "X-API-Version": 104,
            "Accept-Language": "en_US",
            "Auth": self.session_id,
            },
        json = {},
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def send_activation(self, data):
    """
    """
    response = self._conn.put(
        _generate_uri(
            netloc = self.appliance_ip,
            path = "/rest/os-deployment-settings/activation",
            ),
        headers = {
            "X-API-Version": 104,
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.put(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.put(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.put(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.post(
        _generate_uri(
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


def retrieve_ogfsScript(self, ogfsScriptID=None, uri=None):
    """
    basic usage:
        sessionID, ogfsScriptID -> uri, name, codeType, description, source
    """
    assert (ogfsScriptID is None)+(uri is None)==1
    path = "/rest/os-deployment-ogfs-scripts/{ogfsScriptID}".format(**locals()) if uri is None else uri
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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


def edit_ogfsScript(self, properties, ogfsScriptID=None, uri=None):
    """
    basic usage:
        sessionID, ogfsScriptID, properties -> uri, name, codeType, description, source
    """
    assert (ogfsScriptID is None)+(uri is None)==1
    path = "/rest/os-deployment-ogfs-scripts/{ogfsScriptID}".format(**locals()) if uri is None else uri
    response = self._conn.put(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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


def delete_ogfsScript(self, ogfsScriptID=None, uri=None):
    assert (ogfsScriptID is None)+(uri is None)==1
    path = "/rest/os-deployment-ogfs-scripts/{ogfsScriptID}".format(**locals()) if uri is None else uri
    response = self._conn.delete(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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
    response = self._conn.get(
        _generate_uri(
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


def add_OSBP(self, properties):
    """
    basic usage:
        sessionID, properties -> uri, name, description, os,
                                 buildPlanItems, buildPlanCustAttrs
    """
    response = self._conn.post(
        _generate_uri(
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


def retrieve_OSBP(self, buildPlanID=None, uri=None):
    """
    basic usage:
        sessionID, buildPlanID -> uri, name, description, os,
                                  buildPlanItems, buildPlanCustAttrs
    """
    assert (buildPlanID is None)+(uri is None)==1
    path = "/rest/os-deployment-build-plans/{buildPlanID}".format(**locals()) if uri is None else uri
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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


def edit_OSBP(self, properties, buildPlanID=None, uri=None):
    """
    basic usage:
        sessionID, buildPlanID, properties -> uri, name, description, os,
                                              buildPlanItems, buildPlanCustAttrs
    """
    assert (buildPlanID is None)+(uri is None)==1
    path = "/rest/os-deployment-build-plans/{buildPlanID}".format(**locals()) if uri is None else uri
    response = self._conn.put(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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


def delete_OSBP(self, buildPlanID=None, uri=None):
    """
    basic usage:
        sessionID, buildPlanID -> None
    """
    assert (buildPlanID is None)+(uri is None)==1
    path = "/rest/os-deployment-build-plans/{buildPlanID}".format(**locals()) if uri is None else uri
    response = self._conn.delete(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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

def list_package(self):
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = "/rest/os-deployment-install-zips",
            ),
        headers = {
            #"X-API-Version": 108,
            "Accept-Language": "en_US",
            "Auth": self.session_id,
            },
        json = {},
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


# Server Scripts
# --------------

def list_serverScript(self):
    """
    basic usage:
        sessionID -> members
    """
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.post(
        _generate_uri(
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


def retrieve_serverScript(self, serverScriptID=None, uri=None):
    """
    basic usage:
        sessionID, serverScriptID -> uri, name, codeType, runAsSuperUser, description, source

    """
    assert (serverScriptID is None)+(uri is None)==1
    path = "/rest/os-deployment-server-scripts/{serverScriptID}".format(**locals()) if uri is None else uri
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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


def edit_serverScript(self, properties, serverScriptID=None, uri=None):
    """
    basic usage:
        sessionID, serverScriptID, properties -> uri, name, codeType, runAsSuperUser, description, source

    """
    assert (serverScriptID is None)+(uri is None)==1
    path = "/rest/os-deployment-server-scripts/{serverScriptID}".format(**locals()) if uri is None else uri
    response = self._conn.put(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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


def delete_serverScript(self, serverScriptID=None, uri=None):
    assert (serverScriptID is None)+(uri is None)==1
    path = "/rest/os-deployment-server-scripts/{serverScriptID}".format(**locals()) if uri is None else uri
    response = self._conn.delete(
        _generate_uri(
            netloc = self.appliance_ip,
            path = path,
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.post(
        _generate_uri(
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
    assert response.status_code==202, _failure_information(response)
    return response.json()


def retrieve_server(self, serverID):
    """
    basic usage:
        sessionID, serverID -> uri, name, description, customAttributes

    """
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.put(
        _generate_uri(
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
    response = self._conn.delete(
        _generate_uri(
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
    response = self._conn.post(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.delete(
        _generate_uri(
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

def retrieve_network(self):
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = '/rest/appliance/network-interfaces',
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


def retrieve_macs(self):
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = '/rest/appliance/network-interfaces/mac-addresses',
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


def set_network(self, network):
    response = self._conn.post(
        _generate_uri(
            netloc = self.appliance_ip,
            path = '/rest/appliance/network-interfaces',
            ),
        headers = {
            "X-API-Version": 100,
            "Accept-Language": "en_US",
            "Auth": self.session_id,
            },
        json = network,
        )
    assert response.status_code==202, _failure_information(response)
    return None




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
    response = self._conn.put(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.post(
        _generate_uri(
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
    response = self._conn.post(
        _generate_uri(
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
    response = self._conn.put(
        _generate_uri(
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
    response = self._conn.delete(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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

def list_users(self):
    """
    """
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = "/rest/users",
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

def retrieve_user_role(self, user):
    """
    """
    response = self._conn.get(
        _generate_uri(
            netloc = self.appliance_ip,
            path = "/rest/users/role/{user}".format(**locals()),
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

def add_users(self, users):
    """
    """
    response = self._conn.post(
        _generate_uri(
            netloc = self.appliance_ip,
            path = "/rest/users",
            Query = {'multiresource':true} if isinstance(users, list) else {},
            ),
        headers = {
            #"x-api-version": 100,
            "accept-language": "en_us",
            "auth": self.session_id,
            },
        json = users,
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()

def update_user(self, user):
    """
    """
    response = self._conn.put(
        _generate_uri(
            netloc = self.appliance_ip,
            path = "/rest/users",
            ),
        headers = {
            #"x-api-version": 100,
            "accept-language": "en_us",
            "auth": self.session_id,
            },
        json = user,
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()

def update_user_role(self, user, roles):
    """
    """
    response = self._conn.put(
        _generate_uri(
            netloc = self.appliance_ip,
            path = "/rest/users/role",
            ),
        headers = {
            #"x-api-version": 100,
            "accept-language": "en_us",
            "auth": self.session_id,
            },
        json = {
            'userName': user,
            'roles': roles,
            }
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def delete_user(self, user):
    """
    basic usage:
        sessionID, cfgfileID -> None
    """
    response = self._conn.delete(
        _generate_uri(
            netloc = self.appliance_ip,
            path = "/rest/users/{user}".format(**locals()),
            ),
        headers = {
            #"x-api-version": 100,
            "accept-language": "en_us",
            "auth": self.session_id,
            },
        json = {},
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


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
    response = self._conn.get(
        _generate_uri(
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
    response = self._conn.get(
        _generate_uri(
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
