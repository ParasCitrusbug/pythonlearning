
class  Matchs:
    
    def team(self,number):
        total_match = 0
        x = []
        for i in range(1,number+1):
            for j in range(i+1, number+1):
                total_match += 1
                x.append([i,j])
        return total_match
  


obj = Matchs()
print(obj.team(10))
