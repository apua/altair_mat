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
and can be wrapped as a Robot Framework library.


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

Every methods in Altair API can be used as keywords in Robot Framework.
First, create a Robot Framework library as below:

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


Test Data
====================

The test data is writtern in Robot Framework syntax, provides MAT. Please read
the `test_data/MAT` for detail.

To run test, :code:`cd` to `test_data` directory first, and then execute
:code:`pybot` for instance :code:`pybot -L trace -d reports MAT`.

.. note:: User can get Robot Framework by installing RoboGalaxy
