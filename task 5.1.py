import numpy as np 

n_3 = 100000
for i in range(3, 10):
    k = 0
    for _ in range(n_3):
        x = np.random.randint(10, size=(i, i))
        #print(x)
        matrix_in = (x[1:i-1, 1:i-1])
        sum_in = matrix_in.sum()
        sum_out = x.sum() - sum_in
        if sum_out > sum_in:
            k += 1
    print(k/n_3)
