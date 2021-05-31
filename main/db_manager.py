# All of the SQL practice is very bad do not replicate
import sqlite3

def _init_tables():
    command = "CREATE TABLE coins(coin VARCHAR2 PRIMARY KEY, api VARCHAR2 NOT NULL);"
    command2 = "CREATE TABLE prices(coin VARCHAR2 REFERENCES coins(coin), coin_price NUMBER NOT NULL, time DATE PRIMARY KEY);"
    db = db_connect().cursor()
    db.execute(command)
    db.execute(command2)
    insert = "INSERT INTO coins (coin, api) VALUES ('BITCOIN', 'https://api.coindesk.com/v1/bpi/currentprice/USD.json');"
    db.execute(insert)


def db_connect():
    return sqlite3.connect('coin_watch/main/coin_watch.db')


def get_url(coin):
    query = "SELECT api FROM coins WHERE coin = '{0}'".format(coin)
    cur = db_connect().cursor()
    try:
        result = cur.execute(query)
    except sqlite3.OperationalError:
        return "Error"
    return result.fetchone()[0]


def add_price(price, coin):
    conn = db_connect()
    cur = conn.cursor()
    query_insert = "INSERT INTO prices(coin, coin_price) Values('{0}',{1})".format(coin, price)
    try:
        result = cur.execute(query_insert)
        conn.commit()
    except sqlite3.IntegrityError:
        return 1
    return 0


def get_prices(coin):
    cur = db_connect().cursor()
    query_get = "SELECT coin_price FROM prices WHERE coin = '{0}' ORDER BY time".format(coin)
    result = cur.execute(query_get)
    return result.fetchall()


def add_coin(coin, api):
    conn = db_connect()
    cur = conn.cursor()
    query_insert = "INSERT INTO coins(coin, api) Values('{0}','{1}')".format(coin, api)
    try:
        result = cur.execute(query_insert)
        conn.commit()
    except sqlite3.IntegrityError:
        return 1
    return 0