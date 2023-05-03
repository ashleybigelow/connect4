from Connect_4 import winning_board

"""
A function that will calculate the score of the current board based on the 
heuristic

board is a list of lists representing a Connect 4 board
player is a character that represents whose score you are trying to calculate
Heuristic is a number 1 or 2 that determines which heuristic is used by the AI
"""

def score_board(board, player, heuristic):
  score = 0
  # Heruistic 1: Rows of three
  if heuristic == 1:
    score = score + three_heuristic(board, player)
    score = score - three_heuristic(board, opponent(player))
  # Heuristic 2: Count rows of 2 as well
  elif heuristic == 2:
    score = score + 9*three_heuristic(board, player)
    score = score - 9*three_heuristic(board, opponent(player))
    score = score + two_heuristic(board, player)
    score = score - two_heuristic(board, opponent(player))
  # Heuristic 2 with neg values larger
  elif heuristic == 3:
    score = score + 9*three_heuristic(board, player)
    score = score - 1.2*9*three_heuristic(board, opponent(player))
    score = score + two_heuristic(board, player)
    score = score - 1.2*two_heuristic(board, opponent(player))
  # Heuristic 3: weigh by colums
  elif heuristic == 4:
    score = score + add_col_weight(board, player)
  # Heuristic 2 + Heuristic 3
  elif heuristic == 5:
    score = score + 9*three_heuristic(board, player)
    score = score - 1.2*9*three_heuristic(board, opponent(player))
    score = score + two_heuristic(board, player)
    score = score - 1.2*two_heuristic(board, opponent(player))
    score = (score)+(add_col_weight(board, player))
  return score

"""
Returns the opponent of the current player

player is a character representing which players turn it is
"""
def opponent(player):
  if player == 'Y': return 'B'
  else: return 'Y'


def add_col_weight(board,player):
  total = 0
  weight = 0
  pct = 0
  for i in range(0, 6):
    if board[i][0] == player:
      weight+=2
      pct+=1
    if board[i][1] == player:
      weight+=4
      pct+=1
    if board[i][2] == player:
      weight+=8
      pct+=1
    if board[i][3] == player:
      weight+=16
      pct+=1
    if board[i][4] == player:
      weight+=8
      pct+=1
    if board[i][5] == player:
      weight+=4
      pct+=1
    if board[i][6] == player:
      weight+=2
      pct+=1
  total = weight/pct
  return total

"""
Calculates the number of three in a row lines that can become a winning row

board is a list of lists representing a Connect 4 board
player is a character that represents the player who you are calculating the 
score for
"""
def three_heuristic(board, player):
  score = 0
  #Check for three in a row with a blank to the left or right
  for i in range(0, 6):
    for j in range(0, 4):
      if (board[i][j] == player and board[i][j+1] == player and 
      board[i][j+2] == player and board[i][j+3] == " "):
        score += 1
      if (board[i][j] == " " and board[i][j+1] == player and 
      board[i][j+2] == player and board[i][j+3] == player):
        score += 1
  #Check for three in a column with a blank above or below
  for i in range(0, 3):
    for j in range(0, 7):
      if (board[i][j] == player and board[i+1][j] == player and
      board[i+2][j] == player and board[i+3][j] == " "):
        score += 1
      if (board[i][j] == " " and board[i+1][j] == player and
      board[i+2][j] == player and board[i+3][j] == player):
        score += 1
  #Check for three in a diagonal that can be made into a winning line
  for i in range(0, 3):
    for j in range(0, 4):
      if (board[i][j] == player and board[i+1][j+1] == player and 
      board[i+2][j+2] == player and board[i+3][j+3] == " "):
        score += 1
      if (board[i][j] == " " and board[i+1][j+1] == player and 
      board[i+2][j+2] == player and board[i+3][j+3] == player):
        score += 1
  #Check for three in a diagonal that can be made into a winning line
  for i in range(0, 3):
    for j in range(3, 7):
      if (board[i][j] == " " and board[i+1][j-1] == player and 
      board[i+2][j-2] == player and board[i+3][j-3] == player):
        score += 1
      if (board[i][j] == player and board[i+1][j-1] == player and 
      board[i+2][j-2] == player and board[i+3][j-3] == " "):
        score += 1

  return score

"""
Calculates the score given to the number of two chips in a line that could be
formed into a winning line.

board is a list of lists representing a Connect 4 board
player is a character representing the player who you are calculating the score 
for
"""
def two_heuristic(board, player):
  score = 0
  # Two in a row, must check: two spots to left, two to right, or one each
  for i in range(0, 6):
    for j in range(0, 4):
      if (board[i][j] == player and board[i][j+1] == player and
      board[i][j+2] == " " and board[i][j+3] == " "):
        if (j == 0):
          score += 1
        elif (board[i][j-1] != player):
          score += 1
      if (board[i][j] == " " and board[i][j+1] == player and
      board[i][j+2] == player and board[i][j+3] == " "):
        score += 1
      if (board[i][j] == " " and board[i][j+1] == " " and
      board[i][j+2] == player and board[i][j+3] == player):
        if (j == 3):
          score += 1
        elif (board[i][j+4] != player):
          score += 1
  # Two in a column, must check: two above, two below, or one above one below
  for i in range(0, 3):
    for j in range(0, 7):
      if (board[i][j] == player and board[i+1][j] == player and
      board[i+2][j] == " " and board[i+3][j] == " "):
        if (i == 0):
          score += 1
        elif (board[i-1][j] != player):
          score += 1
      if (board[i][j] == " " and board[i+1][j] == player and
      board[i+2][j] == player and board[i+3][j] == " "):
        score += 1
      if (board[i][j] == " " and board[i+1][j] == " " and
      board[i+2][j] == player and board[i+3][j] == player):
        if (i == 2): 
          score += 1
        elif (board[i+4][j] != player):
          score += 1
  #Two in a diagonal - same idea, check if it can be made into a winning line
  for i in range(0, 3):
    for j in range(0, 4):
      if (board[i][j] == player and board[i+1][j+1] == player and 
      board[i+2][j+2] == " " and board[i+3][j+3] == " "):
        if(i == 0 or j == 0): 
          score += 1
        elif(board[i-1][j-1] != player):
          score += 1
      if (board[i][j] == " " and board[i+1][j+1] == player and 
      board[i+2][j+2] == player and board[i+3][j+3] == " "):
        score += 1
      if (board[i][j] == " " and board[i+1][j+1] == " " and 
      board[i+2][j+2] == player and board[i+3][j+3] == player):
        if(i == 2 or j == 3):
          score += 1
        elif(board[i+4][j+4] != player):
          score += 1
  #Two in a diagonal (other direction)
  for i in range(0, 3):
    for j in range(3, 7):
      if (board[i][j] == " " and board[i+1][j-1] == " " and 
      board[i+2][j-2] == player and board[i+3][j-3] == player):
        if (i == 2 or j == 3):
          score +=1
        elif (board[i+4][j-4] != player):
          score += 1
      if (board[i][j] == " " and board[i+1][j-1] == player and 
      board[i+2][j-2] == player and board[i+3][j-3] == " "):
        score += 1
      if (board[i][j] == player and board[i+1][j-1] == player and 
      board[i+2][j-2] == " " and board[i+3][j-3] == " "):
        if(i == 0 or j == 6):
          score += 1
        elif(board[i-1][j+1] != player):
          score += 1

  return score