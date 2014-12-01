# -*-coding=utf8-*-

from __future__ import print_function


import requests


# Settings
# ========

APPLIANCE = "https://10.30.1.235"


# Tools
# =====

def generate_uri(netloc='localhost', path='', Query={}):
    """
    issues:
      - check if URI form is valid, refer RFC 3986

    >>> generate_uri(path='/rest/os-deployment-jobs/', Query={'force': 'true'})
    'https://localhost/rest/os-deployment-jobs/?force=true'
    >>> generate_uri('https://altair.dev-net.local', '/rest/os-deployment-jobs/')
    'https://altair.dev-net.local/rest/os-deployment-jobs/'
    """
    from urllib import quote
    from urlparse import urljoin

    if netloc.endswith('/'):
        netloc = netloc[:-1]
    if '://' in netloc:
        scheme, netloc = netloc.split('://')
    else:
        scheme, netloc = 'https', netloc
    if not path.startswith('/'):
        path = '/' + path
    query = '?'*bool(Query) + '&'.join(k+'='+quote(v) for k,v in Query.viewitems())
    return "{scheme}://{netloc}{path}{query}".format(**locals())


def _add_indent(json_content):
    from json import dumps
    return dumps(json_content, indent=2)


def _failure_information(response):
    template = "\n[32mstatus code[m => [33m{}[m\n[34mcontent[m => {}"
    return template.format(response.status_code, _add_indent(response.json()))


# ========
# REST API
# ========

#def method(*args, **kwargs):
#    """
#    HTTP_request Method Path Query Header Body
#    """

# DEPLOYMENT
# ==========

# Configuration Files
# -------------------

def list_cfgfile(sessionID):
    """
    basic usage:
        sessionID -> members
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-install-cfgfiles",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def add_cfgfile(sessionID, properties):
    """
    basic usage:
        sessionID, properties -> uri, name, description, text
    """
    response = requests.post(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-install-cfgfiles",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==201, _failure_information(response)
    return response.json()


def retrieve_cfgfile(sessionID, cfgfileID):
    """
    basic usage:
        sessionID, cfgfileID -> uri, name, description, text
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def edit_cfgfile(sessionID, cfgfileID, properties):
    """
    basic usage:
        sessionID, cfgfileID, properties -> uri, name, description, text
    """
    response = requests.put(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def delete_cfgfile(sessionID, cfgfileID):
    """
    basic usage:
        sessionID, cfgfileID -> None
    """
    response = requests.delete(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==204, _failure_information(response)
    return None


# Deployment Settings
# -------------------

# Device Groups
# -------------

# Facility
# --------

def list_facility(sessionID):
    """
    basic usage:
        sessionID -> members
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-facility",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def retrieve_facility(sessionID, facilityID):
    """
    basic usage:
        sessionID, facilityID -> customAttributes
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-facility/{facilityID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def edit_facility(sessionID, facilityID, properties):
    """
    basic usage:
        sessionID, facilityID, properties -> customAttributes
    """
    response = requests.put(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-facility/{facilityID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


# HP OneView Appliances
# ---------------------

# Jobs
# ----

# OGFS Scripts
# ------------

def list_ogfsScript(sessionID):
    """
    basic usage:
        sessionID -> members
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-ogfs-scripts",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def add_ogfsScript(sessionID, properties):
    """
    basic usage:
        sessionID, properties -> uri, name, codeType, description, source
    """
    response = requests.post(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-ogfs-scripts",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==201, _failure_information(response)
    return response.json()


def retrieve_ogfsScript(sessionID, ogfsScriptID):
    """
    basic usage:
        sessionID, ogfsScriptID -> uri, name, codeType, description, source
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-ogfs-scripts/{ogfsScriptID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def edit_ogfsScript(sessionID, ogfsScriptID, properties):
    """
    basic usage:
        sessionID, ogfsScriptID, properties -> uri, name, codeType, description, source
    """
    response = requests.put(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-ogfs-scripts/{ogfsScriptID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def delete_ogfsScript(sessionID, ogfsScriptID):
    """
    basic usage:
        sessionID, cfgfileID -> None
    """
    response = requests.delete(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==204, _failure_information(response)
    return None


# OS Build Plans
# --------------

def list_OSBP(sessionID):
    """
    basic usage:
        sessionID -> members
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-build-plans",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def add_OSBP(sessionID, properties, parentTask=None):
    """
    basic usage:
        sessionID, properties -> uri, name, description, os,
                                 buildPlanItems, buildPlanCustAttrs
    """
    response = requests.post(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-build-plans",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==201, _failure_information(response)
    return response.json()


def retrieve_OSBP(sessionID, buildPlanID):
    """
    basic usage:
        sessionID, buildPlanID -> uri, name, description, os,
                                  buildPlanItems, buildPlanCustAttrs
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-build-plans/{buildPlanID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def edit_OSBP(sessionID, buildPlanID, properties):
    """
    basic usage:
        sessionID, buildPlanID, properties -> uri, name, description, os,
                                              buildPlanItems, buildPlanCustAttrs
    """
    response = requests.put(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-build-plans/{buildPlanID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def delete_OSBP(sessionID, buildPlanID):
    """
    basic usage:
        sessionID, buildPlanID -> None
    """
    response = requests.delete(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-build-plans/{buildPlanID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==204, _failure_information(response)
    return None


# Packages
# --------

# Server Scripts
# --------------

def list_serverScript(sessionID):
    """
    basic usage:
        sessionID -> members
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-server-scripts",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def add_serverScript(sessionID, properties):
    """
    basic usage:
        sessionID, properties -> uri, name, codeType, runAsSuperUser, description, source

    """
    response = requests.post(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-server-scripts",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==201, _failure_information(response)
    return response.json()


def retrieve_serverScript(sessionID, serverScriptID):
    """
    basic usage:
        sessionID, serverScriptID -> uri, name, codeType, runAsSuperUser, description, source

    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-server-scripts/{serverScriptID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def edit_serverScript(sessionID, serverScriptID, properties):
    """
    basic usage:
        sessionID, serverScriptID, properties -> uri, name, codeType, runAsSuperUser, description, source

    """
    response = requests.put(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-server-scripts/{serverScriptID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def delete_serverScript(sessionID, serverScriptID):
    """
    basic usage:
        sessionID, cfgfileID -> None
    """
    response = requests.delete(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==204, _failure_information(response)
    return None


# Servers
# -------

def list_server(sessionID):
    """
    basic usage:
        sessionID -> members
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-servers",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def add_server(sessionID, properties):
    """
    basic usage:
        sessionID, properties -> uri, name, description, customAttributes

    """
    response = requests.post(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-servers",
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==201, _failure_information(response)
    return response.json()


def retrieve_server(sessionID, serverID):
    """
    basic usage:
        sessionID, serverID -> uri, name, description, customAttributes

    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-servers/{serverID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def edit_server(sessionID, serverID, properties):
    """
    basic usage:
        sessionID, serverID, properties -> uri, name, description, customAttributes

    """
    response = requests.put(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-servers/{serverID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = properties,
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def delete_server(sessionID, serverID):
    """
    basic usage:
        sessionID, cfgfileID -> None
    """
    response = requests.delete(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/os-deployment-install-cfgfiles/{cfgfileID}".format(**locals()),
            ),
        headers = {
            "X-API-Version": 102,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==204, _failure_information(response)
    return None





# SETTINGS
# ========

# Appliance Eula
# --------------

def accept_Eula():
    """
    basic usage:
        supportAccess -> supportAccess, version
    """
    response = requests.post(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/appliance/eula/save",
        ),
        headers = {
            "X-API-Version": 1,
            "Accept-Language": "en_US",
            },
        json = {
            "supportAccess": supportAccess,
        },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def retrieve_Eula():
    """
    basic usage:
        None -> Boolean
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/appliance/eula/status",
            ),
        headers = {
            "X-API-Version": 1,
            "Accept-Language": "en_US",
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


# Appliance Factory Reset
# -----------------------

def reset_factory(sessionID, mode):
    """
    basic usage:
        sessionID, mode -> Location
    """
    #assert (mode in ("BEFORE_RESTORE", "FAILED_RESTORE", "FULL", "PRESERVE_NETWORK", "RECOVERY"))
    #assert (mode in ("FULL", "PRESERVE_NETWORK", "RECOVERY"))
    response = requests.delete(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/appliance",
            Query = {
                "mode": mode,
                },
            ),
        headers = {
            "X-API-Version": 100,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
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

# Startup Progress
# ----------------

# Version
# -------




# SECURITY
# ========

# Active User Sessions
# --------------------

# Authorizations
# --------------

def list_categories_and_actions(sessionID):
    """
    basic usage:
        sessionID -> ??
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/authz/category-actions",
            ),
        headers = {
            "X-Api-Version": 1,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            "If-None-Match": None,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def list_roles_and_associated(sessionID):
    """
    basic usage:
        sessionID -> ??
    """
    response = requests.get(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/authz/role-category-actions",
            ),
        headers = {
            "X-Api-Version": 1,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def check_user_permission(sessionID, actionDto, categoryDto):
    """
    basic usage:
        sessionID, actionDto, categoryDto -> Boolean
    """
    response = requests.post(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/authz/validator",
            ),
        headers = {
            "X-Api-Version": 1,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        json = {
            "actionDto": actionDto,
            "categoryDto": categoryDto,
        },
        verify = False
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

def authenticate(username, password):
    """
    basic usage:
        username, password -> sessionID
    """
    response = requests.post(
        generate_uri(
            netloc = APPLIANCE,
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
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def reconnect_session(sessionID):
    """
    Basic Usage:
        sessionID -> sessionID

    It looks like useless....?
    """
    response = requests.put(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/login-sessions",
            ),
        headers = {
            "X-API-Version": 3,
            "Accept-Language": "en_US",
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def remove_session(sessionID):
    """
    Basic Usage:
        sessionID -> None

    It is explict logout.
    """
    response = requests.delete(
        generate_uri(
            netloc = APPLIANCE,
            path = "/rest/login-sessions",
            ),
        headers = {
            "X-API-Version": 3,
            "Auth": sessionID,
            },
        verify = False
        )
    assert response.status_code==204, _failure_information(response)
    return None


# Roles
# -----

# Sessions
# --------

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




# SEARCH
# ======

# Index Associations
# ------------------

# Index Resources
# ---------------

# Index Search Suggestions
# ------------------------

# Index Trees
# -----------
