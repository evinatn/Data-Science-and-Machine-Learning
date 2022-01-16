import numpy as np

a = np.array([11, 2, 13, 4, 15, 6, 27, 8, 19])

a1 = a.argmax()

a[a1]= 0

for i in a:
    print(i)
