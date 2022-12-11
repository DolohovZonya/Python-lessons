import pandas as pd
import math as m
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("input.6.2.xlsx")
string = df['sequence']
big = []
cons = ''
for pd in string:
    l_pd = list(pd)
    big.append(l_pd)
    new_list = list(map(list, zip(*big)))
for i in range(len(l_pd)):
    df[f'pos{i}'] = new_list[i]
    df_max = df[f'pos{i}'].value_counts().idxmax()
    cons += df_max
    df = df.drop(columns = [f'pos{i}'])
print('cons: ' + cons)
colonka = []
colonka2 = []
colonka3 = []
for pd in string:
    num = 0
    perc = 0
    kant = 0
    for i in range(len(pd)):
        if pd[i] != cons[i]:
            num += 1
            perc = num / len(pd)
            a = 1-((4*perc)/3)
            try:
                kant = -1*(3/4)*m.log(a)
            except:
                kant = 'NaN'
    colonka.append(perc)
    colonka2.append(kant)
for pd in string:
    p = 0
    q = 0
    kimura = 0
    for index in range(len(pd)):
        if pd[index] != cons[index] and pd[index] == 'A':
            if cons[index] == 'G':
                p += 1
            else:
                q += 1
        if pd[index] != cons[index] and pd[index] == 'G':
            if cons[index] == 'A':
                p += 1
            else:
                q += 1
        if pd[index] != cons[index] and pd[index] == 'C':
            if cons[index] == 'T':
                p += 1
            else:
                q += 1
        if pd[index] != cons[index] and pd[index] == 'T':
            if cons[index] == 'C':
                p += 1
            else:
                q += 1
    f = p/len(cons)
    d = q/len(cons)
    try:
        kimura = (-1/2)*(m.log(1 - 2*f - d)) - (1/4)*(m.log(1-2*d))
    except:
        kimura = 'NaN'
    colonka3.append(kimura)
df['distance'] = colonka
df['Kantor'] = colonka2
df['Kimura'] = colonka3
print(df)
df1 = df.drop(columns = ['sequence'])
df2 = df1[df1.isin(['NaN']).any(axis=1)]
df2['Kimura'] = np.where(df2['Kimura'] == 'NaN', 0, 0)
df2['Kantor'] = np.where(df2['Kantor'] == 'NaN', 0, 0)
df3 = df1[np.core.chararray.find(df1.Kantor.values.astype(str),'NaN') < 0]
df3 = df3[np.core.chararray.find(df3.Kimura.values.astype(str),'NaN') < 0]
fig = sns.violinplot(data = [df2['distance'], df3['distance']])
fig.set(xlabel = 'seqs',
ylabel = 'distance',
title = 'distribution'
)
plt.xticks([0,1], ['one nan', 'every known'])
fig.get_figure().savefig('violin.png')
