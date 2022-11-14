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
    'ACT': 'H', 'ACG': 'V', 'ACGT': 'N', '\n': ''}
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
file_name = input()
dna1 = []
dna3 = []
with open(file_name, "r") as buf:
  dna = buf.readlines()
for i in range(len(dna)):
  dna1.append(list(dna[i]))
columnss = [int(i) for i in range(len(dna[0]))]
index = [int(i) for i in range(len(dna))]
df = pd.DataFrame(dna1, index, columnss)
maximum(df, columnss)
for seq in dna1:
  dna2 = []
  num_a = seq.count('A')
  num_t = seq.count('T')
  num_g = seq.count('G')
  num_c = seq.count('C')
  dna2.append(num_a / len(seq))
  dna2.append(num_t / len(seq))
  dna2.append(num_g / len(seq))
  dna2.append(num_c / len(seq))
  dna3.append(dna2)
print(dna3)
x = np.arange(len(dna3))
fig, ax = plt.subplots()
for i in range(len(dna3)):
  ax.bar(x, dna3[i][0])
  ax.bar(x, dna3[i][1], bottom=dna3[i][0])
  ax.bar(x, dna3[i][2], bottom=dna3[i][1])
  ax.bar(x, dna3[i][3], bottom=dna3[i][2])
