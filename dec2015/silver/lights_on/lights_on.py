with open("lightson.in","r") as file_in:
    n,m=file_in.readline().split(" ")
    n,m=(int(n),int(m))
    dict_rooms=dict()
    for next_line in range(m):
        x1,y1,sx,sy=file_in.readline().split(" ")
        x1,y1,sx,sy=(int(x1),int(y1),int(sx),int(sy))
        dict_rooms.setdefault((x1,y1),list())
        dict_rooms[(x1,y1)].append((sx,sy))

import pprint
pprint.pprint(dict_rooms)
