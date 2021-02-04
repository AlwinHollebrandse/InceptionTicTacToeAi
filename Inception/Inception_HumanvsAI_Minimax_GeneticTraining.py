import numpy as np # TODO set up virtual env and pipenv-once there are dependencies
from HelperFunctions import *

PLAYERS = ['X','O']
MAXDIFFICULTY = 5
SOL_PER_POP = 10
NUM_WEIGHTS = 7
NUM_GENERATIONS = 1

# TODO set alpha = minMoveValue and best=maxMoveValue

def singlePointCrossover(parent0, parent1):
    crossoverPoint = int(len(parent0)/2) # TODO or random instead of middle
    firstHalf = parent0[:crossoverPoint]
    secondHalf = parent1[crossoverPoint:]
    return np.concatenate((firstHalf, secondHalf), axis=0)

def uniformCrossover(parent0, parent1):
    singleOffspring = []
    for geneIndex in range(len(parent0)):
        parentGene = np.random.randint(2)
        if parentGene == 0:
            singleOffspring.append(parent0[geneIndex])
        else:
            singleOffspring.append(parent1[geneIndex])
    return singleOffspring

def crossover(parents):
    offspring = []
    np.random.shuffle(parents)
    while len(offspring) < SOL_PER_POP:
        parent0 = parents[np.random.randint(len(parents))]
        parent1 = parents[np.random.randint(len(parents))]
        # singleOffspring = singlePointCrossover(parent0, parent1)
        singleOffspring = uniformCrossover(parent0, parent1)
        offspring.append(singleOffspring)
    return offspring

def mutate(offspringCrossOver):
    for offspring in offspringCrossOver:
        randomIndex = np.random.randint(len(offspring))
        randomValue = np.random.uniform(low=0, high=10.0)
        offspring[randomIndex] = randomValue

def createNewGeneration(winningValues):
    generation = crossover(winningValues)
    mutate(generation)
    return generation

def getFirstLegalMove(board):
    for i in range(9):
        if board[int(i/3)][i%3] == ' ':
            return i
    print('There were no legal moves in this board') # TODO BUG its possible that the the ai needs to choose board itself, which this wouldnt account for
    return None

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
def optimizeMove(player, entire_game_state, scoreChangeValues, localBoardIndex, moveValue, maxDepth, currentDepth, difficulty, alpha, beta): # TODO could make maxdepth variable depending on how many empty spaces there are
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

    bestAILocalMove = None # TODO BUG could technically return None and break. currently bandaided by 'getFirstLegalMove'

    result = checkEntireBoardState(entire_game_state)

    if result == 'X':
        return (moveValue-90, 0, localBoardPlacedIn)
    elif result == 'O':
        return (moveValue+90, 0, localBoardPlacedIn)
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
                        scoreChange = scoreChangeValues[0]
                        if localBoardIndex in [0,2,6,8]: # in corner board
                            scoreChange += scoreChangeValues[1]
                        elif localBoardIndex in [4]: # in center board
                            scoreChange += scoreChangeValues[2]
                        if tempLocalWinner == 'X':
                            tempMoveValue -= scoreChange
                        elif tempLocalWinner == 'O':
                            tempMoveValue += scoreChange

                    if difficulty >= 2 and tempLocalWinner == None:
                        scoreChange = scoreChangeValues[3]
                        (blocked, player) = blocksLocalWin(entire_game_state[localBoardIndex], player, i, j)
                        if blocked and player == 'X':
                            tempMoveValue -= 1
                        elif blocked and player == 'O':
                            tempMoveValue += 1

                    if difficulty >= 3:
                        scoreChange = scoreChangeValues[4]
                        (blocked, player) = blocksGlobalWin(entire_game_state, player, localBoardIndex)
                        if blocked and player == 'X':
                            tempMoveValue -= 1
                        elif blocked and player == 'O':
                            tempMoveValue += 1

                    if difficulty >= 4:
                        scoreChange = getsOneAwayFromLocalWin(entire_game_state[localBoardIndex], player) * scoreChangeValues[5]
                        if player == 'X':
                            tempMoveValue -= scoreChange
                        elif player == 'O':
                            tempMoveValue += scoreChange

                    if difficulty >= 5:
                        scoreChange = getsOneAwayFromGlobalWin(entire_game_state, player) * scoreChangeValues[6]
                        if player == 'X':
                            tempMoveValue -= scoreChange
                        elif player == 'O':
                            tempMoveValue += scoreChange
                    # TODO maybe reward less points the more depth youre looking, based on the idea that the foe has more oppurtunities for mistakes. 

                    (resultMoveValue, bestNextAILocalMove, bestAILocalBoardPlacedIn) = optimizeMove(player=getOpponent(player), entire_game_state=entire_game_state, scoreChangeValues=scoreChangeValues, localBoardIndex=(i*3 + j), moveValue=tempMoveValue, maxDepth=maxDepth, currentDepth=currentDepth, difficulty=difficulty, alpha=alpha, beta=beta)

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

def aiFaceOff(winningValues, new_population, xPlayerIndex, oPlayerIndex, currentGeneration):
    difficulty = 5 # getInputAsValidNumber('Enter the desired AI difficulty (0,' + str(MAXDIFFICULTY) + '): ', MAXDIFFICULTY)
    maxDepth = 5

    availableLocalBoards = [i for i in range(9)]

    global_game_state = [[' ',' ',' '],
                        [' ',' ',' '],
                        [' ',' ',' ']]

    entire_game_state = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]

    globalWinner = None

    print('\nNew Game! current generation: ', currentGeneration)
    printEntireBoard(entire_game_state)

    player_choice = np.random.randint(2)
    if player_choice == 0:
        current_player_idx = 0
        firstPlayer = 'X'
    else:
        current_player_idx = 1
        firstPlayer = 'O'

    print('\n Player', firstPlayer, 'is going first generation:', currentGeneration, ', xPlayerIndex:', xPlayerIndex, ', oPlayerIndex:', oPlayerIndex, ' len of newPop:', len(new_population))

    localBoardIndex = 4

    while globalWinner == None:
        position = None
        localWinner = check_current_state(entire_game_state[localBoardIndex])
        if current_player_idx == 0: # X AI's turn
            print('X AI is plotting your doom')
            (maxMoveValue, position, localBoardIndex) = optimizeMove(player='X', entire_game_state=entire_game_state, scoreChangeValues=new_population[xPlayerIndex], localBoardIndex=localBoardIndex, moveValue=0, maxDepth=maxDepth, currentDepth=0, difficulty=difficulty, alpha=-100, beta=100)

        else: # O AI's turn
            print('O AI is plotting your doom')
            (maxMoveValue, position, localBoardIndex) = optimizeMove(player='O', entire_game_state=entire_game_state, scoreChangeValues=new_population[oPlayerIndex], localBoardIndex=localBoardIndex, moveValue=0, maxDepth=maxDepth, currentDepth=0, difficulty=difficulty, alpha=-100, beta=100)

        if position == None:
            print(position, localBoardIndex)
            position = getFirstLegalMove(entire_game_state[localBoardIndex])
            print_board(global_game_state)
            printEntireBoard(entire_game_state)

        nextLocalBoard = play_move(PLAYERS[current_player_idx], entire_game_state[localBoardIndex], position)
        localWinner = check_current_state(entire_game_state[localBoardIndex])
        if localWinner != None:
            print('localWinner: ' + str(localWinner))
            availableLocalBoards.remove(localBoardIndex)
            fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])
            global_game_state[int(localBoardIndex/3)][localBoardIndex%3] = localWinner

        # print_board(global_game_state)
        # printEntireBoard(entire_game_state)
        print('ai placed at localBoardIndex: ' + str(localBoardIndex) + ', position: ' + str(position))
        
        localBoardIndex = nextLocalBoard
        globalWinner = check_current_state(global_game_state)
        if globalWinner == '-':
            print('Draw!')
        elif globalWinner != None:
            print_board(global_game_state)
            print(str(globalWinner) + ' won!')

            # getting the possible parents for next generation
            if globalWinner == 'X':
                winningValues.append(new_population[xPlayerIndex])
            else:
                winningValues.append(new_population[oPlayerIndex])

        else:
            current_player_idx = (current_player_idx + 1)%2

def winnerTournament(startingWinningValues):
    print('Finding the final winner')
    winningValues = startingWinningValues
    while len(winningValues) > 1:
        roundWinners = []
        xPlayerIndex = 0
        oPlayerIndex = 1 # TODO BUG what if winning values is odd length
        for i in range(0, len(winningValues), 2):
            if xPlayerIndex < len(winningValues) and oPlayerIndex < len(winningValues):
                aiFaceOff(roundWinners, winningValues, xPlayerIndex, oPlayerIndex, len(winningValues))
                xPlayerIndex += 2
                oPlayerIndex += 2
            else:
                if xPlayerIndex < len(winningValues):
                    roundWinners.append(winningValues[xPlayerIndex])
                if oPlayerIndex < len(winningValues):
                    roundWinners.append(winningValues[oPlayerIndex])

        winningValues = roundWinners
    print('The final winning values are:', winningValues)
    np.savetxt('./Inception/GeneticTrainingValues', winningValues, fmt = '%.6f')


def main():
    currentGeneration = 0
    pop_size = (SOL_PER_POP, NUM_WEIGHTS) # The population will have SOL_PER_POP chromosome where each chromosome has NUM_WEIGHTS genes.
    new_population = np.random.uniform(low=0, high=10.0, size=pop_size)
    xPlayerIndex = 0
    oPlayerIndex = 1

    while currentGeneration < NUM_GENERATIONS:
        np.random.shuffle(new_population)
        winningValues = []
        xPlayerIndex = 0
        oPlayerIndex = 1
        while xPlayerIndex < SOL_PER_POP:
            aiFaceOff(winningValues, new_population, xPlayerIndex, oPlayerIndex, currentGeneration)
            xPlayerIndex += 2
            oPlayerIndex += 2
        print('HERE ONE GEN DONE currentGeneration:', currentGeneration)              

        new_population = createNewGeneration(winningValues)
        # np.savetxt('trained_state_values_X.txt', state_values_for_AI_X, fmt = '%.6f')
        currentGeneration += 1
        # TODO rn this doesnt return a single best combinition
    
    winnerTournament(winningValues)
    
    # winnerTournament()
    
if __name__ == '__main__':
    main()

# The final winning values are: [[2.9793802250542036, 3.296807981956942, 9.232239154420398, 5.176796334843605, 7.784129773601993, 3.43421578026331, 6.234167038444548]]
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

