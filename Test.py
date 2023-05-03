from Minimax import *
from Heuristic import *

################################################################################
# BOARDS
#A blank connect 4 board
board1 = []
for i in range(6):
    board1.append([" ", " ", " ", " ", " ", " ", " "])
#A board with a row of three
board_three_row = []
for i in range(5):
    board_three_row.append([" ", " ", " ", " ", " ", " ", " "])
board_three_row.append(["Y", "Y", "Y", " ", "B", "B", "B"])
#A board with three in a column
board_three_col = []
for i in range(3):
    board_three_col.append([" ", " ", " ", " ", " ", " ", " "])
for i in range(4):
  board_three_col.append([" ", " ", "Y", " ", " ", " ", " "])
#A board with three in a diagonal
board_diag = []
for i in range(2):
  board_diag.append([" ", " ", " ", " ", " ", " ", " "])
board_diag.append([" ", " ", " ", " ", " ", " ", " "])
board_diag.append([" ", " ", "Y", " ", " ", " ", " "])
board_diag.append([" ", "Y", "Y", "Y", " ", " ", " "])
board_diag.append(["Y", "B", "B", "B", " ", " ", " "])
################################################################################
# TESTS
"""These are tests that are used to make sure that the functions in Heuristic 
are working properly."""
def test_three_heuristic(outcome, board, player):
  assert (outcome == three_heuristic(board, player))

def test_two_heuristic(outcome, board, player):
  assert (outcome == two_heuristic(board, player))

def test_score_board(outcome, board, player, heuristic):
  assert (outcome == score_board(board, player, heuristic))
################################################################################
#Run the Tests
def run_tests():
  print('Testing helper three_heuristic')
  test_three_heuristic(0, board1, 'Y')
  test_three_heuristic(1, board_three_row, 'Y')
  test_three_heuristic(1, board_three_row, 'B')
  test_three_heuristic(1, board_three_col, 'Y')
  test_three_heuristic(3, board_diag, 'Y')

  print('Testing two_heristic')
  test_two_heuristic(0, board1, 'Y')
  test_two_heuristic(0, board_three_row, 'Y')
  test_two_heuristic(0, board_three_row, 'B')
  test_two_heuristic(0, board_three_col, 'Y')
  test_two_heuristic(3, board_diag, 'Y')

  print('Testing score_board with heuristic 2')
  test_score_board(0, board1, 'Y', 2)
  test_score_board(0, board_three_row, 'Y', 2)
  test_score_board(0, board_three_row, 'B', 2)
  test_score_board(9, board_three_col, 'Y', 2)
  test_score_board(21, board_diag, 'Y', 2)

  print('All tests passed')