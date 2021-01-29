# import numpy as np # TODO set up virtual env

global_game_state = [[' ',' ',' '],
                     [' ',' ',' '],
                     [' ',' ',' ']]

entire_game_state = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                     [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                     [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]
PLAYERS = ['X','O']

def play_move(player, localBoardIndex, position):
    if localBoardIndex[int((position)/3)][(position)%3] is ' ':
        localBoardIndex[int((position)/3)][(position)%3] = player
        return position
    else:
        position = getInputAsValidNumber('That position is not empty, ya blockhead! Choose again (0 to 8): ', 8)
        return play_move(player, localBoardIndex, position)
    
def check_current_state(board):    
    # Check horizontals
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] in ['X', 'O']):
        return board[0][0]
    if (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] in ['X', 'O']):
        return board[1][0]
    if (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] in ['X', 'O']):
        return board[2][0]
    
    # Check verticals
    if (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] in ['X', 'O']):
        return board[0][0]
    if (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] in ['X', 'O']):
        return board[0][1]
    if (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] in ['X', 'O']):
        return board[0][2]
    
    # Check diagonals
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] in ['X', 'O']):
        return board[1][1]
    if (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] in ['X', 'O']):
        return board[1][1]
    
    # Check if draw
    isDraw = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                isDraw = False
                break
    if isDraw:
        return '-'

    return None

def getInputAsValidNumber(string, maxNumber):
    humanInput = input(string)
    try:
        if int(humanInput) not in range(9):
            raise Exception()
    except:
        print('Please enter a valid number (0-',maxNumber,'): ')
        return getInputAsValidNumber(string, maxNumber)
    return int(humanInput)

def fillAllLocalEmptySpaces(board):
    print(board)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = '-'

def print_board(board):
    print('\n-------------')
    print('| ' + str(board[0][0]) + ' | ' + str(board[0][1]) + ' | ' + str(board[0][2]) + ' |')
    print('-------------')
    print('| ' + str(board[1][0]) + ' | ' + str(board[1][1]) + ' | ' + str(board[1][2]) + ' |')
    print('-------------')
    print('| ' + str(board[2][0]) + ' | ' + str(board[2][1]) + ' | ' + str(board[2][2]) + ' |')
    print('-------------')

def printEntireBoard(entire_game_state):
    # TODO refactor via for loop
    # Top 3 games
    print('\n-----------------------------------------')
    print('| ' + str(entire_game_state[0][0][0]) + ' | ' + str(entire_game_state[0][0][1]) + ' | ' + str(entire_game_state[0][0][2]) + ' ||| ' +
          str(entire_game_state[1][0][0]) + ' | ' + str(entire_game_state[1][0][1]) + ' | ' + str(entire_game_state[1][0][2]) + ' ||| ' +
          str(entire_game_state[2][0][0]) + ' | ' + str(entire_game_state[2][0][1]) + ' | ' + str(entire_game_state[2][0][2]) + ' |')
    print('-----------------------------------------')
    print('| ' + str(entire_game_state[0][1][0]) + ' | ' + str(entire_game_state[0][1][1]) + ' | ' + str(entire_game_state[0][1][2]) + ' ||| ' +
          str(entire_game_state[1][1][0]) + ' | ' + str(entire_game_state[1][1][1]) + ' | ' + str(entire_game_state[1][1][2]) + ' ||| ' +
          str(entire_game_state[2][1][0]) + ' | ' + str(entire_game_state[2][1][1]) + ' | ' + str(entire_game_state[2][1][2]) + ' |')
    print('-----------------------------------------')
    print('| ' + str(entire_game_state[0][2][0]) + ' | ' + str(entire_game_state[0][2][1]) + ' | ' + str(entire_game_state[0][2][2]) + ' ||| ' +
          str(entire_game_state[1][2][0]) + ' | ' + str(entire_game_state[1][2][1]) + ' | ' + str(entire_game_state[1][2][2]) + ' ||| ' +
          str(entire_game_state[2][2][0]) + ' | ' + str(entire_game_state[2][2][1]) + ' | ' + str(entire_game_state[2][2][2]) + ' |')    
    print('-----------------------------------------' +
        '\n-----------------------------------------')

    # Middle 3 games
    print('| ' + str(entire_game_state[3][0][0]) + ' | ' + str(entire_game_state[3][0][1]) + ' | ' + str(entire_game_state[3][0][2]) + ' ||| ' +
          str(entire_game_state[4][0][0]) + ' | ' + str(entire_game_state[4][0][1]) + ' | ' + str(entire_game_state[4][0][2]) + ' ||| ' +
          str(entire_game_state[5][0][0]) + ' | ' + str(entire_game_state[5][0][1]) + ' | ' + str(entire_game_state[5][0][2]) + ' |')
    print('-----------------------------------------')
    print('| ' + str(entire_game_state[3][1][0]) + ' | ' + str(entire_game_state[3][1][1]) + ' | ' + str(entire_game_state[3][1][2]) + ' ||| ' +
          str(entire_game_state[4][1][0]) + ' | ' + str(entire_game_state[4][1][1]) + ' | ' + str(entire_game_state[4][1][2]) + ' ||| ' +
          str(entire_game_state[5][1][0]) + ' | ' + str(entire_game_state[5][1][1]) + ' | ' + str(entire_game_state[5][1][2]) + ' |')
    print('-----------------------------------------')
    print('| ' + str(entire_game_state[3][2][0]) + ' | ' + str(entire_game_state[3][2][1]) + ' | ' + str(entire_game_state[3][2][2]) + ' ||| ' +
          str(entire_game_state[4][2][0]) + ' | ' + str(entire_game_state[4][2][1]) + ' | ' + str(entire_game_state[4][2][2]) + ' ||| ' +
          str(entire_game_state[5][2][0]) + ' | ' + str(entire_game_state[5][2][1]) + ' | ' + str(entire_game_state[5][2][2]) + ' |')    
    print('-----------------------------------------' +
        '\n-----------------------------------------')

    # Bottom 3 games
    print('| ' + str(entire_game_state[6][0][0]) + ' | ' + str(entire_game_state[6][0][1]) + ' | ' + str(entire_game_state[6][0][2]) + ' ||| ' +
          str(entire_game_state[7][0][0]) + ' | ' + str(entire_game_state[7][0][1]) + ' | ' + str(entire_game_state[7][0][2]) + ' ||| ' +
          str(entire_game_state[8][0][0]) + ' | ' + str(entire_game_state[8][0][1]) + ' | ' + str(entire_game_state[8][0][2]) + ' |')
    print('-----------------------------------------')
    print('| ' + str(entire_game_state[6][1][0]) + ' | ' + str(entire_game_state[6][1][1]) + ' | ' + str(entire_game_state[6][1][2]) + ' ||| ' +
          str(entire_game_state[7][1][0]) + ' | ' + str(entire_game_state[7][1][1]) + ' | ' + str(entire_game_state[7][1][2]) + ' ||| ' +
          str(entire_game_state[8][1][0]) + ' | ' + str(entire_game_state[2][1][1]) + ' | ' + str(entire_game_state[8][1][2]) + ' |')
    print('-----------------------------------------')
    print('| ' + str(entire_game_state[6][2][0]) + ' | ' + str(entire_game_state[6][2][1]) + ' | ' + str(entire_game_state[6][2][2]) + ' ||| ' +
          str(entire_game_state[7][2][0]) + ' | ' + str(entire_game_state[7][2][1]) + ' | ' + str(entire_game_state[7][2][2]) + ' ||| ' +
          str(entire_game_state[8][2][0]) + ' | ' + str(entire_game_state[8][2][1]) + ' | ' + str(entire_game_state[8][2][2]) + ' |')    
    print('-----------------------------------------')
    print('\n\n\n')

def main():
    availableLocalBoards = [i for i in range(9)]
    globalWinner = None
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
            localBoardIndex = int(input(str(PLAYERS[current_player_idx]) + "'s Turn! Choose which local board to place in (" + ', '.join(str(x) for x in availableLocalBoards) + "): ")) #TODO why doesnt *availableLocalBoards work?
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
        else:
            localBoardIndex = nextLocalBoard

        printEntireBoard(entire_game_state)
        globalWinner = check_current_state(global_game_state)
        if globalWinner == '-':
            print("Draw!")
        elif globalWinner is not None:
            print(str(globalWinner) + " won!")
        else:
            current_player_idx = (current_player_idx + 1)%2

if __name__ == '__main__':
    main()