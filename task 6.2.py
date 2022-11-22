import pandas as pd

df = pd.read_excel("input.6.2.xlsx")
string = df['sequence']
big = []
consensus = ''
for pd in string:
  l_pd = list(pd)
  big.append(l_pd)
  new_list = list(map(list, zip(*big)))
for i in range(len(l_pd)):
  df[f'pos{i}'] = new_list[i]
  df_max = df[f'pos{i}'].value_counts().idxmax()
  consensus += df_max
print(consensus)
