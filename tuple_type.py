# tuple is unchangebla
tuple_create = tuple(("banana", "kiwi", 25, 32.52, "apple"))
tuple_number = (1, 2, 3, 4)
print(tuple_create)

# len of tuple
print(len(tuple_create))

# type of tuple
print(type(tuple_create))

# tuple in slicing
print(tuple_create[2:-1])

# tuple in change useing list
list_create = list(tuple_create)
list_create.append("mango")
list_create[1] = "papaya"
list_create.remove(25)
tuple_create = tuple(list_create)
print(tuple_create)


# tuple in unpack
one, two, *three = tuple_create
print(one, two, three)

# loop in tuple
for i in tuple_create:
    print(i)

list_in_line = [print(j) for j in tuple_create]
i = 0
while i < len(tuple_create):
    print(tuple_create[i])
    i = i + 1

# tuple in join
new_tuple = ("paras", "milan", 14, 21.2)
added_tuple = new_tuple + tuple_create
print(added_tuple)
print(added_tuple * 2)

# tuple method
print(added_tuple.index("banana"))
print(added_tuple.count("milan"))
