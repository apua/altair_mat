import ConfigParser as configparser
import os.path as path


def gen_path_with_script(filename, source_file):
    r'''
    >>> gen_path_with_script('fn', '/dirpath/src')
    '/dirpath/fn'
    '''
    dirname = path.dirname(source_file)
    abspath = path.join(dirname, filename)
    return abspath


def get_settings(config_filename, section):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read([config_filename])
    mapping = dict(config.items(section))
    return mapping
