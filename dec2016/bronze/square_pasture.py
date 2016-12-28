with open("square.in","r") as input_file:
    x1a,y1a,x2a,y2a=tuple(input_file.readline().split(" "))
    x1a,y1a,x2a,y2a=(int(q) for q in [x1a,y1a,x2a,y2a])
    x1b,y1b,x2b,y2b=tuple(input_file.readline().split(" "))
    x1b,y1b,x2b,y2b=(int(q) for q in [x1b,y1b,x2b,y2b])

xmax=max([x1a,x2a,x1b,x2b])
xmin=min([x1a,x2a,x1b,x2b])
ymax=max([y1a,y2a,y1b,y2b])
ymin=min([y1a,y2a,y1b,y2b])
square=max([xmax-xmin,ymax-ymin])
square=square*square

with open("square.out","w") as output_file:
    output_file.write(str(square)+"\n")
