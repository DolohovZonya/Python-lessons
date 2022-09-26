import math as m
a = int(input())
b = int(input())
c = int(input())
x1 = 0
x2 = 0
if a == 0 and b == 0 and c == 0:
  print("корней бесконечно много")
elif c == 0 and a != 0 and b != 0:
  x1 = 0
  x2 += (b/a)*-1
  print(x1, x2)
elif a == 0 and b != 0 and c != 0:
  print((c/b)*-1)
elif b == 0 and a != 0 and c != 0:
  result = -1*(c/a)
  if result > 0:
    x1 += m.sqrt(result)
    x2 -= m.sqrt(result)
    print(x1, x2)
  if result < 0:
    print("корней нет")
else:
  disc = b**2 - 4*a*c 
  if disc > 0:
    x1 += (-b + m.sqrt(disc))/(2*a)
    x2 += (-b - m.sqrt(disc))/(2*a)
    print(x1, x2)
  elif disc == 0:
    x1 += -b/(2*a)
    x2 = x1
    print(x1, x2)
  else:
    print("корней нет")
