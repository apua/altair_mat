from common import *

from pyVim.connect import SmartConnection
from pyVmomi import vim


USAGE_MESSAGE = 'usage: %s vmname [requirement_settings]' % __file__


if len(sys.argv)==2:
    vmname, config = sys.argv[1], get_config(script_related(__file__, 'esxi.cfg'))
elif len(sys.argv)==3:
    vmname, config = sys.argv[1], get_config(sys.argv[2])
else:
    exit(USAGE_MESSAGE)

password = getpass('vSphere password: ')

try:
    del os.environ['http_proxy']
    del os.environ['https_proxy']
except:
    pass

with SmartConnection(host=config['vcenter'],
                     user=config['account'],
                     pwd=password) as si:
    content = si.content
    objView = content.viewManager.CreateContainerView(
        content.rootFolder, [vim.VirtualMachine], True
        )
    vm = next(vm for vm in objView.view if vm.name==vmname)
    objView.Destroy()

    while vm.guest.ipAddress is None:
        time.sleep(3)
    else:
        ip = vm.guest.ipAddress

    print(ip)
