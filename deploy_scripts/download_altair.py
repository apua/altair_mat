from __future__ import division, print_function

import re
import requests
import os
import os.path
import subprocess as sp
import sys
import urlparse

from utils import get_diskspace


USAGE_MESSAGE = 'usage: %s [altair_filename] location' % __file__
FILENAME_PATT = r'ICsp-vmware-7.5.0-\d+.zip'
NIGHTLY_BUILD_PAGE = r'http://altair-ex.cce.hp.com/altair/daily-kits/'
BUFFER_SIZE = 1024


def get_target():
    def get_latest_filename():
        response = requests.get(NIGHTLY_BUILD_PAGE)
        filenames = sorted(re.findall(FILENAME_PATT, response.content))
        latest_filename = filenames.pop()
        return latest_filename

    if   len(sys.argv)==2:
        filename, location = get_latest_filename(), sys.argv[1]
    elif len(sys.argv)==3:
        filename, location = sys.argv[1:]
    else:
        exit(USAGE_MESSAGE)

    diskspace = get_diskspace(location)

    filepath = os.path.join(location, filename)
    if not os.path.exists(location):
        exit('location "{}" doesn`t exist\n'.format(location))
    if os.path.exists(filepath):
        exit('"{}" already exists\n'.format(filepath))

    fileuri = urlparse.urljoin(NIGHTLY_BUILD_PAGE, filename)
    response = requests.head(fileuri)
    filesize = int(response.headers['content-length'])
    if response.status_code!=200:
        exit('"{}" cannot fetch'.format(fileuri))
    if not filesize < diskspace:
        exit('File size:  {}\n'
             'Disk space: {}\n'
             'Disk space is not enough\n'.format(filesize, diskspace))

    print('filename: {}\n'
          'fileuri:  {}\n'
          'filepath: {}\n'.format(filename, fileuri, filepath))

    return fileuri, filepath


def write_fd(stream, fd, total):
    form = '\r{percent:6.2f}% size: {part} / {total}'
    show = lambda s: sys.stdout.write(s) or sys.stdout.flush()
    output = lambda **k: show(form.format(**k))
    fwrite = lambda d: fd.write(d) or fd.flush()

    for i, chunk in enumerate(stream):
        fwrite(chunk)
        part = i*BUFFER_SIZE
        output(percent=part/total*100, part=part, total=total)
    else:
        output(percent=100, part=total, total=total)


def download_file(fileuri, filepath):
    response = requests.get(fileuri, stream=True)
    stream = response.iter_content(chunk_size=BUFFER_SIZE)
    filesize = int(response.headers['content-length'])

    with open(filepath, 'wb') as fd:
        try:
            write_fd(stream, fd, filesize)
        except KeyboardInterrupt:
            os.remove(filepath)
        finally:
            sys.stdout.write('\n')


if __name__=='__main__':
    download_file(*get_target())
