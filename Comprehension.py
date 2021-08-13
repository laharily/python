# A powerful feature of the Python language is to generate a new collection by applying a function to every member of an original collection.
# [expression  for  variable  in collection]
# Where expression is some calculation or operation acting upon the variable name.
# For each member of the collection; the collection comprehension
# sets variable equal to that member, and
# calculates a new value using expression, 
# It then collects these new values into a collection which is the return value of the collection comprehension.

import math
li= [3, 6, 2, 7]
print (li)
new_li = [x*2  for x  in li]
print (new_li) 
# [6, 12, 4, 14]
# Square of original list
newli = [y*y for y in li]
print (newli)
squareroot = [math.sqrt(l) for l in li]
print (squareroot)
factorial = [math.factorial(i) for i in li]
print (factorial)
# Print the values in the list that are greater than three.
for g in li:
    if g>3:
        print (g)
greater = [x for x in li if x>3]
print (greater)

# [expression  for variable  in collection if filter_condition] 
# Filter determines whether expression is performed on each member of the collection 
# When processing each element of list, first check if it satisfies the filter condition. 
# If the filter condition returns False, that element is omitted from the collection before the list comprehension is evaluated.

li = [3, 6, 2, 7, 1, 9]
new_li = [elem * 2 for elem  in   li   if  elem > 4]
print (new_li)
newli = [elem * 2 if elem > 4 else elem*3 for elem  in   li]
print (newli)
