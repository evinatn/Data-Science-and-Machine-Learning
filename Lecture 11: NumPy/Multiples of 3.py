## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np
a = np.array([1,  3,  5,  7,  9, 11, 13, 15, 17, 19])
ind1 = np.where(a % 3 == 0)
for i in ind1:
    print(*i,end= " ")
