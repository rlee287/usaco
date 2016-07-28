time=0
coord=(0,0)
direct_map={"N": (0,1),
            "E": (1,0),
            "S": (0,-1),
            "W": (-1,0)}
pos=dict()
pos[coord]=[time]
inst_list=list()

def diff_list(in_list):
    out_list=list()
    for i in len(in_list)-1:
        out_list.append(in_list[i+1]-in_list[i])
    return out_list

with open("mowing.in","r") as file_handle:
    n=int(file_handle.readline())
    for i in range(n):
        inst_list.append(file_handle.readline())

max_x=float("inf")

for inst in inst_list:
    dirstr,dist=inst.split(" ")
    dist=int(dist)
    direct=direct_map[dirstr]
    for i in range(dist):
        time+=1
        x,y=coord
        dx,dy=direct
        coord=(x+dx,y+dy)
        exist_list=pos.setdefault(coord,[time])
        if exist_list!=[time]:
            max_x=min(time-exist_list[len(exist_list)-1],max_x)
            pos[coord].append(time)

if max_x==float("inf"):
    max_x=-1

with open("mowing.out","w") as file_handle:
    file_handle.write(str(max_x)+"\n")

