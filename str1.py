from datetime import datetime
import numpy as np , statistics as st

def get(data):
    
    days_change=[[],[],[],[],[]]
    x=0
    for i in data['timestamp']:
        date = datetime.fromtimestamp(i)
        if x>0: 
           # today = (data['low'][x] + data['high'][x] )/2
            #yesterday = (data['low'][x-1] + data['high'][x-1]) /2
            today = data['high'][x]
            yesterday = data['low'][x]

            change = (today-yesterday)*100/yesterday
            days_change[date.weekday()].append(change)
        x+=1

    mean =[]
    for a in range(5):
        mean.append(st.mean(days_change[a]))

    return days_change
