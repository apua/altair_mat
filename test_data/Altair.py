r"""
It is a Robot Framework Library which provides keywords to control Altair with API
"""

def _():
    """
    Add "../common/" to search path
    """
    import os, sys
    prog_dir = os.path.dirname(sys.argv[0]) or os.curdir
    relpath = os.path.join(prog_dir, os.path.normpath('../common/'))
    abspath = os.path.abspath(relpath)
    sys.path.append(abspath)
_()

from robot.api import logger

from altair.api import Altair
from altair import utils
utils.output.method = logger.console
