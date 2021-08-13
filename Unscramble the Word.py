import random

jumblestring = ""
lst = []
guesswords = ["puppies", "yellow", "apple" ,"python", "banana"]
tries = 0

rc = random.choice(guesswords)

for x in rc:
    lst.append(x)

while lst:
    r = random.randrange(0,len(lst))
    jumblestring += lst[r]
    lst.remove(lst[r])

print(jumblestring)

print("Unscramble the word. You have three tries:")

while tries < 3:
    guess = input("Can you guess it? ")
    if guess == rc:
        print("You guessed it! :)")
        break
    tries += 1
    
if guess != rc:
    print()
    print("You lost! :(")
    print("The word was: " + rc)
