inventory = ["sword", "healing potion", "shield", "armor"]
print(inventory)
index = int(input("Enter the index number for an item in the inventory: "))
print("At index " + str(index) + " is the " + str(inventory[index]) + ".")
input("Press enter to continue.")

chest = ["gold","gems"]
print("\nYou went exploring and found:")
print(chest)
print("You want to add them to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)
input("Press enter to continue.")

print("\nYou trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("This is your new inventory: ")
print(inventory)
input("Press enter to continue.")

print("\nYou want to use your gold and gems to buy a future-telling orb.")
inventory[4:6] = ["future-telling orb"]
print("Your inventory is now:")
print(inventory)
input("Press enter to continue.")

print("\nIn a great battle, your shield was destroyed.")
del inventory[2]
print("Your new inventory is:")
print(inventory)
input("Press enter to continue.")

print("\nSadly, your crossbow and healing potion were stolen by thieves.")
del inventory[:2]
print("Your new inventory is:")
print(inventory)
input("Press enter to exit.")
