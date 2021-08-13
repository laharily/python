print("Think of a number between 0 and 100.")
input("Hit enter when you have it.")
lowRange = 0
highRange = 100
guess = 50
count = 0
while True:
    print("I guess " + str(guess))
    count += 1
    lhc = input("Is this low, high, or correct? ")
    if lhc == "correct":
        print("Yay! I knew it!")
        print("It took me " + str(count) + " guess(es).")
        break
    elif lhc == "low":
        lowRange = guess
        guess = (guess + highRange)//2
        
    else:
        highRange = guess
        guess = (guess + lowRange)//2
       
