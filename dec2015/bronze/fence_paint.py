with open("paint.in", "r") as input_file:
    line1=input_file.readline()
    a,b=tuple(line1.split(" "))
    a,b=(int(a),int(b))
    line2=input_file.readline()
    c,d=tuple(line2.split(" "))
    c,d=(int(c),int(d))

if c<a:
    a,b,c,d=(c,d,a,b)
dist1=b-a
dist2=d-c
overlap=min(0,int(c)-int(b))
overlap*=-1

with open("paint.out", "w") as output_file:
    output_file.write(str(dist1+dist2-overlap))
    output_file.write("\n")
