"""
def _():
    import os, sys
    prog_dir = os.path.dirname(sys.argv[0]) or os.curdir
    print(prog_dir)
    relpath = os.path.join(prog_dir, os.path.normpath('../common/'))
    print(relpath)
    abspath = os.path.abspath(relpath)
    print(abspath)
    sys.path.append(abspath)
_()

import sys
print(sys.path)
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
