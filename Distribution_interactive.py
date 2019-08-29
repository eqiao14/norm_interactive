

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df


get_ipython().magic('matplotlib notebook')

import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.ticker as tick
import math
from matplotlib.cm import ScalarMappable 
import statistics
import scipy.stats

    
def onclick(event):
    #clear axes, create new data_color scheme to color axes
    plt.cla()
    data_color = list()
    for i in range(4):
        data_color.append(scipy.stats.norm.sf(abs((event.ydata - data_hight[i]) / stdL[i]))*2)

    colors = my_cmap(data_color)
    
    #plot the new bars with updated color schemes and the error bars
    plt.bar(data_x, data_hight, color=colors)
    plt.bar(1992, df.iloc[0].mean(), yerr=std1992*2, align='center', alpha=0, ecolor='black', capsize=10)
    plt.bar(1993, df.iloc[1].mean(), yerr=std1993*2, align='center', alpha=0, ecolor='black', capsize=10)
    plt.bar(1994, df.iloc[2].mean(), yerr=std1994*2, align='center', alpha=0, ecolor='black', capsize=10)
    plt.bar(1995, df.iloc[3].mean(), yerr=std1995*2, align='center', alpha=0, ecolor='black', capsize=10)

    #Set the x-axis to only show the year
    ax = plt.gca()
    ax.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax.xaxis.set_major_locator(tick.FixedLocator([1992,1993,1994,1995]))
    
    #plot red line at the y coordinate that user clicks
    plt.axhline(y=event.ydata, color='r', linestyle='-')
    
    #Set Labels
    ax.set_xlabel('Year')
    ax.set_ylabel('Mean of Distribution')
    ax.set_title('Probability of Y in Distribution')
    #Remove borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    plt.gca().set_title('Probability of Y in Distribution \n Y Value of {} Selected'.format( event.ydata))

    

##Set the data x and y 
data_x = [1992,1993,1994,1995]
data_hight = [df.iloc[0].mean(),df.iloc[1].mean(),df.iloc[2].mean(),df.iloc[3].mean()]

#First plot is only based on height of bar
data_color = [x / max(data_hight) for x in data_hight]

fig, ax = plt.subplots()
#Pull from the divergent bwr color group 
my_cmap = plt.cm.get_cmap('bwr')
colors = my_cmap(data_color)

ax.bar(data_x, data_hight, color=colors)

#Set scale and color of colorbar
sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(0,max(data_color)))
sm.set_array([])

cbar = plt.colorbar(sm)
cbar.set_label('Color', rotation=270,labelpad=25)

#Calculate stdErr of each distribution 
std1992 = df.iloc[0].std()/math.sqrt(3650)
std1993 = df.iloc[1].std()/math.sqrt(3650)
std1994 = df.iloc[2].std()/math.sqrt(3650)
std1995 = df.iloc[3].std()/math.sqrt(3650)

stdL = [std1992,std1993,std1994,std1995]

#plotting error bars
plt.bar(1992, df.iloc[0].mean(), yerr=std1992*2, align='center', alpha=0, ecolor='black', capsize=10)
plt.bar(1993, df.iloc[1].mean(), yerr=std1993*2, align='center', alpha=0, ecolor='black', capsize=10)
plt.bar(1994, df.iloc[2].mean(), yerr=std1994*2, align='center', alpha=0, ecolor='black', capsize=10)
plt.bar(1995, df.iloc[3].mean(), yerr=std1995*2, align='center', alpha=0, ecolor='black', capsize=10)

ax = plt.gca()

#Set the x axis and tick locations 
ax.xaxis.set_major_locator(plt.MaxNLocator(4))
ax.xaxis.set_major_locator(tick.FixedLocator([1992,1993,1994,1995]))
#Set Labels
ax.set_xlabel('Year')
ax.set_ylabel('Mean of Distribution')
ax.set_title('Probability of Y in Distribution')
#Remove borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)


# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event', onclick)







