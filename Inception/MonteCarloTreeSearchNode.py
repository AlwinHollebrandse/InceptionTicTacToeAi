# https://github.com/int8/monte-carlo-tree-search/blob/master/mctspy/tree/nodes.py
import numpy as np
from collections import defaultdict
from HelperFunctions import *

class MonteCarloTreeSearchNode():

    def __init__(self, player, entire_game_state, localBoardIndex, parent=None):
        # print('player: ', player, ', entire_game_state: ', entire_game_state)
        # printEntireBoard(entire_game_state)
        # TODO add property for assiocated move
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
        play_move(self.player, self.entire_game_state[localBoardIndex], position) # TODO pass a copy into the new node?
        next_entire_game_state = copyEntireState(self.entire_game_state)
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
        while checkEntireBoardState(current_rollout_state) == None:            
            printEntireBoard(current_rollout_state)
            print('currentPlayer: ', current_player)

            possible_moves = getAllLegalMoves(current_rollout_state, current_localBoardIndex)
            print('possible_moves: ', possible_moves)

            [position, localBoardIndex_playedIn] = self.rollout_policy(possible_moves) # TODO return [] or tuple ()?          
            play_move(current_player, current_rollout_state[localBoardIndex_playedIn], position)
            localWinner = check_current_state(current_rollout_state[localBoardIndex_playedIn])
            if localWinner != None:
                fillAllLocalEmptySpaces(current_rollout_state[localBoardIndex_playedIn])
            
            current_player = getOpponent(current_player) # TODO before or after playMove? to prevent init player from going twice in a row
            current_localBoardIndex = position
            print('position, localBoardIndex_playedIn, current_localBoardIndex: ', position, localBoardIndex_playedIn, current_localBoardIndex)
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
