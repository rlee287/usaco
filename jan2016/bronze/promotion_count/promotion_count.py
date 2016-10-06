levels_before=list()
levels_after=list()
with open("promotion.in","r") as input_file:
    for lines in input_file:
        before,after=tuple(lines.split(" "))
        before,after=(int(before),int(after))
        levels_before.append(before)
        levels_after.append(after)
gold_plat=levels_after[3]-levels_before[3]
silv_gold=levels_after[2]-levels_before[2]+gold_plat
bronz_silv=levels_after[1]-levels_before[1]+silv_gold
#new_join=levels_after[0]-levels_before[0]+bronz_silv
ans=[str(line)+"\n" for line in (bronz_silv,silv_gold,gold_plat)]
with open("promotion.out","w") as output_file:
    output_file.writelines(ans)
