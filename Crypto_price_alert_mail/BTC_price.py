import requests
import pandas as pd
from time import sleep
import smtplib
from email.message import EmailMessage


def BTC_price(asset='bitcoin'):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'

    payloads = {'ids': asset, 'interval':'id' }
    response = requests.get(url, params=payloads)
    data = response.json()

    crypto_currency = []
    crypto_prices   = []
    crypto_timestamp = []


    for assets in data:
        crypto_currency.append(assets['name'])
        crypto_prices.append(assets['current_price'])
        crypto_timestamp.append(assets['last_updated'])

    raw_data = {
        'assests' : crypto_currency,
        'rates'   : crypto_prices,
        'timestamp': crypto_timestamp

    }

    df = pd.DataFrame(raw_data)
    print(df)
    return df

BTC_price('bitcoin')

loop = 0
while True:
    print(f'----------------------({loop})---------------')


    try:
         df = BTC_price()

    except Exception as e:
        print("could not retriecve data....... Trying again.")

    loop += 1
    sleep(2)

