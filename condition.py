num1 =56
num2 =89

# if condition
print("num2 is big") if num1<num2 else print("num1 is big")

# nested if else
if num2 > num1:
  print("num2 is greater than num1")
elif num1 == num2:
  print("num1 and num2 are equal")
else:
  print("num1 is greater than num2")
    

# use oparetar and, or, not
if num2 > num1 and num1 == num2:
  print("num2 is greater than are equal")
else:
  print("num1 is greater than num2")


#   loops concept

i = 0
while i < 6:
  
  if i == 3:
    break
  if i == 1:
    continue
  print(i)
  i += 1