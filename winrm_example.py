import winrm


def _setup_opener(self):
    import urllib2
    password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, self.endpoint, self.username, self.password)
    auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
    opener = urllib2.build_opener(auth_manager, urllib2.ProxyHandler({}))
    urllib2.install_opener(opener)

winrm.protocol.HttpPlaintext._setup_opener = _setup_opener


s = winrm.Session('10.30.1.63', auth=('administrator', 'Compaq123'))
r = s.run_cmd('ipconfig')
print(r.std_out)
print(r.status_code)
