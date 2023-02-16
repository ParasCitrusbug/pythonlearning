# dict create
dict_crete = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(dict_crete)
# len of dict
print(len(dict_crete))

# type of dict
print(type(dict_crete))

# dict access and change
print(dict_crete["brand"])
print(dict_crete.get("modal"))
print(dict_crete.keys())
print(dict_crete.values())
print(dict_crete.items())
dict_crete["color"] = "red"
dict_crete["year"] = 2000
dict_crete.update({"year1": 2555})
print(dict_crete)

# dict in remove
dict_crete.pop("year1")
dict_crete.popitem()
del dict_crete["model"]  # clear fun
print(dict_crete)

# dict in Loop
for x in dict_crete.keys():
    print(x)
for y in dict_crete.values():
    print(y)
for a, b in dict_crete.items():
    print(a, b)
x = [print(a,b) for a,b in dict_crete.items()]
# dict in copy
copy_dict = dict_crete.copy()
new_dict = dict(dict_crete)
print(copy_dict, new_dict)

# nested list
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}
print(myfamily["child1"])

child1={"name": "Emil", "year": 2004}
child2={"name": "Tobias", "year": 2007}
child3={"name": "Linus", "year": 2011}
new_family = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
}
print(new_family)
print(new_family["child1"]["name"])