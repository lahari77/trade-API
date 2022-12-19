from faker import Faker
import yfinance as yf
from typing import Dict

sample_instruments_data: Dict[str, str] = {}
# sample_instruments: List[str] = ["MSFT", "AMZN", "AAPL", "FB", "TSLA"]
# for i in sample_instruments:
#     ticker = yf.Ticker(i)
#     print(ticker.isin)
#     sample_instruments_data[i] = ticker.isin

# print(sample_instruments_data)

sample_instruments_data = {'MSFT': 'US5949181045', 'AMZN': 'US0231351067', 'AAPL': 'US0378331005', 'FB': 'JP3166980007', 'TSLA': 'US88160R1014'}

import csv 
import time

fake = Faker()
Faker.seed(100)

trade_file = open('trade.csv', 'w', newline='')
csv_writer = csv.writer(trade_file)

trade_details_file = open('trade_details.csv', 'w', newline='')
csv_writer2 = csv.writer(trade_details_file)


def generate_data(records):
    for i in range(records):
        trade = {}
        trade['trade_date_time']  =  fake.date_time_this_year()
        instrument = fake.random_element(elements = ("MSFT", "AMZN", "AAPL", "FB", "TSLA"))
        trade['instrument_id'] = sample_instruments_data[instrument]
        trade['instrument_name'] = instrument
        trade['asset_class'] = fake.random_element(elements = ('Equity', 'Bonds', 'Money market funds', 'Futures', 'Real estate'))
        trade['counterparty'] = fake.name()
        trade['trader'] = fake.name()
        trade['trade_id'] = fake.random_number(digits=10)

        trade['buySellIndicator'] = fake.random_element(elements = ('BUY', 'SELL'))
        trade['price'] = fake.random_int(min = 10, max = 1000000)
        trade['quantity'] = fake.random_int(min = 1, max = 500)
        if i == 0:
            csv_writer.writerow(list(trade.keys())[:7])
            csv_writer2.writerow(list(trade.keys())[6:])
        csv_writer.writerow(list(trade.values())[:7])
        csv_writer2.writerow(list(trade.values())[6:])

generate_data(100)
trade_file.close()
trade_details_file.close()