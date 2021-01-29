The source for the base tic tac toe game and the related ai can be found [here](https://github.com/agrawal-rohit/tic-tac-toe-bot) and [here](https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/)

# Inception Tic Tac Toe Rules
Per [Wikipedia](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe), Inception/Ultimate Tic Tac Toe has rules defined as:
Each small 3 × 3 tic-tac-toe board is referred to as a local board, and the larger 3 × 3 board is referred to as the global board.

The game starts with X playing wherever they want in any of the 81 empty spots. This move "sends" their opponent to its relative location. For example, if X played in the top right square of their local board, then O needs to play next in the local board at the top right of the global board. O can then play in any one of the nine available spots in that local board, each move sending X to a different local board.

If a move is played so that it is to win a local board by the rules of normal tic-tac-toe, then the entire local board is marked as a victory for the player in the global board.

Once a local board is won by a player or it is filled completely, no more moves may be played in that board. If a player is sent to such a board, then that player may play in any other board.

Another version for the game allows players to continue playing in already won boxes if there are still empty spaces. This allows the game to last longer and involves further strategic moves. This is up to the players on which rule to follow. It was shown in 2020 that this set of rules for the game admits a winning strategy for the first player to move, meaning that the first player to move can always win assuming perfect play[5].

Game play ends when either a player wins the global board or there are no legal moves remaining, in which case the game is a draw.

# Inception Minimax Implementation Detail
To make the game more competitive when playing an Ai, it was decided to allow for a proven winning turn one strategy. For this purpose, this implementation will not allow users to play into empty spaces of already won local boards.
 
The AI Minimax bot works by following the minimax algorithm. This algorithm works by having the ai look at a predetermined amount of moves ahead and choosing the optimal move based on a point value for each game state. On odd depth moves, the ai chooses the move that would reward the most points. Then on even depth moves, the ai assumes the foe will play optimally and return the minimum scoring move, ie the move that is the worst for the ai. Points per move are awarded in a few ways (positive points for the ai, negative for the foe). Winning the game rewards 30 points. winning a side local board yields 2 points, corner local board wins reward 2.5 points, and winning the center local board rewards 3 points. Blocking the foe from winning a local board yields a point as does blocking a winning move on the global board. The AI also gets rewarded for getting one move away from winning a local board and on the global board. The points awarded for nearly winning a local board are 0.5 times the amount of potential victories the ai has after that move. For example, if the ai has a place taken in the corner and the center, but the foe has a piece in the opposing corner, the best local move is to not go at the side positions next to the foe's piece. This is because that only lines up a single winning move and not the two the ai could have. Having more winning moves is beneficial because it allows for more flexibility further along the game. This principle is applied for global boards as well, but the reward is just the amount of potential victory paths.
 
This implementation also incorporates alpha beta pruning. This type of heuristic prunes a significant amount of the game tree by not investing branches that cannot result in a better score further up the tree. This heuristic drastically reduces the runtime of the minimax algorithm and lets the ai peer ahead with a getter depth without making the foe wait for too long.
 
## Inception Minimax Difficulty Settings
There are also difficulty settings. Currently there are six accepted difficulty settings that impact the ai (0 - 5). 

### Difficulty 0 (Super Easy)
If the ai is set to difficulty 0 (Super Easy), the ai looks ahead 2 moves and only rewards global wins. 

  The final difficulty setting of 3 enables the ai to peer 6 moves ahead and also rewards blocking global wins.

### Difficulty 1 (Easy)
On difficulty 1 (Easy), the ai only looks 3 moves ahead. This Ai rewards global wins and also rewards winning local boards. More points are rewarded to winning the center and corner boards.

### Difficulty 2 (Medium)
The next created difficulty setting 2 (Medium) lets the ai look ahead by 5 moves. This Ai rewards global wins, local boards victories (with more points resulting from winning the center and corner boards), and rewards blocking local board wins.

### Difficulty 3 (Hard)
On difficulty setting 3 (Hard) the ai look ahead by 5 moves. This Ai rewards global wins, local boards victories (with more points resulting from winning the center and corner boards), rewards blocking local board wins, and also rewards blocking global victories for the foe. (Blocking a victory means that if the foe is a single block away from victory, you get rewards for going there before them)

### Difficulty 4 (Super Hard)
On difficulty 4 (Super Hard) the ai look ahead by 5 moves. This Ai rewards global wins, local boards victories (with more points resulting from winning the center and corner boards), rewards blocking local board wins, and also rewards blocking global victories for the foe. The AI also gets rewarded for getting one move away from winning a local board.

### Difficulty 5 (Insane)
On difficulty 5 (Insane) the ai look ahead by 5 moves. This Ai rewards global wins, local boards victories (with more points resulting from winning the center and corner boards), rewards blocking local board wins, and also rewards blocking global victories for the foe. The AI also gets rewarded for getting one move away from winning a local board and on the global board

## How to use

### Play against the Minimax bot
python3 ./Inception_HumanvsAI_Minimax.py

### Play against random move bot
python3 ./Inception_HumanvsRandom.py

### Play against another human player (Regular tic tac toe)
python3 ./Inception_HumanvsHuman.py







## What's inside this repo?
- A fully playable Tic-Tac-Toe environment.
- A bot trained using Temporal Difference learning (A technique in Reinforcement learning). 
- A bot trained using the Minimax Algorithm.

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
