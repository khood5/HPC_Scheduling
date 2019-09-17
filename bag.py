from pathlib import Path

# pair
cost = "cost"
machine_id = "machine_id"

class bag:
    tasks = dict(list(dict())) # tasks map top a list of costs and machines ex: {'T1': [(10.0, 'M1 '), (20.0, ' M2 ')]}

    def __init__(self, bag):
        self.tasks = bag

    # task as a task id
    def min(self, task):
        machines = self.tasks[task]
        min = machines[0]
        for m in machines:
            if m[cost] < min[cost]:
                min = m
        return min
      
    # task as a task id
    # machine as a tuple (cost, id) ex (10.0, 'M1 ')
    def update(self, taskID, machine):
        self.tasks.pop(taskID)
        for tId in self.tasks:
            for m in self.tasks[tId]:
                if m[machine_id] == machine[machine_id]:
                    m[cost] += machine[cost]
        return None

def min_min(bag,output):
    out = open(Path(output), "w+")
    
    while(len(bag.tasks) != 0):
        task = list(bag.tasks.keys())[0]
        min = bag.min(task)
        for t in bag.tasks:
            if(min != None and bag.min(t) != None):
                if(min[cost] > bag.min(t)[cost]):
                    task = t
                    min = bag.min(t)
            elif(min == None and bag.min(t) != None):
                task = t
                min = bag.min(t)

        out.write(f"Assign {task} -> {min[machine_id]}\n")
        bag.update(task,min)

    out.close()


def min_max(bag,output):
    out = open(Path(output), "w+")
    
    while(len(bag.tasks) != 0):
        task = list(bag.tasks.keys())[0]
        max = bag.min(task)
        for t in bag.tasks:
            if(max != None and bag.min(t) != None):
                if(max[cost] < bag.min(t)[cost]):
                    task = t
                    max = bag.min(t)
            elif(max == None and bag.min(t) != None):
                task = t
                max = bag.min(t)

        out.write(f"Assign {task} -> {max[machine_id]}\n")
        bag.update(task,max)

    out.close()

def sufferage(bag,output):
    pass