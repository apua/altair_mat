from altair import Altair
from pprint import pprint as p
import json

with Altair(appliance_ip='10.30.1.235', username='administrator', password='Compaq123') as api:

    L = api._list_OSBP()

    p(L)
    with open('osbp.json','w') as f:
        json.dump(L, f)
