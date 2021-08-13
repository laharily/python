# Playing Cards
# Demostrates combining objects

class Card(object):
    """ A playing card. """
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """ A hand of playing cards."""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

# main
card1 = Card(rank = "A", suit = "c")
print("Printing a Card object:")
print(card1)

card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "3", suit = "c")
card4 = Card(rank = "4", suit = "c")
card5 = Card(rank = "5", suit = "c")
print("\nPrinting the rest of the objects individually:")
print(card2)
print(card3)
print(card4)
print(card5)

myhand = Hand()
print("\nPrinting my hand before I add any cards:")
print(myhand)

myhand.add(card1)
myhand.add(card2)
myhand.add(card3)
myhand.add(card4)
myhand.add(card5)
print("\nPrinting my hand after adding 5 cards:")
print(myhand)

yourhand = Hand()
myhand.give(card1, yourhand)
myhand.give(card2, yourhand)
print("\nGave the first two cards from my hand to your hand.")
print("Your hand:")
print(yourhand)
print("My hand:")
print(myhand)

myhand.clear()
print("\nMy hand after clearing it:")
print(myhand)

input("\n\nPress the enter key to exit.")
