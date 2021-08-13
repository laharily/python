import random
def backgammon_roll():
    '''backgammon_roll() -> int
    returns the total of a backgammon roll'''
    dice1 = random.randrange(1,6)
    dice2 = random.randrange(1,6)
    if dice1 == dice2:
        return 2*(dice1 + dice2)
    else:
        return dice1 + dice2

score1 = 0
score2 = 0
while score1 <= 100 and score2 <= 100:
    rolled1 = backgammon_roll()
    score1 += rolled1
    print("\nPlayer 1 rolled " + str(rolled1))
    print("\nThe score is: Player 1 has " + str(score1) + ", Player 2 has " + str(score2))
    rolled2 = backgammon_roll()
    score2 += rolled2
    print("\nPlayer 2 rolled " + str(rolled2))
    print("\nThe score is: Player 1 has " + str(score1) + ", Player 2 has " + str(score2))

if score1 > score2:
    print("\nCongratulations, Player 1! You won with a final score of:\n" + str(score1))
elif score1 < score2:
    print("\nCongratulations, Player 2! You won with a final score of:\n" + str(score2))
else:
    print("\nIt was a tie. You'll have to see who's the real winner next time!")
