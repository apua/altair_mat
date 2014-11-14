# -*- coding=utf8 -*-

"""
Fetching directory tree and *mtime* as JSON on Altair Media server.

Issue:
    [ ] Since they are ISO image and SPP, perhaps it is no necessary
            to walk whole directory tree.
    [ ] Use syslog or other notice mechanism but print function.
"""


from time import mktime, strptime
import re
import json

import requests


def site_to_dict(url, path):
    """
    url, path -> dict

    root := tree
    root = { $tree_name: { 'last-modified': long(), 'tree': dict() },
             $leaf_name: { 'last-modified': long(), 'content-length': long()    },
             ... }
    """

    def get_tree(path):
        """
        path -> dict
        """
        uri = url +'/'+ path
        patt = r'(?P<isdir>&lt;dir&gt;)? <A HREF="(?P<path>[^>]*)">(?P<name>[^<]*)</A>' # IIS only
        print("fetch %s" % uri)
        index = requests.get(uri).text
        #tree = {}
        #for mat in re.finditer(patt, index):
        #    name = mat.group('name')
        #    path = mat.group('path')
        #    if mat.group('isdir'):
        #        tree[name] = get_tree(path)
        #    else:
        #        tree[name] = get_leaf(path)
        tree = { mat.group('name'): (get_tree if mat.group('isdir') else get_leaf)(mat.group('path'))
                 for mat in re.finditer(patt, index) }
        return tree

    def get_leaf(path):
        uri = url +'/'+ path
        print("fetch %s" % uri)
        fields = requests.head(uri).headers
        time_format = '%a, %d %b %Y %X GMT' # IIS only
        trans2long = lambda s: mktime(strptime(s, time_format)) if s else ''
        leaf = { 'last-modified': trans2long(fields.get('last-modified')),
                 'content-length': fields.get('content-length',-1) }
        return leaf

    return get_tree(path)


if __name__=='__main__':

    url, path = 'http://15.226.124.71/', '/deploy'
    url, path = 'http://10.30.1.38/', '/deployment'
    filename = 'remote_dirtree.json'
    dir_tree = site_to_dict(url, path)
    with open(filename,'w') as fd:
        json.dump(dir_tree, fd, indent=2)
