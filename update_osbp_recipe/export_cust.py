from pprint import pprint as p
import json
import os
import sys

sys.path.append('../common/')


from altair import Altair
from utils import set_config


if len(sys.argv)!=5:
    sys.exit('usage: cmd appliance_ip username password cust_filepath')
else:
    appliance_ip , username , password , cust_filepath = sys.argv[1:]


type_mapping = {
    'os-deployment-install-cfgfiles': 'configs',
    'os-deployment-ogfs-scripts': 'scripts',
    'os-deployment-server-scripts': 'scripts',
    'os-deployment-install-zips': 'packages',
    }


def cust_osbps():
    def osbp_info(m):
        return {
            'attr': m['buildPlanCustAttrs'],
            'desc': m['description'],
            'type': m['os'],
            'steps': [
                {'name': step['name'],
                 'type': type_mapping[step['type']],
                 'para': step['parameters']}
                for step in m['buildPlanItems']
                ]
            }

    return {
        m['name']: osbp_info(m)
        for m in osbps['members']
        if m['isCustomerContent']
        }


def cust_scripts():
    def script_info(m):
        return {
            'desc': m['description'],
            'cont': m['source'],
            'type': m['codeType'],
            'sudo': m['runAsSuperUser'],
            }

    return {
        m['name']: script_info(m)
        for m in scripts['members']
        if m['isCustomerContent']
        }


def cust_configs():
    def config_info(m):
        return {
            'desc': m['description'],
            'cont': m['text'],
            }

    return {
        m['name']: config_info(m)
        for m in configs['members']
        if m['isCustomerContent']
        }


def gen_cust():
    return {
        'osbp': cust_osbps(),
        'script': cust_scripts(),
        'config': cust_configs(),
        }



with Altair(appliance_ip=appliance_ip,
            username=username,
            password=password) as api:
    osbps = api._list_OSBP()
    scripts = api._list_serverScript()
    configs = api._list_cfgfile()
    packages = api._list_package()

    set_config(gen_cust(), cust_filepath)


raw_input('Press any key to continue...')
