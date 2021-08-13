board = [[".",".",".",".",".",".","."],
                [".",".",".",".",".",".","."],
                [".",".",".",".",".",".","."],
                [".",".",".",".",".",".","."],
                [".",".",".",".",".",".","."],
                [".",".",".",".",".",".","."]]

def draw_board():
     '''draw_board() --> None
     Draws the board'''
     boardString = "\n0  1  2  3  4  5  6 \n" # starts the string with the column numbers
     for line in board: # iterates through the list
          for position in line: # iterates through the lists inside the list
               # formatting
               boardString += " "
               boardString += position # adds each line of list
               boardString += "  " 
          boardString += "\n"
     return boardString

def winner():
     '''winner() --> None
     Finds if there is a winner'''
     for row in range(5,1,-1):
          for column in range(6,-1,-1):
               # if they got 4 in a column
               if board[row][column] != "." and board[row][column]==board[row-1][column]== \
                  board[row-2][column]==board[row-3][column]:
                    return True
               # if they got 4 in a row
               elif board[row][column] != "." and board[row][column]==board[row][column-1]== \
                    board[row][column-2]==board[row][column-3]:
                    return True
               # if they got 4 diagonally
               elif board[row][column] != "." and board[row][column]==board[row-1][column-1]== \
               board[row-2][column-2]==board[row-3][column-3]:
                    return True


# asks for names             
playerX = input("Player X, enter your name: ")
playerO = input("Player O, enter your name: ")
print(draw_board()) 

players = {'X': playerX, 'O': playerO} # keeps track of names

while not winner(): # while nobody wins yet
     # X's turn
     columnX = int(input("\n" + playerX + ", you're X. Which column do you want to play in? "))
     for row in range(5,0,-1): # goes from bottom to top
          if board[row][columnX] == ".": # if empty,
               board[row][columnX] = "X" # put X. otherwise, move up one
               break
     print(draw_board())
     if winner(): # if there is a winner
          winner = players[board[row][columnX]] # winner is set to the value of the letter in the dict
          break
     # O's turn
     columnO = int(input("\n" + playerO + ", you're O. Which column do you want to play in? "))
     for row in range(5,0,-1):
          if board[row][columnO] == ".":
               board[row][columnO] = "O"
               break
     print(draw_board())
     if winner(): 
          winner = players[board[row][columnO]]
          break

# we have a winner!
input("\nConnect 4! Congratulations, " + winner + ", you won! \n\nPress enter to quit the game.")
