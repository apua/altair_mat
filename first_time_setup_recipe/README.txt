These recipes are for easily backup / running first time setup.
(i.e., not consider getting Altair imange and deploying to hypervisor)

The online document will be written latter.

FTS
===

  download & unzip
→ deploy OVA / OVF
→ set pwd & network & reboot
→ set facility → upload WinPE → user → add SUT (async)
→ add OSBP

Issues
======

[ ] Write on wiki
[✓] Improve the variable names in settings::
      __OPSW-Media-LinURI ->
          http_server_host
          http_server_path
      __OPSW-Media-WinPassword ->
          file_share_password
      __OPSW-Media-WinPath ->
          file_share_host
          file_share_name
      __OPSW-Media-WinUser ->
          file_share_user
[✓] Cleaned string::
    u'...' -> '...'
[ ] REST API error handlers have to improve
    such as HTTP response not always have payload (JSON)
[ ] Test `export_altair_info.py`, `initiate_altair.py`, `first_time_setup.py`
[✓] Implement upload WinPE feature and get/add SUTs features
[ ] Implement edit SUT custom attributes feature
