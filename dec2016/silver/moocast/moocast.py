import math
import functools

talkie_power=dict()
reachables=dict()

def hypot(tup1,tup2):
    x1,y1=tup1
    x2,y2=tup2
    squared=((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))
    return math.sqrt(squared)

# Read data into talkie_power
with open("moocast.in","r") as input_file:
    numline=int(input_file.readline())
    for _ in range(numline):
        x,y,p=input_file.readline().split(" ")
        x,y,p=(int(q) for q in (x,y,p))
        talkie_power[(x,y)]=p

# Construct reachables dict

for cow in talkie_power:
    reachables[cow]=list()
    for neighbor_cow in talkie_power:
        if neighbor_cow==cow:
            continue
        if (hypot(cow,neighbor_cow)-0.001)>talkie_power[cow]:
            continue
        reachables[cow].append(neighbor_cow)

traversed=dict()

@functools.lru_cache(maxsize=None)
def can_reach(cow,has_reached=frozenset()):
    reached=has_reached.copy()
    reached=reached|{cow}
    for reachable in reachables[cow]:
        if reachable not in reached:
            reached=reached|can_reach(reachable,reached)
    return reached


def can_reach_num(cow):
    return len(can_reach(cow))

max_reachable=0
for cow in reachables:
    max_reachable=max(max_reachable,can_reach_num(cow))

with open("moocast.out","w") as output_file:
    output_file.write(str(max_reachable)+"\n")
