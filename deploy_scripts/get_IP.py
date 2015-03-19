from pyVim.connect import SmartConnection
from pyVmomi import vim


with SmartConnection(host='10.30.1.33',
                     user='administrator@vsphere.local',
                     pwd='Compaq123') as si:
    content = si.content
    #print(dir(content))
    #print('root folder', content.rootFolder)
    #print(vim.VirtualMachine)
    objView = content.viewManager.CreateContainerView(
        content.rootFolder, [vim.VirtualMachine], True
        )

    vmname = 'ICsp-vmware-7.5.0-20150314'
    vm = next(vm for vm in objView.view if vm.name==vmname)
    objView.Destroy()

    IP = vm.guest.ipAddress
    print(IP)
