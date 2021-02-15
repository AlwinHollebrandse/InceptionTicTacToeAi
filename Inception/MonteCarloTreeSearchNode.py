# https://github.com/int8/monte-carlo-tree-search/blob/master/mctspy/tree/nodes.py
import numpy as np
from collections import defaultdict
from HelperFunctions import *

class MonteCarloTreeSearchNode():

    def __init__(self, player, entire_game_state, localBoardIndex, parent=None):
        self.player = player
        self.entire_game_state = entire_game_state
        self.localBoardIndex = localBoardIndex
        self.parent = parent
        self.children = []
        self._number_of_visits = 0.
        self._results = defaultdict(int)
        self._untried_actions = None

    @property
    def untried_actions(self):
        if self._untried_actions is None:
            self._untried_actions = getAllLegalMoves(self.entire_game_state, self.localBoardIndex)
        return self._untried_actions

    @property
    def q(self):
        wins = self._results[self.parent.player] # TODO for the source, player was a number and not a letter. Will this be an issue?
        loses = self._results[-1 * self.parent.player]
        return wins - loses

    @property
    def n(self):
        return self._number_of_visits

    def expand(self):
        [position, localBoardIndex] = self.untried_actions.pop()
        next_entire_game_state = play_move(self.player, localBoardIndex, position)
        next_localBoardIndex = position
        next_player = getOpponent(self.player)
        child_node = MonteCarloTreeSearchNode(
            next_player, next_entire_game_state, next_localBoardIndex, parent=self
        )
        self.children.append(child_node)
        return child_node

    def is_terminal_node(self):
        if checkEntireBoardState(self.entire_game_state) == None:
            return False
        return True

    def rollout(self):
        current_rollout_state = self.entire_game_state
        current_localBoardIndex = self.localBoardIndex
        current_player = self.player
        while checkEntireBoardState(current_rollout_state) != None:
            getOpponent(current_player) # TODO before or after playMove? to prevent init player from going twice in a row
            possible_moves = getAllLegalMoves(current_rollout_state, current_localBoardIndex)
            [position, current_localBoardIndex] = self.rollout_policy(possible_moves) # TODO return [] or tuple ()?
            current_rollout_state = play_move(self.player, current_localBoardIndex, position)
        winner = checkEntireBoardState(current_rollout_state)
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
        return 0

    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results[result] += 1.
        if self.parent:
            self.parent.backpropagate(result)
    
    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def best_child(self, c_param=1.4):
        choices_weights = [
            (c.q / c.n) + c_param * np.sqrt((2 * np.log(self.n) / c.n))
            for c in self.children
        ]
        return self.children[np.argmax(choices_weights)]

    def rollout_policy(self, possible_moves):        
        return possible_moves[np.random.randint(len(possible_moves))]
