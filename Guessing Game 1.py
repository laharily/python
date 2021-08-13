import random

num = random.randrange(0, 101)
count = 0

print("I'm thinking of a number between 0 and 100.")

while True:
    guess = input("\nEnter your guess: ")
    guess = int(guess)
    if guess > num:
        print("\nSorry, " + str(guess) + " is too high.")
        count += 1
    elif guess < num:
        print("\nSorry, " + str(guess) + " is too low.")
        count += 1
    else:
        print("\nCongratulations, " + str(guess) + " is my number!")
        count += 1
        break

print("\nIt took you " + str(count) + " guesses.")
