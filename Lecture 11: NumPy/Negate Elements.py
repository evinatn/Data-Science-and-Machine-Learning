## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
for i in a:
    if i<=8 and i>=3:
        i=i*-1
        print(i)
    else:
        print(i)
