def odd1 (b):
    oddnum = ( )
    for a in range (0, b):
        if a % 2 != 0:
            odd = (a, )
            oddnum = oddnum + odd
    print (oddnum)
def div (y):
    evennum = ( )
    for x in range (1, y):
        if x % 2 == 0:
            even = (x, )
            evennum = evennum + even
    print (evennum)

def mul (n):
    squarenum = ( )
    for m in range (1, n):
        square2 = (m*m, )
        squarenum = squarenum + square2
    print (squarenum)

n = 21
mul (n)

y = 21
div (y)

b = 22
odd1 (b)

