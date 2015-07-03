r"""
It is a Robot Framework Library which provides keywords to control Altair with API
"""

__import__('sys').path.append('../common/')

from robot.api import logger

from altair.api import Altair as API
from altair import utils
utils.output.method = logger.console


class Altair(object):
    r"""
    A hybrid library class
    """
    ROBOT_LIBRARY_VERSION = __version__ = '0.142857'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def set_appliance_ip(self, appliance_ip):
        self.api = API(appliance_ip)
        return self.api

    def get_session_id(self):
        assert hasattr(self, "api"), \
               "To use Altair API, please set appliance IP and login first"
        return self.api.session_id

    def set_users(self, users):
        existed = {user['login_name'] for user in self.get_users()}
        failed = []
        for user in users:
            method = self.update_user if user['login_name'] in existed else self.add_user
            try:
                method(user)
                self.change_password(user['password'], user['login_name'])
            except:
                failed.append((method.__name__, user['login_name']))

        if failed:
            raise Exception("Some users are add/update failed: {}".format(failed))


def gen_unbound_method(name):
    def unbound_method(self, *a, **k):
        assert hasattr(self, "api"), \
               "To use Altair API, please set appliance IP and login first"
        return getattr(self.api, name)(*a, **k)
    unbound_method.__name__ = name
    return unbound_method


for name in dir(API):
    if name.startswith('_'):
        continue
    keyword = name
    unbound_method = gen_unbound_method(name)
    setattr(Altair, keyword, unbound_method)
