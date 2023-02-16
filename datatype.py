import random

# spicific data type
string = str("jkhksksk")
number = int(5)
dimalnumber = float(20.21)
complexnumber = complex(2 + 2j)
listof = list(("paras", "milan", "amit", 3, 544.544))
setof = set(("paras", "milan", "amit", 3, 544.544))
tupleof = dict(name="paras", number=3, float=544.544)
dictof = tuple(("paras", "milan", "amit", 3, 544.544))

# random number
print(random.randrange(1, 5))

# string
string_var = "lorem ok lakis lioks kaju bafom malmikh"
string_var1 = """    lorem ok lakis lioks kaju 
                    bafom malmikh"""
# length string
print(len(string_var))
# string index
print(string_var[2])
# string for and if
if "ok" in string_var:
    print("yes there")
for string_element in string_var:
    print(string_element)

# string sliciing
print(string_var[2:6])
print(string_var[:6])
print(string_var[8:])
print(string_var[-5:-1])
print(string_var[2:-1])
# reverse string
print(string_var[::-1])

# concatenate string
new_string = string_var + string_var1

# string methods
print(string_var.upper())
print(string_var.lower())
print(string_var.strip())  # remove white space in start and end
print(string_var.replace("ok", "hello"))
print(string_var.split(","))

# string format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# string in useescape for\',\\,\n,\b,\r,\t
new_my_order = str.maketrans("pay", "Pay")
print(myorder.translate(new_my_order))


# bool type
if 5:
    print("true")
print(bool("paras"))
print(bool(""))

# oprater +,-,*,/,

a = 12
b = 25
c = 45

print(a + b)
print(a - b)
print(a * b)
print(a / b)
b += a
print(b)
c /= a
print(c)
