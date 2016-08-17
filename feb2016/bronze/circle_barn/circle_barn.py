import pdb

def permute_list(list_in):
    list_out=list_in.copy()
    list_out.append(list_out.pop(0))
    return list_out

in_list=list()
with open("cbarn.in","r") as input_file:
    num_lines=int(input_file.readline())
    for i in range(num_lines):
        in_list.append(int(input_file.readline()))

try_list=in_list.copy()
#pdb.set_trace()
first_time=True
min_ans=float("inf")
while first_time or try_list!=in_list:
    max_dist=0
    dist_coeff=0
    #try_list.reverse()
    for num_occupants in try_list:
        max_dist+=dist_coeff*num_occupants
        dist_coeff+=1
    #try_list.reverse()
    min_ans=min(min_ans,max_dist)
    try_list=permute_list(try_list)
    first_time=False
print(min_ans)
with open("cbarn.out","w") as output_file:
    output_file.write(str(min_ans)+"\n")
