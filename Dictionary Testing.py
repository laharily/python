# A dictionary is like a list that has key: value pairs.
d = {'fruit': 'strawberry', 'vegetable': 'carrot'}
mix = {'name':'Lahari','age':11,'hobby':'reading','grade':6,'weight':90.5,'height':'5.2','last vacation':'Hawaii'}
# Updating a dictionary.
mix['hobby'] = 'playing'
print (mix)
# Dictionary methods or functions.
# Accessing all the keys.
print (d.keys())
# Accessing all the values.
print (d.values())
print (d.items())
# Deleting a key.
del mix ['weight']
print (mix)

mydict = {"cat":12, "dog":6, "elephant":23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])

