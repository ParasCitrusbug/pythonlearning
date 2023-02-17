import random
x = []
def team(number):  
    total_match = 0
    for i in range(1,number+1):
        for j in range(i+1, number+1):
            total_match += 1
            x.append([i,j])
    print(total_match)
team(14)

for k in x:
    print(k, end=" ")

dict_team = {"winner":[], "loss":[]}
def check_singale_elination(number):
    pass

    