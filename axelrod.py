#!/usr/bin/env python3

''' Axelrod's Tournament '''
import random
import argparse
import sys

# Parameters and Assumptions
R, S, T, P = 3, 0, 5, 1          # payoffs

payoff_mat = [ [(R,R), (S,T)],   # 0th payoff values belong to player A and 1st payoff 
               [(T,S), (P,P)] ]  # values belong to player B (other player)

w = 0.7                          # w > (T-R)/(T-P) & (T-R)/(R-S)
choices = [0,1]                  # 0 = Cooperate, 1 = Defect

# -------------------SIMPLE STRATEGIES----------------------------

# ALL Defect (ALL D)
def all_D():
    ''' no matter what,
        always DEFECT
    '''
    return choices[1]

# Random choice (randomer)
def randomer():
    ''' randomly select a 
        choice 
    '''
    return random.choice(choices)

# Play a game with strategies f and g, n times and report the score for each strategy
def play_loop(n,f,g):
    plays_A = []      # history of all plays ('c' or 'd') by player A
    plays_B = []      # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ B
    game_history = [] # keeps track of all game moves by two players
    for i in range(n):
        plays_A.append(f())
        plays_B.append(g())
        game_history.append((plays_A[i], plays_B[i]))
    score_A, score_B = play_loop_score(game_history)
    return score_A, score_B

def play_loop_score(hist):
    ''' given a game history as list 'hist'
        return the total score for each player 
        based from the payoff matrix
    '''
    score_A = 0
    score_B = 0
    for strat in hist:
        score_A += payoff_mat[strat[0]][strat[1]][0]
        score_B += payoff_mat[strat[0]][strat[1]][1]
    return score_A, score_B


def main(str_1, str_2):
    n = 10                                       # number of iterations of game
    f = getattr(sys.modules[__name__], str_1)
    g = getattr(sys.modules[__name__], str_2)

    score_A, score_B = play_loop(n, f, g)
    print("Score for Player A : {0}", score_A)
    print("Score for Player B : {0}", score_B)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter strategies for two player prisoner's dilemma game")
    parser.add_argument("-options", type=str, help="Available strategy options include : \
                            1. all_D \
                            2. randomer \
                            3. trusting_fool \
                            4. majority_seeker \
                            5. tft")
    parser.add_argument("--s1", help="enter a strategy for first (A) player \
                        See -h for all strategies avaiable", type=str)
    parser.add_argument("--s2", help="enter a strategy for second (B) player \
                        See -h for all strategies avaiable", type=str)
    args = parser.parse_args()
    main(args.s1, args.s2)
   
