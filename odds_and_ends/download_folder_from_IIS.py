"""
Usage example:
    $program    http://10.30.1.38/deployment/spp

This is only for IIS
"""

__import__('sys').path.append('../common/')

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
        s = self.templ.format(p*100, '\033[3m'+int(p)*20*' '+'\033[m')
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
    for a in soup.pre.find_all('a')[1:]:
        yield a.attrs['href']


def get_path(url):
    return chroot+urlparse.urlsplit(url).path


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
    try:
        os.makedirs(get_path(url))
    except:
        pass

    for link in get_links(url):
        url_ = urlparse.urljoin(url, link)
        if link.endswith('/'): # dir
            download_folder(url_)
        else:
            download_file(url_)


if __name__=='__main__':
    if not len(sys.argv)==2:
        exit(__doc__)
    chroot = os.path.dirname(sys.argv[0]) or os.curdir
    download_folder(sys.argv[1])
