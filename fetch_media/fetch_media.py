r"""
Usage: $prog [[$save_to] $download_from]
"""

def _():
    """
    Add "../common/" to search path
    """
    import os, sys
    prog_dir = os.path.dirname(__file__)
    relpath = os.path.join(prog_dir, os.path.normpath('../common/'))
    abspath = os.path.abspath(relpath)
    sys.path.append(abspath)
_()

import os
import urlparse
import sys

import bs4
import requests


def visible_streaming(resp, filename, block_size):
    print("Fetching...    %s" % filename)
    a = resp.headers.get('content-encoding')
    if a: print(a)
    return resp.iter_content(chunk_size=block_size)


def get_links(url):
    os.environ['http_proxy'] = ''
    resp = requests.get(url)
    assert resp.ok

    soup = bs4.BeautifulSoup(resp.content)
    try:
        as_ = soup.pre.find_all('a')[1:]
    except:
        pass
    else:
        for a in as_:
            yield a.attrs['href']


def get_path(chroot, url):
    from os.path import join, abspath, normpath
    urlpath = urlparse.urlsplit(url).path
    path = abspath(join(chroot, normpath(urlpath.split('/',2)[-1])))
    return path


def download_file(chroot, url):
    resp = requests.get(url, stream=True, headers={'Accept-Encoding': None})
    path = get_path(chroot, url)
    block_size = 1024
    with open(path,'w') as f:
        for chunk in visible_streaming(resp, path, block_size):
            f.write(chunk)
            f.flush()


def download_folder(chroot, url):
    path = get_path(chroot, url)
    if not os.path.isdir(path):
        os.makedirs(path)

    for link in get_links(url):
        url_ = urlparse.urljoin(url, link)
        if link.endswith('/'): # dir
            download_folder(chroot, url_)
        else:
            download_file(chroot, url_)


def main():
    prog_dir = os.path.abspath(os.path.dirname(__file__))
    if   len(sys.argv)==1:
        chroot = raw_input("Save files to [default: %s]: "%prog_dir) or prog_dir
        source_path = raw_input("Download files from: ")
    elif len(sys.argv)==2:
        chroot = raw_input("Save files to [default: %s]: "%prog_dir) or prog_dir
        source_path = sys.argv[1]
    elif len(sys.argv)==3:
        chroot, source_path = sys.argv[1:]
    else:
        exit(__doc__)

    # Always assume the given path is a folder
    download_folder(chroot, source_path)


if __name__=='__main__':
    main()
