# 2.
favorite1 = input("Enter your favorite food: ")
favorite2 = input("Enter your second favorite food: ")
print("Here is a new food: " + favorite1 + favorite2)

# 3.
billtotal = input("Enter a restaraunt bill total: $") 
tip15 = int(billtotal) * 15/100
tip20 = int(billtotal) * 20/100
print("The 15 percent tip is: $" + str(tip15))
print("The 20 percent tip is: $" + str(tip20))

# 4.
baseprice = input("Enter the base price of your car: $")
tax = int(baseprice) * 10/100
licensefee = int(baseprice) * 5/100
dealerprep = 300
destinationcharge = 500
totalprice = tax + licensefee + dealerprep + destinationcharge + int(baseprice)
print("The total price of your car is: $" + str(totalprice))
