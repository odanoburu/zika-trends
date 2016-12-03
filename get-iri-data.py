import os
import sys
import time
import numpy as np
import pandas as pd
import datetime

base_url = 'http://iridl.ldeo.columbia.edu/SOURCES/SOURCES/.UCSB/.CHIRPS/.v2p0/.daily/.global/.0p05/.prcp/T/(Jan%202016)/(Dec%202016)/RANGE/X/-44.0/-42.6/RANGE/Y/-23.1/-22.5/RANGE/T/pentadAverage/T/1460.5/VALUE/%5BX/Y/%5D/palettecolor.tiff?filename='
date_range1 = pd.date_range('20160101', '20161130', freq = '5D')
date_range2 = pd.date_range('20160105', '20161130', freq = '5D')
os.system("cd '{}').format('/home/brunocuconato/zika/prcp')
for i in range(len(date_range1)):
    dbeg = date_range1[i].day
    dend = date_range2[i].day
    month = date_range1[i].month
    year = 2016
    change_url = 'data{}{}{}-{}.tiff'.format(year, month, dbeg, dend)
    url = base_url + change_url
    os.system("wget '{}'".format(url))