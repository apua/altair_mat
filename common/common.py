from __future__ import division, print_function, absolute_import

# shell
import os
execfile(os.path.expanduser('~/.pythonstartup.py'))


# libs
from getpass import getpass
from pprint import pprint
import os
import subprocess
import sys
import time

from pyVim.connect import SmartConnection
from pyVmomi import vmodl
from pyVmomi import vim
import requests
import yaml

import altair as A
from altair import Altair
from utils import *


# constants
ALTAIR_SETTINGS = 'settings.cfg'


# methods
altair235 = lambda: Altair(appliance_ip='10.30.1.235', username='administrator', password='Compaq123')
p = lambda v: pprint(v, depth=1)


try:
    del os.environ['http_proxy']
    del os.environ['https_proxy']
except:
    pass