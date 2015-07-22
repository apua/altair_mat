====================
README
====================

:requirement: Robot Framework 2.9+ / Python 2.7+
:support version: Altair combined appliance


The Altair recipes provide:

+ `Altair API`_
+ `first time setup`_ recipe
+ `customized OSBP`_ recipe


The latest archive can be donwnloaded from
`<ftp://csinfs.americas.hpqcorp.net/altair-recipe>`_ with credential `csi/csi`.


Altair API
====================

The Altair API is a wrapper of the original Altair REST-like API.
It provides common use methods for convenience, can be used as context manager,
and can be wrapped as a Robot framework library.


Examples
---------------

Import API:

.. code:: python

    >>> __import__('sys').path.append('common')
    >>> from altair.api import Altair

Use Altair API login/logout manually:

.. code:: python

    >>> api = Altair("10.30.1.235")
    >>> api.login("administrator", "hpvse123")
    >>> api.is_logged_in() # api.session_id is not None
    True
    >>> api.logout()

Use Altair API as context manager:

.. code:: python

    >>> from pprint import pprint
    >>> with Altair("10.30.1.235", "administrator", "hpvse123") as api:
    ...     pprint(api.get_media_settings())
    ...
    {'file_share_host': '10.30.1.38',
     'file_share_name': '/deployment',
     'file_share_password': '......',
     'file_share_user': 'administrator',
     'http_server_host': '10.30.1.38',
     'http_server_path': '/deployment'}

Every methods in Altair API can be used as keywords in Robot framework.
First, create a Robot framework library as below:

.. code:: python

    # filename: Altair.py
    from altair.api import Altair

Then, one can write test data like this:

.. code:: robotframework

    *** Settings ***
    Library             Altair      10.30.1.235     administrator   hpvse123
    Suite Setup         Login
    Suite Teardown      Logout

    *** Test Cases ***
    Check login state
        ${logged}=          is logged in
        Should be true      ${logged}

    Show Media Settings
        ${settings}=        Get media settings
        Log to console      ${settings}


Executeing Recipe
====================

In command line, just enter :code:`python $recipe_name`, or enter absolute path
of python interpreter such as :code:`C:\python27\python.exe $recipe_name`.

In GUI, right click the recipe and choose "Edit with IDE", then click "Run →
Run Module" (or press F5 directly).

.. note: Be aware of which Python version it takes


Customized OSBP
====================

The recipe is used to export/import Altair appliance customized OSBPs.


Usage
---------------

0. For first time use, please copy `settings.txt.template` as `settings.txt`,
   and then edit `setting.txt` by overwritting "......" as below:

   .. code:: yaml

       login_information:
           appliance_ip: 10.30.1.235
           password: hpvse123
           username: administrator

       cust_filepath:
           cust_osbp_20150229.txt

   In the example above, customized OSBPs will be exported to or imported from
   the custom file `cust_osbp_20150229.txt`.

1. To export customized OSBPs from existed Altair appliance, just execute the
   script `export_custom_osbps.py`; if the custom file already exists, it will
   ask user if replacing the file or not.

2. To import customized OSBPs from custom file, just execute the script
   `import_custom_osbps.py`.


First Time Setup
====================

The recipe is used to export Altair appliance settings, and run first time
setup on "combined appliance version" Altair.

.. note::

    Since combined appliance version Altair has to be set network in
    VM console first, the first time setup recipe will not contain setting
    network part until now.



Usage
---------------

0. For first time use, please copy `settings.txt.template` as `settings.txt`,
   and then edit `setting.txt` by overwritting "......" as below:

   .. code:: yaml

       login_information:
           appliance_ip: 10.30.1.235
           password: hpvse123
           username: administrator

1. To export Altair appliance settings, just execute the script
   `export_facility_settings.py`, it will write full appliance settings to
   `settings.txt`, and generate `variables.py` used to be variable file of
   Robot Framework test data.

2. The `first_time_setup.py` will login and set appliance according to
   `setting.txt`. To do so, just execute it.

   It doesn`t try to add SUTs and import `customized OSBP`_\ s.


.. Run MAT
.. ====================
..
.. These are Altair early MAT test data base on RoboGalaxy and Robot Framework.
..
.. Please refer to `<https://rndwiki.corp.hpecorp.net/confluence/x/mo2XOw>`_,
.. for more information about intallation and execution.
..
..
.. Command
.. =======
..
.. Dry Run:
.. `pybot -L trace -d reports  -i FTS -i add_suts --dryrun MAT`
..
.. Run:
.. `pybot -L trace -d reports  -i FTS -i add_suts MAT`
..
..
..
..
..
.. .. Issues
.. .. ======
.. ..
.. .. [✓] improve `add sut` that display progress
.. .. [✓] implement OSBP feature
.. .. [✓] improve job progress
.. .. [✓] refine `variables.py` generator
.. .. [ ] set custom attributues of SUTs
.. .. [ ] improve `wait job finish` messages
.. .. [ ] provide "run OSBPs test cases generator"
..
..
..
..
.. .. [ ] MAT - avoid user forget to set administrator password
.. .. [ ] MAT - "add user" should be idempotemt
.. .. [✓] recipe - "update administrator" feature
.. .. [ ] YAML dump can indicate newline charactor?
.. .. [ ] YAML dump with order dict
..
..
..
..
.. Issues
.. ======
..
.. :✓: Write on wiki
.. :✓: Improve the variable names in settings::
..       __OPSW-Media-LinURI ->
..           http_server_host
..           http_server_path
..       __OPSW-Media-WinPassword ->
..           file_share_password
..       __OPSW-Media-WinPath ->
..           file_share_host
..           file_share_name
..       __OPSW-Media-WinUser ->
..           file_share_user
.. :✓: Cleaned string::
..     u'...' -> '...'
.. :✓: Implement upload WinPE feature and get/add SUTs features
.. :_: Implement edit SUT custom attributes feature
.. :_: REST API error handlers have to improve
..     such as HTTP response not always have payload (JSON)
.. :_: Test `export_altair_info.py`, `initiate_altair.py`, `first_time_setup.py`
..
..
..
.. =======================================
..
.. .. Issues
.. .. ======
.. ..
.. .. - Click on Windows should run and show the state.
.. ..
.. .. - Explain the data structure of YAML file.
.. ..
.. ..   generating customized data::
.. ..
.. ..       osbp
.. ..           $name:
.. ..               attr: ...
.. ..               desc: ...
.. ..               type: ...
.. ..               steps:
.. ..                   - name: ...
.. ..                     type: ...
.. ..                     para: ...
.. ..       script
.. ..           $name:
.. ..               desc: ...
.. ..               cont: ...
.. ..               type: ...
.. ..               sudo: ...
.. ..       config
.. ..           $name:
.. ..               desc: ...
.. ..               cont: ...
.. ..
.. .. - Include Packages:
.. ..     + Requists
.. ..     + PyYAML
.. ..
.. .. - Clean and import all OSBPs every time is expensive.
.. ..
.. .. - Service temporarily unavailable error handling.
.. ..
.. .. - Clean customized OSBPs could be force and fast.
.. ..
.. ..   issues:
.. ..
.. ..       #. using `api._list_index({'category': '...'})` is faster,
.. ..          but no `isCustomerContent` field,
.. ..          needs to know where is the end index of builtins
.. ..
.. ..       #. delete methods are the same when using uri but id
.. ..
.. .. - Export OSBP recipe can be more simple
.. ..
.. .. - Let settings and customized OSBPs data as .txt file so that even notepad can open it.
.. ..
.. .. - Verification:
.. ..   Given `A` is the exported.
.. ..   Import `A` to another Altair and export from the Altair as `B`.
.. ..   Check if `A` is the same with `B`.
.. ..
.. .. - Remove data is not necessary; consider update just necessary part with diff feature (not implement yet)
.. ..
.. .. - Need modulization.
.. ..
.. ..
.. .. After discussion
.. .. ==============================
.. ..
.. .. [✓] Merge export cust feature to API class
.. .. [✓] Use methods that fetching index and then retrieving one by one
.. .. [✓] Use imperative to rewrite fetching
.. .. [✓] Only export scripts and config files of customized OSBPs
.. .. [✓] Use index data to fast distinguish customized data
.. .. [✓] The YAML file data structure has been added `ogfsScript` and `serverScript`.
.. ..     So now it looks like that::
.. ..
.. ..       osbp:
.. ..           $name:
.. ..               attr: ...
.. ..               desc: ...
.. ..               type: ...
.. ..               steps:
.. ..                   - { name: ... , type: ... , para: ... }
.. ..                   - { name: ... , type: ... , para: ... }
.. ..       ogfsScript:
.. ..           $name: { desc: ... , cont: ... , type: ... }
.. ..       serverScript:
.. ..           $name: { desc: ... , cont: ... , type: ... , sudo: ... }
.. ..       config:
.. ..           $name: { desc: ... , cont: ... }
.. ..
.. .. [✓] Add "all" argument to fetch all cust even if it is not belong to any OSBP
.. .. [ ] Update usage to wiki
.. .. [ ] Write wiki to remind user that the recipes are based on *name*
.. .. [ ] If package name is a little different, think as same
.. .. [ ] Merge imporing feature and collect some useful function to API class
.. .. [✓] Explain the requirements:
.. ..     + Python
.. ..     + Git (Finally, we just use CSINFS but Teamforge)
.. .. [✓] Support *custom attirbutes of osbps*
.. .. [✓] "export_cust_info" and "import_cust_info" are not explicit enough
.. ..     replaced with "export_custom_osbps" and "import_custom_osbps"
.. ..
.. .. Altair:
.. .. [ ] 統一 naming REST API
.. .. [ ] 令訊息更明確
.. .. [ ] Add `verbose` option or logger to methods
.. .. [ ] Replace assertion error with customized Altair API exceptions
.. .. [ ] Let some REST call can be wait and retry (how to design??)
.. ..
.. .. [✓] Let OSBP backup in DOS file format
.. ..
.. ..
.. .. Wiki
.. .. ====
.. ..
.. .. Requirement
.. .. Python 2.7.x – https://www.python.org/downloads/
.. .. Git – https://git-scm.com/download/
.. .. Accessibility of recipe source code – git clone ssh://apua.juan@cgit-pro.austin.hp.com:29418/altair-recipe
.. .. Please install Python and use git clone to get Altair recipe, and enter into "altair-reciep/update_osbp_recipe".
.. .. There is a setting file "settings.txt.template". Please edit it and save as "settings.txt".
