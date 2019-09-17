# Kendirc Hood
# Cloud Computing HW 2 
# pt:2 Min-Min / Min-Max scheduler
from pathlib import Path
import pandas as pd  
import numbers

# input: vaild CSV file
# output: bag object (vector of maps)
def parser(FileName):
    rawData = pd.read_csv(Path(FileName))  
  
    machines = rawData.columns[1:]
    bag = dict()
    
    m = machines[0]
    for index, row in rawData.iterrows():
        task = row[0]
        bag[task] = dict()
        vals = row[1:]
        for v in vals:
            if isinstance(float(v), numbers.Number):
                bag[task][float(v)] = next(m)
                
    print (bag)
    return "foo"