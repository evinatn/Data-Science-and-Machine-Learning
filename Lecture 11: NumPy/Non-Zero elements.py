import numpy as np
nparray=np.array([1,2,0,0,4,0])
for i in np.where(nparray!=0)[0]:
  print(i,end=" ")
