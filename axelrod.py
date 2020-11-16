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

# Trusting Fool
def trusting_fool():
    ''' no matter what,
        always COOPERATE
    '''
    return choices[0]

# Play a game with strategies f and g, n times and report the score for each strategy
def play_loop(n,f,g, p_hist=False):
    plays_A = []      # history of all plays ('c' or 'd') by player A
    plays_B = []      # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ B
    game_history = [] # keeps track of all game moves by two players
    for i in range(n):
        plays_A.append(f())
        plays_B.append(g())
        game_history.append((plays_A[i], plays_B[i]))
    score_A, score_B = play_loop_score(game_history)
    if p_hist:
        moves_A = show_moves(plays_A)
        moves_B = show_moves(plays_B)
        with open('moves.txt', 'w') as f:
            f.write('A' + '   |   ' + 'B' + '\n')
            f.write('---------' + '\n')
            for i in range(len(moves_A)):
                f.write(moves_A[i] + '   |   ' + moves_B[i] + '\n')
    return score_A, score_B

def show_moves(play):
    ''' given a history of plays by
        any player return a human readable
        output list
    '''
    moves = list(map(lambda x : 'D' if x else 'C' , play))
    return moves

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


def main(str_1, str_2, n, show):
    n = n                                       # number of iterations of game
    f = getattr(sys.modules[__name__], str_1)
    g = getattr(sys.modules[__name__], str_2)

    score_A, score_B = play_loop(n, f, g, show)
    print("Score for Player A : {0}", score_A)
    print("Score for Player B : {0}", score_B)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter strategies for two player Prisoner's Dilemma game")
    # TODO -options is help only, not argument, FIX
    parser.add_argument("-options", type=str, help="Available strategy options include : \
                            1. all_D \
                            2. randomer \
                            3. trusting_fool \
                            4. majority_seeker \
                            5. tft")
    parser.add_argument("--s1", default="all_D", help="enter a strategy for first (A) player \
                        See -h for all strategies avaiable", type=str)
    parser.add_argument("--s2", default="all_D", help="enter a strategy for second (B) player \
                        See -h for all strategies avaiable", type=str)
    parser.add_argument("--n", help="enter number of games between the two players with \
                        s1 and s2 as their strategies. \
                        See -h for all strategies avaiable", type=int, default=100)
    parser.add_argument("--show", help="Write the moves made by both players in output file \
                        './moves.txt' \
                        See -h for all strategies avaiable", type=bool, default=False)
    args = parser.parse_args()
    main(args.s1, args.s2, args.n, args.show)
   
