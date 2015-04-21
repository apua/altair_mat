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

from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim
import requests
import yaml

from altair import Altair
from utils import *


# constants
CONFIG_FILENAME = 'settings.cfg'


# methods
altair235 = lambda: Altair(appliance_ip='10.30.1.235', username='administrator', password='Compaq123')
p = lambda v: pprint(v, depth=1)
