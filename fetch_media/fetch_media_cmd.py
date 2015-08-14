import os
import sys

import fetch_media

def progress(p):
    if os.name=='posix':
        return '\033[3m'+int(p*20)*' '+'\033[m'
    elif os.name=='nt':
        return int(p*20)*'#'
    else:
        return 'Fetching...'


class Bar(object):
    def __init__(self, path, total):
        self.templ = "{{1:<20}} {{0:6.2f}}% {path}".format(**locals())
        self.total=total
        self._acc = 0

    @property
    def acc(self):
        return self._acc
    @acc.setter
    def acc(self, v):
        self._acc = v
        p = 1.0*v/self.total
        s = self.templ.format(p*100, progress(p))
        if v==self.total:
            print('\r'+s)
        else:
            sys.stdout.write('\r'+s)
            sys.stdout.flush()

fetch_media.Bar = Bar
fetch_media.main()
