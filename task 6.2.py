import pandas as pd

df = pd.read_excel("input.6.2.xlsx")
string = df['sequence']
cons = list(string)
print(type(string))
print(type(cons[1]))
for i in range(len(cons)):
  num_a = 0
  num_t = 0
  num_c = 0
  num_g = 0
  max_num = []
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
  print(max_num)
  if max_number == num_a:
    print('A')
  if max_number == num_t:
    print('T')
  if max_number == num_c:
    print('C')
  if max_number == num_g:
    print('G')

print(df)
