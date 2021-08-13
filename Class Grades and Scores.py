# open the files
inFile = open('classgrades.txt','r')
outFile = open('classscores.txt','w')
grades = inFile.readlines() # read lines into a list called grade
inFile.close()
outFile.writelines(grades) # write grade into the output file

for line in grades:
    line = line.split()
    nums = line[1:] # get the numbers of each line
    average = 0        # initialize the average
    count = 0            # intialize the variable for counting the numbers
    # find the average of all the numbers in the line
    for num in nums:
        average += int(num)
        count += 1
    average = average//count
    print(line[0] + ": " + str(average))

outFile.close()
    
    
