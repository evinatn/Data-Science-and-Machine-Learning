import numpy as np
import csv
data = csv.DictReader(open('terrorismData.csv'), skipinitialspace=True)
killed=[]
usa=[]
country=[]
for row in data:
  killed.append(row['Killed'])
  country.append(row['Country'])

np_killed=np.array(killed)
np_country=np.array(country)
np_killed[np_killed=='']='0'

bool_arr = np_country == 'United States'

ans=np_killed[bool_arr]
ans=np.array(ans,dtype=float)
for i in ans:
  print(int(i))

