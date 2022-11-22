import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def maximum(df, columns):
  codes = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T', 
    'GA': 'R', 'TC': 'Y', 'GC': 'S', 'TA': 'W', 
    'TG': 'K', 'CA': 'M', 'GCT': 'B', 'TGC': 'B',
    'CTG': 'B', 'GTC': 'B', 'TCG': 'B', 'ATC': 'D', 
    'TCA': 'D', 'TAC': 'D', 'CAT': 'D', 'CTA': 'D', 
    'AGC': 'V', 'GAC': 'V', 'GCA': 'V', 'CAG': 'V',
    'CGA': 'V', 'AG': 'R', 'CT': 'Y', 'CG': 'S', 'AT': 'W', 
    'GT': 'K', 'AC': 'M', 'CGT': 'B', 'AGT': 'D', 
    'ACT': 'H', 'ACG': 'V', 'ACGT': 'N'}
  string = ''
  for i in columns:
    df_dict = dict(df[i].value_counts())
    keys = ''
    max = 0
    for k, v in df_dict.items():
      if v < max:
        continue
      if v > max:
        max = v
      if v == max:
        keys += k
    for k in codes.keys():
      if keys == k:
        string += codes[k]
  print(string)
def bar(df, columns):
  codes = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
  x = columnss
  fig, ax = plt.subplots()
  for i in columns:
    df_dict = dict(df[i].value_counts())
    for k, v in df_dict.items():
      cd = codes.copy()
      for key in cd.keys():
        if k == key:
          cd[key] = v
      ax.bar(x, cd['A'])
      ax.bar(x, cd['T'], bottom=cd['A'])
      ax.bar(x, cd['C'], bottom=cd['T'])
      ax.bar(x, cd['G'], bottom=cd['C'])
  fig.show()
file_name = input()
dna1 = []
with open(file_name, "r") as buf:
  dna = buf.readlines()
for i in range(len(dna)):
  dna1.append(list(dna[i]))
for sp in dna1:
  for i in range(len(sp)):
    if sp[i] == '\n':
      sp.remove('\n')
columnss = [int(i) for i in range(len(dna1[0]))]
index = [int(i) for i in range(len(dna1))]
df = pd.DataFrame(dna1, index, columnss)
maximum(df, columnss)
bar(df, columnss)
