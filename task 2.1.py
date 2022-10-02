import random as rd
def number(a, b):
  return(rd.randint(a,b))
x = number(1, 100)
count = 0
print("Введите число")
guess = int(input())
while guess != x and guess != -1:
  if guess > x:
    print("ваше число больше загаданного")
    guess = int(input())
    count +=1
  elif guess < x:
    print("ваше число меньше загаданного")
    guess = int(input())
    count +=1
if guess == -1:
  print("проигрыш(")
if guess == x:
  if count == 1:
    print("вы победили, вы использовали 1 попыткy")
  elif count <= 4:
    print(f"вы победили, вы использовали {count} попытки")
  elif count >= 5:
    print(f"Вы победили, вы использовали {count} попыток")
