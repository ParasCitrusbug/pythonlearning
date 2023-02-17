import re
import csv
class file_of_csv:

    def csv_file_write(self,**dict1):
        lendict= len(dict1)
        filename = input("enter file name with extention: ")
        check_regex = re.compile(r"[a-zA-Z0-9]+[.]csv$")
        if re.fullmatch(check_regex, filename):
            dict_key = [x for x in dict1.keys()]
            dict_value = [i for i in dict1.values()]
            print(dict_value)        
            with open(filename, "w") as csvdata:
                csvwrite = csv.writer(csvdata)
                csvwrite.writerow(dict_key)
                csvwrite.writerow(dict_value)
                
	        
        else:
	        print("please Enter csv file only")
       
obj = file_of_csv()
dict1 = {"Name" :"milan",
        "number" :741258,
        "email" :"milan@gmail.com",
        "age" :20
                     }
obj.csv_file_write(**dict1)
