""" 
Creating the Connect 4 Board, this is a List of Lists (2D List), where each
of the inner lists represents a row on a connect 4 board.
"""
connect_4_board = []
for i in range(6):
    connect_4_board.append([" ", " ", " ", " ", " ", " ", " "])

"""
reset_board is a function that resets the board so that it is blank again and 
ready to be used.
"""
def reset_board():
  for i in range(6):
    for j in range(7):
      connect_4_board[i][j] = " "

""" 
create_board is a function that draws the current board in the terminal.

board is a list of lists that represents a Connect-4 Board.
"""
def create_board(board):
    print("  0   1   2   3   4   5   6")
    print("+---+---+---+---+---+---+---+")

    for i in range(6):
        print("| " + add_color(board[i][0]) + " | " + add_color(board[i][1]) + 
        " | " + add_color(board[i][2]) + " | " + add_color(board[i][3]) + 
        " | " + add_color(board[i][4]) + " | " + add_color(board[i][5]) + 
        " | " + add_color(board[i][6]) + " |")
        print("+---+---+---+---+---+---+---+")

"""
add_color is a function that takes in a character and makes it either blue or
yellow, depending on which character is used.

text is the character that you want to color
"""
def add_color(text):
  if text == 'Y':
    return "\033[1;33m" + text + "\033[0m"
  elif text == 'B':
    return "\033[1;96m" + text + "\033[0m"
  else:
    return text

""" 
update_board is a function that updates the board based on what the player 
chooses.

board is a list of lists representing a Connect 4 Board
col is an integer representing which column was chosen
turn is a character representing which characters turn it is
"""
def update_board(board, col, turn):
  if board[5][col] == " ": board[5][col] = turn
  elif board[4][col] == " ": board[4][col] = turn
  elif board[3][col] == " ": board[3][col] = turn
  elif board[2][col] == " ": board[2][col] = turn
  elif board[1][col] == " ": board[1][col] = turn
  elif board[0][col] == " ": board[0][col] = turn
  return board

""" 
game_over is a function that checks to see if the game is over or not.

board is a list of lists representing a Connect-4 board
"""
def game_over(board):
  return winning_board(board, 'Y') or winning_board(board, 'B') or tie(board)

""" 
winning_board is a function that checks to see if a player p had four in a row 
on the board. If they do, then the output is true. Otherwise, the game outputs 
false.

board is a list of lists representing a Connect-4 board
p is a character representing the player who you are checking for a win
"""
def winning_board(board, p):
  ## Check for a horizontal win
  for i in range(0, 6):
    for j in range(0, 4):
      if (board[i][j] == p and board[i][j+1] == p and 
      board[i][j+2] == p and board[i][j+3] == p):
        return True

  ## Check for a vertical win
  for i in range(0, 3):
    for j in range(0, 7):
      if (board[i][j] == p and board[i+1][j] == p and
      board[i+2][j] == p and board[i+3][j] == p):
        return True

  ## Check for a diagonal win (down and right)
  for i in range(0, 3):
    for j in range(0, 4):
      if (board[i][j] == p and board[i+1][j+1] == p and board[i+2][j+2] == p and
      board[i+3][j+3] == p):
        return True
  
  ## Check for a diagonal win (up and right)
  for i in range(0, 3):
    for j in range(3, 7):
      if (board[i][j] == p and board[i+1][j-1] == p and board[i+2][j-2] == p and
      board[i+3][j-3] == p):
        return True

  return False

"""
tie is a function that checks to see if there was a tie

board is a list of lists that represents a Connect-4 board
"""
def tie(board):
  # make sure that the board is not full
  if (board[0][0]!=" " and board[0][1]!=" " and board[0][2]!=" " and 
  board[0][3]!=" " and board[0][4]!=" " and board[0][5]!=" " and 
  board[0][6]!=" "): return True
  else: return False

""" 
play_game is a function that starts the game for two players who are manually 
playing

board is a list of lists representing a Connect 4 board
"""
def play_game(board):
  #Set up the game
  turn = "Y"
  create_board(board)

  #until someone wins, have players alternate turns
  while (not game_over(board)):
    col_choice = player_choice(board, turn)
    # update the board
    board = update_board(board, int(col_choice), turn)
    create_board(board)
    turn = "B" if turn == "Y" else "Y"
  if winning_board(board, 'Y'): print('Y wins!')
  elif winning_board(board, 'B'): print('B wins!')
  else: print('There was a tie!')
  reset_board()

"""
player_choice is a function that asks the user to choose a column and then adds 
a piece to that column for them.

board is a list of lists representing a Connect 4 board
turn is a character, either 'B' or 'Y', representing which characters turn it is
"""
def player_choice(board, turn):
  # make sure the user enters a number 0 - 6 and that the column is not full
  not_num = True
  # make sure that the user enters a number that is allowed
  while not_num:
    col_choice = input(turn + " Choose a Column: ")
    try: int(col_choice)
    except: print("Enter a number 0 - 6")
    else: 
      if int(col_choice) <= 6 and int(col_choice) >= 0:
        if board[0][int(col_choice)]!=" ":
          print("Column Full, Pick Another")
        else: not_num = False
      else:
        print("Enter a number 0 - 6")
  return col_choice