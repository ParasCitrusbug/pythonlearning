# set create 
# not allow dublicate
set_create = {"apple","banana",True, 25,12.21}

# set len and type
print(len(set_create))
print(type(set_create))

#access item
for x in set_create:
  print(x)

print("banana" in set_create)

# set method to chande
set_fruite = {"kiwi","papaya"}
set_create.add("mango")
set_create.update(set_fruite)


# set remove
set_create.remove("banana")
print(set_create)
set_create.discard(25)
print(set_create)
set_create.pop()
print(set_create)

# set method for set math
set_create.union(set_fruite)
set_create.intersection_update(set_fruite)
print(set_create)
intersection_set =  set_create.intersection(set_fruite)
print(intersection_set)

set_create.symmetric_difference_update(set_fruite)
print(set_create)

