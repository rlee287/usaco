import heapq
import random

class PriorityQueue:
    def __init__(self):
        self.priorities=list()
        self.tasks=dict()

    def addtask(self,task,priority):
        self.tasks[priority]=self.tasks.get(priority,list())+[task]
        heapq.heappush(self.priorities,priority)

    def getpriority(self):
        big_priority=heapq.heappop(self.priorities)
        tasklist=self.tasks.pop(big_priority)
        return random.choice(tasklist)

if __name__=="__main__":
    test=PriorityQueue()
    #a,d,b,c
    for priority,task in zip([0,4,6,3],["a","b","c","d"]):
        test.addtask(task,priority)
    for _ in range(4):
        print(test.getpriority())
