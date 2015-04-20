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


def download_file(filename):
    path = os.path
    stdout = sys.stdout

    filepath = path.join(LOCATION, filename)
    assert not path.exists(filepath), (
        '"{}" already exists\n'.format(filepath)
        )

    fileuri = urlparse.urljoin(NIGHTLY_BUILD_PAGE, filename)
    resp = requests.get(fileuri, stream=True)
    stream = resp.iter_content(chunk_size=BUFFER_SIZE)
    content_length = resp.headers['content-length']

    total = int(content_length)
    output_form = '\r{percent:6.2f} size: {now} / {total}'

    diskspace = get_diskspace()
    assert total < diskspace, (
        'File size:  {}\n'
        'Disk space: {}\n'
        'Disk space is not enough\n'.format(total, diskspace)
        )

    with open(filepath, 'wb') as f:
        for i, chunk in enumerate(stream):
            if chunk:
                f.write(chunk)
                f.flush()
                now = i*BUFFER_SIZE
                percent = now / total * 100
                stdout.write(output_form.format(**locals()))
                stdout.flush()
        percent, now = 100, total
        stdout.write(output_form.format(**locals()) + '\n')
        stdout.flush()


if __name__=='__main__':
    filename = get_latest_filename()
    try:
        download_file(filename)
    except KeyboardInterrupt:
        os.remove(filename)
    except AssertionError as E:
        sys.stdout.write(E.message)
