#!/usr/bin/env python
# -*- coding=utf8 -*-

"""
Deploying OVF "Deploy Test" to vCenter/ESXi server

NOTICE: This is just a script, not an useful module/package.
"""

from __future__ import print_function

import argparse
import getpass
import subprocess

from _modify_ovf import modify_ovf


# for *nix
_importOVF = '''(
  "{ovftool}",
    "--noSSLVerify",
    {net_args},
    "--datastore={datastore}",
    "--name={vmname}",
    "{source}",
    "{target}",
  )'''

# The OVF Tool
#ovftool = 'C:\Program Files\VMware\VMware OVF Tool\ovftool.exe'
ovftool = 'ovftool'

# The VMname you would take
#vmname = 'Deploy Test'
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
network = ('Dev_Net', )
#network = ('Cirrus_Net', 'Dev_Net')

# OVF source
#source = 'C:\Users\juana\Desktop\ovf_dep_test\ova_dep_test.ovf'
source = '/ovf/ICsp-vmware-7.4.1-20141113/ICsp-vmware-7.4.1-20141113.ovf'
#source = '/ovf/deploy test/deploy test.ovf'
#source = '/ovf/deploy_test/deploy_test.ovf'

###############################################################################

# Generate shell command

modify_ovf(fn=source)
if   len(network)==1:
    net_args = '"--net:Appliance={0}", "--net:Deployment={0}"'.format(*network)
elif len(network)==2:
    net_args = '"--net:Appliance={0}", "--net:Deployment={1}"'.format(*network)
else:
    raise Exception('Number of network(s) should be one or two.')

_target = 'vi://{account}:{password}@{server}:{port}/{search_term}'
_search_term = '{datacenter}/host/{host}/{resource_pool}/'

search_term = _search_term.format(**locals())
target = _target.format(**locals())
#importOVF = _importOVF.replace('\n  ','').format(**locals()) #for M$ Windows
importOVF = eval(_importOVF.replace('\n  ','').format(**locals()))

#print(' '.join(importOVF)) ; exit()

###############################################################################

# Running shell process

## for Windows
#proc = subprocess.Popen(importOVF, stdout=subprocess.PIPE, shell=True)
#print proc.communicate()[0]
#print proc.poll()

## Forget M$ Windows. Run on *nix
try:
    proc_output = subprocess.check_output(importOVF)
    print(proc_output)
except subprocess.CalledProcessError as E:
    print(E.output)
