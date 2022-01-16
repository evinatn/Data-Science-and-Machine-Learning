## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np
import csv

with open('terrorismData.csv','r',encoding="utf8") as obj:
    file_data = csv.DictReader(obj,skipinitialspace = True)
    
    killed = []
    wounded = []
    month = []
    city = []
    group=[]
    for row in file_data:
        if row['Country'] == 'India' and row['Year'] == '1999' and row['State'] == 'Jammu and Kashmir':
            killed.append(row['Killed'])
            wounded.append(row['Wounded'])
            month.append(row['Month'])
            city.append(row['City'])
            #print(row)
            group.append(row['Group'])
            
np_killed = np.array(killed)
np_wounded = np.array(wounded)
np_month = np.array(month,dtype = int)
np_city = np.array(city)
np_group = np.array(group)

np_killed[np_killed == ''] = '0.0'
np_wounded[np_wounded == ''] = '0.0'

np_killed = np.array(np_killed,dtype= float)
np_wounded = np.array(np_wounded,dtype = float)

np_casuality = np_killed + np_wounded

ind_mo = (np_month <= 7 ) & (np_month >= 5)
ind_mo

np_casuality = np_casuality[ind_mo]
np_city = np_city[ind_mo]
np_group = np_group[ind_mo]

k = np_casuality.argmax()
print(int(np_casuality[k]),np_city[k],np_group[k])
