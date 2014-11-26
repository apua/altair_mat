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

# Deployment Settings
# -------------------

# Device Groups
# -------------

# Facility
# --------

# HP OneView Appliances
# ---------------------

# Jobs
# ----

# OGFS Scripts
# ------------

# OS Build Plans
# --------------

# Packages
# --------

# Server Scripts
# --------------

# Servers
# -------




# SETTINGS
# ========

# Appliance Eula
# --------------

# Appliance Factory Reset
# -----------------------

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
            netloc = appliance,
            path = "/rest/login-sessions",
            ),
        headers = {
            "x-api-version": 3,
            "accept-language": "en_us",
            },
        json = {
            "username": username,
            "password": password,
            "authlogindomain": none,
            "authnhost": none
            },
        verify = false
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
    return response.json()


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
