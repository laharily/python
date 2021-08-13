import random

# 1.

r = random.randint(1,5)
f1 = "Fortune is coming your way!"
f2 = "Mistakes will happen. Turn them into opportunities."
f3 = "Don't trust your new friend. Ignore any invitations-it's a trap!"
f4 = "You will not make what you are trying out for, so try for something else."
f5 = "Laughter makes all things better!"

if r == 1:
    print(f1)
elif r == 2:
    print(f2)
elif r == 3:
    print(f3)
elif r == 4:
    print(f4)
else:
    print(f5)

# 2.

flipcoins = 0
heads = 0
tails = 0
while flipcoins <= 100:

    r = random.randint(1,2)
    if r == 1:
        heads += 1
    else:
        tails += 1
    flipcoins += 1

print("Heads: " + str(heads))
print("Tails: " + str(tails))

# 3.

r = random.randint(1,20)
tries = 0
guess = input("Try to guess my number. It's between 1 to 20, inclusive. You only have 5 tries: ")
while int(guess) != r and tries <= 5:

    if int(guess) > r:
        print("Try a lower number.")
        guess = input("Guess again: ")
        tries += 1
    elif int(guess) < r:
        print("Try a higher number.")
        guess = input("Guess again: ")
        tries += 1

if int(guess) == r:
    print("Congratulations! You guessed my number!")
if tries > 5:
    print("Oh no! You exceeded the limit of the guesses! Better luck next time!")

# 4.

n = 0
while True:
    n += 1
    if n == 5:
        continue
    if n > 10:
        break
    print(n)

print()
exitprogram = input("Press enter to exit.")

# 5.

username = input("Username: ")
password = input("Password: ")

if username == "Lahari" and password == "ly":
    print("Welcome to the clubhouse, Lahari!")
elif username == "Aashita" and password == "ak1":
    print("Welcome to the clubhouse, Aashita!")
elif username == "Afhseen" and password == "ak2":
    print("Welcome to the clubhouse, Afsheen!")
elif username == "Nithya" and password == "na":
    print("Welcome to the clubhouse, Nithya!")
elif username == "Vedavi" and password == "vk":
    print("Welcome to the clubhouse, Vedavi!")
elif username == "Rhea" and password == "rk":
    print("Welcome to the clubhouse, Rhea!")
elif username == "Sydney" and password == "sb":
    print("Welcome to the clubhouse, Sydney!")
else:
    print("Sorry! You can't enter the clubhouse.")

# 6.

word = input("Enter a word: ")

for x in word:
    print(x)

# 7.

print("Counting:")
for x in range(10):
    print(x)
print()

print("Counting by 5's:")
for x in range(0,50,5):
    print(x)
print()

print("Counting backwards:")
for x in range(10,0,-1):
    print(x)

# 8.

message = input("Enter your message: ")
print()
length = len(message)
print("The length of your message is: " + str(length) + " characters.")
print()

if 'e' in message:
    print("The most common letter in the English language, 'e', is in your message.")
else:
    print("The most common letter in the English language, 'e', is not in your message.")
