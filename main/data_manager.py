import json
import urllib.request as ur
import db_manager as db

def _get_new_data(coin):
    url = db.get_url(coin)
    info  = json.loads(ur.urlopen(url).read())
    return info['bpi']['USD']['rate_float']

def _update_db(price, coin):
    return db.add_price(price,coin)

def update():
    result = _update_db(_get_new_data())
    if(result == 1):
        print("ERROR Inserting new price")