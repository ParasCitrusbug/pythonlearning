import csv
list1 =["paras","miln","12","25"]
with open("csvone.csv", "w") as csvdata:
                csvwrite = csv.writer(csvdata)
                
                csvwrite.writerows(list1)