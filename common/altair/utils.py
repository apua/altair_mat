from collections import OrderedDict
import functools
import os
import sys
import time
import yaml


def generate_uri(netloc='localhost', path='', Query={}):
    """
    issues:
      - check if URI form is valid, refer RFC 3986

    >>> generate_uri(path='/rest/os-deployment-jobs/', Query={'force': 'true'})
    'https://localhost/rest/os-deployment-jobs/?force=true'
    >>> generate_uri('https://altair.dev-net.local', '/rest/os-deployment-jobs/')
    'https://altair.dev-net.local/rest/os-deployment-jobs/'
    """
    from urllib import quote
    from urlparse import urljoin

    if netloc.endswith('/'):
        netloc = netloc[:-1]
    if '://' in netloc:
        scheme, netloc = netloc.split('://')
    else:
        scheme, netloc = 'https', netloc
    if not path.startswith('/'):
        path = '/' + path
    query = '?'*bool(Query) + '&'.join(k+'='+quote(v) for k,v in Query.viewitems())
    return "{scheme}://{netloc}{path}{query}".format(**locals())


def add_indent(json_content):
    from json import dumps
    return dumps(json_content, indent=2)


def failure_information(response):
    import os

    if os.name=='nt':
        template = "\nstatus code => {}\ncontent => {}"
    else:
        template = "\n\x1b[32mstatus code\x1b[m => \x1b[33m{}\x1b[m\n\x1b[34mcontent\x1b[m => {}"
    return template.format(response.status_code, add_indent(response.json()))


def script_related(script_path, cfgfn):
    import os.path
    dirname = os.path.split(script_path)[0]
    return os.path.join(dirname, cfgfn)


def get_diskspace(location):
    import subprocess as sp

    command = 'df -B 1 --output=avail {}'.format(location)
    output = sp.check_output(command.split())
    size = int(output.splitlines()[1])
    return size


def set_config(data, config_path):
    def represent_ordereddict(dumper, data):
        repr_data = dumper.represent_data
        value = [(repr_data(k), repr_data(v)) for k,v in data.items()]
        return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)

    #yaml.add_representer(OrderedDict, represent_ordereddict)
    yaml.SafeDumper.add_representer(OrderedDict, represent_ordereddict)
    with open(config_path, 'w') as fp:
        #yaml.dump(data, stream=fp,
        yaml.safe_dump(data, stream=fp,
                       default_flow_style=False, indent=4,
                       allow_unicode=True, encoding='utf-8')
                       # Do not use `line_break` manually,
                       # since Python interpreter will handle it
                       #allow_unicode=True, encoding='utf-8', line_break='\r\n')


def get_config(config_path):
    with open(config_path, 'r') as fp:
        try:
            return clean_unicode(yaml.load(fp))
        except yaml.scanner.ScannerError as e:
            msg_templ = (
                'There is format error in "{filename}" line {linenum}.\n'
                'Hint: {problem}.\n'
                )
            linenum = int(e.problem_mark.line) + 1
            filename = e.problem_mark.name
            problem = e.problem
            raise Exception(msg_templ.format(**locals()))


def clean_unicode(s):
    """
    Find and encode unicode string recursively
    It supports tuple, list, and dict
    """
    if isinstance(s, unicode):
        return s.encode('utf8')
    elif isinstance(s, tuple):
        return tuple(clean_unicode(i) for i in s)
    elif isinstance(s, list):
        return list(clean_unicode(i) for i in s)
    elif isinstance(s, dict):
        return dict((clean_unicode(k), clean_unicode(s[k])) for k in s)
    else:
        return s


def retry(times=None, wait=None):
    """
    Given times of retry and seconds of waiting,
    return a decorator wating a period of time and retrying if failed.
    """
    if times is None and wait is None:
        times
    def dec(func):
        @functools.wraps(func)
        def func_(*a,**k):
            for _ in range(times):
                try:
                    return func(*a, **k)
                except Exception as e:
                    output(e.message)
                    output("\033[7m"+"....wait and retry"+"\033[m")
                    time.sleep(wait)
        return func_
    return dec


def output(msg, newline=True):
    output.method(msg, newline)
output.method = lambda m, n: sys.stdout.write(m + (os.linesep if n else ''))
