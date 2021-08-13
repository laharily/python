scores = []
choice = None
while choice != "0":
    
    print("Choices:\n\n0 - Exit \n1 - Show scores \n2 - Add a score \n3 - Remove a score \n4 - Sort scores")
    choice = input("\nWhat is your choice? ")
    if choice == "0":
        print("Goodb1ye!")
    elif choice == "1":
        print("\nHigh Scores:")
        for x in scores:
            print(x)
        print()
    elif choice == "2":
        addscore = int(input("What score did you get? "))
        scores.append(addscore)
        print()
    elif choice == "3":
        removescore = int(input("What score do you want to remove? "))
        if removescore in scores:
            scores.remove(removescore)
            print()6yt555t
        else:
            print("Sorry, " + str(removescore) + " is not in High Scores.")
        print()
    elif choice == "4":
        scores.sort(reverse = True)
    else:
        print("\nSorry, but " + choice + " isn't a valid response!")
        print()
