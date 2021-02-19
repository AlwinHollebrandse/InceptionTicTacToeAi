The source for the base tic tac toe game and the related ai can be found [here](https://github.com/agrawal-rohit/tic-tac-toe-bot) and [here](https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/)

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
