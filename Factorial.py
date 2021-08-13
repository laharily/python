n = int(input("Enter an integer: "))
factorial = 1
for x in range(1, n+1):
    factorial *= x

print("The factorial of", n, "is:", factorial)
