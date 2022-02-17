#!/usr/bin/env python3
import json
import os
import sqlite3
import sys
from datetime import datetime, date
from os import system

import requests

today = date.today()
LINE = 70
ASKS = PRICE = BIDS = 0.0
db_file = "earn-spent.db"


def create_database():
    if os.path.exists(db_file):
        # system('clear')
        print("Today date is: ", today)
    else:
        # os.system(db_file)
        con = sqlite3.connect(db_file
                              )
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS earn (
                        dt TEXT PRIMARY KEY,
                        price INTEGER,
                        total_earn DECIMAL,
                        net_earn DECIMAL);   
                    ''')

        cur.execute('''CREATE TABLE IF NOT EXISTS spent
                        (   dt          TEXT PRIMARY KEY,
                            price   integer,
                            spent_btc   DECIMAL,
                            spent_usd   INTEGER,
                            description TEXT
                        );                                                                 
                    ''')
        # cur.execute('''CREATE INDEX idx_spent_dt ON spent(dt)''')

        con.commit()
        con.close()


def ticker():
    global ASKS
    global PRICE
    global BIDS

    url = 'https://api.gemini.com/v1/pubticker/btcusd'
    resp = requests.get(url=url)
    data = json.loads(resp.text)

    ASKS = float(data['ask'])
    PRICE = float(data['last'])
    BIDS = float(data['bid'])

    print("+" + "-" * LINE)
    print("| ASKS      : {:0,.2f}".format(ASKS))
    print("| PRICE     : {:0,.2f}".format(PRICE))
    print("| BID       : {:0,.2f}".format(BIDS))
    print("+" + "-" * LINE)


def display_records():
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    print("                   *** EARNED ***")
    for row in cur.execute('SELECT * FROM earn ORDER BY dt'):
        print(row)

    print("+" + LINE * "-")
    print("                   *** PURCHASED ***")
    for row in cur.execute('SELECT * FROM buy ORDER BY dt'):
        print(row)

    print("+" + LINE * "-")
    print("                    *** SPENT ***")
    for row in cur.execute('SELECT * FROM spent ORDER BY dt'):
        print(row)

    sql = '''SELECT net_earn FROM earn ORDER BY dt DESC LIMIT 1'''
    cur.execute(sql)
    net_earn = cur.fetchone()

    sql = '''SELECT sum(buy_btc) AS total FROM buy;'''
    cur.execute(sql)
    buy = cur.fetchone()

    sql = 'SELECT sum(spent_btc) AS total FROM spent'
    cur.execute(sql)
    spent = cur.fetchone()

    remainder = net_earn[0] + buy[0] - spent[0]
    net_earn_usd = float(net_earn[0]) * PRICE

    print("+" + LINE * "-")
    print("| Net Earned       : {:3,.8f} / ${:3,.2f}".format(net_earn[0], net_earn_usd))
    print("| Bought           : {:3,.8f}".format(buy[0]))
    print("| Spent            : {:3,.8f}".format(spent[0]))
    print("+" + LINE * "-")
    print("| Remainder BTC    : {:3,.8f}".format(remainder))
    remainder_usd = remainder * PRICE
    print("| Remainder USD    : ${:3,.2f}".format(remainder_usd))
    print("+" + LINE * "-")
    con.close()


def insert_earn_record(record):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    sql = '''INSERT OR REPLACE INTO earn (
                          dt
                        , price
                        , total_earn 
                        , net_earn)
             VALUES (?,?,?,?)
          '''

    cur.execute(sql, record)
    con.commit()
    con.close()


def insert_buy_record(record):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    sql = '''INSERT OR REPLACE INTO buy (
                          dt
                        , price
                        , buy_btc
                        , total )
             VALUES (?,?,?,?)
          '''

    cur.execute(sql, record)
    con.commit()
    con.close()


def insert_spent_record(record):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    sql = '''INSERT OR REPLACE INTO spent (
                          dt
                        , price
                        , spent_btc
                        , spent_usd
                        , description )
             VALUES (?, ?, ?, ?, ?)
          '''

    cur.execute(sql, record)
    con.commit()
    con.close()


def total_buy():
    # find total purchased
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    sql = '''SELECT sum(buy_btc) AS total FROM buy;'''
    cur.execute(sql)
    purchased = cur.fetchone()
    con.close()
    return float(purchased[0])


def main(argv):
    # print('Number of arguments:', len(argv), 'arguments.')
    # print('Argument List:', str(argv))
    # -------------- Earn -------------------#
    if argv[1] == "earn":
        now = datetime.now()
        dt = now.strftime("%Y-%m-%d %H:%M:%S").format(datetime.now())

        total_earn = float(input("Enter BTC Earn  : "))
        bought = total_buy()
        net_earn = round(total_earn - bought, 8)

        event = (dt, int(PRICE), total_earn, net_earn)
        print(event)
        submit = input("Submit y/n: ")
        if submit == 'y':
            insert_earn_record(event)

    # -------------- Earn -------------------#
    elif argv[1] == "buy":
        now = datetime.now()
        dt = now.strftime("%Y-%m-%d %H:%M:%S").format(datetime.now())

        btc_price = input("Enter BTC Price  : ")
        btc_price = btc_price.replace(',', '')

        bought = input("Enter BTC Bought : ")
        total_paid = input("Total USD Paid : ")

        event = (dt, float(btc_price), float(bought), float(total_paid))
        print(event)
        submit = input("Submit y/n: ")
        if submit == 'y':
            insert_buy_record(event)

    # -------------------- Spend ---------------------- #
    elif argv[1] == "spent":
        now = datetime.now()
        dt = now.strftime("%Y-%m-%d %H:%M:%S").format(datetime.now())
        spent_btc = input("Enter BTC Spent : ")
        spent_usd = int(round(float(spent_btc) * PRICE))
        # spent_usd = math.ceil(float(spent_btc) * PRICE)
        description = input("Description     : ")
        event = (dt, int(PRICE), spent_btc, spent_usd, description)
        print(event)
        submit = input("Submit y/n: ")
        if submit == 'y':
            insert_spent_record(event)


if __name__ == "__main__":
    create_database()
    ticker()
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        display_records()
