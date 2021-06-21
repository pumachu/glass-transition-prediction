import matplotlib.pyplot as plt
from pylab import cm
from pylab import *
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib as mpl
import sys

# Edit the font, font size, and axes width
plt.rcParams['font.size'] = 12
plt.rcParams['axes.linewidth'] = 2

fig,ay = plt.subplots(nrows=3,ncols=2,sharex='col')
ax = ay.reshape(6)
def movingaverage(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')


T2 = []   ## temperature
D2 = []   ## density
f = open(sys.argv[1],'r')
l = f.readlines()
for line in l:
    if '0.0' in line:
        tmp = line.split()
        if float(tmp[0]) > 1000.0:
           T2.append(tmp[1])
           D2.append(tmp[2])
T2 = np.array(T2,dtype='float')
D2 = np.array(D2,dtype='float')

dic = {'temp':T2,'dens':D2}
df = pd.DataFrame(dic)

for n,fr in enumerate([50,100,150,200,250,300]):
    X = []
    R2 = []
    for T in range(0,800-fr):
        df1 = df[df.loc[:,'temp'] < float(T)+float(fr)]
        df1 = df1[df1.loc[:,'temp'] >= float(T)]
        X1 = df1.loc[:,'temp'].values
        Y1 = df1.loc[:,'dens'].values
        slope, intercept, r_value, p_value, std_err = stats.linregress(X1,Y1)
        X.append(float(T))
        R2.append(r_value**2.0)
    ax[n].plot(X,R2,label=str(fr))
    ax[n].legend(loc='lower left')
plt.show()

