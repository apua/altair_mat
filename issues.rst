Issues
======

:✓: improve `add sut` that display progress
:✓: implement OSBP feature
:✓: improve job progress
:✓: refine `variables.py` generator
:_: set custom attributues of SUTs
:_: improve `wait job finish` messages
:_: provide "run OSBPs test cases generator"




:_: MAT - avoid user forget to set administrator password
:_: MAT - "add user" should be idempotemt
:✓: recipe - "update administrator" feature
:_: YAML dump can indicate newline charactor?
:_: YAML dump with order dict


Issues
======

:✓: Write on wiki
:✓: Improve the variable names in settings::
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
:✓: Cleaned string::
    u'...' -> '...'
:✓: Implement upload WinPE feature and get/add SUTs features
:_: Implement edit SUT custom attributes feature
:_: REST API error handlers have to improve
    such as HTTP response not always have payload (JSON)
:_: Test `export_altair_info.py`, `initiate_altair.py`, `first_time_setup.py`


Issues
======

- Click on Windows should run and show the state.

- Explain the data structure of YAML file.

  generating customized data::

      osbp
          $name:
              attr: ...
              desc: ...
              type: ...
              steps:
                  - name: ...
                    type: ...
                    para: ...
      script
          $name:
              desc: ...
              cont: ...
              type: ...
              sudo: ...
      config
          $name:
              desc: ...
              cont: ...

- Include Packages:
    + Requists
    + PyYAML

- Clean and import all OSBPs every time is expensive.

- Service temporarily unavailable error handling.

- Clean customized OSBPs could be force and fast.

  issues:

      #. using `api._list_index({'category': '...'})` is faster,
         but no `isCustomerContent` field,
         needs to know where is the end index of builtins

      #. delete methods are the same when using uri but id

- Export OSBP recipe can be more simple

- Let settings and customized OSBPs data as .txt file so that even notepad can open it.

- Verification:
  Given `A` is the exported.
  Import `A` to another Altair and export from the Altair as `B`.
  Check if `A` is the same with `B`.

- Remove data is not necessary; consider update just necessary part with diff feature (not implement yet)

- Need modulization.


After discussion
==============================

:✓: Merge export cust feature to API class
:✓: Use methods that fetching index and then retrieving one by one
:✓: Use imperative to rewrite fetching
:✓: Only export scripts and config files of customized OSBPs
:✓: Use index data to fast distinguish customized data
:✓: The YAML file data structure has been added `ogfsScript` and `serverScript`.
    So now it looks like that::

      osbp:
          $name:
              attr: ...
              desc: ...
              type: ...
              steps:
                  - { name: ... , type: ... , para: ... }
                  - { name: ... , type: ... , para: ... }
      ogfsScript:
          $name: { desc: ... , cont: ... , type: ... }
      serverScript:
          $name: { desc: ... , cont: ... , type: ... , sudo: ... }
      config:
          $name: { desc: ... , cont: ... }

:✓: Add "all" argument to fetch all cust even if it is not belong to any OSBP
:_: Update usage to wiki
:_: Write wiki to remind user that the recipes are based on *name*
:_: If package name is a little different, think as same
:_: Merge imporing feature and collect some useful function to API class
:✓: Explain the requirements:
    + Python
    + Git (Finally, we just use CSINFS but Teamforge)
:✓: Support *custom attirbutes of osbps*
:✓: "export_cust_info" and "import_cust_info" are not explicit enough
    replaced with "export_custom_osbps" and "import_custom_osbps"

Altair:
:_: 統一 naming REST API
:_: 令訊息更明確
:_: Add `verbose` option or logger to methods
:_: Replace assertion error with customized Altair API exceptions
:_: Let some REST call can be wait and retry (how to design??)

:✓: Let OSBP backup in DOS file format
