import mail, downloader as dl  ,str1, str2, str3, chart

data = dl.get2("SPY",0)
#days_change = str1.get(data)
#x, day_dev = str2.get(days_change[4])
#chart.show(x,day_dev)

#print(day_dev)]
#mail.send(str(data))

period_rice_fall_weeks = str3.get(data) # Convetr array of values to lenghtitudes of continus raice or fall period in week unit 

xx, yy = str2.get(period_rice_fall_weeks) # Convetr array of values to standard deviation histogram 2D array
chart.show(xx,yy)
