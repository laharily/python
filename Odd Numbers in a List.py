number = [9, -6, 36.9876087, 13, 103, 122, 1000, 55, 23, 32.5]
odd = 0
even = 0
negative = 0
for n in number:
    if n %2 != 0:
        odd = odd + 1
    else:
        even = even + 1
    if n < 0:
        negative = negative + 1
print ("The number of odd numbers in the list is: ", odd)
print ("The number of even numbers in the list is: ", even)
print ("The number of negative numbers in the list is: ", negative)
