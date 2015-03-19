import requests

from .tools import _generate_uri, _failure_information


# Appliance Eula
# --------------

def accept_Eula(appliance_ip, supportAccess):
    """
    basic usage:
        supportAccess ("yes"/"no") -> supportAccess, version
    """
    assert supportAccess.lower() in ('yes', 'no')
    response = requests.post(
        _generate_uri(
            netloc = appliance_ip,
            path = "/rest/appliance/eula/save",
        ),
        headers = {
            "X-API-Version": 1,
            "Accept-Language": "en_US",
            },
        json = {
            "supportAccess": supportAccess,
        },
        verify = False,
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


def retrieve_Eula(appliance_ip, ):
    """
    basic usage:
        None -> Boolean
    """
    response = requests.get(
        _generate_uri(
            netloc = appliance_ip,
            path = "/rest/appliance/eula/status",
            ),
        headers = {
            "X-API-Version": 1,
            "Accept-Language": "en_US",
            },
        json = {},
        verify = False,
        )
    assert response.status_code==200, _failure_information(response)
    return response.json()


