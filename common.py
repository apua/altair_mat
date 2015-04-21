# libs
from __future__ import division, print_function, absolute_import

from pprint import pprint
import os
import sys

import requests
import yaml

from altair import Altair
from utils import *

# shell
execfile(os.path.expanduser('~/.pythonstartup.py'))


# constants
CONFIG_FILENAME = 'settings.cfg'


# methods
altair235 = lambda: Altair(appliance_ip='10.30.1.235', username='administrator', password='Compaq123')
p = lambda v: pprint(v, depth=1)
