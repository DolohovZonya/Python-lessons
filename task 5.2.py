from timeit import default_timer as dt
import random as rd
import numpy as np
import matplotlib.pyplot as plt

labels = ['2*2', '4*4', '8*8', '16*16', '32*32', '64*64', '128*128']
h_t = []
np_t = []
h_end = []
np_end = []
np_st = []
h_st = []
numpy_d = {}
hand_d = {}
for i in range(2,9):
  b = 2**i
  matrix = [[0]*b for i in range(b)]
  matrix2 = [[0]*b for i in range(b)]
  init_m = [[0]*b for i in range(b)]
  new_matrix = [[0]*b for i in range(b)]
  for w in range(len(matrix)):
    for j in range(len(matrix)):
      matrix[w][j] = rd.randint(0, 9)
      matrix2[w][j] = rd.randint(0, 9)
  start = dt()
  for i in range(3):
    for f in range(len(matrix)):
      for x in range(len(matrix)):
        for y in range(len(matrix)):
          new_matrix[f][x] += matrix[f][y]*matrix2[y][x]
    new_matrix = init_m
  duration = dt() - start
  h_t.append(duration)
  h_end.append(np.mean(h_t))
  hand_d[b] = np.mean(h_t)
  h_st.append(np.std(h_t))
  start2 = dt()
  for i in range(3):
    m_numpy = np.dot(matrix, matrix2)
  duration2 = dt() - start2
  np_t.append(duration2)
  np_end.append(np.mean(np_t))
  numpy_d[b] = np.mean(np_t)
  np_st.append(np.std(np_t))
print('no numpy: ', h_t, 'numpy: ', np_t)
fig1 = plt.figure(2, figsize=(12,8))
gridForm = (1,1)
ay = plt.subplot2grid(gridForm, (0,0))
ay.bar(labels, hand_d.values())
ay.set_title("hand time")
ay.set_xlabel("matrix size")
ay.set_ylabel("time")
ay.set_xticklabels(labels)
plt.yscale('log')
plt.show()
fig2 = plt.figure(1, figsize=(12,8))
gridForm = (1,1)
ax = plt.subplot2grid(gridForm, (0,0))
ax.bar(labels, numpy_d.values())
ax.set_title("numpy time")
ax.set_xlabel("matrix size")
ax.set_ylabel("time")
ax.set_xticklabels(labels)
plt.yscale('log')
plt.show()
