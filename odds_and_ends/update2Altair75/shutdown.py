from altair import Altair

with Altair( appliance_ip = '10.30.1.233', username='administrator', password='Compaq123') as api: api.shutdown('HALT')
