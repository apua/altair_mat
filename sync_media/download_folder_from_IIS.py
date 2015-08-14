r"""
Usage: $prog    $save_to    $download_from

This recipe is a simple script to fetch media source. It expects given media source (eg: http://16.100.111.195/deployment/spp/ ), the location to save (eg: `C:\MediaShare\Media` , the result will be `C:\MediaShare\Media\spp\`) .

It is design only for IIS virtual directories, and it will ignore the directory which contains `index.html`.

Besides, the default saving path is where the script locates, it will be used if not given where to save.
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

import os
import urlparse
import sys

import bs4
import requests


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
        s = self.templ.format(p*100, int(p*20)*'#')
        #s = self.templ.format(p*100, '\033[3m'+int(p*20)*' '+'\033[m')
        if v==self.total:
            print('\r'+s)
        else:
            sys.stdout.write('\r'+s)
            sys.stdout.flush()


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


def get_path(url):
    from os.path import join, abspath, normpath
    urlpath = urlparse.urlsplit(url).path
    path = abspath(join(chroot, normpath(urlpath.split('/',2)[-1])))
    return path


def download_file(url):
    rq = requests.get(url, stream=True)
    path = get_path(url)
    chunk_size = 1024
    with open(path,'w') as f:
        bar = Bar(path, int(rq.headers['content-length']))
        for chunk in rq.iter_content(chunk_size=chunk_size):
            #if chunk: # filter out keep-alive new chunks
            #    f.write(chunk)
            #    f.flush()
            #    bar.acc += len(chunk)
            f.write(chunk)
            f.flush()
            bar.acc += len(chunk)


def download_folder(url):
    path = get_path(url)
    if not os.path.isdir(path):
        os.makedirs(get_path(url))

    for link in get_links(url):
        url_ = urlparse.urljoin(url, link)
        if link.endswith('/'): # dir
            download_folder(url_)
        else:
            download_file(url_)


if __name__=='__main__':

    prog_dir = os.path.dirname(sys.argv[0]) or os.path.abspath(os.curdir)
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
    download_folder(source_path)
