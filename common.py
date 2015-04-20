# for Python shell
try:
    import readline
    import rlcompleter
    import atexit
    import os
except ImportError:
    print("Python shell enhancement modules not available.")
else:
    histfile = os.path.join(os.environ["HOME"], ".pythonhistory")
    import rlcompleter
    readline.parse_and_bind("tab: complete")
    if os.path.isfile(histfile):
        readline.read_history_file(histfile)
    atexit.register(readline.write_history_file, histfile)
    del os, histfile, readline, rlcompleter, atexit
    print("Python shell history and tab completion are enabled.")


# altair
from altair import Altair


# yaml
import yaml
from utils import set_config, get_config

# sys
import sys

CONFIG_FILENAME = 'settings.cfg'
