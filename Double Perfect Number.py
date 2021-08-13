doublePerfect = []
for x in range(121, 1000):
    properDivisor = []
    for y in range(1, x):
        if x % y == 0:
            properDivisor.append(y)
    if sum(properDivisor) == x*2:
            doublePerfect.append(x)

print(doublePerfect)
