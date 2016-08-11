import pprint

def adjacent_rooms(room,n):
    x,y=room
    list_adjacent=set()
    if x>1:
        list_adjacent.add((x-1,y))
    if x<n:
        list_adjacent.add((x+1,y))
    if y>1:
        list_adjacent.add((x,y-1))
    if y<n:
        list_adjacent.add((x,y+1))
    return list_adjacent

with open("lightson.in","r") as file_in:
    n,m=file_in.readline().split(" ")
    n,m=(int(n),int(m))
    dict_rooms=dict()
    for next_line in range(m):
        x1,y1,sx,sy=file_in.readline().split(" ")
        x1,y1,sx,sy=(int(x1),int(y1),int(sx),int(sy))
        dict_rooms.setdefault((x1,y1),list())
        dict_rooms[(x1,y1)].append((sx,sy))
    for i in range(1,n+1):
        for j in range(1,n+1):
            dict_rooms.setdefault((i,j),list())

pprint.pprint(dict_rooms)

rooms_lit=set()
visited_rooms=set()
current_room=(1,1)
rooms_lit.add(current_room)
lit_unvisited=True
while lit_unvisited:
    for switch in dict_rooms[current_room]:
        rooms_lit.add(switch)
        lit_unvisited_adjacent=rooms_lit & adjacent_rooms(current_room,n)
        lit_unvisited_adjacent -= visited_rooms
        lit_unvisited_set=rooms_lit-visited_rooms
        lit_unvisited=(len(lit_unvisited_adjacent)>0)
        visited_rooms.add(current_room)
        if lit_unvisited:
            current_room=list(lit_unvisited_adjacent)[0]

pprint.pprint(rooms_lit)
with open("lightson.out","w") as file_handle:
    file_handle.write(str(len(rooms_lit))+"\n")
