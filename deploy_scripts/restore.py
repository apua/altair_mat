from common import *


if len(sys.argv)==1:
    config_path = script_related(__file__, ALTAIR_SETTINGS)
elif len(sys.argv)==2:
    config_path = sys.argv[2]
else:
    exit('usage: %s [altair_settings]'%__file__)


try:
    config = get_config(config_path)
except Exception as e:
    exit(e.message)


with Altair(appliance_ip='10.30.1.235',
            username='administrator',
            password='Compaq123') as api:

    api.set_media_settings(config['media settings'])
    api.set_product_keys(config['product keys'])
    api.set_facility_attributes(config['facility attributes'])

    # bwlow is not idempotent
    api.set_activation_key(config['activation key'])

    #api.update_user_info(config['login user'])

    # below is not idempotent
    for user in config['other users']:
        api.add_user(user)

    # OSBPs
    # WinPE
