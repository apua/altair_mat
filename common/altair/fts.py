from __future__ import absolute_import

from .utils import generate_uri, failure_information

def setup(api):
    supportAccess, version = api._accept_Eula(supportAccess='no')

    passwd_info = {'newPassword':api.password, 'oldPassword':'admin', 'userName':'administrator'}
    api._change_default_adminpass(passwd_info)
