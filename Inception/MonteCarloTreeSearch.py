import HelperFunctions
from MonteCarloTreeSearchNode import MonteCarloTreeSearchNode

# TODO abstract so all of these use the same params
def getBestMove(player, board, localBoardIndex, simulations_number):
    rootNode = MonteCarloTreeSearchNode(player=player, entire_game_state=board, localBoardIndex=localBoardIndex)
    return monteCarlo_best_action(rootNode, simulations_number)

# TODO abstract
def getStartingLocalBoardIndex():
    return None

def monteCarlo_best_action(rootNode, simulations_number):
    for _ in range(0, simulations_number): # TODO or time limit TODO break after all possible moves are done?
        v = tree_policy(rootNode)
        reward = v.rollout()
        v.backpropagate(reward)
    # to select best child go for exploitation only
    preMoveEntireBoard = rootNode.entire_game_state
    postMoveEntireBoard = rootNode.best_child(c_param=0.).entire_game_state
    return HelperFunctions.getMove(preMoveEntireBoard, postMoveEntireBoard)
    # TODO could save state of best child for next move when ai vs ai

# selects node to run rollout/playout for
def tree_policy(rootNode):
    current_node = rootNode
    while not current_node.is_terminal_node():
        if not current_node.is_fully_expanded():
            return current_node.expand()
        else:
            current_node = current_node.best_child()
    return current_node