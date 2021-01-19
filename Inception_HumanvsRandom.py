# import numpy as np # TODO set up virtual env
import random

global_game_state = [[' ',' ',' '],
                     [' ',' ',' '],
                     [' ',' ',' ']]

entire_game_state = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                     [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                     [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]
players = ['X','O']

def play_move(player, localBoard, block_num):
    if localBoard[int((block_num)/3)][(block_num)%3] is ' ':
        localBoard[int((block_num)/3)][(block_num)%3] = player
        return block_num
    else:
        block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
        return play_move(player, localBoard, block_num)
    
    
def check_current_state(board):
    # Check if draw
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return 'Draw'
    
    # Check horizontals
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] is not ' '):
        return board[0][0]
    if (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] is not ' '):
        return board[1][0]
    if (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] is not ' '):
        return board[2][0]
    
    # Check verticals
    if (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] is not ' '):
        return board[0][0]
    if (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] is not ' '):
        return board[0][1]
    if (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] is not ' '):
        return board[0][2]
    
    # Check diagonals
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not ' '):
        return board[1][1]
    if (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] is not ' '):
        return board[1][1]
    
    return None

def getAvailableLocalMoves(board):
    availableMoves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is ' ':
                availableMoves.append(i*3 + (j))
    print(availableMoves)
    return availableMoves

def fillAllLocalEmptySpaces(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = '-'

def print_board(board): # TODO is a local board print needed?
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

# Playing
availableLocalBoards = [i for i in range(9)]
globalWinner = ai_localBoard = ai_Block_num = None
print("New Game!")
printEntireBoard(entire_game_state)
player_choice = input("Choose which player goes first - X(human) or O(\"ai\"): ")
if player_choice.lower() == 'x':
    current_player_idx = 0
else:
    current_player_idx = 1

if current_player_idx == 0: # human
    localBoard = int(input(str(players[current_player_idx]) + "'s Turn! Choose which local board to place first (0 to 8): "))
else: # ai
    localBoard = random.choice(availableLocalBoards)

while globalWinner == None:
    localWinner = check_current_state(entire_game_state[localBoard])
    # print_board(entire_game_state[localBoard])
    while localWinner is not None: # TODO add check to ensure person's value is 0-8 (see minimax)
        if current_player_idx == 0: # human
            localBoard = int(input(str(players[current_player_idx]) + "'s Turn! Choose which local board to place in (" + ', '.join(str(x) for x in availableLocalBoards) + "): ")) #TODO why doesnt *availableLocalBoards work?
            localWinner = check_current_state(entire_game_state[localBoard])
        else: # ai
            localBoard = random.choice(availableLocalBoards)
            localWinner = check_current_state(entire_game_state[localBoard])

    if current_player_idx == 0: # human # TODO add check to ensure person's value is 0-8 (see minimax)
        block_num = int(input(str(players[current_player_idx]) + "'s Turn! LocalBoard: " + str(localBoard) + ". Choose where to place (0 to 8): ")) # TODO only show valid moves
    else: # ai
        block_num = random.choice(getAvailableLocalMoves(entire_game_state[localBoard]))
        ai_Block_num = block_num
        ai_localBoard = localBoard
    
    nextLocalBoard = play_move(players[current_player_idx], entire_game_state[localBoard], block_num)
    localWinner = check_current_state(entire_game_state[localBoard])
    if localWinner is not None:
        print("localWinner: " + str(localWinner))
        availableLocalBoards.remove(localBoard)
        fillAllLocalEmptySpaces(entire_game_state[localBoard])
        global_game_state[int((localBoard)/3)][(localBoard)%3] = localWinner
        print_board(global_game_state)
    else:
        localBoard = nextLocalBoard

    if current_player_idx == 1: # ai
        printEntireBoard(entire_game_state)
        print("ai placed at localBoard: " + str(ai_localBoard) + ", position: " + str(ai_Block_num))
        
    globalWinner = check_current_state(global_game_state)
    if globalWinner == '-':
        print("Draw!")
    elif globalWinner is not None:
        print(str(globalWinner) + " won!")
    else:
        current_player_idx = (current_player_idx + 1)%2
    
    

# TODO skipped me on turn 1... ai has 2 prints...but one wasnt actauly "there"...its a print bug
# TODO I got to go twice BUG - could also be print bug. havent seen it again
# TODO it skipped my placement...related to above bug?...but I cant place there after, so non empty? - BUG doesnt print all