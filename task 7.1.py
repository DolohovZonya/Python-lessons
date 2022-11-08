import matplotlib.pyplot as plt
dna = list(input())
plt.hist(dna, bins = len(dna), range = (0, len(dna)))
plt.show()
import matplotlib.pyplot as plt
dna = list(input())
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
plt.show()
