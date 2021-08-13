x = "x"
o = "o"
empty = " "
tie = "tie"
numsquares = 9
def displayinstruct():
    print(
        """
        Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
        This will be a showdown between your human brain and my silicon processor.

        You will make your move known by entering a number, 0-8. The number will
        correspond to the board position as illustrated:

        0 | 1 | 2
        ------------
        3 | 4 | 5
        ------------
        6 | 7 | 8

        Prepare yourself, human. The ultimate battle is about to begin. \n
        """
        )

def askyesorno(question):
    """Asks a yes or no question."""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

def asknumber(question,low,high):
    """Asks for a number within a range."""
    response = -1
    while response not in range(low,high):
        response = int(input(question))
    return response

def pieces():
    """Determines if player or computer goes first."""
    gofirst = askyesorno("Do you require the first move? (y/n): ")
    if gofirst == "y":
        print("\nThen take the first move. You will need it.")
        human = x
        computer = o
    else:
        print("\nYour bravery will be your undoing...I will go first.")
        computer = x
        human = o
    return computer, human

def newboard():
    """Creates new game board."""
    board = []
    for square in range(numsquares):
        board.append(empty)
    return board

def displayboard(board):
    """Displays board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legalmoves(board):
    """Creates list of legal moves."""
    moves = []
    for square in range(numsquares):
        if board[square] == empty:
            moves.append(square)
    return moves

def winner(board):
    """Determines the game winner."""
    waystowin = ((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))

    for row in waystowin:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner
    if empty not in board:
        return tie
    return None

def humanmove(board,human):
    """Gets human move."""
    legal = legalmoves(board)
    move = None
    while move not in legal:
        move = asknumber("Where will you move? (0-8): ", 0, numsquares)
        if move not in legal:
            print("\nThat square is already occupied, foolish human. Choose another.\n")
    print("Fine...")
    return move

def computermove(board,computer,human):
    """Makes computer move."""
    # Makes a copy to work with since function will be changing list.
    board = board[:]
    # The best positions to have, in order.
    bestmoves = (4,0,2,6,8,1,3,5,7)
    print("I shall take square number", end=" ")
    # If computer can win, takes that move
    for move in legalmoves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # If done checking this move, undoes it
        board[move] = empty
    # If human can win, blocks that move
    for move in legalmoves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # If done checking this move, undoes it
        board[move] = empty
    # Since no one can wine on next move, pick best open square
    for move in bestmoves:
       if move in legalmoves(board):
           print(move)
           return move

def nextturn(turn):
    """Switch turns."""
    if turn == x:
        return o
    else:
        return x

def congratwinner(thewinner,computer,human):
    """Congratulates the winner."""
    if thewinner != tie:
        print(thewinner, "won!\n")
    else:
        print("It's a tie!\n")
    if thewinner == computer:
        print("As I predicted, human, I am triumphant once more. \n" \
              "Proof that computers are superior to humans.")
    elif thewinner == human:
        print("No, no! It cannot be! Somehow you tricked me, human. \n" \
              "But never again! I, the computer, so swear it!")
    elif thewinner == tie:
        print("You were most lucky, human, and somehow you managed to tie to me. \n" \
              "Celebrate today...for this is the best you will ever achieve.")

def main():
    displayinstruct()
    computer, human = pieces()
    turn = x
    board = newboard()
    displayboard(board)

    while not winner(board):
        if turn == human:
            move = humanmove(board,human)
            board[move] = human
        else:
            move = computermove(board,computer,human)
            board[move] = computer
        displayboard(board)
        turn = nextturn(turn)
    thewinner = winner(board)
    congratwinner(thewinner,computer,human)

# start the program
main()
input("\nPress enter to quit.")
