https://gist.github.com/jupihes/98ae06d2e65eba5cd73d057de95be8c6#file-persian_to_gregorian-py

import datetime
import jdatetime
from pandas import to_datetime

def p_to_g(d):
    '''
    Persian date instance to Gregorian date instance converstion assuming input date format to be format="%Y/%m/%d"
    and provide output in same format.
    '''
    d = d.split('/')

    return to_datetime(jdatetime.date(int(d[0]), int(d[1]),int(d[2])).togregorian(),\#utc=True, 
                       format="%Y/%m/%d")

############
sample_date = '1330/12/09'

gdate = p_to_g(sample_date)
Out[1]: Timestamp('1952-02-29 00:00:00+0000')
    
gdate.date()
Out[2]: datetime.date(1952, 2, 29)
