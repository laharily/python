attributes = ["Strength","Health","Wisdom","Dexterity"]
points = 30
newdict = {}

while points > 0:

    attributechoice = input("\nYou have 4 attributes you can assign points to. Press 0 for Strength, 1 for Health, 2 for Wisdom, and 3 for Dexterity: ")
    pointschoice = input("\nYou have " + str(points) + " points left. How many points do you want to assign to " + attributes[int(attributechoice)] + "? ")
    attributechoice = attributes[int(attributechoice)]
    print(attributechoice)
    newdict[attributechoice] = pointschoice
    points -= int(pointschoice)
    print("\nYou now have " + str(points) + " points left.")
    print(newdict)
