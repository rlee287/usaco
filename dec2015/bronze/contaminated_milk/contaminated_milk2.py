with open("badmilk.in", "r") as input_file:
    line_sizes=input_file.readline()
    n,m,d,s=tuple(line_sizes.split(" "))
    n,m,d,s=tuple([int(temp_var) for temp_var in [n,m,d,s]])

    milk_count=dict(zip(list(range(1,m+1)),[0]*m))
    person_drank=dict()
    person_sick=dict()
    p_done=set()
    #print("line_drink")
    for record in range(d):
        line_drink=input_file.readline()
        #print(line_drink)
        p,milk,t=tuple(line_drink.split(" "))
        p,milk,t=tuple([int(temp_var) for temp_var in [p,milk,t]])
        if p not in p_done:
            milk_count[milk]+=1
            p_done|={p}
        person_drank[p]=person_drank.get(p,list())+[(milk,t)]
    ##print(milk_count)

    #print("line_sick")
    for sick_record in range(s):
        line_sick=input_file.readline()
        #print(line_sick)
        p,t=tuple(line_sick.split(" "))
        p,t=tuple(int(temp_var) for temp_var in [p,t])
        person_sick[p]=t

set_possible=set(range(1,m+1))
from pprint import pprint
print("Initial possible")
pprint(set_possible)
pprint(person_drank)
pprint(person_sick)
for person,milk_record in person_drank.items():
    drank_before_sick=set()
    if person in person_sick.keys():
        time_sick=person_sick[person]
    else:
        time_sick=-1 #sentinel value
    print("Person",person)
    for milk,time in milk_record:
        print(milk,time)
        if time<=time_sick:
            print('Drank {0} at time {1} before sick at {2}'.format(milk,time,time_sick))
            drank_before_sick|={milk}
        elif time_sick==-1:
            drank_before_sick|=set(range(1,m+1))
    set_possible&=drank_before_sick
    print("Narrow down to")
    pprint(set_possible)
pprint(set_possible)
medicine=max([milk_count[p] for p in set_possible]+[0])
print(medicine)
with open("badmilk.out","w") as output_file:
    output_file.write(str(medicine)+"\n")
