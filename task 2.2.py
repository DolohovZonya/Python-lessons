N = int(input())
if N == 1:
  print(1)
elif N == 2:
  print(1, 1, sep='\t')
else:
  a = 0
  b = 1
  print(a, b)
  for i in range(2, N):
    print(a + b)
    a, b = b, a+b
