print("Opening and closing the file.")
file = open("readit.rtf","r")
file.close()

print("\nReading characters from the file.")
file = open("readit.rtf","r")
print(file.read(1))
print(file.read(5))
file.close()

print("\nReading the entire file at once.")
file = open("readit.rtf","r")
wholething = file.read()
print(wholething)
file.close()

print("\nReading characters from a line.")
file = open("readit.rtf","r")
print(file.readline(1))
print(file.readline(5))
file.close()

print("\nReading one line at a time.")
file = open("readit.rtf","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

print("\nReading the entire file onto a list.")
file = open("readit.rtf","r")
lines = file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
file.close()

print("\nLooping through the file, line by line.")
file = open("readit.rtf","r")
for line in file:
    print(line)
file.close()

input("\nPress the enter key to exit.")
