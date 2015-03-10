This "folder" contains recipes for deploying Altair appliance.

Now it focus on "Altair Combined Appliance".
"Altair Combined Appliance" is the newest version of Altair,
and often deployed repeatly in labs.

There are some steps have no solution yet,
but the deploying steps are clearly now.

Another information follows: https://rndwiki2.atlanta.hp.com/confluence/display/csitestdevel/Deploying+Altair


requirement
-----------

:[x]: `paramiko` and dependency

      it is bad for Windows, consider `pscp.exe` and `plink.exe`

:[v]: `requests`

:[v]: `urllib3`
      which dependent on `requests`

:[ ]: `pyvmomi`


recipe - feature mapping
------------------------

`check_env.py`
    Check if environment is OK or not.

.. Downloading sources would be manual and has no script.

.. Added WinPE might has to be automatical

`build_config.py`
    Dump OSBPs and customized settings to help users setting credentials.

    The settings and OSBPs should put in the same directory with the scripts.

`import_ovf.py`
    Import OVF/OVA file and then take snapshot.

    It is hard to implement now.

`set_network.py`
    Set IPs and disable built-in DHCP server through vmtools.

`change_adminpass.py`
    Altair Combined Appliance has default password,
    it should be changed rather than set from first boot.

`set_appliance.py`
    Set appliance with existed settings and OSBPs.

    The settings and OSBPs should put in the same directory with the scripts.

`update_appliace.py`
    Upload `osd-osbp-package` if necessary and `YUM`/`RPM` update.

`take_snapshot.py`
    Optional. Shutdown, take a snapshot, and turn on.

`shutdown_appliance.py`
    Optional. Just shutdown appliance.


Developing Issues
=================

#. other useful API wrapper

#. control vm with PyVmomi

#. testing

#. OSBP backup technic

#. use Putty tools to send command / copy file to appliance

#. inject scripts to guest OS and run it with PyVmomi

#. implement PyVmomi "importting OVF" feature

#. use PyVmomi to modify settings of vm

#. check user`s environment for deploying Altair with PyVmomi

#. splitting REST API to multiple modules if necessary

#. add tutorial for the recipes (such as fill in passwords)

- off-line yum update has some problem?
