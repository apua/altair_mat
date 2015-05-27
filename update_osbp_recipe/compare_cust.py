r"""This script try to find which data needs to be upload / update"""

__import__('sys').path.append('../common/')

from altair import Altair
from utils import get_config, set_config
from common import *

older = get_config('cust-combinedAppliance-20150527_3.yml')
newer = get_config('csi-altair.yml')

Uploads = {}
Updates = {}
Removes = {}

for category in ('osbp','ogfsScript','serverScript','config'):
    ncate = newer[category]
    ocate = older[category]

    added_names     = ncate.viewkeys() - ocate.viewkeys()
    deprecate_names = ocate.viewkeys() - ncate.viewkeys()
    same_names      = ncate.viewkeys() & ocate.viewkeys()
    
    Uploads[category] = {name: ncate[name] for name in added_names}
    Removes[category] = {name: ocate[name] for name in deprecate_names}
    Updates[category] = {name: ncate[name] for name in same_names if ncate[name]!=ocate[name]}
