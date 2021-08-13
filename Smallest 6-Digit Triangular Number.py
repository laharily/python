sums = 0
nextdigit = 0
while True:
    sums += nextdigit
    if sums >= 100000 and sums <= 999999:
        print("The smallest 6-digit triangular number is: " + str(sums))
        break
    nextdigit += 1
    
    
    
