from datetime import datetime, timedelta
from gdax import GDAX

LOCALHOURUTC = 6

def querymonthlydata(conversion, year, month, granularity):
    start = datetime(year, month, 1, LOCALHOURUTC, 0, 0)
    if month < 12:
        end = datetime(year, month + 1, 1, LOCALHOURUTC, 0, 0)
    else:
        end = datetime(year+1, 1, 1, LOCALHOURUTC, 0, 0)
    df = conversion.fetch(start, end, granularity)
    return df


if __name__ == "__main__":
    for yy in [2017, 2018]:
        for mm in range(1, 13):
            print('querying year={}, month={}'.format(yy, mm))
            df = querymonthlydata(GDAX('BTC-USD'), yy, mm, 1)
            # convert back to local time
            df.index = df.index - timedelta(hours=LOCALHOURUTC)
            df.to_csv(str(yy) + '_' + str(mm) + '.csv')
