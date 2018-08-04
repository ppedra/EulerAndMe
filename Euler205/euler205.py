def add_to_dict(dictionary,element):
    if element in dictionary:
        dictionary[element]+=1
    else:
        dictionary[element]=1


"""
the possible sums of the dices and the amount of times they show up are:
"""
#cd as in Colins Dices
cd_sum_dict={}
cd=[0]*6
for cd[0] in range(1,7):
    for cd[1] in range(1,7):
        for cd[2] in range(1,7):
            for cd[3] in range(1,7):
                for cd[4] in range(1,7):
                    for cd[5] in range(1,7):
                        #6**6 times. 46656 times.
                        loop_sum = sum(cd)
                        add_to_dict(cd_sum_dict,loop_sum)

#pd as in Peter Dices
pd=[0]*9
pd_sum_dict={}
for pd[0] in range(1,5):
    for pd[1] in range(1,5):
        for pd[2] in range(1,5):
            for pd[3] in range(1,5):
                for pd[4] in range(1,5):
                    for pd[5] in range(1,5):
                        for pd[6] in range(1,5):
                            for pd[7] in range(1,5):
                                for pd[8] in range(1,5):
                                    #4**9 times. 262144 times
                                    loop_sum = sum(pd)
                                    add_to_dict(pd_sum_dict,loop_sum)


"""
print("Colins - 6*6sides")
print(cd_sum_dict)
print("Peter - 9*4sides")
print(pd_sum_dict)
"""

peter_won = 0
for pd_keys in pd_sum_dict:
    for cd_keys in cd_sum_dict:
        #we are cheking the values of the sum
        if pd_keys>cd_keys:
            #is bigger, ok, but who many games can produce this key/sum?
            #and how many games this key/sum can beat?
            peter_won += (pd_sum_dict[pd_keys]*cd_sum_dict[cd_keys])

#9 dices of 4 sides plus 6 of 6 sides
total_combinations = (4**9) * (6**6)  

print("peter_won ",peter_won)
print("total_combinations ",total_combinations)
print("peter_won/total_combinations ",peter_won/total_combinations)
print("              rounded answer ",round(peter_won/total_combinations,7))
