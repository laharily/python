file1 = open("hobbies.txt", "r")
# The contents of a file can be read into a list using the read line function.
list1 = []
for line in file1:
    list1 = line.strip("\n").split()
    print (list1)
