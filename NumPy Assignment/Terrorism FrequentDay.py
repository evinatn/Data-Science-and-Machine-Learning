## Open and read data file as specified in the question
## Print the required output in given format
import csv
import numpy as np
with open("terrorismData.csv",encoding="utf8") as file_obj:
    file_data=csv.DictReader(file_obj,skipinitialspace=True)
    attack=[]
    for row in file_data:
        attack.append(row['Day'])
    attack=np.array(attack,dtype=int)
    a,counts=np.unique(attack,return_counts=True)
    x=counts.argmax()
    print(a[x],counts[x])
