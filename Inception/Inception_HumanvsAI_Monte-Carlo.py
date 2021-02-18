# import numpy as np # TODO set up virtual env and pipenv-once there are dependencies
from HelperFunctions import *
from MonteCarloTreeSearchNode import MonteCarloTreeSearchNode

PLAYERS = ['X','O']
simulations_number = 500

def monteCarlo_best_action(rootNode, simulations_number):
    for _ in range(0, simulations_number): # TODO or time limit TODO break after all possible moves are done?
        v = tree_policy(rootNode)
        reward = v.rollout()
        v.backpropagate(reward)
    # to select best child go for exploitation only
    preMoveEntireBoard = rootNode.entire_game_state
    postMoveEntireBoard = rootNode.best_child(c_param=0.).entire_game_state
    return getMove(preMoveEntireBoard, postMoveEntireBoard)

# selects node to run rollout/playout for
def tree_policy(rootNode):
    current_node = rootNode
    while not current_node.is_terminal_node():
        if not current_node.is_fully_expanded():
            return current_node.expand()
        else:
            current_node = current_node.best_child()
    return current_node

def main():
    play_again = 'Y'
    while play_again.lower() == 'y':
        availableLocalBoards = [i for i in range(9)]
        
        entire_game_state = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], 
                            [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                            [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]

        # human must go first and play in board 0 for bug
        # entire_game_state = [[['X','O',' '],[' ','O',' '],['X','X','O']], [['O','X',' '],['O','X',' '],[' ','O',' ']], [['X','X','X'],['-','-','O'],['-','-','-']], 
        #                     [['X','-','O'],['X','-','-'],['X','-','O']], [['-','-','-'],['O','X','-'],['O','O','O']], [['-','-','-'],['-','-','X'],['O','O','O']],
        #                     [['O','O','O'],['-','-','-'],['X','-','-']], [['-','-','O'],['-','-','X'],['X','X','X']], [['O','X',' '],['X','X',' '],['O','O','X']]]

        global_game_state = computeGlobalState(entire_game_state)
        globalWinner = check_current_state(global_game_state)

        print('\nNew Game!')
        printEntireBoard(entire_game_state)
        player_choice = input('Choose which player goes first - X(human) or O(Monte-Carlo AI): ')
        if player_choice.lower() == 'x':
            current_player_idx = 0
        else:
            current_player_idx = 1
            
        if current_player_idx == 0: # human
            localBoardIndex = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! Choose which local board to place first (0 to 8): ', 8)
        else: # ai
            localBoardIndex = None

        while globalWinner == None:
            position = None
            if current_player_idx == 0: # Human's turn
                localWinner = check_current_state(entire_game_state[localBoardIndex])
                while localWinner != None:
                    localBoardIndex = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! Local board ' + str(localBoardIndex) + ' was unavailable. Choose which local board to place in: ', 8)
                    localWinner = check_current_state(entire_game_state[localBoardIndex])
                position = getInputAsValidNumber(str(PLAYERS[current_player_idx]) + '\'s Turn! localBoardIndex: ' + str(localBoardIndex) + '. Choose where to place (0 to 8): ', 8)

            else: # AI's turn
                print('AI is plotting your doom')
                rootNode = MonteCarloTreeSearchNode(player='O', entire_game_state=entire_game_state, localBoardIndex=localBoardIndex)
                (position, localBoardIndex) = monteCarlo_best_action(rootNode, simulations_number)
                # (maxMoveValue, position, localBoardIndex) = optimizeMove(player='O', entire_game_state=entire_game_state, localBoardIndex=localBoardIndex, moveValue=0, maxDepth=maxDepth, currentDepth=0, difficulty=difficulty, alpha=-100, beta=100)

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
                print_board(global_game_state)
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
