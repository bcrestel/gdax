from datetime import datetime

from gdax import GDAX


if __name__ == "__main__":
    # actual time is 6h prior to the one entered
    df = GDAX('BTC-USD').fetch(\
    datetime(2018, 1, 2, 14, 0, 0), datetime(2018, 1, 2, 14, 30, 0), 1)
    print(df)
    df.to_csv('data.csv')
