from altair import Altair
from pprint import pprint as p
import json

with Altair(appliance_ip='10.30.1.235', username='administrator', password='Compaq123') as api:

    j = api._list_OSBP()
    with open('osbps.json','w') as fp:
        json.dump(j, fp, indent=2)
