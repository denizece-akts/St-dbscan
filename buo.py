from ndbc import Station
from datetime import datetime
import numpy as np


def write_buoy_to_csv(buoyid, startyear, endyear):
    s = Station(buoyid, datetime(startyear, 1, 1), datetime(endyear, 1, 1))

    s.atmp[s.atmp > 900] = np.nan
    s.dewp[s.dewp > 900] = np.nan
    s.wtmp[s.wtmp > 900] = np.nan
    s.wvht[s.wvht > 90] = np.nan
    s.apd[s.apd > 90] = np.nan


    with open('buoy_' + str(buoyid) + '.csv', 'w') as f:
        for n in range(s.time.size):
            record = [
                s.time[n].strftime('%Y-%m-%d %H:%M:%S'),
                '%.1f' % s.wdir[n],
                '%.1f'%s.wspd[n],
                '%.1f'%s.pres[n],
                '%.1f'%s.atmp[n],
                '%.1f'%s.wtmp[n],
                '27.504',
                '90.462'
            ]
            f.write(','.join(record) + '\n')


buoys = ["42041"]

for buoy in buoys:
    print('processing buoy:', buoy)
    write_buoy_to_csv(buoy, 2005, 2005)