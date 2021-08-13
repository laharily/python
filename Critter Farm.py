# Critter Farm
# A virtual pet to care for

class Farm(object):
    """A virtual farm"""
    def __init__(self):
        self.critters = []
        critter1 = Critter("Almond", 3, 2)
        critter2 = Critter("Chick", 1, 2)
        critter3 = Critter("Piglet", 4, 1)
        critter4 = Critter("Sheepy", 1, 10)
        critter5 = Critter("Goaty", 4, 7)
        self.critters.append(critter1)
        self.critters.append(critter2)
        self.critters.append(critter3)
        self.critters.append(critter4)
        self.critters.append(critter5)

    def sayname(self):
        for crit in self.critters:
            crit.sayname()
            
    def talk(self):
        for crit in self.critters:
            crit.talk()

    def eat(self):
        for crit in self.critters:
            crit.eat()

    def play(self):
        for crit in self.critters:
            crit.play()

    def __tostr__(self):
        for crit in self.critters:
            crit.__tostr__()
            
class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def sayname(self):
        print(self.name)

    def __passtime(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__passtime

    def eat(self, food = 4):
        print("Brruppp! Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__passtime()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__passtime()

    def __tostr__(self):
        print("\nMy name is: " + str(self.name))
        print("My hunger level is: " + str(self.hunger))
        print("My boredom level is: " + str(self.boredom))
        print(self.mood)

def main():
    crit = Farm()

    choice = None
    while choice != "0":
        print \
                  ("""
Critter Caretaker

0 - Quit
1 - Find out the names of your critters
2 - Listen to your critters
3 - Feed your critters
4 - Play with your critters
                   """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Goodbye.")

        # listen to your critter
        elif choice == "1":
            crit.sayname()

        # feed your critter
        elif choice == "2":
            crit.talk()

        # play with your critter
        elif choice == "3":
            crit.eat()

        elif choice == "4":
            crit.play()
            
        elif choice == "5":
            print("Sneaky! You have entered the secret choice! You will be revealed all our personal information:")
            crit.__tostr__()
            

        # some random unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\nPress enter to exit.")
            
