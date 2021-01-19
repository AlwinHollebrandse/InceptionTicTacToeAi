# import numpy as np # TODO set up virtual env
# TODO rename localBoard to localBoardIndex when needed for clarity
# TODO rename block_num to position?
# TODO BUG RecursionError: maximum recursion depth exceeded in comparison
# TODO maybe repurpose a python chess bot
# TODO BUG pruning minimax breaks when theres a local winner found...probably something with picking the new local board
# https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

players = ['X','O']

def play_move(player, localBoard, block_num):
    if localBoard[int((block_num)/3)][(block_num)%3] is ' ':
        localBoard[int((block_num)/3)][(block_num)%3] = player
        return block_num
    else:
        block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
        return play_move(player, localBoard, block_num)

def copy_entire_game_state(entire_game_state): # TODO add one for just global?
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
            if board[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return '-'
    
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

def checkEntireBoardState(entire_game_state):
    temp_global_game_state = [[' ',' ',' '],
                         [' ',' ',' '],
                         [' ',' ',' ']]
    for i in range(9):
        localWinner = check_current_state(entire_game_state[i])
        if localWinner != None:
            temp_global_game_state[int((i)/3)][(i)%3] = localWinner

    return check_current_state(temp_global_game_state)  

def fillAllLocalEmptySpaces(board):
    print(board)
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

# # TODO right now this uses a heuristc that returns the local board has the most O's in it out of the available boards. This should use the minmax too
# def findBestLocalBoard(entire_game_state):


# NOTE could be combined to a single method, that would be less readable but also less redundant
def max_alpha_beta(entire_game_state, localBoardIndex, alpha, beta, depth): # TODO limit iterations?-not super feasible. if not end has been reached, all moves willl be equally viable right?...so do random? or just best local move
    if localBoardIndex == None:
        localBoardsToCheck = []
        for i in range(9):
            if check_current_state(entire_game_state[i]) == None:
                localBoardsToCheck.append(i)

    else:
        localBoardsToCheck = [localBoardIndex]
    

    
    maxv = -2
    # px = None
    # py = None
    bestAIMaxLocalMove = None

    # result = check_current_state(entire_game_state[localBoard]) # TODO use local or global? ideally, global, but local is easier to start with

    result = checkEntireBoardState(entire_game_state)

    # print('max result: ' + str(result))
    # if result in ['X', 'O', '-']:
    #     print('max winner')
    # print('max depth: ', depth)

    if result == 'X':
        return (-1, 0)
    elif result == 'O':
        return (1, 0)
    elif result == '-':
        return (0, 0)

    depth += 1

    for localBoardIndex in localBoardsToCheck:
        for i in range(0, 3): # TODO this only checks local board rn... convert to ultimate
            for j in range(0, 3):
                if entire_game_state[localBoardIndex][i][j]  == ' ': # self.current_state[i][j] == ' ': # TODO ensure that a filled local Board wont be seen here. ie have to check for '-'
                    # self.current_state[i][j] = 'O'
                    entire_game_state[localBoardIndex][i][j] = 'O'
                    # print('max localBoard: ' + str(localBoardIndex))
                    # print('past max')
                    (moveValue, bestAIMinLocalMove) = min_alpha_beta(entire_game_state, (i*3 + j), alpha, beta, depth) # TODO what if that next board is done?
                    if moveValue > maxv:
                        maxv = moveValue
                        # px = i # TODO what are px and py
                        # py = j
                        bestAIMaxLocalMove = (i*3 + j)
                    # self.current_state[i][j] = ' '
                    entire_game_state[localBoardIndex][i][j] = ' '

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if maxv >= beta:
                        # print('max here')
                        return (maxv, bestAIMaxLocalMove) # px, py)

                    if maxv > alpha:
                        alpha = maxv

    # print('max2 here')
    return (maxv, bestAIMaxLocalMove) # px, py)


def min_alpha_beta(entire_game_state, localBoardIndex, alpha, beta, depth):
    # TODO cant handle picking a new localboard
    minv = 2

    # qx = None
    # qy = None
    bestAIMinLocalMove = None

    # result = check_current_state(entire_game_state[localBoard]) # TODO use local or global?

    result = checkEntireBoardState(entire_game_state)
    
    # global_game_state[int((localBoard)/3)][(localBoard)%3] = localWinner
    # result = check_current_state(global_game_state)
    # globalWinner = check_current_state(global_game_state) # where -1 is 'X' aka human # TODO


    # print('min result: ' + str(result))
    # if result in ['X', 'O', '-']:
    #     print('min winner')
    # print('min depth: ', depth)

    if result == 'X':
        return (-1, 0)
    elif result == 'O':
        return (1, 0)
    elif result == '.':
        return (0, 0)

    depth += 1

    for i in range(0, 3):  # TODO this only checks local board rn... convert to ultimate
        for j in range(0, 3):
            if entire_game_state[localBoardIndex][i][j]  == ' ': # self.current_state[i][j] == ' ': # TODO ensure that a filled local Board wont be seen here. ie have to check for '-'
                # self.current_state[i][j] = 'X'
                entire_game_state[localBoardIndex][i][j] = 'X'
                # print('min localBoard: ' + str(localBoardIndex))
                (moveValue, bestAIMaxLocalMove) = max_alpha_beta(entire_game_state, (i*3 + j), alpha, beta, depth) # TODO if the local board is full, then the move will be on a different board
                # print('past min')
                if moveValue < minv:
                    minv = moveValue
                    bestAIMinLocalMove = (i*3 + j)
                # self.current_state[i][j] = '.'
                entire_game_state[localBoardIndex][i][j] = ' '

                if minv <= alpha:
                    # print('min here')
                    return (minv, bestAIMinLocalMove)

                if minv < beta:
                    beta = minv

    # print('min2 here')
    return (minv, bestAIMinLocalMove)

'''
Minimax Algorithm
'''
def getBestMove(entire_game_state, global_game_state, localBoard, player):
    global_winner_loser = check_current_state(global_game_state)
    if global_winner_loser == 'O': # If AI won
        return 1
    elif global_winner_loser == 'X': # If Human won
        return -1
    elif global_winner_loser == '-':    # Draw condition
        return 0
        
    moves = []
    empty_cells = []
    localWinner = check_current_state(entire_game_state[localBoard])
    
    # if the given local board is alreday completed, check all global moves
    if localWinner is not None:
        for currentLocalBoard in range(9):
            if global_game_state[int((currentLocalBoard)/3)][(currentLocalBoard)%3] is ' ':
                for i in range(3):
                    for j in range(3):
                        if entire_game_state[currentLocalBoard][i][j] is ' ':
                            empty_cells.append(currentLocalBoard * 9 + (i*3 + j))

    else: # if the local board has a valid move, check all local moves
        for i in range(3):
            for j in range(3):
                if entire_game_state[localBoard][i][j] is ' ':
                    empty_cells.append(localBoard * 9 + (i*3 + j))
    
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

# Playing
play_again = 'Y'
while play_again.lower() == 'y':
    global_game_state = [[' ',' ',' '],
                         [' ',' ',' '],
                         [' ',' ',' ']]

    entire_game_state = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                         [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                         [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]

    globalWinner = ai_localBoard = ai_Block_num = None

    print("\nNew Game!")
    printEntireBoard(entire_game_state)
    player_choice = input("Choose which player goes first - X(human) or O(MiniMax AI): ")
    if player_choice == 'X' or player_choice == 'x':
        current_player_idx = 0
    else:
        current_player_idx = 1
        
    if current_player_idx == 0: # human
        localBoard = int(input(str(players[current_player_idx]) + "'s Turn! Choose which local board to place first (0 to 8): "))
    else: # ai
        localBoard = 0

    while globalWinner == None:
        block_num = None
        localWinner = check_current_state(entire_game_state[localBoard])
        if current_player_idx == 0: # Human's turn
            while localWinner != None and block_num in range(9):
                localBoard = int(input(str(players[current_player_idx]) + "'s Turn! Choose which local board to place in"))# TODO (" + ', '.join(str(x) for x in availableLocalBoards) + "): ")) #TODO why doesnt *availableLocalBoards work?
                localWinner = check_current_state(entire_game_state[localBoard])
            block_num = int(input(str(players[current_player_idx]) + "'s Turn! LocalBoard: " + str(localBoard) + ". Choose where to place (0 to 8): ")) # TODO only show valid moves

        else: # AI's turn
            # block_num = getBestMove(entire_game_state, global_game_state, localBoard, players[current_player_idx]) # Broken none pruning

            if check_current_state(entire_game_state[localBoard]) != None:
                localBoard = None
            (m, block_num) = max_alpha_beta(entire_game_state, localBoard, alpha=-2, beta=2, depth=0)
            # TODO check if the ai is actually limited to current localBoard when possible...
            ai_Block_num = block_num % 9
            ai_localBoard = int(block_num / 9) # TODO need toi chec if this is a valid localBoard
            if localBoard == None:
                localBoard = int(block_num / 9)

        print('current_player_idx: ' , current_player_idx) # TODO BUG current bug is that the ai always returns 0!
        nextLocalBoard = play_move(players[current_player_idx], entire_game_state[localBoard], block_num)
        localWinner = check_current_state(entire_game_state[localBoard])
        if localWinner is not None:
            print("localWinner: " + str(localWinner))
            # availableLocalBoards.remove(localBoard) # TODO update all available boards...
            fillAllLocalEmptySpaces(entire_game_state[localBoard])
            global_game_state[int((localBoard)/3)][(localBoard)%3] = localWinner
            print_board(global_game_state)
        else:
            localBoard = nextLocalBoard

        if current_player_idx == 1: # ai
            printEntireBoard(entire_game_state)
            print("ai placed at localBoard: " + str(ai_localBoard) + ", position: " + str(ai_Block_num)) # TODO bug always prints localboard = 0, and always places at 0? also cant handle picking a new localboard
            
        globalWinner = check_current_state(global_game_state)
        if globalWinner == '-':
            print("Draw!")
        elif globalWinner is not None:
            print(str(globalWinner) + " won!")
        else:
            current_player_idx = (current_player_idx + 1)%2
            
    play_again = input('Wanna try again?(Y/N) : ')
    if play_again == 'N':
        print('GG!')
    
