import random

# Setting up the game
hangman = (
    """
  ------
  |    |
  |
  |
  |
  |
  |
  |
  |
__________

""",
"""
  ------
  |    |
  |    O
  |
  |
  |
  |
  |
  |
__________
""",
"""
------
  |    |
  |    O
  |   -+-
  |
  |
  |
  |
  |
__________
""",
"""
------
  |    |
  |    O
  |  /-+-
  |
  |
  |
  |
  |
__________
""",
"""
------
  |    |
  |    O
  |  /-+-\
  |
  |
  |
  |
  |
__________
""",
"""
------
  |    |
  |    O
  |  /-+-\
  |    |
  |
  |
  |
  |
__________
""",
"""
------
  |    |
  |    O
  |  /-+-\
  |    |
  |    |
  |   /
  |  /
  |
__________
""",
"""
------
  |    |
  |    O
  |  /-+-/
  |    |
  |    |
  |   | |
  |   | |
  |
__________
""")

maxwrong = len(hangman) - 1
words = ("PUPPIES","PYTHON","VIOLIN","OVERUSED","CLAM","CONFETTI")
word = random.choice(words)
sofar = "_" * len(word)
wrong = 0
used = []
print("Welcome to Hangman. Good luck!")

while wrong < maxwrong and sofar != word:
    print(hangman[wrong])
    print("You've used the following letters: " + str(used))
    print("So far, the word is: " + str(sofar))
    guess = input("\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed the letter " + str(guess) + ".")
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)
    if guess in word:
        print("\nYes! " + str(guess) + " is in the word!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += sofar[i]
        sofar = new
    else:
        print("\nSorry, " + str(guess) + " isn't in the word.")
        wrong += 1

if wrong == maxwrong:
    print(hangman[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")

print("\nThe word was: " + str(word))

input("\nPress enter to exit.")            
          
