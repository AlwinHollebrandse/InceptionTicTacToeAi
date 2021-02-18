# import numpy as np # TODO set up virtual env and pipenv-once there are dependencies
from HelperFunctions import *

PLAYERS = ['X','O']
MAXDIFFICULTY = 5

# TODO set alpha = minMoveValue and best=maxMoveValue

def blocksLocalWin(board, player, i, j):
    opponent = getOpponent(player)
    board[i][j] = opponent
    blocked = False
    if check_current_state(board) == opponent:
        blocked = True
    board[i][j] = player
    return blocked, player

def blocksGlobalWin(entire_game_state, player, localBoardIndex):
    temp_global_game_state = computeGlobalState(entire_game_state)
    return blocksLocalWin(temp_global_game_state, player, int(localBoardIndex/3), localBoardIndex%3)

def getsOneAwayFromLocalWin(board, player):
    amountOfPotentialWins = 0
    if check_current_state(board) == None:
        for i in range(9):
            if board[int(i/3)][i%3] == ' ':
                board[int(i/3)][i%3] = player
                if check_current_state(board) == player:
                    amountOfPotentialWins += 1
                board[int(i/3)][i%3] = ' '
    return amountOfPotentialWins

def getsOneAwayFromGlobalWin(entire_game_state, player):
    temp_global_game_state = computeGlobalState(entire_game_state)
    return getsOneAwayFromLocalWin(temp_global_game_state, player)

# NOTE if player == 'X' (human), the ai will perform a "min" calc. If the player == 'O' (ai), the the ai will perform a "max" calc.
def optimizeMove(player, entire_game_state, localBoardIndex, moveValue, maxDepth, currentDepth, difficulty, alpha, beta): # TODO could make maxdepth variable depending on how many empty spaces there are
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

    if result == 'X':
        return (moveValue-31, 0, localBoardPlacedIn)
    elif result == 'O':
        return (moveValue+30, 0, localBoardPlacedIn)
    elif result == '-':
        return (moveValue, 0, localBoardPlacedIn)

    if currentDepth >= maxDepth:
        return (moveValue, 0, localBoardPlacedIn)

    currentDepth += 1

    for localBoardIndex in localBoardsToCheck:
        for i in range(0, 3):
            for j in range(0, 3):
                if entire_game_state[localBoardIndex][i][j]  == ' ':
                    entire_game_state[localBoardIndex][i][j] = player

                    tempMoveValue = moveValue
                    tempLocalWinner = check_current_state(entire_game_state[localBoardIndex])
                    if tempLocalWinner in ['X', 'O', '-']:
                        fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])

                    if difficulty >= 1:
                        scoreChange = 2
                        if localBoardIndex in [0,2,6,8]: # in corner board
                            scoreChange += .5
                        elif localBoardIndex in [4]: # in center board
                            scoreChange += 1
                        if tempLocalWinner == 'X':
                            tempMoveValue -= scoreChange
                        elif tempLocalWinner == 'O':
                            tempMoveValue += scoreChange
                    if difficulty >= 2 and tempLocalWinner == None:
                        (blocked, player) = blocksLocalWin(entire_game_state[localBoardIndex], player, i, j)
                        if blocked and player == 'X':
                            tempMoveValue -= 1
                        elif blocked and player == 'O':
                            tempMoveValue += 1
                    if difficulty >= 3:
                        (blocked, player) = blocksGlobalWin(entire_game_state, player, localBoardIndex)
                        if blocked and player == 'X':
                            tempMoveValue -= 1
                        elif blocked and player == 'O':
                            tempMoveValue += 1  
                    if difficulty >= 4:
                        scoreChange = getsOneAwayFromLocalWin(entire_game_state[localBoardIndex], player) * 0.5 # TODO should this be multiplied? how many points should any of these be? 
                        if player == 'X':
                            tempMoveValue -= scoreChange
                        elif player == 'O':
                            tempMoveValue += scoreChange
                    if difficulty >= 5:
                        scoreChange = getsOneAwayFromGlobalWin(entire_game_state, player) * 1 # TODO should this be multiplied? how many points should any of these be? 
                        if player == 'X':
                            tempMoveValue -= scoreChange
                        elif player == 'O':
                            tempMoveValue += scoreChange
                    # TODO maybe reward less points the more depth youre looking, based on the idea that the foe has more oppurtunities for mistakes. 

                    (resultMoveValue, bestNextAILocalMove, bestAILocalBoardPlacedIn) = optimizeMove(player=getOpponent(player), entire_game_state=entire_game_state, localBoardIndex=(i*3 + j), moveValue=tempMoveValue, maxDepth=maxDepth, currentDepth=currentDepth, difficulty=difficulty, alpha=alpha, beta=beta)

                    if player == 'O' and resultMoveValue > maxMoveValue:
                        maxMoveValue = resultMoveValue
                        bestAILocalMove = (i*3 + j)
                        localBoardPlacedIn = localBoardIndex
                    elif player == 'X' and resultMoveValue < minMoveValue:
                        minMoveValue = resultMoveValue
                        bestAILocalMove = (i*3 + j)
                        localBoardPlacedIn = localBoardIndex

                    entire_game_state[localBoardIndex][i][j] = ' '
                    replaceAllUnavailableWithEmptySpaces(entire_game_state[localBoardIndex])

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if player == 'O':
                        if maxMoveValue >= beta:
                            return (maxMoveValue, bestAILocalMove, localBoardPlacedIn)

                        if maxMoveValue > alpha:
                            alpha = maxMoveValue

                    elif player == 'X':
                        if minMoveValue <= alpha:
                            return (minMoveValue, bestAILocalMove, localBoardPlacedIn)

                        if minMoveValue < beta:
                            beta = minMoveValue
   
    if player == 'O': # ai's optimal move value
        return (maxMoveValue, bestAILocalMove, localBoardPlacedIn)
    else: # human's optimal move value
        return (minMoveValue, bestAILocalMove, localBoardPlacedIn)

def main():
    play_again = 'Y'
    while play_again.lower() == 'y':
        difficulty = getInputAsValidNumber('Enter the desired AI difficulty (0,' + str(MAXDIFFICULTY) + '): ', MAXDIFFICULTY)
        maxDepth = 2
        if difficulty == 1:
            maxDepth = 3
        elif difficulty == 2:
            maxDepth = 4
        elif difficulty == 3:
            maxDepth = 5
        elif difficulty == 4:
            maxDepth = 6
        elif difficulty == 5:
            maxDepth = 7

        availableLocalBoards = [i for i in range(9)]

        entire_game_state = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                            [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                            [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]

        global_game_state = computeGlobalState(entire_game_state)
        globalWinner = check_current_state(global_game_state)

        print('\nNew Game!')
        printEntireBoard(entire_game_state)
        player_choice = input('Choose which player goes first - X(human) or O(MiniMax AI): ')
        if player_choice.lower() == 'x':
            current_player_idx = 0
        else:
            current_player_idx = 1
            
        if current_player_idx == 0: # human
            localBoardIndex = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! Choose which local board to place first (0 to 8): ', 8)
        else: # ai
            localBoardIndex = 4

        while globalWinner == None:
            position = None
            localWinner = check_current_state(entire_game_state[localBoardIndex])
            if current_player_idx == 0: # Human's turn
                while localWinner != None:
                    localBoardIndex = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! Local board ' + str(localBoardIndex) + ' was unavailable. Choose which local board to place in: ', 8)
                    localWinner = check_current_state(entire_game_state[localBoardIndex])
                position = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! localBoardIndex: ' + str(localBoardIndex) + '. Choose where to place (0 to 8): ', 8)

            else: # AI's turn
                print('AI is plotting your doom')
                (maxMoveValue, position, localBoardIndex) = optimizeMove(player='O', entire_game_state=entire_game_state, localBoardIndex=localBoardIndex, moveValue=0, maxDepth=maxDepth, currentDepth=0, difficulty=difficulty, alpha=-100, beta=100)

            nextLocalBoard = play_move(PLAYERS[current_player_idx], entire_game_state[localBoardIndex], position)
            localWinner = check_current_state(entire_game_state[localBoardIndex])
            if localWinner != None:
                print('localWinner: ' + str(localWinner))
                # print('available localboards: ' + ', '.join(str(x) for x in availableLocalBoards))
                availableLocalBoards.remove(localBoardIndex)
                fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])
                global_game_state[int(localBoardIndex/3)][localBoardIndex%3] = localWinner
                # print_board(global_game_state)

            if current_player_idx == 1: # ai
                print_board(global_game_state)
                printEntireBoard(entire_game_state)
                print('ai placed at localBoardIndex: ' + str(localBoardIndex) + ', position: ' + str(position))
            
            localBoardIndex = nextLocalBoard
            globalWinner = check_current_state(global_game_state)
            if globalWinner == '-':
                print('Draw!')
            elif globalWinner != None:
                print_board(global_game_state)
                print(str(globalWinner) + ' won!')
            else:
                current_player_idx = (current_player_idx + 1)%2
                
        play_again = input('Wanna try again?(Y/N): ')
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


# -----------------------------------------
# | O | X |   |||   | O | X |||   |   | O |
# -----------------------------------------
# |   |   |   |||   |   |   |||   |   | X |
# -----------------------------------------
# |   |   |   |||   |   |   |||   |   |   |
# -----------------------------------------
# -----------------------------------------
# |   |   |   ||| X |   |   |||   |   |   |
# -----------------------------------------
# |   |   | X |||   |   |   ||| O |   |   |
# -----------------------------------------
# |   |   |   |||   |   |   ||| O |   |   |
# -----------------------------------------
# -----------------------------------------
# | O |   |   |||   |   |   |||   |   |   |
# -----------------------------------------
# |   |   |   |||   |   |   |||   |   |   |
# -----------------------------------------
# | X |   |   |||   |   |   |||   |   |   |
# -----------------------------------------
# ai went 6,0, after human went 6,6


# TODO my idea to imporve this is to use a genetic alg to find the best values for the scores. To accomplish this,
# I will set up 1+ listof values that are the randomly genertaed scores. For both x and o (ai vs ai), using depth 5 for speed/acuracy blend 
# the winner will have its score combined with different winners...probaly via average or random value between the scores. The issue is slecting the best "winner"
# because not all ais win as well. Natievly, winning in less moves is better, but that could also be caused by the foe being mega bad so it might not be ideal
