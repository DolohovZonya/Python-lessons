from timeit import default_timer
import random as rd
x = 2
for i in range(1, x+1):
  b = 2**i
  matrix = [[0]*b for i in range(b)]
  matrix2 = [[0]*b for i in range(b)]
  new_matrix = [[0]*b for i in range(b)]
  for w in range(len(matrix)):
    for j in range(len(matrix)):
      matrix[w][j] = rd.randint(0, 9)
      matrix2[w][j] = rd.randint(0, 9)
      start = default_timer()
      for i in range(101):
        new_matrix[w][j] = matrix[w][j]*matrix2[w][j]
      duration = default_timer() - start
  print(matrix, matrix2, new_matrix, duration)
