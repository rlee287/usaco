min_cow_x=float("inf")
min_cow_y=float("inf")
max_cow_x=0
max_cow_y=0
cow_list=list()
cow_list_x=list()
cow_list_y=list()
with open("balancing.in","r") as input_file:
    n,b=tuple(input_file.readline().split(" "))
    n,b=(int(n),int(b))
    max_cow_x=b
    max_cow_y=b
    for lineno in range(n):
        x,y=tuple(input_file.readline().split(" "))
        x,y=(int(x),int(y))
        min_cow_x=min(min_cow_x,x)
        min_cow_y=min(min_cow_y,y)
        max_cow_x=max(max_cow_x,x)
        max_cow_y=max(max_cow_y,y)
        cow_list.append((x,y))
        cow_list_x.append(x)
        cow_list_y.append(y)

cow_list_x.sort()
cow_list_y.sort()
cow_list_x=[q+1 for q in cow_list_x]
del cow_list_x[-1]
cow_list_y=[q+1 for q in cow_list_y]
del cow_list_y[-1]

min_cow_partition=float("inf")
for a in cow_list_x:
    for b in cow_list_y:
        i,ii,iii,iv=(0,0,0,0)
        for cow in cow_list:
            x,y=cow
            if x<a:
                if y<b:
                    iii+=1
                else:
                    ii+=1
            else:
                if y<b:
                    iv+=1
                else:
                    i+=1
        max_partition=max([i,ii,iii,iv])
        min_cow_partition=min(max_partition,min_cow_partition)
with open("balancing.out","w") as output_file:
    output_file.write(str(min_cow_partition)+"\n")
