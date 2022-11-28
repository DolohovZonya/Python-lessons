#зачтено
import math as m

a = int(input())
b = int(input())
c = int(input())
x1 = 0
x2 = 0
if a == 0:
  if b == 0:
    if c == 0:
      print("infinite num of roots")
    else:
      print("unreal")
  else:
    if c == 0:
      print(0)
    else:
      x1 = -1*(c/b)
      print(x1)
else:
  if b == 0:
    if c == 0:
      print(0)
    else:
      x1 = m.sqrt(c / a)
      x2 = -1*(x1)
      print(x1, x2)
  else:
    if c == 0:
      x2 = b / a
      x1 = 0
      print(x1, x2)
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
        print("no roots")
