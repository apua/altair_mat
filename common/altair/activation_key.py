from base64 import b64encode, b64decode

def get_activation_key(api):
    key = api._retrieve_activation()['activationCode']
    return b64encode(key)

def set_activation_key(api, key_):
    activation = api._retrieve_activation()
    activation['activationCode'] =  b64decode(key_)
    api._send_activation(activation)
