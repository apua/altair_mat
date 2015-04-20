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


def get_target():
    def get_latest_filename():
        response = requests.get(NIGHTLY_BUILD_PAGE)
        filenames = sorted(re.findall(FILENAME_PATT, response.content))
        latest_filename = filenames.pop()
        return latest_filename

    if   len(sys.argv)==1:
        filename = get_latest_filename()
    elif len(sys.argv)==2:
        filename = sys.argv[1]
    else:
        exit('usage: %s [altair_filename]' % __file__)

    filepath = os.path.join(LOCATION, filename)
    if os.path.exists(filepath):
        exit('"{}" already exists\n'.format(filepath))

    fileuri = urlparse.urljoin(NIGHTLY_BUILD_PAGE, filename)
    if requests.head(fileuri).status_code!=200:
        exit('"{}" cannot fetch\n'.format(fileuri))

    return fileuri, filepath


def get_diskspace():
    command = 'df -B 1 --output=avail {}'.format(LOCATION)
    output = sp.check_output(command.split())
    size = int(output.splitlines()[1])
    return size


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
    resp = requests.get(fileuri, stream=True)
    stream = resp.iter_content(chunk_size=BUFFER_SIZE)
    filesize = int(resp.headers['content-length'])

    diskspace = get_diskspace()
    if not filesize < diskspace:
        exit('File size:  {}\n'
             'Disk space: {}\n'
             'Disk space is not enough'.format(filesize, diskspace))

    with open(filepath, 'wb') as fd:
        try:
            write_fd(stream, fd, filesize)
        except KeyboardInterrupt:
            os.remove(filepath)
        finally:
            sys.stdout.write('\n')


if __name__=='__main__':
    download_file(*get_target())
