# =====
# Tools
# =====

def _generate_uri(netloc='localhost', path='', Query={}):
    """
    issues:
      - check if URI form is valid, refer RFC 3986

    >>> _generate_uri(path='/rest/os-deployment-jobs/', Query={'force': 'true'})
    'https://localhost/rest/os-deployment-jobs/?force=true'
    >>> _generate_uri('https://altair.dev-net.local', '/rest/os-deployment-jobs/')
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


def _add_indent(json_content):
    from json import dumps
    return dumps(json_content, indent=2)


def _failure_information(response):
    import os

    if os.name=='nt':
        template = "\nstatus code => {}\ncontent => {}"
    else:
        template = "\n\x1b[32mstatus code\x1b[m => \x1b[33m{}\x1b[m\n\x1b[34mcontent\x1b[m => {}"
    return template.format(response.status_code, _add_indent(response.json()))



