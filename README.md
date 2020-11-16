# Evolution of Cooperation

## Prisoner's Dilemma simulations with different strategies
	
- Two Players (A and B (other player))
- Two choices (Cooperation (C), Defection (D))

#### Payoff Matrix
Player A (along row), Player B (along column)

	      |  C    |   D   |
	|-----|---------------|
	|     | (R,R) | (S,T) |
	|  C  |       |       |
  	| --- |---------------|
	|     |       |       |
	|  D  | (T,S) | (P,P) |
	| --- |---------------|

For purpose of demonstration let, 
`T = 5, R = 3, P = 1 and S = 0`

**Ensure you have python3.7 installed on your system**

### Installation
- Clone this repository into a suitable directory
```
git clone https://github.com/adypd97/prisoners_dilemma.git
```

- change directory and make ```sim.py``` and ```axelrod.py``` into executables
```
cd prisoners_dilemma/ && chmod +x {sim,axelrod}.py
```

### 1) One time Two Player Prisoner's Dilemma Game
See ```./sim.py```


### 2) Iterated Two Player Prisoner's Dilemma Game
See ```./axelrod.py```

- Strategies available to players A and B are
	- All Defect (all_D)
	- Poor-Trusting-Fool (trusting_fool)
	- Random     (randomer)
	- Go-by-Majority    (majority_seeker)
	- Tit-For-Tat       (tft)

- How to Use :
```
usage: axelrod.py [-h] [-options OPTIONS] [--s1 S1] [--s2 S2] [--n N] [--show SHOW]

Enter strategies for two player Prisoner's Dilemma game

optional arguments:
  -h, --help        show this help message and exit
  -options OPTIONS  Available strategy options include : 1. all_D 2. randomer
                    3. trusting_fool 4. majority_seeker 5. tft
  --s1 S1           enter a strategy for first (A) player See -h for all
                    strategies avaiable
  --s2 S2           enter a strategy for second (B) player See -h for all
                    strategies avaiable
  --n N             enter number of games between the two players with s1 and
                    s2 as their strategies. See -h for all strategies avaiable
  --show SHOW       Write the moves made by both players in output file
                    './moves.txt' See -h for all strategies avaiable
```

- Example :
Pick tft as strategy for player A and all_D as strategy for player B.
Play the game for 1000 iterations. Also, save the actions by each player
in ```moves.txt``` (for viewing later). 
```
 > ./axelrod.py --s1=tft --s2=all_D --n=1000 --show=True
```

### Resources 
`https://www.classes.cs.uchicago.edu/archive/1998/fall/CS105/Project/node3.html`


### TODO
- [ ] Make it work on Windows 10 
