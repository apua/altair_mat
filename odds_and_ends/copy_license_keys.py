# -*-coding=utf8-*-

from __future__ import print_function
from pprint import pprint as print
import requests


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
    template = "\nstatus code => {}\ncontent => {}"
    return template.format(response.status_code, _add_indent(response.json()))


# ========
# REST API
# ========


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
        json = {},
        verify = False
        )
    assert response.status_code==204, _failure_information(response)
    return None



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
        json = {},
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
        json = {},
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


if __name__=='__main__':
    src = {'appliance': '10.100.0.5',
           'username': 'administrator',
           'password': 'hpinvent'}
    dst = {'appliance': '10.100.0.7',
           'username': 'april',
           'password': 'applianceadmin'}

    '''
    APPLIANCE = src['appliance']
    src['session'] = authenticate(username=src['username'],
                                  password=src['password']).get('sessionID')
    try:
        payload = retrieve_facility(sessionID=src['session'], facilityID=1)
        keys = {k:v for k,v in payload['customAttributes'].iteritems()
                    if k.startswith('Product')}
        from pprint import pprint as print
        #print(payload)
        print(len(keys)); print(keys)
    finally:
        remove_session(sessionID=src['session'])
    '''

    keys = {u'ProductKey_Win2008-DC-x64': u'C9QWY-XPVWF-WGRBF-KK48F-WPWG9',
            u'ProductKey_Win2008-Ent-x64': u'9CJRX-D98XB-PWFDC-TWTXJ-4XTXD',
            u'ProductKey_Win2008-Std-x64': u'9CJRX-D98XB-PWFDC-TWTXJ-4XTXD',
            u'ProductKey_Win2008-Web-x64': u'HV9RJ-BVWYD-TBK9M-VDM3P-Q2WJB',
            u'ProductKey_Win2008R2-DC-x64': u'2Y2TG-3JJBJ-HMVY7-9QWQJ-P8VJR',
            u'ProductKey_Win2008R2-Ent-x64': u'CYPHP-RJ7XK-T8FQ4-V9XYB-HDB3H',
            u'ProductKey_Win2008R2-Fnd-x64': u'74YFP-3QFB3-KQT8W-PMXWJ-7M648',
            u'ProductKey_Win2008R2-Std-x64': u'CYPHP-RJ7XK-T8FQ4-V9XYB-HDB3H',
            u'ProductKey_Win2008R2-Web-x64': u'GF8KJ-9P8MD-6BKRF-MW7G3-WGXXT',
            u'ProductKey_Win2012-DC-x64': u'QK88F-NDM7Y-XY4B7-WTC33-3PBT8',
            u'ProductKey_Win2012-Std-x64': u'VKNY3-J9799-FDCFM-R9BRX-CDG9P',
            u'ProductKey_Win2012R2-DC-x64': u'JGXYY-7NMTC-MHKY3-QCC9B-VQRG7',
            u'ProductKey_Win2012R2-Std-x64': u'N4CM4-V7WVF-BB26H-QHBYP-DC9CJ'}
    print(len(keys)); print(keys)

    APPLIANCE = dst['appliance']
    dst['session'] = authenticate(username=dst['username'],
                                  password=dst['password']).get('sessionID')
    try:
        payload = retrieve_facility(sessionID=dst['session'], facilityID=1)
        #keys = {k:v for k,v in payload['customAttributes'].iteritems()
        #            if k.startswith('Product')}
        
        #print(payload)
        #print(len(keys)); print(keys)
        payload['customAttributes'].update(keys)
        edit_facility(sessionID=dst['session'], facilityID=1, properties=payload)
        payload = retrieve_facility(sessionID=dst['session'], facilityID=1)
        keys = {k:v for k,v in payload['customAttributes'].iteritems()
                    if k.startswith('Product')}
        print(keys)
    finally:
        remove_session(sessionID=dst['session'])
