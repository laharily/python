def taxicab(num):
    firstx = 0
    firsty = 0
    foundfirst = False
    foundsecond = False
    for x in range(1,23):
        for y in range(1,23):
            if x**3 + y**3 == num:
                if foundfirst == False:
                    foundfirst = True
                    firstx = x
                    firsty = y
                    continue
                elif firstx != y and firsty != x:
                    foundsecond = True
                    print("Found the number: " + str(num))
                    break
        if foundfirst == True and foundsecond == True:
            break

for i in range(1000,10000):
    taxicab(i)
    
            
