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


def wait_boot(appliance_ip):
    from itertools import count
    import time
    import sys

    I = interval = 2
    C = connection_timeout = 2
    path = '/rest/appliance/progress'
    uri = _generate_uri(netloc=appliance_ip, path=path)
    headers = {'X-API-Version': 100}
    send_request = lambda t=C: requests.get(
        uri, headers=headers,
        verify=False, timeout=t
        )
    get_status_code = lambda: send_request().status_code
    get_json = lambda: send_request().json()
    write = lambda s: sys.stdout.write(s) or sys.stdout.flush()

    write('wait until network available ....')
    for t in count():
        i = (t+3)%4+1
        write('\b'*4 + '.'*i + ' '*(4-i))
        try:
            send_request()
            break
        except:
            pass
        time.sleep(I)
    write('\n')

    write('wait until OS turned on ....')
    for t in count():
        i = (t+3)%4+1
        write('\b'*4 + '.'*i + ' '*(4-i))
        try:
            status_code = get_status_code()
            if status_code==200:
                break
        except:
            pass
        time.sleep(I)
    write('\n')

    write('wait until service turned on ....' + ' '*5)
    for t in count():
        i = (t+3)%4+1
        try:
            j = get_json()
            p = 100.0 * j['complete'] / j['total']
            write('\b'*9 + '.'*i + ' '*(4-i) + ' %3.0f%%' % p)
            if j['complete'] == j['total']:
                break
        except:
            pass
        time.sleep(I)
    write('\n')
