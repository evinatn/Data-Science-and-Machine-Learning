import numpy as np
b=(np.arange(10) == 4).astype(int)
for i in range(10):
    print(b[i],end=" ")
