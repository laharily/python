# Receive and Return
# Demonstrates parameters and return values

def display(message):
    print(message)

def givemefive():
    five = 5
    return five

def askyesorno(question):
    """Asks a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

# main
display("Here's a message for you.\n")

number = givemefive()
print("Here's what I got from givemefive(): " + str(number))

answer = askyesorno("\nPlease enter 'y' or 'n': ")
print("Thanks for entering " + answer)

input("\nPress enter to exit.")
