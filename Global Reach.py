
# Global Reach
# Demostrates global variables

def readglobal():
    print("From inside the local scope of readglobal(), value is: " + str(value))

def shadowglobal():
    value = -10
    print("From inside the local scope of shadowglobe(), value is: " + str(value))

def changeglobal():
    global value
    value = -10
    print("From inside the local scope of changeglobal(), value is: " + str(value))

# main
# value is a global variable because we're in the global scope here
value = 10
print("In the global scope, value has been set to: " + str(value) + ".\n")

readglobal()
print("Back in the global scope, value is still: " + str(value) + ".\n")

shadowglobal()
print("Back in the global scope, value is still: " + str(value) + ".\n")

changeglobal()
print("Back in the global scope, value has changed to: " + str(value) + ".")

input("\nPress enter to exit.")
