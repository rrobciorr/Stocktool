import numpy as np , statistics as st

# Convetr array of values to standard deviation histogram 2D array
def get(day_change):
    arr = day_change
    arr.sort()
    min = arr[0]
    max = arr[-1]

    day_dev=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    x=0
    pold=min
    for p in np.linspace(min,max,41):
        if p!= min:
            for i in arr:
                if pold<=i<=p:
                    day_dev[x].append(i)
            x+=1
        pold = p

    q =[]
    mean =[]
    for a in range(40):
        if day_dev[a]:
            q.append(len(day_dev[a]))
            mean.append(round(st.mean(day_dev[a]),1))
        else:
            q.append(0)
            mean.append(0)

    return mean ,q 