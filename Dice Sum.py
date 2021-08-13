.# Write a python program called diceSum that prompts the user for a desired sum, then repeatedly simulates the rolling of 2 six-sided dice until their sum is the desired sum. Here is a
# sample dialogue with the user:
# Desired dice sum: 9
# 4 and 3 = 7
# 3 and 5 = 8
# 5 and 6 = 11
# 5 and 6 = 11
# 1 and 5 = 6
# 6 and 3 = 9 

import random
i = input("Enter a desired dice sum between 2 and 12.")
dice1 = random.randrange (1,7)
dice2 = random.randrange (1,7)
while (dice1 + dice2) != (int)i:
    dice1 = random.randrange (1,7)
    dice2 = random.randrange (1,7)
    print (dice1, " and ", dice2, " = ", dice1 + dice2)
