# TODO this is basically the main method from other games, that lets 2 agents face each other
# TODO as such, refactor the other play files to either call this, or just override the best move function 
import logging
import HelperFunctions

from tqdm import tqdm

log = logging.getLogger(__name__)


class Arena():
    """
    An Arena class where any 2 agents can be pit against each other.
    """

    # TODO reintroduce these lambas
    def __init__(self, player1Move, player2Move, player1StartingBoardIndexMove, player2StartingBoardIndexMove, display=None):
        """
        Input:
            player 1,2: two functions that takes board as input, return action
            game: Game object
            display: a function that takes board as input and prints it (e.g.
                     display in othello/OthelloGame). Is necessary for verbose
                     mode.
        see othello/OthelloPlayers.py for an example. See pit.py for pitting
        human players/other baselines with each other.
        """
        self.player1Move = player1Move
        self.player2Move = player2Move
        self.player1StartingBoardIndexMove = player1StartingBoardIndexMove
        self.player2StartingBoardIndexMove = player2StartingBoardIndexMove
        self.display = display
        self.PLAYERS = ['X','O']
        self.simulations_number = 500 # TODO having this depends on which ai version is used

    def playGame(self, startingPlayer=0, verbose=False):
        """
        Executes one episode of a game.
        Returns:
            either
                winner: player who won the game (1 if player1Move, -1 if player2Move)
            or
                draw result returned from the game that is neither 1, -1, nor 0.
        """
        players = [self.player1Move, self.player2Move]
        startingIndexes = [self.player1StartingBoardIndexMove, self.player2StartingBoardIndexMove]
        current_player_idx = startingPlayer
        board = HelperFunctions.getInitBoard()
        localBoardIndex = startingIndexes[startingPlayer] # TODO getStartingLocalBoardIndex()
        it = 0
        while HelperFunctions.isGameOver(board) == False:
            it += 1
            if verbose:
                HelperFunctions.print_board(HelperFunctions.computeGlobalState(board))
                HelperFunctions.printEntireBoard(board)
                print("Turn ", str(it), "Player ", str(self.PLAYERS[current_player_idx]))
                # self.display(board)
            # action = players[curPlayer + 1](self.game.getCanonicalForm(board, curPlayer))

            # TODO import MonteCarloTreeSearchNode as GAME when refactoring
            (position, localBoardIndex) = players[current_player_idx]
            # (position, localBoardIndex) = getBestMove(player=self.PLAYERS[current_player_idx], board=board, localBoardIndex=localBoardIndex, simulations_number=self.simulations_number)
            # TODO could save sub tree of best child for root opf next round for better perforcamnce?

            # valids = self.game.getValidMoves(self.game.getCanonicalForm(board, curPlayer), 1)
            # valids = HelperFunctions.getAllLegalMoves(board, localBoardIndex)

            # TODO re-add error handling
            # if valids[action] == 0:
            #     log.error(f'Action {action} is not valid!')
            #     log.debug(f'valids = {valids}')
            #     assert valids[action] > 0
            # board, curPlayer = self.game.getNextState(board, curPlayer, action)
            nextLocalBoard = HelperFunctions.play_move(self.PLAYERS[current_player_idx], board[localBoardIndex], position)
            localBoardIndex = nextLocalBoard
            current_player_idx = (current_player_idx + 1)%2

        globalWinner = HelperFunctions.check_current_state(HelperFunctions.computeGlobalState(board))
        if verbose:
            HelperFunctions.print_board(HelperFunctions.computeGlobalState(board))
            HelperFunctions.printEntireBoard(board)
            print("Game over: Turn ", str(it), "Result ", str(globalWinner))
        return globalWinner

    def playGames(self, num, verbose=False):
        """
        Plays num games in which player1Move starts num/2 games and player2Move starts
        num/2 games.
        Returns:
            oneWon: games won by player1Move
            twoWon: games won by player2Move
            draws:  games won by nobody
        """

        num = int(num / 2)
        xWon = 0
        oWon = 0
        draws = 0
        for _ in tqdm(range(num), desc="Arena.playGames (1)"):
            gameResult = self.playGame(verbose=verbose)
            if gameResult == 'X':
                xWon += 1
            elif gameResult == 'O':
                oWon += 1
            else:
                draws += 1

        # self.player1Move, self.player2Move = self.player2Move, self.player1Move

        for _ in tqdm(range(num), desc="Arena.playGames (2)"):
            gameResult = self.playGame(startingPlayer=1, verbose=verbose)
            if gameResult == 'O':
                oWon += 1
            elif gameResult == 'X':
                xWon += 1
            else:
                draws += 1

        return xWon, oWon, draws