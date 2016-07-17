import pdb
import pprint

with open("badmilk.in", "r") as input_file:
    line_sizes=input_file.readline()
    n,m,d,s=tuple(line_sizes.split(" "))
    n,m,d,s=tuple([int(temp_var) for temp_var in [n,m,d,s]])
    person_drank=dict()
    person_sick=dict()
    for record in range(d):
        line_drink=input_file.readline()
        p,milk,t=tuple(line_drink.split(" "))
        p,milk,t=tuple([int(temp_var) for temp_var in [p,milk,t]])
        add_to_dict=person_drank.get(p,list())
        add_to_dict.append((milk,t))
        person_drank[p]=add_to_dict
    assert list(person_drank.keys())==list(range(1,n+1))
    for j in range(n):
        line_sick=input_file.readline()
        if line_sick=="" or line_sick=="\n":
            break
        p,t=tuple(line_sick.split(" "))
        p=int(p)
        t=int(t)
        person_sick[p]=t
    milk_sick=dict()
    for sick_person,time_sick in person_sick.items():
        milks_drank=person_drank[sick_person]
        for milk_id, time_drank in milks_drank:
            if time_drank<time_sick:
                milk_sick[milk_id]=milk_sick.get(milk_id,0)+1
    pprint.pprint(person_drank)
    pprint.pprint(person_sick)
    pprint.pprint(milk_sick)
