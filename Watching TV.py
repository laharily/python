class Tv(object):
    """A virtual TV"""
    def __init__(self, channel = 1, volume = 10):
        self.channel = channel
        self.volume = volume

    def nextchannel(self):
        self.channel += 1
        if self.channel > 10:
            self.channel = 10
        print("You're watching channel " + str(self.channel))

    def previouschannel(self):
        self.channel -= 1
        if self.channel < 1:
            self.channel = 1
        print("You're watching channel " + str(self.channel))

    def raisevolume(self):
        self.volume += 10
        if self.volume > 50:
            self.volume = 50
        print("Increased the volume to: " + str(self.volume))

    def lowervolume(self):
        self.volume -= 10
        if self.volume < 1:
            self.volume = 1
        print("Decreased the volume to: " + str(self.volume))

def main():

    tv = Tv()

    choice = None
    while choice != "0":
        print \
              ("""
Watching TV

0 - Turn off the TV
1 - Next channel
2 - Previous channel
3 - Raise volume
4 - Lower volume
               """)

        choice = input("Choice: ")
        print()
        
        if choice == "0":
            print("Goodbye.")

        elif choice == "1":
            tv.nextchannel()

        elif choice == "2":
            tv.previouschannel()

        elif choice == "3":
            tv.raisevolume()

        elif choice == "4":
            tv.lowervolume()

        else:
            print("Sorry, but " + str(choice) + " isn't a valid choice.")

main()
input("\nPress the enter key to exit.")

            
