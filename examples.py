import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from gdax import GDAX


if __name__ == "__main__":
    # the time you enter is UTC time (Greenwich)
    df1min = GDAX('BTC-USD').fetch(\
    datetime(2018, 1, 1, 6, 0, 0), datetime(2018, 1, 24, 6, 0, 0), 1)

    # Convert index from UTC to local time
    df1min.index = df1min.index - timedelta(hours=6)

    # resample according to lower freq
    freq = '20min'
    dflowfreq = df1min[['open','close']].resample(freq).mean()
    dflowfreq['low'] = df1min['low'].resample(freq).min()
    dflowfreq['high'] = df1min['high'].resample(freq).max()
    dflowfreq['volume'] = df1min['volume'].resample(freq).sum()

    # compute daily normalized volume (0-1)
    dflowfreq['date'] = dflowfreq.index.date
    dflowfreq['nvol'] = dflowfreq.volume / dflowfreq.groupby('date').volume.transform(np.max)
    # plot daily normalized volume all on same x-axis
    dflowfreq.groupby('date').nvol.plot(use_index=False); plt.show()
