import requests
import pandas as pd
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage


def btc(asset='bitcoin'):
    url1 = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'

    payloads = {'ids': asset, 'interval': 'id'}
    response = requests.get(url1, params=payloads)
    data = response.json()

    crypto_prices = []


    for assets in data:
        crypto_prices.append(assets['current_price'])

    raw_data = {
        'rates': crypto_prices,
    }

    df = pd.DataFrame(raw_data)
    k = raw_data['rates']
    print(*k)
    return k

k = [btc()]

desired_price = int(input("Enter the desisred price of BTC price: "))


def mail_alert(sender,receiver,password,price_text):
   msg = MM()
   msg['Subject'] = "Price alert"
   msg['from'] = sender
   msg['to']  = receiver
   SLL_context = ssl.create_default_context()
   server = smtplib.SMTP_SSL(host="abc@gmail.com", port = 465, context = SLL_context)
   server.login(sender,password)
   server.sendmail(sender,receiver,msg.as_string())


    bitcoin_history = []
        price = k
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

if (price < desired_price):
   mail_alert()


