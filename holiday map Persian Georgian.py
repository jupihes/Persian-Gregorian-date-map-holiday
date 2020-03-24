# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 2020
@author: hesam.mo
"""
import pandas as pd
import requests  

def Persian_year_list(y=1398):
    date_list = []
    if y%4 == 3:
        k = 31 # leap year identifiation 1395 was leap year
    else:
        k = 30
    for i in range(1,13): # for 12 months
        if i<7: # first 6 months
            for j in range(1,32):
                date_list.append(str(y)+'-'+str(i)+'-'+str(j))
        elif i<12: # next 5 months
            for j in range(1,31):
                date_list.append(str(y)+'-'+str(i)+'-'+str(j))
        else: # Esfand
            for j in range(1,k):
                date_list.append(str(y)+'-'+str(i)+'-'+str(j))
    return 


def date_mapping(date_list):
    L = []
    for i in date_list:
        # url = 'https://pholiday.herokuapp.com/date/'+ i
    
        txt = requests.get('https://pholiday.herokuapp.com/date/'+ i).json()
        if len(txt.get('events')) == 0:
            event = [] # txt.get('events')[1].get('event')
            #holiday_status = False
        elif len(txt.get('events'))>1:
            event = txt.get('events')[1].get('event')
            #holiday_status = True
        else:
            event = txt.get('events')[0].get('event')
            #holiday_status = True
        L.append([txt.get('date'),txt.get('gdate'),txt.get('isHoliday'), event])
    
    return(pd.DataFrame(L,columns = ['pdate','gdate','holiday','event']))

L = []
df = pd.DataFrame(L,columns = ['pdate','gdate','holiday','event'])
for i in range(1393,1399):
    df = pd.concat([df,date_mapping(Persian_year_list(i))],ignore_index=True) 
    

# df = pd.concat([df93,df94,df95,df96,df97,df98],ignore_index=True)

## adding part to identify weekends
df.loc[df.holiday == True, 'holiday or weekend'] = True 
df.loc[df[df.event =='جمعه'].index.values - 1, 'holiday or weekend'] = True
df.loc[df['holiday or weekend']> 0, 'holiday or weekend'] = 1
df.loc[df['holiday or weekend'] != 1, 'holiday or weekend'] = 0
