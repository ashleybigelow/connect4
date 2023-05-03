import copy
import random

from Heuristic import *
from Connect_4 import *

AI_CHIP = 'B'
OTHER_CHIP = 'Y'

"""
A function that is used to calculate the next best move that the AI should
pick, I started by using an algorithm that gives one point for every three in
a row that has the possibility to be completed.

board is a list of lists representing a Connect 4 board. depth is an integer
representing how deep you want the pruning to go. alpha represents the alpha
constant in alpha beta pruning. beta represents the beta constant in alpha beta
pruning. max_player is a boolean that is true if you are runniing the pruning
for the maximum player (in this case, the AI), or false if it is the minimum
player (the player)

this returns a tuple of two values, the first represents the best value and the
second represents which column that gives the best value
"""
def minimax(board, depth, alpha, beta, max_player, heuristic):
  # Base case- If there is no more moves to be made, return None. The score is
  # based on the cercumstances
  if depth == 0 or game_over(board): 
    if game_over(board):
      if winning_board(board, AI_CHIP):
        return None, 1000000
      elif winning_board(board, OTHER_CHIP):
        return None, -100000
      else:
        return None, 0     
    else:
      return None, score_board(board, AI_CHIP, heuristic)

  open_cols = valid_cols(board) # A list of columns that can be selected.

  # Run the alpha beta pruning
  if max_player: #if it is the AI's turn
    best = -100000
    column = random.choice(open_cols)
    for col in open_cols: #loops through each of the possible child nodes
      new_board = copy.deepcopy(board)
      new_board = update_board(new_board, col, AI_CHIP)
      value = minimax(new_board, depth - 1, alpha, beta, False, heuristic)[1]
      if value > best:
        best = value
        column = col
      alpha = max(alpha, best)
      if beta <= alpha:
        break
    return column, best
  else: #If it is the other players turn
    best = 100000
    column = random.choice(open_cols)
    for col in open_cols: #loops through each of the possible child nodes
      new_board = copy.deepcopy(board)
      new_board = update_board(new_board, col, OTHER_CHIP)
      value = minimax(new_board, depth - 1, alpha, beta, True, heuristic)[1]
      if value < best:
        best = value
        column = col
      beta = min(beta, best)
      if beta <= alpha:
        break
    return column, best


""" 
A function that returns the columns that are not full

board is a valid connect 4 board, which is a list of lists
"""
def valid_cols(board):
  ans = []
  for i in range(7):
    if board[0][i] == " ":
      ans.append(i)
  return ans

"""
A function that allows the user to play against the AI at a certian depth
and using a certain heuristic.

board is a list of lists representing a Connect 4 board, depth is a number
representing how deep you want the minimaxing to go, and heuristic is a number
correlating with which heueristic you want the AI to use.
"""
def play_against_AI(board, depth, heuristic):
  #Set up the game
  depth = int(depth)
  turn = "Y"
  create_board(board)
  while not game_over(board):
    if turn == 'B':
      col, val = minimax(board, depth, -100000, 100000, AI_CHIP, heuristic)
      board = update_board(board, col, 'B')
      create_board(board)
    else:
      col_choice = player_choice(board, turn)
      # update the board
      board = update_board(board, int(col_choice), turn)
      create_board(board)
    turn = "B" if turn == "Y" else "Y"
  if winning_board(board, 'Y'): print('You win!')
  elif winning_board(board, 'B'): print('You lose :(')
  else: print('There was a tie!')
  reset_board()

""" 
A function that plays two heuristics against eachother. It call the minimax
function using the given depths and heuristics to play the game.

board is a list of lists that represents a Connect-4 board
depth is an integer representing the depth the user wants the first AI to run at
depth2 is an integer representing the depth the user wants the second AI to run 
at
heuristic is a number representing the heuristic that the first AI will use
heuristic2 is a number representhing the heuristic that the second AI will use
"""
def play_AI_against_itself(board, depth, depth2, heuristic, heuristic2):
  #Set up the game
  depth = int(depth)
  turn = "B"
  while not game_over(board):
    if turn == 'B':
      col, val = minimax(board, depth, -100000, 100000, 'B', heuristic)
      board = update_board(board, col, turn)
    else:
      col, val = minimax(board, depth2, -100000, 100000, 'Y', heuristic2)
      board = update_board(board, col, turn)
    turn = "B" if turn == "Y" else "Y"
  if winning_board(board, 'B'): return 'AI 1 Wins'
  elif winning_board(board, 'Y'): return 'AI 2 Wins'
  else: return 'There was a tie!'

"""
This function runs plays 2 heuristics against one another for all depths 1-5,
printing the results so you can see how many times each heuristic won.

board is a list of lists representing a Connect-4 board
heuristic is a number representing the heuristic that the first AI will use
heuristic2 is a number representhing the heuristic that the second AI will use
"""
def test_ai(board, heuristic, heuristic2):
  ai1 = 0
  ai2 = 0
  tie = 0
  for i in range(1,6):
    for j in range(1, 6):
      print('('+str(i)+','+str(j)+'): '+ play_AI_against_itself(board, i, j, heuristic, heuristic2))
      #play_AI_against_itself(board, i, j, heuristic, heuristic2)
      if winning_board(board, 'B'): 
        ai1+=1
      elif winning_board(board, 'Y'): 
        ai2+=1
      else:
        tie+=1
      reset_board()
  print('heuristic ' + str(heuristic) + " #wins: " + str(ai1))
  print('heuristic ' + str(heuristic2) + " #wins: " + str(ai2))
  print('Ties: ' + str(tie))

def run_multiple_tests(board, heuristic, heuristic2):
  for i in range(10):
    test_ai(board, heuristic, heuristic2)