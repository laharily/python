import random

# 1.

'''s = input("Enter a string: ")
for x in range(5):
    randpos = random.randint(0,len(s))
    print(s[randpos])'''

# 2.

word = input("Enter a word: ")
for x in range(0,len(word),2):
    print(word[x])

