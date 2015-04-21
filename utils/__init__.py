def get_diskspace(location):
    import subprocess as sp

    command = 'df -B 1 --output=avail {}'.format(location)
    output = sp.check_output(command.split())
    size = int(output.splitlines()[1])
    return size


def set_config(data, config_path):
    import yaml

    with open(config_path, 'w') as fp:
        yaml.safe_dump(data, stream=fp,
                       default_flow_style=False, indent=4,
                       allow_unicode=True, encoding='utf-8')


def get_config(config_path):
    import yaml

    with open(config_path, 'r') as fp:
        try:
            return yaml.load(fp)
        except yaml.scanner.ScannerError as e:
            msg_templ = (
                'There is format error in "{filename}" line {linenum}.\n'
                'Hint: {problem}.\n'
                )
            linenum = int(e.problem_mark.line) + 1
            filename = e.problem_mark.name
            problem = e.problem
            raise Exception(msg_templ.format(**locals()))
