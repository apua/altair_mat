r"""
It is a Robot Framework Library which provides keywords to control Altair with API
"""

__import__('sys').path.append('../common/')

from robot.api import logger

from altair.api import Altair
from altair import utils
utils.output.method = logger.console
