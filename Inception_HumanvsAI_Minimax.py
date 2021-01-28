# import numpy as np # TODO set up virtual env and pipenv-once there are dependencies
# https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

PLAYERS = ['X','O']
MAXDEPTH = 5
# TODO set alpha = minMoveValue and best=maxMoveValue

def play_move(player, localBoardIndex, position):
    if localBoardIndex[int(position/3)][position%3] == ' ':
        localBoardIndex[int(position/3)][position%3] = player
        return position
    else:
        position = int(input('Block != empty, ya blockhead! Choose again: '))
        return play_move(player, localBoardIndex, position)

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

def checkEntireBoardState(entire_game_state):
    # print('checkEntireBoardState')
    # printEntireBoard(entire_game_state)
    temp_global_game_state = [[' ',' ',' '],
                         [' ',' ',' '],
                         [' ',' ',' ']]
    for i in range(9):
        localWinner = check_current_state(entire_game_state[i])
        if localWinner != None:
            temp_global_game_state[int(i/3)][i%3] = localWinner

    # print('temp_global_game_state:')
    # print_board(temp_global_game_state)
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

def getOpponent(player):
    if player == 'X':
        return 'O'
    return 'X'

def blocksLocalWin(board, player, i, j):
    opponent = getOpponent(player)
    board[i][j] = opponent
    blocked = False
    if check_current_state(board) == opponent:
        blocked = True
    board[i][j] = player
    return blocked, player

def blocksGlobalWin(entire_game_state, player, localBoardIndex):
    temp_global_game_state = [[' ',' ',' '],
                         [' ',' ',' '],
                         [' ',' ',' ']]
    for i in range(9):
        localWinner = check_current_state(entire_game_state[i])
        if localWinner != None:
            temp_global_game_state[int(i/3)][i%3] = localWinner

    return blocksLocalWin(temp_global_game_state, player, int(localBoardIndex/3), localBoardIndex%3)

def optimizeMove(player, entire_game_state, localBoardIndex, moveValue, depth, difficulty, alpha, beta): # TODO limit iterations?-not super feasible. if not end has been reached, all moves willl be equally viable right?...so do random? or just best local move
    print(player, ', init  localBoardIndex: ' + str(localBoardIndex), ', moveValue: ', moveValue, ', depth: ', depth)
    localBoardPlacedIn = getFirstAvailableBoard(entire_game_state)
    if check_current_state(entire_game_state[localBoardIndex]) != None:
        localBoardsToCheck = []
        for i in range(9):
            if check_current_state(entire_game_state[i]) == None:
                localBoardsToCheck.append(i)

    else:
        localBoardsToCheck = [localBoardIndex]
        localBoardPlacedIn = localBoardIndex
    
    maxMoveValue = -100 # TODO combine into 1 var if possible
    minMoveValue = 100

    bestAILocalMove = None # TODO BUG could technically return None and break

    result = checkEntireBoardState(entire_game_state)

    if result in ['X', 'O', '-']:
        print(player, ', global winner, result: ', result, ', localBoardIndex: ', localBoardIndex, ', depth: ', depth)

    if result == 'X':
        return (moveValue-31, 0, localBoardPlacedIn)
    elif result == 'O':
        return (moveValue+30, 0, localBoardPlacedIn)
    elif result == '-':
        return (moveValue, 0, localBoardPlacedIn)

    if depth >= MAXDEPTH:
        return (moveValue, 0, localBoardPlacedIn)

    depth += 1

    for localBoardIndex in localBoardsToCheck:
        for i in range(0, 3):
            for j in range(0, 3):
                if entire_game_state[localBoardIndex][i][j]  == ' ':
                    entire_game_state[localBoardIndex][i][j] = player

                    print(player, ' placed at localBoardIndex: ' + str(localBoardIndex), ', location: ', (i*3 + j), ', depth: ', depth)

                    tempMoveValue = moveValue
                    tempLocalWinner = check_current_state(entire_game_state[localBoardIndex])
                    if tempLocalWinner in ['X', 'O', '-']:
                        fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])

                    if difficulty >= 2:
                        scoreChange = 2
                        if localBoardIndex in [0,2,6,8]: # in corner board
                            scoreChange += .5
                        elif localBoardIndex in [4]: # in center board
                            scoreChange += 1
                        if tempLocalWinner == 'X':
                            tempMoveValue -= scoreChange
                        elif tempLocalWinner == 'O':
                            tempMoveValue += scoreChange
                    if difficulty >= 2 and tempLocalWinner == None: # TODO do the same but for global moves
                        (blocked, player) = blocksLocalWin(entire_game_state[localBoardIndex], player, i, j)
                        if blocked and player == 'X':
                            tempMoveValue -= 1
                        elif blocked and player == 'O':
                            tempMoveValue += 1
                    if difficulty >= 3: # TODO do the same but for global moves # TODO also add reward for getting 1 away from a win
                        (blocked, player) = blocksGlobalWin(entire_game_state, player, localBoardIndex)
                        if blocked and player == 'X':
                            tempMoveValue -= 1
                        elif blocked and player == 'O':
                            tempMoveValue += 1  
                    if difficulty >= 4: # TODO also reward geeting 1 away from a win, but less than a local win and punish for letting the human get 2 in a winning row
                        tempMoveValue += 0
                    # TODO get more points for taking more useful psotions in local boards?

                    # printEntireBoard(entire_game_state)

                    (resultMoveValue, bestNextAILocalMove, bestAILocalBoardPlacedIn) = optimizeMove(player=getOpponent(player), entire_game_state=entire_game_state, localBoardIndex=(i*3 + j), moveValue=tempMoveValue, depth=depth, difficulty=difficulty, alpha=alpha, beta=beta)

                    if player == 'O' and resultMoveValue > maxMoveValue:
                        maxMoveValue = resultMoveValue
                        bestAILocalMove = (i*3 + j)
                        localBoardPlacedIn = localBoardIndex
                        # print('HERE MAX', 'resultMoveValue:', resultMoveValue, 'maxMoveValue:', maxMoveValue, 'bestAILocalMove:', bestAILocalMove, 'depth:',depth)
                    elif player == 'X' and resultMoveValue < minMoveValue:
                        minMoveValue = resultMoveValue
                        bestAILocalMove = (i*3 + j)
                        localBoardPlacedIn = localBoardIndex
                        # print('HERE MIN', 'resultMoveValue:', resultMoveValue, 'minMoveValue:', minMoveValue, 'bestAILocalMove:', bestAILocalMove, 'depth:',depth)

                    entire_game_state[localBoardIndex][i][j] = ' '
                    replaceAllUnavailableWithEmptySpaces(entire_game_state[localBoardIndex])

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if player == 'O':
                        if maxMoveValue >= beta:
                            print('HERE maxMoveValue:',maxMoveValue,'beta:',beta)
                            return (maxMoveValue, bestAILocalMove, localBoardPlacedIn)

                        if maxMoveValue > alpha:
                            alpha = maxMoveValue

                    elif player == 'X':
                        if minMoveValue <= alpha:
                            print('HERE minMoveValue:',minMoveValue,'alpha:',alpha)
                            return (minMoveValue, bestAILocalMove, localBoardPlacedIn)

                        if minMoveValue < beta:
                            beta = minMoveValue
   
    # print(player, 'RETURN FINAL maxMoveValue:', maxMoveValue, 'minMoveValue:', minMoveValue, 'bestAILocalMove:',bestAILocalMove, 'depth:',depth)
    if player == 'O': # ai's optimal move value
        # print(player, 'RETURN maxMoveValue:', maxMoveValue, 'bestAILocalMove:',bestAILocalMove, 'depth:',depth)
        return (maxMoveValue, bestAILocalMove, localBoardPlacedIn)
    else: # human's optimal move value
        # print(player, 'RETURN minMoveValue:', minMoveValue, 'bestAILocalMove:',bestAILocalMove, 'depth:',depth)
        return (minMoveValue, bestAILocalMove, localBoardPlacedIn)

def main():
    play_again = 'Y'
    difficulty = 3
    while play_again.lower() == 'y':
        global_game_state = [[' ',' ',' '],
                            [' ',' ',' '],
                            [' ',' ',' ']]

        entire_game_state = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                            [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
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
            localBoardIndex = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! Choose which local board to place first (0 to 8): ')
        else: # ai
            localBoardIndex = 0

        while globalWinner == None:
            position = None
            localWinner = check_current_state(entire_game_state[localBoardIndex])
            if current_player_idx == 0: # Human's turn
                while localWinner != None:
                    localBoardIndex = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! Local board ' + str(localBoardIndex) + ' was unavailable. Choose which local board to place in: ')
                    localWinner = check_current_state(entire_game_state[localBoardIndex])
                position = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! localBoardIndex: ' + str(localBoardIndex) + '. Choose where to place (0 to 8): ')

            else: # AI's turn
                # (maxMoveValue, position, localBoardIndex) = max_alpha_beta(entire_game_state=entire_game_state, localBoardIndex=localBoardIndex, moveValue=0, depth=0, difficulty=difficulty, alpha=-100, beta=100)
                (maxMoveValue, position, localBoardIndex) = optimizeMove(player='O', entire_game_state=entire_game_state, localBoardIndex=localBoardIndex, moveValue=0, depth=0, difficulty=difficulty, alpha=-100, beta=100)
                print('maxMoveValue: ', maxMoveValue, ', ai_Block_num: ', position, ', ai_localBoard: ', localBoardIndex)

            print('current_player_idx: ' , current_player_idx, ', localBoardIndex: ', localBoardIndex) # TODO BUG current bug is that the ai always returns 0
            nextLocalBoard = play_move(PLAYERS[current_player_idx], entire_game_state[localBoardIndex], position)
            localWinner = check_current_state(entire_game_state[localBoardIndex])
            if localWinner != None:
                print('localWinner: ' + str(localWinner))
                # availableLocalBoards.remove(localBoardIndex) # TODO update all available boards...
                fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])
                global_game_state[int(localBoardIndex/3)][localBoardIndex%3] = localWinner
                print_board(global_game_state)

            if current_player_idx == 1: # ai
                printEntireBoard(entire_game_state)
                print('ai placed at localBoardIndex: ' + str(localBoardIndex) + ', position: ' + str(position)) # TODO bug always prints localBoardIndex = 0, and always places at 0? also cant handle picking a new localBoardIndex
            
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

# TODO BUG visual?
# -----------------------------------------
# | X | O | X ||| - | X | O |||   | O | X |
# -----------------------------------------
# |   |   | O ||| - | X | - ||| O |   |   |
# -----------------------------------------
# |   |   | X ||| - | X | - ||| O | X | X |
# -----------------------------------------
# -----------------------------------------
# | O |   |   |||   |   | O ||| X |   | X |
# -----------------------------------------
# | X | O | X ||| O | X |   ||| O |   |   |
# -----------------------------------------
# | X |   | X |||   | X |   ||| X |   |   |
# -----------------------------------------
# -----------------------------------------
# |   |   |   |||   | O | O ||| O | - | - |
# -----------------------------------------
# | X | O | O |||   |   | O ||| O |   | - |
# -----------------------------------------
# |   |   |   |||   |   |   ||| O | - | - |
# -----------------------------------------

# human went 3,8
# ai went in 8,6, to get the local win, but then the center piece istn a '-',
# but i think its purely visual. because i made him move in board 8 again, and he went in board 7 like he picked