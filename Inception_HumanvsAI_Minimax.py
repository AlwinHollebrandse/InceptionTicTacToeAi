# import numpy as np # TODO set up virtual env
# TODO rename localBoard to localBoardIndex?
# TODO rename block_num to position

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

def copy_entire_game_state(entire_board): # TODO add one for just global?
    new_entire_game_state = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                     [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                     [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                new_entire_game_state[i][j][k] = entire_board[i][j][k]
    return new_entire_game_state

def copy_global_game_state(board): # TODO add one for just global?
    new_global_game = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range(3):
        for j in range(3):
            new_global_game[i][j] = board[i][j]
    return new_global_game
    
def check_current_state(board):
    # Check if draw
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return None, "Draw"
    
    # Check horizontals
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] is not ' '):
        return board[0][0], "Done"
    if (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] is not ' '):
        return board[1][0], "Done"
    if (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] is not ' '):
        return board[2][0], "Done"
    
    # Check verticals
    if (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] is not ' '):
        return board[0][0], "Done"
    if (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] is not ' '):
        return board[0][1], "Done"
    if (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] is not ' '):
        return board[0][2], "Done"
    
    # Check diagonals
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not ' '):
        return board[1][1], "Done"
    if (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] is not ' '):
        return board[1][1], "Done"
    
    return None, "Not Done"

def fillAllLocalEmptySpaces(board):
    print(board)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = '-'

def print_board(board): # TODO is a local board print needed?
    print('\n--------------')
    print('| ' + str(board[0][0]) + ' | ' + str(board[0][1]) + ' | ' + str(board[0][2]) + ' |')
    print('-------------')
    print('| ' + str(board[1][0]) + ' | ' + str(board[1][1]) + ' | ' + str(board[1][2]) + ' |')
    print('-------------')
    print('| ' + str(board[2][0]) + ' | ' + str(board[2][1]) + ' | ' + str(board[2][2]) + ' |')
    print('-------------')

def printEntireBoard():
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
global_current_state = "Not Done"
availableLocalBoards = [i for i in range(9)]
globalWinner = None
print("New Game!")
printEntireBoard()
player_choice = input("Choose which player goes first - X or O: ")
if player_choice.lower() == 'x':
    current_player_idx = 0
else:
    current_player_idx = 1

localBoard = int(input(str(players[current_player_idx]) + "'s Turn! Choose which local board to place first (0 to 8): "))
while global_current_state == "Not Done":
    localWinner, local_current_state = check_current_state(entire_game_state[localBoard])
    # print_board(entire_game_state[localBoard])
    while local_current_state != "Not Done":
        localBoard = int(input(str(players[current_player_idx]) + "'s Turn! Choose which local board to place in (" + ', '.join(str(x) for x in availableLocalBoards) + "): ")) #TODO why doesnt *availableLocalBoards work?
        localWinner, local_current_state = check_current_state(entire_game_state[localBoard])

    block_num = int(input(str(players[current_player_idx]) + "'s Turn! LocalBoard: " + str(localBoard) + ". Choose where to place (0 to 8): ")) # TODO only show valid moves
    nextLocalBoard = play_move(players[current_player_idx], entire_game_state[localBoard], block_num)
    localWinner, local_current_state = check_current_state(entire_game_state[localBoard])
    if local_current_state != "Not Done":
        print("localWinner: " + str(localWinner))
        availableLocalBoards.remove(localBoard)
        fillAllLocalEmptySpaces(entire_game_state[localBoard])
        global_game_state[int((localBoard)/3)][(localBoard)%3] = localWinner
        print_board(global_game_state)
    else:
        localBoard = nextLocalBoard

    printEntireBoard()
    globalWinner, global_current_state = check_current_state(global_game_state)
    if globalWinner is not None:
        print(str(globalWinner) + " won!")
    else:
        current_player_idx = (current_player_idx + 1)%2
    
    if global_current_state is "Draw":
        print("Draw!")




def getBestMove(entire_game_state, global_game_state, localBoard, player):
    '''
    Minimax Algorithm
    '''
    global_winner_loser, done = check_current_state(global_game_state)
    if done == "Done" and global_winner_loser == 'O': # If AI won
        return 1
    elif done == "Done" and global_winner_loser == 'X': # If Human won
        return -1
    elif done == "Draw":    # Draw condition
        return 0
        
    moves = []
    empty_cells = {}
    localWinner, local_current_state = check_current_state(entire_game_state[localBoard])
    
    # if the given local board is alreday completed, check all global moves
    if local_current_state != "Not Done":
        for currentLocalBoard in range(9):
            if global_game_state[int((currentLocalBoard)/3)][(currentLocalBoard)%3] is ' ':
                empty_cells[currentLocalBoard] = []
                for i in range(3):
                    for j in range(3):
                        if entire_game_state[currentLocalBoard][i][j] is ' ':
                            empty_cells[currentLocalBoard].append(i*3 + j)

    else: # if the local board has a valid move, check all local moves
        empty_cells[localBoard] = []
        for i in range(3):
            for j in range(3):
                if entire_game_state[localBoard][i][j] is ' ':
                    empty_cells[localBoard].append(i*3 + j)
    
    for empty_cell in [currentLocalBoard in empty_cells]: # TODO check formatting/ fucntionality
        move = {}
        move['index'] = {}
        move['index']['localBoard'] = currentLocalBoard
        move['index']['block_num'] = empty_cell
        new_entire_game_state = copy_entire_game_state(entire_game_state)
        new_global_game_state = copy_global_game_state(global_game_state)
        play_move(new_entire_game_state[currentLocalBoard], player, empty_cell)

        if player == 'O':    # If AI
            # make more depth tree for human
            result = getBestMove(new_entire_game_state, new_global_game_state, currentLocalBoard, 'X')
            move['score'] = result
        else:
            # make more depth tree for AI
            result = getBestMove(new_entire_game_state, new_global_game_state, currentLocalBoard, 'O')
            move['score'] = result
        
        moves.append(move)

    # Find best move
    best_move = None
    if player == 'O':   # If AI player
        best = -infinity
        for move in moves:
            if move['score'] > best:
                best = move['score']
                best_move = move['index']
    else:
        best = infinity
        for move in moves:
            if move['score'] < best:
                best = move['score']
                best_move = move['index']
                
    return best_move

# Playing
play_again = 'Y'
while play_again == 'Y' or play_again == 'y':
    game_state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
    current_state = "Not Done"
    print("\nNew Game!")
    print_board(game_state)
    player_choice = input("Choose which player goes first - X (You - the petty human) or O(The mighty AI): ")
    winner = None
    
    if player_choice == 'X' or player_choice == 'x':
        current_player_idx = 0
    else:
        current_player_idx = 1
        
    while current_state == "Not Done":
        if current_player_idx == 0: # Human's turn
            block_choice = int(input("Oye Human, your turn! Choose where to place (1 to 9): "))
            play_move(game_state ,players[current_player_idx], block_choice)
        else:   # AI's turn
            block_choice = getBestMove(game_state, players[current_player_idx])
            play_move(game_state ,players[current_player_idx], block_choice)
            print("AI plays move: " + str(block_choice))
        print_board(game_state)
        winner, current_state = check_current_state(game_state)
        if winner is not None:
            print(str(winner) + " won!")
        else:
            current_player_idx = (current_player_idx + 1)%2
        
        if current_state is "Draw":
            print("Draw!")
            
    play_again = input('Wanna try again?(Y/N) : ')
    if play_again == 'N':
        print('GG!')
    
