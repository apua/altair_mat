from __future__ import division, print_function

import re
import requests
import os
import subprocess as sp
import sys
import urlparse


NIGHTLY_BUILD_PAGE = r'http://altair-ex.cce.hp.com/altair/daily-kits/'
FILENAME_PATT = r'ICsp-vmware-7.5.0-\d+.zip'
BUFFER_SIZE = 1024
LOCATION = '/ovf/'


def get_diskspace():
    command = 'df -B 1 --output=avail {}'.format(LOCATION)
    output = sp.check_output(command.split())
    size = int(output.splitlines()[1])
    return size


def get_latest_filename():
    response = requests.get(NIGHTLY_BUILD_PAGE)
    filenames = sorted(re.findall(FILENAME_PATT, response.content))
    latest_filename = filenames.pop()
    return latest_filename


def write_file(stream, f, total):
    form = '\r{percent:6.2f}% size: {part} / {total}'
    show = lambda s: sys.stdout.write(s) or sys.stdout.flush()
    output = lambda **k: show(form.format(**k))
    fwrite = lambda d: f.write(d) or f.flush()

    for i, chunk in enumerate(stream):
        fwrite(chunk)
        part = i*BUFFER_SIZE
        output(percent=part/total*100, part=part, total=total)
    else:
        output(percent=100, part=total, total=total)


def download_file(fileuri, filepath):
    resp = requests.get(fileuri, stream=True)
    stream = resp.iter_content(chunk_size=BUFFER_SIZE)
    filesize = int(resp.headers['content-length'])

    diskspace = get_diskspace()
    if not filesize < diskspace:
        print('File size:  {}\n'
              'Disk space: {}\n'
              'Disk space is not enough'.format(filesize, diskspace))
        exit(1)

    with open(filepath, 'wb') as fd:
        try:
            write_file(stream, fd, filesize)
        except KeyboardInterrupt:
            os.remove(filepath)
        finally:
            sys.stdout.write('\n')


if __name__=='__main__':
    filename = get_latest_filename()
    filepath = os.path.join(LOCATION, filename)
    fileuri = urlparse.urljoin(NIGHTLY_BUILD_PAGE, filename)

    if os.path.exists(filepath):
        '"{}" already exists\n'.format(filepath)

    download_file(fileuri, filepath)
