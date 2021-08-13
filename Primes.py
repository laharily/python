def is_multiple(x,y):
    '''is_multiple(x,y) -> bool
    returns True is x is a multiple of y, False otherwise'''
    # print("Checking if " + str(x) + " is a multiple of " + str(y))  # TEST PRINT
    # check if y divides evenly into x
    return (x % y == 0)

def is_prime(n):
    '''is_prime(n) -> bool
    returns True if n is prime, False if n is not prime'''
    isPrime = True  # initialize the isPrime variable
    if n == 1:
        return False
    # check every divisor from 2 up to sqrt(n)
    for div in range(2, int(n**0.5) + 1):
        # print("div = " + str(div))  # TEST PRINT
        if is_multiple(n,div):
            isPrime = False  # n isn't prime!
    return isPrime

count = 0
sumnum = 0
num = 1
while count < 100:
    if is_prime(num):
        sumnum += num
        count += 1
    num += 1

print(sumnum)
