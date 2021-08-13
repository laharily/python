file = open("wordlist.py" , "r")
count = 0
for line in file:
    if len(line) == 10:
        count += 1

print(count)
        
