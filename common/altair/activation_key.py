from base64 import b64encode, b64decode

def get_activation_status(api):
    resp = api._retrieve_activation()
    status = resp['status'].lower()
    if status not in ('activated', 'trial', 'trial_expired', 'unactivated'):
        raise NotImplementedError
    return status

def get_activation_key(api):
    resp = api._retrieve_activation()
    status = resp['status'].lower()
    if status in ('activated',):
        return b64encode(resp['activationCode'])

def set_activation_key(api, key_):
    activation = api._retrieve_activation()
    activation['activationCode'] =  b64decode(key_)
    api._send_activation(activation)
