Abstract
========

It is a package containing steps of deploying OVF.
Run it by ``python -m deploy_scripts``, and
set arguments in `./deploy_scripts/__init__.py`.


Design
======

Input:
    + OVF path (not support OVA, which is a tar file of OVF)
    + vSphere account/password
    + target VMname
    + target storage
    + target appliance NIC and deployment NIC

Output:
    + the appliace IP of appliance VM

State (Side Effect):
    + **modify OVF for setting virtual NIC**
    + take storage about ?? GB space
    + the appliace would be turned on.

Consider:
    + storage space
    + virtual network and NIC
    + DHCP server
    + usable appliance IP


Background
==========

The steps should be a single script, but there is some functionality
should be replaced in better tools or better ways, thus I keep it
as splitted scripts for convenience.

Consider the target environment as own DHCP server and virtual network,
so the appliance IP would be generated after running these steps
without turning on DHCP server of Alair manually.


Issue
=====

[v] Use PySphere as current VMware python binding module.

[v] Modify OVF for setting NICs of appliance, which is a workaround.

[ ] Use `configparser` Python standard module to deduplicate
    getting arguments method.

future jobs
```````````

[ ] Merge this pacakge as single script.
    The README should be docstring of the script.
