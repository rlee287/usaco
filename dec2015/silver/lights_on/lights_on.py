import pprint

def adjacent_rooms(room,n):
    x,y=room
    list_adjacent=list()
    if x>1:
        list_adjacent.append((x-1,y))
    if x<n:
        list_adjacent.append((x+1,y))
    if y>1:
        list_adjacent.append((x,y-1))
    if y<n:
        list_adjacent.append((x,y+1))

with open("lightson.in","r") as file_in:
    n,m=file_in.readline().split(" ")
    n,m=(int(n),int(m))
    dict_rooms=dict()
    for next_line in range(m):
        x1,y1,sx,sy=file_in.readline().split(" ")
        x1,y1,sx,sy=(int(x1),int(y1),int(sx),int(sy))
        dict_rooms.setdefault((x1,y1),list())
        dict_rooms[(x1,y1)].append((sx,sy))

pprint.pprint(dict_rooms)

rooms_lit=set()
visited_rooms=set()
current_room=(1,1)
rooms_lit.add(current_room)
visited_rooms.add(current_room)
first_time=True
lit_unvisited=True
while first_time:
    for switch in dict_rooms[current_room]:
        rooms_lit.add(switch)
