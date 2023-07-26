from Connect_4 import *
from Test import *

"""Allows the user to choose what they want to do"""
if __name__ == '__main__':
  end = False
  while not end:
    print("Options:")
    print("1 - Run tests")
    print("2 - Manally play Connect 4")
    print("3 - Play against AI")
    print("4 - Play AI against itself")
    print("5 - Run AI's against each other with all depth combn 1-5")
    print("6 - Run 5 Ten Times")
    print("quit - Exit program")
    option = input("Select an Option: ")
    if option == "1":
      run_tests()
    elif option == "2":
      play_game(connect_4_board)
    elif option == "3":
      print('*Note that a number higher than 6 may take a while to load')
      depth = input('What depth should the AI run at? ')
      heruistic = input('Which Heuristic would you like to play against? ')
      play_against_AI(connect_4_board, int(depth), int(heruistic))
    elif option == "4":
      heruistic = input('Which Heuristic would you like the first AI to use? ')
      depth = input('What depth would you like the first AI to use? ')
      heruistic2 = input('Which Heuristic would you like the second AI to use? ') 
      depth2 = input('What depth would you like the second AI to use? ')
      print(play_AI_against_itself(connect_4_board, int(depth), int(depth2), int(heruistic), int(heruistic2)))
      reset_board()
    elif option == '5':
      h1 = input('h1: ')
      h2 = input('h2: ')
      test_ai(connect_4_board, int(h1), int(h2))
    elif option == '6':
      h1 = input('h1: ')
      h2 = input('h2: ')
      run_multiple_tests(connect_4_board, int(h1), int(h2))
    elif option == "quit":
      end = True
    else: 
      print("Choose a number 0-6")