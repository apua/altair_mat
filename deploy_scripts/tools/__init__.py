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
            from textwrap import dedent
            msg_templ = dedent('''
                There is format error in "{filename}" line {linenum}.
                Hint: {problem}.
                ''').strip()
            linenum = int(e.problem_mark.line) + 1
            filename = e.problem_mark.name
            problem = e.problem
            raise Exception(msg_templ.format(**locals()))
