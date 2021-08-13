n = int(input("Enter a number greater or equal to 3: "))
currentv = 2
prevV1 = 1
prevV2 = 1

for i in range(3, n+1):
    currentv = prevV1 + prevV2
    prevV2 = prevV1
    prevV1 = currentv
    

print("The Fibonacci number corresponding to that number is: ", currentv)
