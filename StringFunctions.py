#learning about string functions
convince = '''I am responsible.
I will take care of it and take it for walks and feed it and find a proper petcare when we are on trips.
I will also have a lot of money and I will do chores around the house.'''
#len function is used to find the length of a string or the number of characters in a string
print (len (convince))
#       012345   These are the indexes for each letter in the string. The index always starts at 0.
#                It always ends at the length of the string minus 1.
name = "Lahari 123"

#index of the character in a string
i = name.index('L')
print (i)
j = name.index('2')
print (j)

#find a character in the string using index value
k = name[5]
print (k)
l = name[9]
print (l)

#in function allows you to check for a particular character or sequence of characters in a string
friendName = "Sydney Bachellor1x3"
m = 'z' in friendName
print (m)
n = 'Bach' in friendName
print (n)
print ("Hi there!", friendName)              
#trying to print a substring in a string. The ending index value is always 1+ the index of the ending character.
#the substring of a string is also called slicing.
o = friendName[:6]
print (o)
p = friendName[7:16]
print (p)
q = friendName[7:]
print (q)
s = "add"
print (s=="add")

