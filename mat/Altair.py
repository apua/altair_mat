r"""
It is a Robot Framework Library which provides keywords to control Altair with API
"""

__import__('sys').path.append('../common/')

from inspect import getmembers
from robot.api import logger
from altair.api import Altair as API

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


def gen_unbound_method(name):
    def unbound_method(self, *a, **k):
        assert hasattr(self, "api"), \
               "To use Altair API, please set appliance IP and login first"
        return getattr(self.api, name)(*a, **k)
    unbound_method.__name__ = name
    return unbound_method


for name, value in getmembers(API):
    if name.startswith('_'):
        continue
    keyword = name
    unbound_method = gen_unbound_method(name)
    setattr(Altair, keyword, unbound_method)
