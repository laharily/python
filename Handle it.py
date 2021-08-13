# Handle it
# Demonstrates how to handle exceptions

try:
    num = float(input("Enter a number: "))
except:
    print("\nSomething went wrong!")

try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("\nThat was not a number.")

# Handling multiple exception types

print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "--->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong!")

print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "--->", end=" ")
        print(float(value))
    except TypeError:
        print("I can only convert a string or a number!")
    except ValueError:
        print("I can only convert a string or digits!")

# Getting an exception's argument

try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("\nThat was not a number! Or as Python would say...")
    print(e)

# Try/except/else

print()
try:
    num = float(input("Enter a number: "))
except ValueError:
    print("\nThat was not a number!")
else:
    print("\nYou entered the number " + str(num))

input("\nPress enter to exit.")
    
