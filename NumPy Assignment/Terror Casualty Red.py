import csv
import numpy as np
path='terrorismData.csv'
casualty=[]
## Here we filter out the data
with open(path, 'r',encoding='ISO-8859-1') as data:
  reader = csv.DictReader(data)
  for row in reader:
    if row['State']=='Jharkhand' or row['State']=='Odisha' or row['State']=='Andhra Pradesh' or row['State']=='Chhattisgarh':
      casualty.append([row['Killed'],row['Wounded']])
npcasualty=np.array(casualty)
## Coverting the empty values present in Killed and wounded feature to Zero
npcasualty[npcasualty=='']=0
## Converting the string value to float
npcasualty=np.array(npcasualty,dtype=float)
## Now Summing up the Killed and wounded feature to find out the casualty
npcasualty=np.sum(npcasualty,axis=1)
maxCasualty=np.sum(npcasualty)
print(int(maxCasualty))
