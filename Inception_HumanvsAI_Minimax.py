# import numpy as np # TODO set up virtual env and pipenv-once there are dependencies
# TODO rename block_num to position?
# TODO BUG RecursionError: maximum recursion depth exceeded in comparison
# TODO maybe repurpose a python chess bot
# https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

players = ['X','O']
MAXDEPTH = 1

def play_move(player, localBoardIndex, block_num):
    if localBoardIndex[int((block_num)/3)][(block_num)%3] == ' ':
        localBoardIndex[int((block_num)/3)][(block_num)%3] = player
        return block_num
    else:
        block_num = int(input('Block != empty, ya blockhead! Choose again: '))
        return play_move(player, localBoardIndex, block_num)

def copy_entire_game_state(entire_game_state): # TODO add one for just global? TODO delte method when removing other minimax code
    new_entire_game_state = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                     [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                     [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                new_entire_game_state[i][j][k] = entire_game_state[i][j][k]
    return new_entire_game_state

def copy_global_game_state(board): # TODO keep?
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
            if board[i][j] == ' ':
                draw_flag = 1
    if draw_flag == 0:
        return '-'
    
    # Check horizontals
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != ' '):
        return board[0][0]
    if (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != ' '):
        return board[1][0]
    if (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != ' '):
        return board[2][0]
    
    # Check verticals
    if (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != ' '):
        return board[0][0]
    if (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != ' '):
        return board[0][1]
    if (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != ' '):
        return board[0][2]
    
    # Check diagonals
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' '):
        return board[1][1]
    if (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != ' '):
        return board[1][1]
    
    return None

def checkEntireBoardState(entire_game_state):
    print('checkEntireBoardState')
    printEntireBoard(entire_game_state)
    temp_global_game_state = [[' ',' ',' '],
                         [' ',' ',' '],
                         [' ',' ',' ']]
    for i in range(9):
        localWinner = check_current_state(entire_game_state[i])
        if localWinner != None:
            temp_global_game_state[int((i)/3)][(i)%3] = localWinner

    print('temp_global_game_state:')
    print_board(temp_global_game_state)
    return check_current_state(temp_global_game_state)

def getFirstAvailableBoard(entire_game_state):
    for i in range(9):
        if check_current_state(entire_game_state[i]) == None:
            return i
    return 999999 # TODO error

def fillAllLocalEmptySpaces(board):
    # return [['-' if x == ' ' else x for x in row] for row in board]

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = '-'
    # print(board)

def replaceAllUnavailableWithEmptySpaces(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = ' '

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

def getInputAsValidNumber(string):
    humanInput = input(string)
    try:
        if int(humanInput) not in range(9):
            raise Exception()
    except:
        print('Please enter a valid number (0-8): ')
        return getInputAsValidNumber(string)
    return int(humanInput)


# NOTE could be combined to a single method, that would be less readable but also less redundant
# TODO dont need global board as aparam
def max_alpha_beta(entire_game_state, localBoardIndex, alpha, beta, depth): # TODO limit iterations?-not super feasible. if not end has been reached, all moves willl be equally viable right?...so do random? or just best local move
    localBoardPlacedIn = getFirstAvailableBoard(entire_game_state)
    if check_current_state(entire_game_state[localBoardIndex]) != None:
        localBoardsToCheck = []
        for i in range(9):
            if check_current_state(entire_game_state[i]) == None:
                localBoardsToCheck.append(i)

    else:
        localBoardsToCheck = [localBoardIndex]
        localBoardPlacedIn = localBoardIndex

    print('max localBoardsToCheck: ', localBoardsToCheck)
    if depth >= MAXDEPTH:
        return (0, 0, localBoardPlacedIn)
    
    maxv = -2
    bestAIMaxLocalMove = None

    tempLocalWinner = check_current_state(entire_game_state[localBoardIndex])
    if tempLocalWinner in ['X', 'O', '-']:
        fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])

    result = checkEntireBoardState(entire_game_state)

    if result in ['X', 'O', '-']:
        print('max global winner, result: ', result, ', localBoardIndex: ', localBoardIndex, ', depth: ', depth)

    if result == 'X':
        return (-1, 0, localBoardPlacedIn)
    elif result == 'O':
        return (1, 0, localBoardPlacedIn)
    elif result == '-':
        return (0, 0, localBoardPlacedIn)

    depth += 1

    for localBoardIndex in localBoardsToCheck:
        for i in range(0, 3):
            for j in range(0, 3):
                if entire_game_state[localBoardIndex][i][j]  == ' ':
                    entire_game_state[localBoardIndex][i][j] = 'O'

                    print('max localBoardIndex: ' + str(localBoardIndex), ', new index: ', (i*3 + j), ', depth: ', depth)
                    printEntireBoard(entire_game_state)

                    (moveValue, bestAIMinLocalMove, bestAIMinLocalBoard) = min_alpha_beta(entire_game_state=entire_game_state, localBoardIndex=(i*3 + j), alpha=alpha, beta=beta, depth=depth) # TODO what if that next board is done?
                    if moveValue > maxv:
                        maxv = moveValue
                        bestAIMaxLocalMove = (i*3 + j)
                        localBoardPlacedIn = localBoardIndex

                    entire_game_state[localBoardIndex][i][j] = ' '
                    replaceAllUnavailableWithEmptySpaces(entire_game_state[localBoardIndex])

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if maxv >= beta:
                        return (maxv, bestAIMaxLocalMove, localBoardPlacedIn)

                    if maxv > alpha:
                        alpha = maxv

    return (maxv, bestAIMaxLocalMove, localBoardPlacedIn)

# TODO BUG when the ai returns the best place after choosing a new board, the board doesnt delete all the temp moves it made.
def min_alpha_beta(entire_game_state, localBoardIndex, alpha, beta, depth):
    localBoardPlacedIn = getFirstAvailableBoard(entire_game_state)
    if check_current_state(entire_game_state[localBoardIndex]) != None:
        localBoardsToCheck = []
        for i in range(9):
            if check_current_state(entire_game_state[i]) == None:
                localBoardsToCheck.append(i)

    else:
        localBoardsToCheck = [localBoardIndex]
        localBoardPlacedIn = localBoardIndex

    print('min localBoardsToCheck: ', localBoardsToCheck)
    if depth >= MAXDEPTH: # TODO make a variable depth depending on how many move options you have...ex you dont have to pick a whole new local board as well
        return (0, 0, localBoardPlacedIn)

    minv = 2

    bestAIMinLocalMove = None

    tempLocalWinner = check_current_state(entire_game_state[localBoardIndex])
    if tempLocalWinner in ['X', 'O', '-']:
        fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])

    result = checkEntireBoardState(entire_game_state)
    if result in ['X', 'O', '-']:
        print('min global winner, result: ', result, ', localBoardIndex: ', localBoardIndex, ', depth: ', depth)

    if result == 'X': # TODO somehow incoperate that giving the foe local wins is bad
        return (-1, 0, localBoardPlacedIn)
    elif result == 'O':
        return (1, 0, localBoardPlacedIn)
    elif result == '.':
        return (0, 0, localBoardPlacedIn)

    depth += 1

    for localBoardIndex in localBoardsToCheck:
        for i in range(0, 3):
            for j in range(0, 3):
                if entire_game_state[localBoardIndex][i][j]  == ' ':
                    entire_game_state[localBoardIndex][i][j] = 'X'

                    print('min localBoardIndex: ' + str(localBoardIndex), ', new index: ', (i*3 + j), ', depth: ', depth)
                    printEntireBoard(entire_game_state)

                    (moveValue, bestAIMaxLocalMove, bestAIMaxLocalBoard) = max_alpha_beta(entire_game_state=entire_game_state, localBoardIndex=(i*3 + j), alpha=alpha, beta=beta, depth=depth) # TODO if the local board is full, then the move will be on a different board
                    if moveValue < minv:
                        minv = moveValue
                        bestAIMinLocalMove = (i*3 + j)
                        localBoardPlacedIn = localBoardIndex
                    entire_game_state[localBoardIndex][i][j] = ' '
                    replaceAllUnavailableWithEmptySpaces(entire_game_state[localBoardIndex])

                    if minv <= alpha:
                        return (minv, bestAIMinLocalMove, localBoardPlacedIn)

                    if minv < beta:
                        beta = minv

    return (minv, bestAIMinLocalMove, localBoardPlacedIn)

def main():
    play_again = 'Y'
    while play_again.lower() == 'y':
        global_game_state = [[' ',' ',' '],
                            [' ',' ',' '],
                            [' ',' ',' ']]

        entire_game_state = [[['O',' ','X'],[' ','X',' '],['X',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [['O',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                            [['O',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                            [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]

        globalWinner = None

        print('\nNew Game!')
        printEntireBoard(entire_game_state)
        player_choice = input('Choose which player goes first - X(human) or O(MiniMax AI): ')
        if player_choice.lower() == 'x':
            current_player_idx = 0
        else:
            current_player_idx = 1
            
        if current_player_idx == 0: # human
            localBoardIndex = getInputAsValidNumber(str(players[current_player_idx]) + '\'s Turn! Choose which local board to place first (0 to 8): ')
        else: # ai
            localBoardIndex = 0

        while globalWinner == None:
            block_num = None
            localWinner = check_current_state(entire_game_state[localBoardIndex])
            if current_player_idx == 0: # Human's turn
                while localWinner != None:
                    localBoardIndex = getInputAsValidNumber(str(players[current_player_idx]) + '\'s Turn! Local board ' + str(localBoardIndex) + ' was unavailable. Choose which local board to place in: ')
                    localWinner = check_current_state(entire_game_state[localBoardIndex])
                block_num = getInputAsValidNumber(str(players[current_player_idx]) + '\'s Turn! localBoardIndex: ' + str(localBoardIndex) + '. Choose where to place (0 to 8): ')

            else: # AI's turn
                # block_num = getBestMove(entire_game_state, global_game_state, localBoardIndex, players[current_player_idx]) # Broken none pruning

                # if check_current_state(entire_game_state[localBoardIndex]) != None:
                #     localBoardIndex = None
                (m, block_num, localBoardIndex) = max_alpha_beta(entire_game_state=entire_game_state, localBoardIndex=localBoardIndex, alpha=-2, beta=2, depth=0)
                # TODO check if the ai is actually limited to current localBoardIndex when possible...
                # ai_Block_num = block_num # TODO is the %9 needed?
                # ai_localBoard = int(block_num / 9) # TODO need to check if this is a valid localBoardIndex
                # if localBoardIndex == None:
                #     localBoardIndex = int(block_num / 9)
                # localBoardIndex = ai_localBoard
                print('m: ', m, ', ai_Block_num: ', block_num, ', ai_localBoard: ', localBoardIndex)

            print('current_player_idx: ' , current_player_idx, ', localBoardIndex: ', localBoardIndex) # TODO BUG current bug is that the ai always returns 0
            nextLocalBoard = play_move(players[current_player_idx], entire_game_state[localBoardIndex], block_num)
            localWinner = check_current_state(entire_game_state[localBoardIndex])
            if localWinner != None:
                print('localWinner: ' + str(localWinner))
                # availableLocalBoards.remove(localBoardIndex) # TODO update all available boards...
                fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])
                global_game_state[int((localBoardIndex)/3)][(localBoardIndex)%3] = localWinner
                print_board(global_game_state)

            if current_player_idx == 1: # ai
                printEntireBoard(entire_game_state)
                print('ai placed at localBoardIndex: ' + str(localBoardIndex) + ', position: ' + str(block_num)) # TODO bug always prints localBoardIndex = 0, and always places at 0? also cant handle picking a new localBoardIndex
            
            localBoardIndex = nextLocalBoard
            globalWinner = check_current_state(global_game_state)
            if globalWinner == '-':
                print('Draw!')
            elif globalWinner != None:
                print(str(globalWinner) + ' won!')
            else:
                current_player_idx = (current_player_idx + 1)%2
                
        play_again = input('Wanna try again?(Y/N) : ')
        if play_again == 'N':
            print('GG!')
    
if __name__ == '__main__':
    main()




# TODO BUG
# with this board state, humna just won board 1 by placing in 6. But ai then placed in board 2 which isnt allowed
# -----------------------------------------
# | O | - | X ||| O | O | X ||| O | O |   |
# -----------------------------------------
# | - | X | - ||| O | X | O |||   |   |   |
# -----------------------------------------
# | X | - | - ||| X | - | - ||| X |   |   |
# -----------------------------------------
# -----------------------------------------
# | O | X |   ||| O | X | O |||   |   |   |
# -----------------------------------------
# |   |   |   ||| - | X | - |||   |   |   |
# -----------------------------------------
# |   |   |   ||| - | X | - |||   | X |   |
# -----------------------------------------
# -----------------------------------------
# | O |   |   ||| O |   |   |||   |   |   |
# -----------------------------------------
# |   |   |   |||   |   |   |||   |   |   |
# -----------------------------------------
# | O |   |   |||   |   |   |||   |   |   |
# -----------------------------------------

# ai placed at localBoardIndex: 2, position: 2

# resulted in board state: Note the '-' in board 8
# -----------------------------------------
# | O | - | X ||| O | O | X ||| O | O | O |
# -----------------------------------------
# | - | X | - ||| O | X | O ||| - | - | - |
# -----------------------------------------
# | X | - | - ||| X | - | - ||| X | - | - |
# -----------------------------------------
# -----------------------------------------
# | O | X |   ||| O | X | O |||   |   |   |
# -----------------------------------------
# |   |   |   ||| - | X | - |||   |   |   |
# -----------------------------------------
# |   |   |   ||| - | X | - |||   | X |   |
# -----------------------------------------
# -----------------------------------------
# | O |   |   ||| O |   |   |||   |   |   |
# -----------------------------------------
# |   |   |   |||   |   |   |||   | - |   |
# -----------------------------------------
# |   |   |   |||   |   |   |||   |   |   |
# -----------------------------------------




















'''
Minimax Algorithm
'''
def getBestMove(entire_game_state, global_game_state, localBoardIndex, player):
    global_winner_loser = check_current_state(global_game_state)
    if global_winner_loser == 'O': # If AI won
        return 1
    elif global_winner_loser == 'X': # If Human won
        return -1
    elif global_winner_loser == '-':    # Draw condition
        return 0
        
    moves = []
    empty_cells = []
    localWinner = check_current_state(entire_game_state[localBoardIndex])
    
    # if the given local board is alreday completed, check all global moves
    if localWinner != None:
        for currentLocalBoard in range(9):
            if global_game_state[int((currentLocalBoard)/3)][(currentLocalBoard)%3] == ' ':
                for i in range(3):
                    for j in range(3):
                        if entire_game_state[currentLocalBoard][i][j] == ' ':
                            empty_cells.append(currentLocalBoard * 9 + (i*3 + j))

    else: # if the local board has a valid move, check all local moves
        for i in range(3):
            for j in range(3):
                if entire_game_state[localBoardIndex][i][j] == ' ':
                    empty_cells.append(localBoardIndex * 9 + (i*3 + j))
    
    for empty_cell in empty_cells:
        move = {}
        move['index'] = empty_cell
        new_entire_game_state = copy_entire_game_state(entire_game_state)
        new_global_game_state = copy_global_game_state(global_game_state)
        temp_block_num = empty_cell % 9
        temp_localBoard = int(empty_cell / 9)
        play_move(player, new_entire_game_state[temp_localBoard], temp_block_num)

        if player == 'O':    # If AI
            # make more depth tree for human
            result = getBestMove(new_entire_game_state, new_global_game_state, temp_localBoard, 'X')
            move['score'] = result
        else:
            # make more depth tree for AI
            result = getBestMove(new_entire_game_state, new_global_game_state, temp_localBoard, 'O')
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