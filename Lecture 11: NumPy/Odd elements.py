## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
for i in range(10):
  if a[i]%2 !=0:
    a[i]=-1
for i in range(10):
  print(a[i],end=" ")
