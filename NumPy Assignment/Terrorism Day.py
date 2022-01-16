## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np
import csv
data = csv.DictReader(open('terrorismData.csv'), skipinitialspace=True)

day=[]
attack=[]
 
for row in data:
  attack.append(row['AttackType'])
  day.append(row['Day'])

np_day=np.array(day)
np_attack=np.array(attack)

np_day[np_day=='']='0'

np_day=np.array(np_day,dtype=float)
sum=0
for i in np_day:
  if int(i)<21 and int(i)>=10:
    sum=sum+1
print(sum)
