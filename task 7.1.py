import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = np.arange(4)

def histogramm(dna):
  dna1 = list(dna)
  plt.hist(dna1)
def pie(dna):
  dna1 = []
  num_a = dna.count('A')
  num_t = dna.count('T')
  num_g = dna.count('G')
  num_c = dna.count('C')
  dna1.append(num_a)
  dna1.append(num_t)
  dna1.append(num_g)
  dna1.append(num_c)
  labels = ['A', 'T', 'G', 'C']
  colors = ['red', 'green', 'blue', 'yellow']
  explode = [0, 0, 0, 0]
  plt.pie(dna1, explode=explode, labels=labels, colors=colors, autopct="%.2f%%", shadow=False, startangle=90)
def hist_codons(dna):
  dna1 = []
  for i in range(0, (len(dna) - 2), 3):
    dna1.append(dna[i:i+3])
  plt.hist(dna1, bins = 10)
def boxplot(dna):
  dna1 = []
  dna2 = []
  for i in range(0, (len(dna) - 2), 3):
    dna1.append(dna[i:i+3])
  for i in dna1:
    dna2.append(dna1.count(i))
  fig = sns.boxplot(data=dna2)
  plt.xticks([0], ["codons"])
with open('string_one.txt', "r") as buf:
  dna = buf.read()

ax1 = plt.subplot(2,2,1)
histogramm(dna)
ax2 = plt.subplot(2,2,2)
pie(dna)
ax3 = plt.subplot(2,2,3)
hist_codons(dna)
ax4 = plt.subplot(2,2,4)
boxplot(dna)
