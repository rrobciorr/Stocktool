import numpy as np , statistics as st
from datetime import datetime
# IDEA SCRIPT :
# input days change 
# output tab with continus raice or fall period in [weeks] unit 
#
# Convetr array of values to lenghtitudes of continus raice or fall period in week unit 
def get(data):
    weeks=[]
    monday=0
    init = 1
    #Parse market data format to weeks format : [[monday_open,friday_close],...]
    for t,o,c in zip(data['timestamp'],data['open'], data['close']):
        date = datetime.fromtimestamp(t)
        if date.weekday() == 0:
            monday = o
            init = 0
        if date.weekday() == 4    & init != 1:
            friday = c
            weeks.append([monday,friday])

    raice_period = 0
    is_change_directory = 0
    old_directory = 0
    actual_period=0
    period_tab = []
    init = 1    
    # convert weeks to  tab with continus raice or fall period in [weeks] unit        
    for week in weeks:
        monday = week[0]
        friday = week[1]

        if init:
            if monday < friday :
                old_directory = 1
                init = 0
      
        directory = 0
        if monday < friday:
            directory = 1

        if directory !=  old_directory:
            is_change_directory ^= 1 #toogle status
  
        if is_change_directory: #close and save the period and return to init set
            period_tab.append(actual_period)
            actual_period = 0
      
        if directory:
            actual_period += 1
        else:
            actual_period -= 1

    return period_tab