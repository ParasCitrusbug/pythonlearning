import random
x = []
def team(number):  
    total_match = 0
    for i in range(1,number+1):
        for j in range(i+1, number+1):
            total_match += 1
            x.append([i,j])
    
team(14)



dict_team = {"winner":[], "loss":[]}
create_team = []
def check_singale_elination(number):
    teamlist= []
    for i,j in random.choice(number,2):
        te

check_singale_elination(10)

print(create_team)
