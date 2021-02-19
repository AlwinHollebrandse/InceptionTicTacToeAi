import numpy as np
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import HelperFunctions

class MonteCarloTreeSearchNode():

    def __init__(self, player, entire_game_state, localBoardIndex, parent=None):
        self.player = player
        self.entire_game_state = entire_game_state
        self.localBoardIndex = localBoardIndex
        self.parent = parent
        self.children = []
        self._number_of_visits = 0.
        self._results = 0
        self._untried_actions = None

    @property
    def untried_actions(self):
        if self._untried_actions is None:
            self._untried_actions = HelperFunctions.getAllLegalMoves(self.entire_game_state, self.localBoardIndex)
        return self._untried_actions

    @property
    def q(self):
        return self._results

    @property
    def n(self):
        return self._number_of_visits

    def expand(self):
        [position, localBoardIndex] = self.untried_actions.pop()
        next_entire_game_state = HelperFunctions.copyEntireState(self.entire_game_state)
        HelperFunctions.play_move(self.player, next_entire_game_state[localBoardIndex], position) # TODO pass a copy into the new node?
        next_localBoardIndex = position
        next_player = HelperFunctions.getOpponent(self.player)
        child_node = MonteCarloTreeSearchNode(
            next_player, next_entire_game_state, next_localBoardIndex, parent=self
        )
        self.children.append(child_node)
        return child_node

    def is_terminal_node(self):
        if HelperFunctions.checkEntireBoardState(self.entire_game_state) == None:
            return False
        return True

    def rollout(self):
        current_rollout_state = HelperFunctions.copyEntireState(self.entire_game_state)
        current_localBoardIndex = self.localBoardIndex
        current_player = self.player
        while HelperFunctions.checkEntireBoardState(current_rollout_state) == None:            
            possible_moves = HelperFunctions.getAllLegalMoves(current_rollout_state, current_localBoardIndex)
            [position, localBoardIndex_playedIn] = self.rollout_policy(possible_moves)   
            HelperFunctions.play_move(current_player, current_rollout_state[localBoardIndex_playedIn], position)
            localWinner = HelperFunctions.check_current_state(current_rollout_state[localBoardIndex_playedIn])
            if localWinner != None:
                HelperFunctions.fillAllLocalEmptySpaces(current_rollout_state[localBoardIndex_playedIn])
            
            current_player = HelperFunctions.getOpponent(current_player)
            current_localBoardIndex = position
        
        winner = HelperFunctions.checkEntireBoardState(current_rollout_state)
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
        return 0

    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results += result
        if self.parent:
            self.parent.backpropagate(result)
    
    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def calcUCBs(self, c_param=1.4):
        choices_weights = [
            (c.q / c.n) + c_param * np.sqrt((2 * np.log(self.n) / c.n))
            for c in self.children
        ]
        return choices_weights

    def best_child(self, c_param=1.4):
        allUCBs = self.calcUCBs(c_param)
        return self.children[np.argmax(allUCBs)]

    def rollout_policy(self, possible_moves):        
        return possible_moves[np.random.randint(len(possible_moves))]
