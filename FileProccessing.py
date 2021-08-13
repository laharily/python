# The open function takes in two parameters: the name of the file, and the mode
# of opening. "r" means open in read mode and "w" means open in write mode
file1 = open("hobbies.txt", "r")
# The contents of a file can be read into a string using the read function
s = file1.read()
# The read function reads the end of line character too. To remove this, we use
# the strings replace function.
s = s.strip("\n")
print (s)
# All open files must be closed
file1.close()
