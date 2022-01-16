import numpy as np
import csv
path='terrorismData.csv'
date=[]
with open(path,'r',encoding='ISO-8859-1') as data:
  reader=csv.DictReader(data)
  for row in reader:
    date.append([row['Day'],row['Month'],row['Year']])
npdate=np.array(date,dtype=int)
npdate=npdate[npdate[:,2]==2010]
npdate=npdate[npdate[:,1]==1]
npdate=npdate[npdate[:,0] =1]
print(npdate.shape[0])
