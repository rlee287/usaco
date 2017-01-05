import math
import pprint
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
    if len(reachables[cow])==0:
        reachables[cow]=0

traversed=dict()

@functools.lru_cache(maxsize=None)
def can_reach_num(cow,has_reached=frozenset()):
    reached=has_reached.copy()
    can_reach=1
    if reachables[cow]==0 or (cow in reached):
        return can_reach
    else:
        for reachable in reachables[cow]:
            if cow not in reached:
                can_reach+=can_reach_num(reachable,reached)
        reached=reached|{cow}
    return can_reach

max_reachable=0
for cow in reachables:
    max_reachable=max(max_reachable,can_reach_num(cow))

print(can_reach_num.cache_info())

with open("moocast.out","w") as output_file:
    output_file.write(str(max_reachable)+"\n")
