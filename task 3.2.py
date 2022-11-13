import random as rd
def number(a, b):   
  return(rd.randint(a,b))
N = number(1, 12)

max_val = 0
max_seq = ''
min_val = 12
in_count = 0
num_s = ''
for i in range(N):
    l = rd.randint(1, 12)
    seq =''.join([rd.choice('ATGC') for _ in range(l)])
    print(f'> Sequence {i +1}')
    if l > 60:
        print(seq[:60])
        print(seq[60:])
    else:
        print(seq)
    if l >= max_val:
        max_val = l
    if l <= min_val:
        min_val = l
    if l == max_val:
      max_seq = seq
    if l == min_val:
      min_seq = seq
    count = (seq.count('G') + seq.count('C')) / l
    if count > in_count:
      in_count = count
      num = i+1
      num_s = seq
print("longest:", max_seq, "shortest:", min_seq, "biggest gc value:", num_s)
