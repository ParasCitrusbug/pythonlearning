import platform
import re
import datetime
x = dir(platform)
# print(x)

Date = datetime.datetime.now()
print(Date)
print(Date.year)

print(Date.strftime("%A"))

new_date = datetime.datetime(2022,12,2)
print(new_date)

txt = "The Rain in Spain "

find_method = re.findall("\s", txt)
search_method = re.search("\W", txt)
print(find_method)
print(search_method.endpos)
