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
  fin_list = []
  codes = ['A', 'T',
           'C', 'G']
  fin_list = []
  for j in codes:
    lst = np.zeros(len(columns))
    for i in range(len(lst)):
      lst[i] = df[i].to_string(index=False).count(j)
    fin_list.append(lst)
  x = np.arange(len(fin_list[0]))
  plt.bar(x, fin_list[0], color='blue',
          label=codes[0])
  plt.bar(x, fin_list[1], color='green',
          bottom=fin_list[0], label=codes[1])
  plt.bar(x, fin_list[2], color='yellow',
          bottom=(fin_list[1]+fin_list[0]), label=codes[2])
  plt.bar(x, fin_list[3], color='red',
          bottom=(fin_list[2]+fin_list[1]+fin_list[0]), label=codes[3])
  plt.legend()
  plt.xlabel('position')
  plt.ylabel('nucleotides num')
  plt.show()
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
