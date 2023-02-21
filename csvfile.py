import re
import csv


class FileOfCsv:
    """This class is add to dict in csv file create and add data to csv file."""

    def csv_file_write(self, **dict1: dict) -> str:
        """This is add to dict in csv file create and add data to csv file."""
        filename = input("enter file name with extention: ")
        check_regex = re.compile(r"[a-zA-Z0-9]+[.]csv$")
        if re.fullmatch(check_regex, filename):
            dict_key = [x for x in dict1.keys()]
            dict_value = [i for i in dict1.values()]
            with open(filename, "w") as csvdata:
                csvwrite = csv.writer(csvdata)
                csvwrite.writerow(dict_key)
                csvwrite.writerow(dict_value)
                csvdata.close()
                return str

        else:
            return "please Enter csv file only"


obj = FileOfCsv()
dict1 = {"Name": "milan", "number": 741258, "email": "milan@gmail.com", "age": 20}

print(obj.csv_file_write(**dict1))
