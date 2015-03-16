from __future__ import division, print_function

from pprint import pprint as p


NIGHTLY_BUILD_PAGE = r'http://altair-ex.cce.hp.com/altair/daily-kits/'
FILENAME_PATT = r'ICsp-vmware-7.5.0-\d+.zip'
BUFFER_SIZE = 1024


def get_latest_filename():
    import re
    import requests

    response = requests.get(NIGHTLY_BUILD_PAGE)
    filenames = sorted(re.findall(FILENAME_PATT, response.content))
    latest_filename = filenames.pop()
    return latest_filename


def download_file(filename):
    import os.path as path
    import requests
    from sys import stdout

    if path.exists(filename):
        raise OSError('"%s" already exists' % filename)

    resp = requests.get(NIGHTLY_BUILD_PAGE+filename, stream=True)
    stream = resp.iter_content(chunk_size=BUFFER_SIZE)
    content_length = resp.headers['content-length']

    total = int(content_length)
    output_form = '\r{percent:f} size: {now} / {total}'

    with open(filename, 'wb') as f:
        for i, chunk in enumerate(stream):
            if chunk:
                f.write(chunk)
                f.flush()
                now = i*BUFFER_SIZE
                percent = now / total
                stdout.write(output_form.format(**locals()))
                stdout.flush()


if __name__=='__main__':

    filename = get_latest_filename()
    try:
        download_file(filename)
    except KeyboardInterrupt:
        import os
        print()
        os.remove(filename)
