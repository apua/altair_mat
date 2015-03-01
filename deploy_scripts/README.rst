This "folder" contains recipes for deploying Altair appliance.

Now it focus on "Altair Combined Appliance".
"Altair Combined Appliance" is the newest version of Altair,
and often deployed repeatly in labs.

There are some steps have no solution yet,
but the deploying steps are clearly now.

Another information follows: https://rndwiki2.atlanta.hp.com/confluence/display/csitestdevel/Deploying+Altair


Below is the "recipe - feature" mapping:

`check_env.py`
    Check if environment is OK or not.

`build_env.py`
    Assist user to download source, and set credentials, ...etc.

`import_ovf.py`
    Import OVF/OVA file and then take snapshot.

    It is hard to implement now.

`set_network.py`
    Set IPs and disable built-in DHCP server.

    There is no way has been found yet.

`dump_info.py`
    Dump OSBPs and customized settings.

    OSBPs backup feature has to be implemented!!

`upload_info.py`
    Upload info created by `dump_info.py` and `build_env.py`.

`update_appliace.py`
    Upload `osd-osbp-package` if necessary and `YUM`/`RPM` update.

`take_snapshot.py`
    Optional. Shutdown, take a snapshot, and turn on.

