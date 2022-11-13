import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def consensus(df, string):
    for i in columns:
      a = dict(df[i].value_counts())
      x = max(a, key = a.get)
      string += x
    return string
file_name = input()
dna1 = []
dna3 = []
string = ''
with open(file_name, "r") as buf:
  dna = buf.readlines()
for i in range(len(dna)):
  dna1.append(list(dna[i]))
columns = [int(i) for i in range(len(dna[0]))]
index = [int(i) for i in range(len(dna))]
print(columns)
df = pd.DataFrame(dna1, index, columns)
consensus(df, string)
for i in columns:
  a = dict(df[i].value_counts())
  x = max(a, key = a.get)
  string += x
print(string)
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
  print(dna3[i][0])
  ax.bar(x, dna3[i][0])
  ax.bar(x, dna3[i][1], bottom=dna3[i][0])
  ax.bar(x, dna3[i][2], bottom=dna3[i][1])
  ax.bar(x, dna3[i][3], bottom=dna3[i][2])
