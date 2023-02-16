# list create
fruite = ["banana", "apple", "kiwi"]
fruite1 = ["pineapple", "papaya"]
number_list = [1, 2, 3, 4, 5]
bool_list = [True, False, False]
all_con_list = ["banana", 25, True, "paras"]

# list lenght
print(len(fruite))
print(type(fruite))

# list access
print(fruite[:2])
print(fruite[:-1])
print(fruite[1])

# list in change
fruite[1] = "orange"
fruite.insert(1, "cherry")
fruite.append("mango")
fruite.extend(fruite1)


# list remove method
fruite.remove("kiwi")
fruite.pop()  # given to the index
del fruite[0]
fruite1.clear()

# loop in list
for i in fruite:
    print(i)

list_in_line = [print(j) for j in fruite]
i = 0
while i < len(fruite):
    print(fruite[i])
    i = i + 1

# list comprehension
fruites = [k for k in fruite if "a" in k]
print(fruites)


# list in sort function
fruites.sort()
print(fruites)
fruites.sort(reverse=True)
fruites.sort(key=str.lower)
fruites.reverse()

# copylist
new_fruite = fruites.copy()

# list join useing three append extend concatenate
