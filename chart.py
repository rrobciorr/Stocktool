import matplotlib.pyplot as plt
import numpy as np

def show(x,y):

    N = len(y)
    menMeans = y

    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    p1 = ax.bar(ind, menMeans, width,  label='Men')

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind, labels=x)
    ax.legend()

    # Label with label_type 'center' instead of the default 'edge'
    ax.bar_label(p1, label_type='center')

    plt.show()