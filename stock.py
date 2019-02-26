import subprocess
import json


def getquote(stock):
    command = 'curl -v https://api.robinhood.com/quotes/' + \
        stock + '/ -H "Accept: application/json"'
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    quote = json.loads(out.decode("utf-8"))
    return quote


stock = 'SPY'


def getfdmtl(stock):
    command = 'curl -v https://api.robinhood.com/fundamentals/' + \
        stock + '/ -H "Accept: application/json"'
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    fdmtl = json.loads(out.decode("utf-8"))
    return fdmtl


getfdmtl('SPY')


def getmkt():
    command = 'curl -v https://api.robinhood.com/markets/ / -H "Accept: application/json"'
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    mkt = json.loads(out.decode("utf-8"))
    return mkt['results']


markets = getmkt()
len(markets)
markets[0]
markets[1]
markets[2]
markets[3]
markets[4]
markets[5]

import matplotlib.pyplot as plt
import numpy as np
import quandl
import requests

r = requests.get('https://api.robinhood.com/fundamentals/MSFT/')
msft=r.json()
msft
msft['open']