geek = {"404":"Clueless. From the web error message 404, meaning page not found.",
        "Googling":"Searching the Internet for background information on a person.",
        "Keyboard Plague":"The collection of debris found in computer keyboards.",
        "Link Rot":"The process by which web page links become obsolete.",
        "Percussive Maintenance":"The act of striking an electronic device to make it work.",
        "Uninstalled":"Being fired. Especially popular during the dot-bomb era."}

choice = None
while choice != "0":

    print("\nGeek Translator\n\n0 - Quit\n1 - Look up a geek term\n2 - Add a geek term\n3 - Redefine a geek term\n4 - Delete a geek term\n")
    choice = input("Choice: ")

    if choice == "0":
        print("\nGoodbye!")
    elif choice == "1":
        term = input("What geek term do you want me to translate? ")
        if term in geek:
            definition = geek[term]
            print("\n" + term + " means: " + definition)
        else:
            print("\nSorry, I don't know " + term + ".")
    elif choice == "2":
        term = input("What geek term do you want me to add? ")
        if term not in geek:
            definition = input("What is the definition? ")
            geek[term] = definition
            print("\n" + term + " has been added to the dictionary.")
        else:
            print("\nThat term already exists in the dictionary.")
    elif choice == "3":
        term = input("What term do you want me to redefine? ")
        if term in geek:
            definition = input("What should be the new definition? ")
            geek[term] = definition
            print("\n" + term + " has been redefined.")
        else:
            print("\nThat term doesn't exist in the dictionary. Try adding it!")
    elif choice == "4":
        term = input("What geek term do you want to delete? ")
        if term in geek:
            del geek[term]
            print("\n" + term + " has been deleted.")
        else:
            print("\nThat term doesn't exist in the dictionary.")
    else:
        print("\nSorry, but " + choice + " isn't a valid choice.")

input("\nPress enter to exit.")
