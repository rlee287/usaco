from collections import Counter
import string

def merge_counter_old(c1,c2):
    subcounter=c1-c2
    for key in subcounter:
        if subcounter[key]<0:
            subcounter[key]=0
    return c2+subcounter

wordlist=list()
list_counters=list()
with open("blocks.in","r") as input_file:
    line_count=int(input_file.readline())
    for _ in range(line_count):
        appendtuple=input_file.readline().split(" ")
        wordlist.append(appendtuple)

for word1, word2 in wordlist:
    count1=Counter(word1)
    count2=Counter(word2)
    count=merge_counter_old(count1,count2)
    list_counters.append(count)

final_counter=list_counters.pop()
for remain_counter in list_counters:
    #final_counter=merge_counter(final_counter,remain_counter)
    # Inline of merge_counter function
    # final_counter.subtract(remain_counter)
    # for key in final_counter:
    #     if final_counter[key]<0:
    #         final_counter[key]=0
    final_counter+=remain_counter

with open("blocks.out","w") as output_file:
    for keyval in string.ascii_lowercase:
        val=final_counter[keyval]
        output_file.write(str(val)+"\n")
