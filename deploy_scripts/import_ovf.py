from common import *


USAGE_MESSAGE = 'usage: ./import_ovf.py ovffile[requirement_settings]'

if len(sys.argv)==2:
    ovffile, config = sys.argv[1], get_config(script_related(__file__, 'esxi.cfg'))
elif len(sys.argv)==3:
    ovffile, config = sys.argv[1], get_config(sys.argv[2])
else:
    exit(USAGE_MESSAGE)

password = getpass('vSphere password: ')

command = (
    'ovftool --noSSLVerify'
           ' --datastore={datastore}'
           ' --net:Template=Dev_Net'
           ' {ovffile}'
           ' vi://{account}:{password}@{vcenter}:443/{datacenter}/host/{host}/{resource}/'
    .format(ovffile=ovffile, password=password, **config)
    )

os.system(command)
