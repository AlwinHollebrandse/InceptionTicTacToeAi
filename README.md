The source for the base tic tac toe game and the related ai can be found [here](https://github.com/agrawal-rohit/tic-tac-toe-bot)

# Inception Tic Tac Toe Rules
Per [Wikipedia](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe), Inception/Ultimate Tic Tac Toe has rules defined as:
Each small 3 × 3 tic-tac-toe board is referred to as a local board, and the larger 3 × 3 board is referred to as the global board.

The game starts with X playing wherever they want in any of the 81 empty spots. This move "sends" their opponent to its relative location. For example, if X played in the top right square of their local board, then O needs to play next in the local board at the top right of the global board. O can then play in any one of the nine available spots in that local board, each move sending X to a different local board.

If a move is played so that it is to win a local board by the rules of normal tic-tac-toe, then the entire local board is marked as a victory for the player in the global board.

Once a local board is won by a player or it is filled completely, no more moves may be played in that board. If a player is sent to such a board, then that player may play in any other board.

Another version for the game allows players to continue playing in already won boxes if there are still empty spaces. This allows the game to last longer and involves further strategic moves. This is up to the players on which rule to follow. It was shown in 2020 that this set of rules for the game admits a winning strategy for the first player to move, meaning that the first player to move can always win assuming perfect play[5].

Game play ends when either a player wins the global board or there are no legal moves remaining, in which case the game is a draw.

# Implementation Detail
To amke the game more competive when playing an Ai, it was decided to allow for a proven winning turn one strategy. For this purpose, this implementation will not allow users to play into empty spaces of already won local boards.


# A Tic Tac Toe Bot 

![tictactoe](https://user-images.githubusercontent.com/29514438/89706167-c3120200-d980-11ea-8fdc-b3593c004ea4.png)

This is the code repository for my article on Medium - [Playing Games with Python - Tic Tac Toe](https://towardsdatascience.com/lets-beat-games-using-a-bunch-of-code-part-1-tic-tac-toe-1543e981fec1), where I have tried to take the famous Tic-Tac-Toe game and create a bot proficient enough to beat human players, if not the game itself.

## What's inside this repo?
- A fully playable Tic-Tac-Toe environment.
- A bot trained using Temporal Difference learning (A technique in Reinforcement learning). 
- A bot trained using the Minimax Algorithm.

## How to use

### Play against the RL bot
run ``` python testing_(HumanvsAI)_ReinforcementLearning.py```

### Play against the Minimax bot
run ``` python HumanvsAI_Minimax.py```

### Play against another human player (Regular tic tac toe)
run ``` python HumanvsHuman.py```

## Training the RL Bot
Out of the two implementations, only the RL bot needs to train in order to reach proficiency. It does so by play 1v1 with another RL bot sharing the same state values in order to learn to beat itself and eventually become better. The `num_iterations` parameter controls the number of games that will be played among the bots.

run ```python training_(AIvsAI)_ReinforcementLearning.py```

## Testing the two bots by making them play among themselves
I wrote anotherr script in order to see which bot performed better in very brutal 1v1 fashion. The `num_iterations` parameter controls the number of games that will be played among both the bots.

run ```python Showdown_Minimax_vs_RL.py```

## To Try
- [x] Minimax Algorithm
- [x] Temporal Difference Learning
- [ ] Q Learning
- [ ] Genetic Algorithms