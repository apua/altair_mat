def get_suts(api):
    def get_attr(sut):
        cust_attrs = {}
        for d in sut['customAttributes']:
            name, scope, value = d['key'], d['values'][0]['scope'], d['values'][0]['value']
            if scope!='facility' and not name.startswith('__OPSW'):
                cust_attrs[name] = value
        return cust_attrs

    suts = (api._retrieve_server(uri=m['uri'])
            for m in api._list_index({'category': 'osdserver'})['members'])
    return [{'ilo_ip_address': sut['ilo']['ipAddress'],
             'username': sut['ilo']['username'],
             'password': '....',
             'custom_attributes': get_attr(sut)}
            for sut in suts]

def add_sut(api, setting):
    properties = {'port': 443,
                  'ipAddress': setting['ilo_ip_address'],
                  'username': setting['username'],
                  'password': setting['password']}
    return api._add_server(properties)['uri']
