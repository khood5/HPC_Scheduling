# Kendirc Hood
# Cloud Computing HW 2 
# pt:2 Min-Min / Min-Max scheduler
from pathlib import Path
import pandas as pd  
from bag import bag
from bag import cost
from bag import machine_id

# input: vaild CSV file
# output: bag object (vector of maps)
def parser(FileName):
    rawData = pd.read_csv(Path(FileName))  
  
    machines = rawData.columns[1:]
    bagOf = dict()
    
    m = 0
    for index, row in rawData.iterrows():
        task = str(row[0]).strip()
        bagOf[task] = list()
        vals = row[1:]
        for v in vals:
            try:
                bagOf[task].append({cost:float(v), machine_id:str(machines[m]).strip()})
            except ValueError:
                pass # not a number so skip
            m += 1
        m = 0
                
    return bag(bagOf)