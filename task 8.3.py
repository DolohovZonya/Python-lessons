from Bio import pairwise2
def compare(sym1, sym2):
  if sym1 == sym2:
    return 1
  else:
    return -1

def NW(x, y, g):
  lx = len(x)
  ly = len(y)
  matrix = [[0]*(lx+1) for i in range(ly+1)]
  print(*matrix, sep='\n')
  for i in range(lx+1):
    matrix[0][i] = g*i
  for j in range(ly+1):
    matrix[j][0] = g*j
  for i in range(1, ly+1):
    for j in range(1, lx):
      diag = matrix[i-1][j-1] + compare(x[j-1], y[i-1])
      up = matrix[i-1][j] + g
      left = matrix[i][j-1] + g
      matrix[i][j] = max(diag, up, left)
  print(*matrix, sep='\n')
  #обратный ход
  i = ly
  j = lx 
  alig1 = []
  alig2 = []
  while (i != 0) and (j != 0):
    if matrix[i][j] == (matrix[i-1][j] + g) and (i != 0):
      i = i-1
      alig1.append('-')
      alig2.append(y[i])
    elif matrix[i][j] == (matrix[i][j-1] + g) and (j != 0):
      j = j-1
      alig2.append('-')
      alig1.append(x[j])  
    diag = matrix[i-1][j-1] + compare(x[j-1], y[i-1])
    up = matrix[i-1][j] + g
    left = matrix[i][j-1] + g
    if matrix[i][j] == diag:
      i = i-1
      j = j-1
      alig1.append(x[j])
      alig2.append(y[i])
    elif matrix[i][j] == up:
      i = i-1
      alig1.append('-')
      alig2.append(y[i])
    else:
      j = j-1
      alig2.append('-')
      alig1.append(x[j])     
  while i != 0:
    i = i-1
    alig1.append('-')
    alig2.append(y[i])
  while j != 0:
    j = j-1
    alig1.append(x[i])
    alig2.append('-')
  return matrix[-1][-1], ''.join(alig1[::-1]), ''.join(alig2[::-1])
  aligments = pairwise2.align.globalms(x, y, 1, -1, -1, -1)
s1 = 'ATGCAGCCTCGCGC'
s2 = 'ATGCCCGTAGAGCCG'
gap = -1
print(NW(s1, s2, gap))
