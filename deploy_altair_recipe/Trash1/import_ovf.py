import os

command = 'ovftool --noSSLVerify --datastore=apua --net:Template=Dev_Net {ovf_file} vi://{account}:{password}@{vcenter}:443/automation/host/{host}/Resources/
'
os.system(command)
