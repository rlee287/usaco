with open("pails.in","r") as input_file:
    x,y,m=tuple(input_file.readline().split(" "))
    x,y,m=(int(x),int(y),int(m))

max_milk=0

for num_y in range(m//y+1):
    remain_space=m-num_y*y
    num_x=remain_space//x
    max_milk=max(max_milk,x*num_x+y*num_y)

with open("pails.out","w") as output_file:
    output_file.write(str(max_milk)+"\n")
