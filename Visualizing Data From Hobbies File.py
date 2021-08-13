file1 = open("hobbies.txt", "r")
hobbies = { }
for h in file1:
    list1 = h.split()
    key = list1[2]
    if key in hobbies:
        hobbies[key] = hobbies[key] + 1
    else:
        hobbies[key] = 1
print (hobbies)
