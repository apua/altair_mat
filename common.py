# libs
from altair import Altair

import yaml
from utils import set_config, get_config

from pprint import pprint

import os
import sys


# shell
execfile(os.path.expanduser('~/.pythonstartup.py'))


# constants
CONFIG_FILENAME = 'settings.cfg'


# methods
altair235 = lambda: Altair(appliance_ip='10.30.1.235', username='administrator', password='Compaq123')
p = lambda v: pprint(v, depth=1)
