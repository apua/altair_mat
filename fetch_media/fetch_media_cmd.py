import os
import sys

import fetch_media

def visible_streaming(resp, filename, block_size):
    if os.name=='posix':
        def form(p): return '|{:<27}| {:>4.0%}'.format('\033[7m'+' '*int(p*20)+'\033[m', p)
    elif os.name=='nt':
        def form(p): return '|{:<20}| {:>4.0%}'.format('#'*int(p*20), p)
    else:
        def form(*a): return "Fetching...    "

    status_bar = "\r{{}} {filename}".format(**locals()).format
    total = int(resp.headers['Content-Length'])
    times = total//block_size + (total%block_size and 1)
    stream = resp.iter_content(chunk_size=block_size)
    for t in range(times):
        try:
            chunk = next(stream)
            sys.stdout.write(status_bar(form(float(t+1)/times)))
            sys.stdout.flush()
            yield chunk
        except:
            sys.stdout.write(os.linesep)
            sys.stderr.write('[FAIL] %s' % filename)
            sys.stderr.flush()
            break
    else:
        print('')

fetch_media.visible_streaming = visible_streaming
fetch_media.main()
