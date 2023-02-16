import platform
import datetime
x = dir(platform)
# print(x)

Date = datetime.datetime.now()
print(Date)
print(Date.year)

print(Date.strftime("%A"))

new_date = datetime.datetime(2022,12,2)
print(new_date)