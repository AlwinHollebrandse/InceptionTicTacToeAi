def play_move(player, localBoard, position):
    # print('player, localBoard, position:', player, localBoard, position)
    if localBoard[int(position/3)][position%3] == ' ':
        localBoard[int(position/3)][position%3] = player
        return position
    else:
        position = getInputAsValidNumber('That position is not empty, ya blockhead! Choose again (0 to 8): ', 8)
        return play_move(player, localBoard, position)

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

def computeGlobalState(entire_game_state):
    temp_global_game_state = [[' ',' ',' '],
                              [' ',' ',' '],
                              [' ',' ',' ']]
    for i in range(9):
        localWinner = check_current_state(entire_game_state[i])
        if localWinner != None:
            temp_global_game_state[int(i/3)][i%3] = localWinner

    return temp_global_game_state

def checkEntireBoardState(entire_game_state):
    temp_global_game_state = computeGlobalState(entire_game_state)
    return check_current_state(temp_global_game_state)

def copyLocalState(localBoard):
    temp_state = [[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]
    for i in range(9):
        temp_state[int(i/3)][i%3] = localBoard[int(i/3)][i%3]
    return temp_state

def copyEntireState(entire_game_state):
    return [copyLocalState(entire_game_state[i]) for i in range(9)]

def getAllBlankSpacesInLocalBoard(board):
    allBlankSpaces = []
    for i in range(9):
        if board[int(i/3)][i%3] == ' ':
            allBlankSpaces.append(i)
    return allBlankSpaces

def getAllLegalMoves(entire_game_state, localBoardIndex):
    allLegalMoves = []
    if localBoardIndex != None and check_current_state(entire_game_state[localBoardIndex]) == None:
        for i in getAllBlankSpacesInLocalBoard(entire_game_state[localBoardIndex]):
            allLegalMoves.append([i, localBoardIndex])

    else:
        for j in range(9):
            for i in getAllBlankSpacesInLocalBoard(entire_game_state[j]):
                allLegalMoves.append([i, j])

    return allLegalMoves

def getFirstAvailableBoard(entire_game_state):
    for i in range(9):
        if check_current_state(entire_game_state[i]) == None:
            return i
    return 999999 # TODO error

def fillAllLocalEmptySpaces(board):
    # return [['-' if x == ' ' else x for x in row] for row in board] # TODO this is a more pythonic version, but using it would mean changing the caller to replace the board passed here
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = '-'

def replaceAllUnavailableWithEmptySpaces(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = ' '

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
          str(entire_game_state[8][1][0]) + ' | ' + str(entire_game_state[8][1][1]) + ' | ' + str(entire_game_state[8][1][2]) + ' |')
    print('-----------------------------------------')
    print('| ' + str(entire_game_state[6][2][0]) + ' | ' + str(entire_game_state[6][2][1]) + ' | ' + str(entire_game_state[6][2][2]) + ' ||| ' +
          str(entire_game_state[7][2][0]) + ' | ' + str(entire_game_state[7][2][1]) + ' | ' + str(entire_game_state[7][2][2]) + ' ||| ' +
          str(entire_game_state[8][2][0]) + ' | ' + str(entire_game_state[8][2][1]) + ' | ' + str(entire_game_state[8][2][2]) + ' |')    
    print('-----------------------------------------')
    print('\n\n\n')

def getInputAsValidNumber(string, maxNumber):
    humanInput = input(string)
    try:
        if int(humanInput) not in range(9):
            raise Exception()
    except:
        print('Please enter a valid number (0-',maxNumber,'): ')
        return getInputAsValidNumber(string, maxNumber)
    return int(humanInput)

def getOpponent(player):
    if player == 'X':
        return 'O'
    return 'X'

def getMove(preMoveEntireBoard, postMoveEntireBoard):
    for localBoardIndex in range(9):
        for i in range(9):
            if preMoveEntireBoard[localBoardIndex][int(i/3)][i%3] != postMoveEntireBoard[localBoardIndex][int(i/3)][i%3]:
                return [i, localBoardIndex]
    print('ERROR no difference found')
    return None
    