# I think it will print "hello %s" 20 times. Then, the user will type a number.
# If it is less than 9, than the code will break.

for x in range(0, 20):
    print('hello %s' % x)
    if x < 9:
        break
