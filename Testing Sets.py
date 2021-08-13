#  A set is a list of values. You can store different values or data types just
#  like a tuple, but you can change the values. A tuple doesn't allow you to
#  change the values. A set is always sorted.
#  A set removes duplicates.

mix = {"Lahari", 11, "Reading", 6, "A", 90.5, 5.2, "Lahari"}
print (mix)

set1 = {1, 2, 3, 35, 24, 3125, 98519, 0}
set2 = {1, 3, 2435, 78, 89, 9, 98159, 32}

# A union means combining more than one set together.
set3 = set1|set2
print (set3)

# An intersection means that you get a set with common values.
set4 = set1&set2
print (set4)

# A difference means the resulting set has unique values from the first set.
set5 = set1-set2
set6 = set2-set1
print (set5)
print (set6)

# A symmetric difference means elements that are in the first and the second but
# but not in both.
set7 = set1^set2
print (set7)

# Swimming is a set of students that are taking swimming lesosns. Tennis is a
# set of students who are taking tennis lessons.
swimming = {"Lahari", "Sydney", "Aashita"}
tennis = {"Rhea", "Nithya", "Vedavi", "Lahari"}
# List of students taking swimming and tennis lessons.
print (swimming&tennis)
