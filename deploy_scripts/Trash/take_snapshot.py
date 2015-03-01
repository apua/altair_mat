#!/usr/bin/env python
# -*- coding=utf8 -*-

"""
After deploying "Deploy Test", take a snapshot.

NOTICE: This is just a script, not an useful module/package.
"""

from __future__ import print_function

from pysphere import VIServer


# Settings
# ========

# vCenter/ESXi server and account/password
server = '10.30.1.33'
#server = '10.30.1.33'
account = 'administrator@vsphere.local'
password = 'Compaq123'

vmname = 'deploy_altair_test'
datastore = 'apua'


# Run
# ===

viserver = VIServer()
viserver.connect(server, account, password)
try:
    path = "[{datastore}] {vmname}/{vmname}.vmx".format(**locals())
    vm = viserver.get_vm_by_path(path)
    
    assert vm.is_powered_off(), Exception("VM should be powered off currently"
                                          "because it is just deployed.")
    
    vm.create_snapshot(name="deploy OVF", description="", sync_run=True)
finally:
    viserver.disconnect()
