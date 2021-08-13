print("Creating a text file with the write() method.")
file = open("writeit.txt","w")
file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3.\n")
file.close()

print("\nCreating a file with the writelines() method.")
file = open("writeit.txt","w")
lines = ["Line 1\n","This is line 2\n","This is line 3\n"]
file.writelines(lines)
file.close()

print("\nReading the newly created file.")
file = open("writeit.txt","r")
print(file.read())
file.close()

input("\nPress the enter key to exit.")

