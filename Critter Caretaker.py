# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

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
        print("Sneaky! You have entered the secret choice! You will be revealed all the personal information:")
        print("My name is: " + str(self.name))
        print("My hunger level is: " + str(self.hunger))
        print("My boredom level is: " + str(self.boredom))
        # print(self.mood())

def main():
    critname = input("What do you want to name your critter? ")
    crit = Critter(critname)

    choice = None
    while choice != "0":
        print \
                  ("""
Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter
                   """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Goodbye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            crit.eat()

        # play with your critter
        elif choice == "3":
            crit.play()

        elif choice == "4":
            crit.__tostr__()

        # some random unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\nPress enter to exit.")
            
