from datetime import datetime

from gdax import GDAX

def btc_usd_1min(start, end):
  return GDAX('BTC-USD').fetch(start, end, 1)

def btc_usd_30min(start, end):
  return GDAX('BTC-USD').fetch(start, end, 30)


def btc_usd_1day(start, end):
  return GDAX('BTC-USD').fetch(start, end, 1440)


if __name__ == "__main__":
  #data_frame = btc_usd_1day(datetime(2018, 1, 1), datetime(2018, 1, 30))
  data_frame = btc_usd_1min(datetime(2018, 1, 21), datetime(2018, 1, 22))
  print(data_frame)

  # Save to CSV.
  data_frame.to_csv('data.csv')
