a = 2345
b = 12345678
c = 6
if a > b and a > c:
    print ("a is bigger.")
elif b > a and b > c:
   print ("b is bigger.")
elif c > a and c > b:
    print ("c is bigger.")
elif a == b and b > c:
    print ("a and b are bigger.")
elif b == c and c > a:
    print ("b and c are bigger.")
elif a == c and c > b:
    print ("a and c are bigger.")
else:
    print ("All of them are equal.")


