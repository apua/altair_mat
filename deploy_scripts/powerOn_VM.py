#!/usr/bin/env python
# -*- coding=utf8 -*-

"""
NOTICE: This is just a script, not an useful module/package.
"""

from __future__ import print_function

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl


# Settings
# ========

vmname = 'deploy_altair_test'

# "Default installation of vCenter Server, VirtualCenter,
# and ESXi use port 443." from "OVF Tool User's Guide".
port = 443

# vCenter/ESXi server and account/password
#server = 'vcenter.dev-net.local'
server = '10.30.1.33'
account = 'administrator@vsphere.local'
password = 'Compaq123'

# Server Resources
datacenter = 'automation'
host = '10.30.1.14'
resource_pool = 'Resources' #default

# Deploying settings
datastore = 'apua'
network = 'Dev_Net'


# Run
# ===

si = SmartConnect(host=server, user=account, pwd=password, port=port)
try:
    content = si.content
    objView = content.viewManager.CreateContainerView(
        content.rootFolder, [vim.VirtualMachine], True
        )
    vm = next(vm for vm in objView.view if vm.name==vmname)
    objView.Destroy()
    vm.PowerOn()
finally:
    Disconnect(si)
