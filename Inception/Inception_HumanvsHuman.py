# import numpy as np # TODO set up virtual env
from HelperFunctions import *

PLAYERS = ['X','O']

def main():
    play_again = 'Y'
    while play_again.lower() == 'y':
        availableLocalBoards = [i for i in range(9)]

        entire_game_state = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                     [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                     [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]

        global_game_state = computeGlobalState(entire_game_state)
        globalWinner = check_current_state(global_game_state)
        
        print("New Game!")
        printEntireBoard(entire_game_state)
        player_choice = input("Choose which player goes first - X or O: ")
        if player_choice.lower() == 'x':
            current_player_idx = 0
        else:
            current_player_idx = 1

        localBoardIndex = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! Choose which local board to place first (0 to 8): ', 8)
        while globalWinner == None:
            localWinner = check_current_state(entire_game_state[localBoardIndex])
            while localWinner is not None:
                localBoardIndex = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! Local board ' + str(localBoardIndex) + ' was unavailable. Choose which local board to place in: ', 8)
                localWinner = check_current_state(entire_game_state[localBoardIndex])

            position = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! localBoardIndex: ' + str(localBoardIndex) + '. Choose where to place (0 to 8): ', 8)
            nextLocalBoard = play_move(PLAYERS[current_player_idx], entire_game_state[localBoardIndex], position)
            localWinner = check_current_state(entire_game_state[localBoardIndex])
            if localWinner is not None:
                print("localWinner: " + str(localWinner))
                availableLocalBoards.remove(localBoardIndex)
                fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])
                global_game_state[int((localBoardIndex)/3)][(localBoardIndex)%3] = localWinner
                print_board(global_game_state)

            printEntireBoard(entire_game_state)
            localBoardIndex = nextLocalBoard
            globalWinner = check_current_state(global_game_state)
            if globalWinner == '-':
                print("Draw!")
            elif globalWinner is not None:
                print(str(globalWinner) + " won!")
            else:
                current_player_idx = (current_player_idx + 1)%2
        play_again = input('Wanna try again?(Y/N): ')
        if play_again == 'N':
            print('GG!')

if __name__ == '__main__':
    main()
