import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
import pandas as pd
import numpy as np
from scipy import stats
import sys

# Edit the font, font size, and axes width
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 2


fig,ax = plt.subplots(figsize=(8,8))


color = ['#E99497','#F3C583','#E8E46E','#B3E283']
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

for n,fr in enumerate([150,200,250,300]):
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

    X = np.array(X,dtype='float')
    R2 = np.array(R2,dtype='float')
    dic = {'X':X,'R2':R2}
    df = pd.DataFrame(dic)
    df1 = df[df.loc[:,'X'] > X[np.argmin(R2)] ]
    X1 = df1.loc[:,'X'].values.tolist()
    Y1 = df1.loc[:,'R2'].values.tolist()
    range1 = X1[Y1.index(max(Y1))]

    df1 = df[df.loc[:,'X'] < X[np.argmin(R2)] ]
    X1 = df1.loc[:,'X'].values.tolist()
    Y1 = df1.loc[:,'R2'].values.tolist()
    range2 = X1[Y1.index(max(Y1))]

    print('Fitting Range1:[',range1,',',range1+fr,')')
    print('Fitting Range2:[',range2,',',range2+fr,')')

    dic = {'temp':T2,'dens':D2}
    df = pd.DataFrame(dic)


    df1 = df[df.loc[:,'temp'] < range1+float(fr)]
    df1 = df1[df1.loc[:,'temp'] >= range1]
    X1 = df1.loc[:,'temp'].values
    Y1 = df1.loc[:,'dens'].values

    df2 = df[df.loc[:,'temp'] <range2+float(fr)]
    df2 = df2[df2.loc[:,'temp'] >= range2]
    X2 = df2.loc[:,'temp'].values
    Y2 = df2.loc[:,'dens'].values

    m1,b1 = polyfit(X1, Y1, 1)
    m2,b2 = polyfit(X2, Y2, 1)
    X = np.linspace(100.0,700.0,100)
    Tg = (b2-b1)/(m1-m2)
    print (fr,Tg-273.15)
    XX1 = np.linspace(Tg-50.0,range1+fr,100)
    XX2 = np.linspace(range2,Tg+50.0,100)
    Tg = (b2-b1)/(m1-m2)
    ax.plot(XX1,m1*XX1+b1,lw=2,c=color[n],label=str(fr)+' K')
    ax.plot(XX2,m2*XX2+b2,lw=2,c=color[n])
    ax.legend()
    Tg = '{:3.2f}'.format(Tg-273.15)

ax.scatter(T2,D2,s=1,c='black')
ax.set_xlabel('Temperature (K)')
ax.set_ylabel(r'Density (kg/m$^3$)')
plt.show()
