def isThisTheNumber(n):
    n = str(n)
    digit3 = int(n[2])
    digit2 = int(n[1])
    digit1 = int(n[0])
    n = int(n)
    sumSquare = digit1**2 + digit2**2 + digit3**2
    if n%11 == 0:
        if n/11 == sumSquare:
            return True
nums = []
for n in range(100,1000):
    if isThisTheNumber(n):
        nums.append(n)

print(nums)
