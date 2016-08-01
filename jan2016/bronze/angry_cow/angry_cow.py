def explode_bales(bale_set,bale_start):
    if bale_start not in bale_set:
        return 0
    new_bales={bale_start}
    bales_left=bale_set.copy()
    total_bales=set()
    radius=1
    #print("Starting with bale",bale_start)
    while new_bales:
        #print("  Radius is",radius)
        possible_bales=set()
        for bale_exploded in new_bales:
            possible_bales|={bale_exploded+n for n in
                             range(-radius,radius+1)
                             if (n>=0 and n<=1000000000)}
        new_bales=set()
        new_bales=possible_bales & bales_left
        #print("    Exploding",new_bales)
        total_bales |= new_bales
        bales_left -= new_bales
        #print("    Bales left",bales_left)
        radius+=1
        if radius > 30:
            break
    #print("Total Bales exploded",total_bales)
    return len(total_bales)

list_bales=set()
with open("angry.in","r") as input_file:
    num_columns=int(input_file.readline())
    for i in range(num_columns):
        bale_num=int(input_file.readline())
        list_bales.add(bale_num)

max_bales=0
for bale in list_bales:
    max_bales=max(max_bales,explode_bales(list_bales,bale))

with open("angry.out","w") as output_file:
    output_file.write(str(max_bales)+"\n")
