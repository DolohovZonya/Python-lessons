from timeit import default_timer as dt
import random as rd
import numpy as np
x = 3
for i in range(1, x+1):
  b = 2**i
  k = 0
  k2 = 0
  matrix = [[0]*b for i in range(b)]
  matrix2 = [[0]*b for i in range(b)]
  new_matrix = [[0]*b for i in range(b)]
  for w in range(len(matrix)):
    for j in range(len(matrix)):
      matrix[w][j] = rd.randint(0, 9)
      matrix2[w][j] = rd.randint(0, 9)
      start = dt()
      for i in range(101):
        new_matrix[w][j] = matrix[w][j]*matrix2[w][j]
      duration = dt() - start
      k += duration
      start2 = dt()
      for i in range(101):
       m_numpy = np.dot(matrix, matrix2)
      duration2 = dt() - start2
      k2 += duration2
  print(new_matrix, '\n', m_numpy, '\n', duration, '\n', duration2)
