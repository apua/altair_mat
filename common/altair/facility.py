def get_media_settings(self):
    customAttributes = self._retrieve_facility(1)['customAttributes']
    media_settings = {k: v for k, v in customAttributes.items()
                           if k.startswith('__OPSW-Media')}
    media_settings['__OPSW-Media-WinPassword'] = ''
    return media_settings

def get_product_keys(self):
    customAttributes = self._retrieve_facility(1)['customAttributes']
    product_keys = {k: v for k, v in customAttributes.items()
                         if k.startswith('ProductKey_')}
    return product_keys

def get_facility_attributes(self):
    customAttributes = self._retrieve_facility(1)['customAttributes']
    product_keys = {k: v for k, v in customAttributes.items()
                         if not k.startswith('ProductKey_') and
                            not k.startswith('__OPSW') and
                            k != 'device_discovery_naming_rules'}
    return product_keys

def get_pxeboot_default(self):
    customAttributes = self._retrieve_facility(1)['customAttributes']
    attr_name = '__OPSWpxeboot_default'
    return {attr_name: customAttributes[attr_name]}

def set_media_settings(self, settings):
    facility = self._retrieve_facility(1)
    facility['customAttributes'].update(settings)
    self._edit_facility(1, facility)

def set_product_keys(self, keys):
    facility = self._retrieve_facility(1)
    facility['customAttributes'].update(keys)
    self._edit_facility(1, facility)

def set_facility_attributes(self, attributes):
    facility = self._retrieve_facility(1)
    facility['customAttributes'].update(attributes)
    self._edit_facility(1, facility)

def set_pxeboot_default(self, default):
    facility = self._retrieve_facility(1)
    facility['customAttributes'].update(default)
    self._edit_facility(1, facility)
