def max_alpha_beta(entire_game_state, localBoardIndex, moveValue, depth, difficulty, alpha, beta): # TODO limit iterations?-not super feasible. if not end has been reached, all moves willl be equally viable right?...so do random? or just best local move
    print('init max localBoardIndex: ' + str(localBoardIndex), ', moveValue: ', moveValue, ', depth: ', depth)
    localBoardPlacedIn = getFirstAvailableBoard(entire_game_state)
    if check_current_state(entire_game_state[localBoardIndex]) != None:
        localBoardsToCheck = []
        for i in range(9):
            if check_current_state(entire_game_state[i]) == None:
                localBoardsToCheck.append(i)

    else:
        localBoardsToCheck = [localBoardIndex]
        localBoardPlacedIn = localBoardIndex
    
    maxMoveValue = -100 # TODO DIFF, should be param
    bestAIMaxLocalMove = None # TODO DIFF, should be param, but this one is just a var name

    result = checkEntireBoardState(entire_game_state)

    if result in ['X', 'O', '-']:
        print('max global winner, result: ', result, ', localBoardIndex: ', localBoardIndex, ', depth: ', depth)

    if result == 'X':
        return (moveValue-31, 0, localBoardPlacedIn)
    elif result == 'O':
        print('HERE MAX')
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
                    entire_game_state[localBoardIndex][i][j] = 'O' # TODO DIFF, should be param

                    print('max O placed at localBoardIndex: ' + str(localBoardIndex), ', location: ', (i*3 + j), ', depth: ', depth)

                    tempMoveValue = moveValue
                    tempLocalWinner = check_current_state(entire_game_state[localBoardIndex])
                    if tempLocalWinner in ['X', 'O', '-']:
                        fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])
                        # print('MAX HERE')
                        # printEntireBoard(entire_game_state)
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
                        (blocked, player) = blocksLocalWin(entire_game_state[localBoardIndex], 'O', i, j)
                        if blocked and player == 'X':
                            tempMoveValue -= 1
                        elif blocked and player == 'O':
                            tempMoveValue += 1
                    if difficulty >= 3: # TODO do the same but for global moves # TODO also add reward for getting 1 away from a win
                        (blocked, player) = blocksGlobalWin(entire_game_state, 'O', localBoardIndex)
                        if blocked and player == 'X':
                            tempMoveValue -= 1
                        elif blocked and player == 'O':
                            tempMoveValue += 1  
                    if difficulty >= 4: # TODO also reward geeting 1 away from a win, but less than a local win and punish for letting the human get 2 in a winning row
                        tempMoveValue += 0

                    # printEntireBoard(entire_game_state)

                    (resultMoveValue, bestAIMinLocalMove, bestAIMinLocalBoard) = min_alpha_beta(entire_game_state=entire_game_state, localBoardIndex=(i*3 + j), moveValue=tempMoveValue, depth=depth, difficulty=difficulty, alpha=alpha, beta=beta)
                    if resultMoveValue > maxMoveValue: # TODO DIFF, should be param
                        maxMoveValue = resultMoveValue
                        bestAIMaxLocalMove = (i*3 + j)
                        localBoardPlacedIn = localBoardIndex
                        print('HERE MAX', 'resultMoveValue:', resultMoveValue, 'maxMoveValue:', maxMoveValue, 'bestAIMaxLocalMove:',bestAIMaxLocalMove)

                    entire_game_state[localBoardIndex][i][j] = ' '
                    replaceAllUnavailableWithEmptySpaces(entire_game_state[localBoardIndex])

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    # if maxMoveValue >= beta:
                    #     print('HERE maxMoveValue:',maxMoveValue,'beta:',beta)
                    #     return (maxMoveValue, bestAIMaxLocalMove, localBoardPlacedIn)

                    # if maxMoveValue > alpha:
                    #     alpha = maxMoveValue

    print('max RETURN maxMoveValue:',maxMoveValue,'bestAILocalMove:',bestAIMaxLocalMove)
    return (maxMoveValue, bestAIMaxLocalMove, localBoardPlacedIn) # TODO DIFF, should be param var name

def min_alpha_beta(entire_game_state, localBoardIndex, moveValue, depth, difficulty, alpha, beta):
    print('init min localBoardIndex: ' + str(localBoardIndex), ', moveValue: ', moveValue, ', depth: ', depth)
    localBoardPlacedIn = getFirstAvailableBoard(entire_game_state)
    if check_current_state(entire_game_state[localBoardIndex]) != None:
        localBoardsToCheck = []
        for i in range(9):
            if check_current_state(entire_game_state[i]) == None:
                localBoardsToCheck.append(i)

    else:
        localBoardsToCheck = [localBoardIndex]
        localBoardPlacedIn = localBoardIndex

    minMoveValue = 100

    bestAIMinLocalMove = None

    result = checkEntireBoardState(entire_game_state)
    if result in ['X', 'O', '-']:
        print('min global winner, result: ', result, ', localBoardIndex: ', localBoardIndex, ', depth: ', depth)

    if result == 'X':
        print('HERE MIN')
        return (moveValue-31, 0, localBoardPlacedIn)
    elif result == 'O':
        return (moveValue+30, 0, localBoardPlacedIn)
    elif result == '.':
        return (moveValue, 0, localBoardPlacedIn)

    if depth >= MAXDEPTH: # TODO make a variable depth depending on how many move options you have...ex you dont have to pick a whole new local board as well
        return (moveValue, 0, localBoardPlacedIn)

    depth += 1

    for localBoardIndex in localBoardsToCheck:
        for i in range(0, 3):
            for j in range(0, 3):
                if entire_game_state[localBoardIndex][i][j]  == ' ':
                    entire_game_state[localBoardIndex][i][j] = 'X'

                    print('min X placed at localBoardIndex: ' + str(localBoardIndex), ', location: ', (i*3 + j), ', depth: ', depth)



                    # TODO if the ai is gloablly ahead, reward wining local boards more, and the oppoiste if behind
                    tempMoveValue = moveValue
                    tempLocalWinner = check_current_state(entire_game_state[localBoardIndex])
                    if tempLocalWinner in ['X', 'O', '-']:
                        fillAllLocalEmptySpaces(entire_game_state[localBoardIndex])
                        # print('MIN HERE')
                        # printEntireBoard(entire_game_state)
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
                    if difficulty >= 2:# TODO also add reward for getting 1 away from a win
                        (blocked, player) = blocksLocalWin(entire_game_state[localBoardIndex], 'X', i, j)
                        if blocked and player == 'X':
                            tempMoveValue -= 1
                        elif blocked and player == 'O':
                            tempMoveValue += 1
                    if difficulty >= 3: # TODO do the same but for global moves # TODO also add reward for getting 1 away from a win
                        (blocked, player) = blocksGlobalWin(entire_game_state, 'X', localBoardIndex)
                        if blocked and player == 'X':
                            tempMoveValue -= 1
                        elif blocked and player == 'O':
                            tempMoveValue += 1  
                    if difficulty >= 4: # TODO also reward geeting 1 away from a win, but less than a local win and punish for letting the human get 2 in a winning row
                        tempMoveValue += 0
                    # TODO add punishment for letting foe go in a board where they have the advantage?

                    # printEntireBoard(entire_game_state)

                    (resultMoveValue, bestAIMaxLocalMove, bestAIMaxLocalBoard) = max_alpha_beta(entire_game_state=entire_game_state, localBoardIndex=(i*3 + j), moveValue=tempMoveValue, depth=depth, difficulty=difficulty, alpha=alpha, beta=beta)
                    if resultMoveValue < minMoveValue:
                        minMoveValue = resultMoveValue
                        bestAIMinLocalMove = (i*3 + j)
                        localBoardPlacedIn = localBoardIndex
                        print('HERE MIN', 'resultMoveValue:', resultMoveValue, 'minMoveValue:', minMoveValue, 'bestAIMinLocalMove:',bestAIMinLocalMove)

                    entire_game_state[localBoardIndex][i][j] = ' '
                    replaceAllUnavailableWithEmptySpaces(entire_game_state[localBoardIndex])

                    # if minMoveValue <= alpha: # TODO how does alphabeta actaully work in conjunction with the recursion approach? you dont know the node value until the subtree has been solved, meaning trimming a branch is pointless because its already been solved
                    #     print('HERE minMoveValue:',minMoveValue,'alpha:',alpha)
                    #     return (minMoveValue, bestAIMinLocalMove, localBoardPlacedIn)

                    # if minMoveValue < beta:
                    #     beta = minMoveValue

    print('min RETURN minMoveValue:',minMoveValue,'bestAILocalMove:',bestAIMinLocalMove)
    return (minMoveValue, bestAIMinLocalMove, localBoardPlacedIn)