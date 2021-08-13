# The open function takes in two parameters: the name of the file, and the mode
# of opening. "r" means open in read mode and "w" means open in write mode
file1 = open("hobbies.txt", "r")
# The contents of a file can be read into a list line by line.  
for line in file1:
    list1 = line.split()
    print (list1)
# All open files must be closed
file1.close()
