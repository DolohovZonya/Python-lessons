import pandas as pd

def concensus(string):
  cons = list(string)
  num_a = 0
  num_t = 0
  num_c = 0
  num_g = 0
  max_num = []
  for i in range(len(string)):
    if cons[i] == 'A':
      num_a += 1
    if cons[i] == 'T':
      num_t += 1
    if cons[i] == 'C':
      num_c += 1
    if cons[i] == 'G':
      num_g += 1
  max_num.append(num_a)
  max_num.append(num_g)
  max_num.append(num_t)
  max_num.append(num_c)
  max_number = max(max_num)
  if max_number == num_a:
    return 'A'
  if max_number == num_t:
    return 'T'
  if max_number == num_c:
    return 'C'
  if max_number == num_g:
    return 'G'
df = pd.read_excel("input.6.2.xlsx")
df["sequence"].apply(concensus)

print(df)
