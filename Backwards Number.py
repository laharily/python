# swaps the digits in a 4-digit number that was inputted
fourDigNum = int(input("Enter a 4-digit number: "))
backwards = ""
for x in range(4):
    n = fourDigNum % 10
    n = str(n)
    backwards += n
    fourDigNum = fourDigNum // 10
backwards = int(backwards)
print("The 4-digit number backwards is:", backwards)
