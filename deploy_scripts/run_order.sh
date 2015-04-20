'
configurations:
    config
    altair_source
    ovf_location, latest_ovf_name
    vcenter
    host
    networks
    credential
    vm_name
'
 
# check disk space first
# update latest ovf name
./download_altair.py

# check disk space first
./unzip.py

./check_env.py

./import_ovf.py

./take_snapshot.py 'import_ovf'

./turn_on.py

# wait vm turning on until getting ip
./get_ip.py

./wait_boot.py

./initiate.py

./wait_shutdown.py

./take_snapshot.py 'initiate'

./turn_on.py

./wait_boot.py

./restore.py


# others
# ======

'
wait function
set network
set administrator
upload WinPE ?
'
