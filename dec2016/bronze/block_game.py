from collections import Counter
import string
import itertools
import array

wordlist=list()
list_counters=list()
with open("blocks.in","r") as input_file:
    line_count=int(input_file.readline())
    for _ in range(line_count):
        appendlist=input_file.readline().split(" ")
        wordlist.append(appendlist)
        # base=len(appendlist)

# def base_split(num,div_base):
#     out_list=list()
#     remain=num
#     while remain>=div_base:
#         remain,append_num=divmod(remain,div_base)
#         out_list.append(append_num)
#     out_list.append(remain)
#     return out_list

def merge_counter_old(c1,c2):
    subcounter=c1-c2
    for key in subcounter:
        if subcounter[key]<0:
            subcounter[key]=0
    return c2+subcounter

def merge_counter(c1,c2):
    c1.subtract(c2)
    # c1.elements ignores elements <=0
    c1=(+c1)
    # for key in c1:
    #     if c1[key]<0:
    #         c1[key]=0
    return c2+c1

#for permute in range(base**line_count):
for permute in itertools.product([0,1],repeat=line_count):
    # list_visible=list()
    #list_indicies=base_split(permute,base)
    # list_indicies=bin(permute)
    # list_indicies=list_indicies.replace("0b","")
    # list_indicies=[int(char) for char in list_indicies]
    # list_indicies=array.array("B",list_indicies)
    # list_indicies.reverse()
    # while len(list_indicies)<line_count:
    #     list_indicies.append(0)
    count=Counter()
    for i in range(line_count):
        word=wordlist[i][permute[i]]
        count.update(word)
    list_counters.append(count)

final_counter=list_counters.pop()
for remain_counter in list_counters:
    #final_counter=merge_counter(final_counter,remain_counter)
    # Inline of merge_counter function
    final_counter.subtract(remain_counter)
    for key in final_counter:
        if final_counter[key]<0:
            final_counter[key]=0
    final_counter+=remain_counter

with open("blocks.out","w") as output_file:
    for keyval in string.ascii_lowercase:
        val=final_counter[keyval]
        output_file.write(str(val)+"\n")
