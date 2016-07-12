with open("speeding.in", "r") as input_file:
    sizestr=input_file.readline()
    n,m=tuple(sizestr.split(" "))
    n=int(n)
    m=int(m)
    speed_list=dict()
    dist_road=0
    for i in range(n):
        lengthspeed=input_file.readline()
        dist,limit=tuple(lengthspeed.split(" "))
        dist=int(dist)
        limit=int(limit)
        speed_list[dist_road]=limit
        dist_road+=dist
    dist_road=0
    cow_list=dict()
    for i in range(m):
        lengthcow=input_file.readline()
        dist,speed=tuple(lengthcow.split(" "))
        dist=int(dist)
        speed=int(speed)
        cow_list[dist_road]=speed
        dist_road+=dist

dists=list(speed_list.keys())+list(cow_list.keys())
dists=list(set(dists))
dists.sort()
prev_cow=0
prev_limit=0
max_exceed=0
for dist in dists:
    cow_speed=cow_list.get(dist,prev_cow)
    speed_limit=speed_list.get(dist,prev_limit)
    max_exceed=max(max_exceed,cow_speed-speed_limit)
    prev_cow=cow_speed
    prev_limit=speed_limit

with open("speeding.out", "w") as output_file:
    output_file.write(str(max_exceed))
    output_file.write("\n")
