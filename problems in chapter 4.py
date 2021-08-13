import random

# 2.

'''word = input("Enter a word: ")
for x in range(len(word)-1,-1,-1):
    print(word[x])

# 3.

message = input("Enter a message: ")
newstring = ""
for x in message:
    if x.lower() == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        continue
    else:
        newstring += x

print(newstring)

# 4.

word = "pizza"

while True:

    enter = input("Type 'quit' if you want to quit. Otherwise, press enter. ")
    if enter.lower() == "quit":
        break
    print()
    beginning = input("To slice the pizza, enter a starting position from 0 to 4: ")
    ending = input("Now enter an ending postition from 1 to 5: ")
    print()
    print("Your pizza is sliced into: " + word[int(beginning):int(ending)])
    print()'''

# 5.

while True:

    enter = input("Type 'quit' if you want to quit. Otherwise, press enter. ")
    if enter.lower() == "quit":
        break
    print()
    starting = input("Enter a starting number: ")
    ending = input("Enter an ending number: ")
    amount = input("Enter the amount by which to count: ")
    for x in range(int(starting),int(ending),int(amount)):
        print(x)
