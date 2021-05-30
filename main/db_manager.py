# All of the SQL practice is very bad do not replicate

import sqlite3

def db_connect():
    return sqlite3.connect('../info_db.db')

def get_url(coin):
    query = "SELECT api_url FROM coins WHERE coin_name = '{0}'".format(coin)
    cur = db_connect().cursor()
    result = cur.execute(query)
    url = result.fetchone()[0]
    return url

def add_price(price, coin):
    query_id = "SELECT coin_id FROM coins WHERE coin_name ='{0}'".format(coin)
    cur = db_connect().cursor()
    result = cur.execute(query_id)
    id = result.fetchone()[0]
    try:
        query_insert = "INSERT INTO prices(coin_id, price) Values({0},{1})".format(id, price)
        cur.execute(query_id)
    except sqlite3.IntegrityError:
        return 1
    return 0