# -*- coding=utf8 -*-

r"""
It is just a script importing OVF to indicated target.
The program depends on VMware OVF tool and, thus it is not recommanded to use.
But its behavior could be referred.

Issues:

  ☑ Check if the given network/datacenter/... is wrong, it would give error message.
  ☑ Test on M$ Windows.
  ☐ Test on Unix-like.
  ☐ Provid a method let user be able to check OVF file validation
  ☐ If remote target has not enough info or wrong object,
     it should raise exception to output error message and stop process.
  
"""


import subprocess

# usage: ``importOVF.replace('\n  ','')``
_importOVF = '''
  "{ovftool}"
    --noSSLVerify
    --datastore="{datastore}"
    --network="{network}"
    --name="{name}"
    "{source}"
    "{target}"
  '''


ovftool = 'C:\Program Files\VMware\VMware OVF Tool\ovftool.exe'

name = 'qwer' # the VM name you will take

# "Default installation of vCenter Server, VirtualCenter,
# and ESXi use port 443." from "OVF Tool User's Guide".
port = 443

server = 'vcenter.dev-net.local'
server = '10.30.1.33'
account = 'administrator@vsphere.local'
password = 'Compaq123'

datacenter = 'automation'
host = '10.30.1.14'
resource_pool = 'Resources' #default

datastore = 'apua'
network = 'Dev_Net'

source = 'C:\Users\juana\Desktop\ovf_dep_test\ova_dep_test.ovf'

_target = 'vi://{account}:{password}@{server}:{port}/{search_term}'
_search_term = '{datacenter}/host/{host}/{resource_pool}/'

search_term = _search_term.format(**locals())
target = _target.format(**locals())
importOVF = _importOVF.replace('\n  ','').format(**locals())
#print(importOVF)


"""
- On Windows, ``shell=True`` should be set.
- The ``universal_newlines=True`` might be set since `\r\n` is ugly.
- use ``Popen.communicate()[0]`` to get stdout/stderr message
  *and then* use ``Popen.poll()`` check status.
"""

proc = subprocess.Popen(importOVF, stdout=subprocess.PIPE, shell=True)
print proc.communicate()[0]
print proc.poll()
