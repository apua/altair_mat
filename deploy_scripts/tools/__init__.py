def gen_path(filename, source_file):
    r'''
    >>> gen_path('fn', '/dirpath/src')
    '/dirpath/fn'
    '''
    import os.path as path

    dirname = path.dirname(source_file)
    abspath = path.join(dirname, filename)
    return abspath


def set_config(data, config_path):
    import yaml
    with open(config_path, 'w') as fp:
        yaml.safe_dump(data, stream=fp,
                       default_flow_style=False, indent=4,
                       allow_unicode=True, encoding='utf-8')


def get_config(config_path):
    import yaml
    with open(config_path, 'r') as fp:
        return yaml.load(fp)
