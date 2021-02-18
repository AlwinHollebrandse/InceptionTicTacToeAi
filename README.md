The source for the base tic tac toe game and the related ai can be found [here](https://github.com/agrawal-rohit/tic-tac-toe-bot) and [here](https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/)

# Inception Tic Tac Toe Rules
Per [Wikipedia](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe), Inception/Ultimate Tic Tac Toe has rules defined as:
Each small 3 × 3 tic-tac-toe board is referred to as a local board, and the larger 3 × 3 board is referred to as the global board.

The game starts with X playing wherever they want in any of the 81 empty spots. This move "sends" their opponent to its relative location. For example, if X played in the top right square of their local board, then O needs to play next in the local board at the top right of the global board. O can then play in any one of the nine available spots in that local board, each move sending X to a different local board.

If a move is played so that it is to win a local board by the rules of normal tic-tac-toe, then the entire local board is marked as a victory for the player in the global board.

Once a local board is won by a player or it is filled completely, no more moves may be played in that board. If a player is sent to such a board, then that player may play in any other board.

Another version for the game allows players to continue playing in already won boxes if there are still empty spaces. This allows the game to last longer and involves further strategic moves. This is up to the players on which rule to follow. It was shown in 2020 that this set of rules for the game admits a winning strategy for the first player to move, meaning that the first player to move can always win assuming perfect play[5].

Game play ends when either a player wins the global board or there are no legal moves remaining, in which case the game is a draw.

To make the game more competitive when playing an AI, it was decided to allow for a proven winning turn one strategy. For this purpose, all implementations will not allow users to play into empty spaces of already won local boards.

# Inception Monte-Carlo Implementation Details
The decision to use a Monte-Carlo Tree Search (MCTS) to let the ai pick its moves was inspired by Google's AlphaGo program. This program used a combination of a MCTS and a Neural Network to create the world's best Go player. For the purposes of a MCTS implementation, each node represents a legal move that a given player can make. A MCTS works by exploring nodes selected by combining the exploitation value (how well a particular node is expected to perform in terms of global wins) with its exploration value (how many times a node has been explored in the search). Once a node is selected based on the max UCB value (the combination of exploitation and exploration), it gets expanded. This means that a possible subsequent move gets simulated. From this new node, the node performs a `rollout`-a potential playout of the game is performed by choosing repeatedly having both players pick random moves until a game is concluded. If the game ends in a 'O' victory, the chosen node gets a value of 1. If player 'X' wins, the reward is -1. A draw yields a 0 value result. This result is then back propagated up the tree, modifying all parents exploitation and exploration values. Once enough iterations has been performed, the root node (the actual current board state) returns the move of its child with the best exploitation value, i.e. the node with the most known follow up paths to victory. A more thorough explanation with a worked through example can be found [here](https://www.analyticsvidhya.com/blog/2019/01/monte-carlo-tree-search-introduction-algorithm-deepmind-alphago/). The source code that was used as inspiration can be found [here](https://github.com/int8/monte-carlo-tree-search/blob/master/mctspy/tree/nodes.py).

# Inception Minimax Implementation Details
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
All dependencies were managed with pipenv. To install them, run ```pipenv install``` while in the folder containing this code. If that is done, run ```pipenv shell``` to enter the virtual env that holds all dependencies.

### Play against the Minimax bot
```python3 ./Inception/Inception_HumanvsAI_Minimax.py```

### Play against random move bot
```python3 ./Inception/Inception_HumanvsRandom.py```

### Play against another human player (Regular tic tac toe)
```python3 ./Inception/Inception_HumanvsHuman.py```

# Training
While the Minimax algorithm works well for getting the AI to choose moves, the values of the rewards/punishments were chosen arbitrarily. To alleviate that issue, several machine learning approaches were used to find more optimal values for the 7 rewards/punishment values for each move. It should be noted that a concern of these training approaches is the fitness equation. Due to the nature of the problem there is no optimal solution. This means that a "best" winner can only be determined by a tournament, otherwise any individual who beat another individual is better than the loser. However, this might be impacted by which individual went first. While there might be a minimum required amount of moves to win the game, that number will be impossible to reach depending on the opponents play. Additionally, due to the single elimination approach to both the overall winner and the the generational winners, rewarding the AI that took the least amount of moves as the best winner (and thus is more likely to be selected as a parent) also depends on the AI matchup. As a result, the current approach is limited.
 
# Genetic Algorithm Training
This training approach works by having the AI face itself. An arbitrary value of 10 was chosen as the population size. The initial generation has the 7 reward/punishment values be randomly selected floats between 0 and 10. The algorithm is currently set to run for 15 generations. Each generation gets shuffled and pair up. The 'X' AI gets assigned to one of the pairs and the 'O' AI gets assigned to the other. A coin flip determines which AI goes first. The winner has its values tracked and saved as a parent of the next generation. This results in (population size)/2 winners per generation. Offspring are created by performing crossover and then mutation. There are 2 kinds of crossover implemented here: single point and uniform. The general crossover algorithm is to shuffle the parents and while there are less than the population size number of children, take two randomly selected parents and make them create a new child with either single point or uniform methods. Single point works by taking the middle point of the parents and using the left side of parent0 with the right side of parent1. Uniform works by randomly picking the respective parent's gene for each gene the child needs. Mutation occurs by randomly selecting one of the child's genes and assigning it to a random float 0-10. Once this is repeated for the desired amount of times, the new generation is completed and can begin the next round of competition. After the desired amount of generations has been completed, a final winner is selected. This is done by running a single elimination tournament of the final generation's winners. The overall winner has its values saved to `Inception/GeneticTrainingValues.txt` to be used when facing either human opponents or differently trained AIs. Currently this training is done with uniform crossover and a lookahead depth of 5.
 











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
