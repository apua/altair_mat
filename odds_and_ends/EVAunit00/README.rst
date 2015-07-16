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


2015.01.15
==========

Replace CSI Taipei `Altair 7.3` with `Altair 7.5`.

We just transfer "Facility Custom Attributes", "Product Keys", "OSBP", and "Scripts";
"User and Groups", "Servers" has not find (or assure) solutions yet;
we just know that "Configuration Files" and some customized data can not backup in simple way after testing
(because the result of searching index have no `osdCustomerContent` attribute).

In addition, the installed `Altair 7.5` uses shared network NICs but indepent network NICs as current `Altair 7.3`, it has to change VM netwroks and change guestOS IPs.

hmm.....maybe just set network manually now.
