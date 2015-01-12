The page describes what I want to make here, how, and something I concern:

  - Using single configuration file with Python2.x standard library `ConfigParser`.

  - Fixing some different attribute names/name space problem in current scripts.

  - Add more setting scripts, such as "copy license keys".

  - All scripts are in a single module `scrips.py`.

  - Collect tasks to `main.py`. It would migrate to Ansible in the future.


Code Structure
==============

::
   .
   ├── README.rst
   ├── main.py
   ├── altair.py
   ├── scripts.py
   └── settings.cfg
