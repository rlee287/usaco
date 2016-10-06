from collections import Counter

set_possible=set()
set_impossible=set()

with open("badmilk.in", "r") as input_file:
    line_sizes=input_file.readline()
    n,m,d,s=tuple(line_sizes.split(" "))
    n,m,d,s=tuple([int(temp_var) for temp_var in [n,m,d,s]])

    milk_count=Counter(list(range(1,m+1)))
    person_drank=dict()
    person_sick=dict()
    #print("line_drink")
    for record in range(d):
        line_drink=input_file.readline()
        #print(line_drink)
        p,milk,t=tuple(line_drink.split(" "))
        p,milk,t=tuple([int(temp_var) for temp_var in [p,milk,t]])
        milk_count[p]+=1
        person_drank[p]=person_drank.get(p,list())+[(milk,t)]

    #print("line_sick")
    for sick_record in range(s):
        line_sick=input_file.readline()
        #print(line_sick)
        p,t=tuple(line_sick.split(" "))
        p,t=tuple(int(temp_var) for temp_var in [p,t])
        person_sick[p]=t

for person,milk_record in person_drank.items():
    nodrink_accumulate=set(range(1,m+1))
    if person in person_sick.keys():
        time_sick=person_sick[person]
    else:
        time_sick=-1
    for milk,time in milk_record:
        if time<=time_sick:
            set_possible|={milk}
        else:
            set_impossible|={milk}
        nodrink_accumulate.remove(milk)
    if time_sick==-1:
        set_possible|=nodrink_accumulate
    else:
        set_impossible|=nodrink_accumulate
print(set_possible)
print(set_impossible)
set_possible-=set_impossible
print(milk_count)
medicine=max([milk_count[p] for p in set_possible])
print(medicine)
with open("badmilk.out","w") as output_file:
    output_file.write(str(medicine)+"\n")
