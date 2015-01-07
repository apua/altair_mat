import winrm


s = winrm.Session('10.30.1.63', auth=('administrator', 'Compaq123'))
r = s.run_cmd('ipconfig')
print(r.std_out)
print(r.status_code)
