class Altair(object):

    # media settings, product keys, facility attributes
    # =================================================

    def get_media_settings(self):
        pass

    def set_media_settings(self, settings):
        pass

    def get_product_keys(self):
        pass

    def set_product_keys(self, keys):
        pass

    def get_facility_attributes(self):
        pass

    def set_facility_attributes(self, attrs):
        pass

    # the activation key
    # ==================

    def get_activation_key(self):
        from base64 import b64encode
        key = ''
        return b64encode(key)

    def set_activation_key(self, key_):
        from base64 import b64decode
        key = b64decode(key_)
        pass

    # OSBPs and related
    # =================

    def get_osbps(self):
        pass

    def upload_osbps(self, osbps):
        pass

    # WinPE
    # =====

    def upload_winpe(self, abs_path):
        pass

    # users
    # =====

    def get_users(self):
        return {}

    def add_user(self, user_data):
        pass

    def update_user(self, user_data):
        pass

    def change_password(self, new_password):
        pass

    # network
    # =======

    def get_network_settings(self):
        '''
        include DHCP server
        '''
        return {}


def collect_methods(*module_names):
    from importlib import import_module

    for module_name in module_names:
        module = import_module(module_names, __path__)
        for attr_name in dir(module):
            if not attr_name.startswith('_'):
                attr_value = getattr(module, attr_name)
                yield attr_name, attr_value


for name, method in collect_methods():
    setattr(Altair, '_'+name, method)

for name, method in collect_methods():
    setattr(Altair, name, method)
