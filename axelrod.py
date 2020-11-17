#!/usr/bin/env python3

''' Axelrod's Tournament '''
import random
import argparse
import sys

# Parameters and Assumptions
R, S, T, P = 3, 0, 5, 1          # payoffs

payoff_mat = [ [(R,R), (S,T)],   # 0th payoff values belong to player A and 1st payoff 
               [(T,S), (P,P)] ]  # values belong to player B (other player)

w = 0.95                          # w > (T-R)/(T-P) & (T-R)/(R-S)
choices = [0,1]                  # 0 = Cooperate, 1 = Defect

# -------------------SIMPLE STRATEGIES----------------------------
# TODO : Refactor strategies into its own module

# ALL Defect (ALL D)
def all_D(self_hist, opp_hist):
    ''' no matter what,
        always DEFECT
    '''
    return choices[1]

# Random choice (randomer)
def randomer(self_hist, opp_hist):
    ''' randomly select a 
        choice 
    '''
    return random.choice(choices)

# Trusting Fool
def trusting_fool(self_hist, opp_hist):
    ''' no matter what,
        always COOPERATE
    '''
    return choices[0]

# Majority Seeker
def majority_seeker(self_hist, opp_hist):
    ''' cooperate on the first round,
        in subsequent rounds, check history of
        other player's moves, see what move
        was in majority, pick that as current move
    '''
    opp_total_moves = len(opp_hist)
    opp_defect_moves = len(list(filter(lambda x : x == choices[1], opp_hist)))
    current_move = choices[0] 
    if not opp_total_moves:     # first move is to cooperate
        return current_move
    else:
        if opp_total_moves and opp_defect_moves / opp_total_moves >= 0.5:
            current_move = choices[1]
        else:
            current_move = choices[0]
    return current_move

# Tit-For-Tat 
def tft(self_hist, opp_hist):
    ''' cooperate in the first move
        then, do whatever the other 
        did in the previous move
    '''
    current_move = choices[0]
    if not len(opp_hist):      # first move is to cooperate
        return current_move
    else:                      # do whatever opponent did in previous move
        prev_move = len(opp_hist) - 2
        current_move = opp_hist[prev_move]
    return current_move

#Alternating C and D
def alt(self_hist, opp_hist):
    ''' alternate between C and D,
        starting with C initially
    '''
    n = len(self_hist)
    if n % 2 == 0:
        return choices[0]
    else:
        return choices[1]

#-------------------------------------------------------------------

def play_loop(n, f, g, p_hist=False):
    ''' play a game with f and g as the strategies 
        for player A and B respectively for n iterations.

        default p_hist = False -> do you want to save
        history of move by both players separately? 
    '''
    plays_A = []                   # history of all plays ('c' or 'd') by player A
    plays_B = []                   # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ B
    game_history = []              # keeps track of all game moves by two players
    for i in range(n):
        plays_A.append(f(plays_A, plays_B))
        plays_B.append(g(plays_B, plays_A))
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

def nth_prob(i):
    ''' return probability of ith interaction'''
    return w**i

def show_moves(play):
    ''' given a history of plays by
        any player return a human readable
        output list
    '''
    moves = list(map(lambda x : 'D' if x else 'C' , play))
    return moves

def play_loop_score(hist): 
    '''given a game history as list hist
        return the total score for each player 
         based from the payoff matrix
    '''
    score_A = 0.0
    score_B = 0.0
    i = 0
    for strat in hist:
        score_A += nth_prob(i)*payoff_mat[strat[0]][strat[1]][0]
        score_B += nth_prob(i)*payoff_mat[strat[0]][strat[1]][1]
        i += 1
    return score_A, score_B


def main(str_1, str_2, n, show):
    n = n                                       # number of iterations of game
    f = getattr(sys.modules[__name__], str_1)
    g = getattr(sys.modules[__name__], str_2)

    score_A, score_B = play_loop(n, f, g, show)
    print("Score for Player A : {:.3f}".format(score_A))
    print("Score for Player B : {:.3f}".format(score_B))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter strategies for two player Prisoner's Dilemma game")
    # TODO -options is help only, not argument, FIX
    parser.add_argument("-options", type=str, help="Available strategy options include : \
                            1. all_D \
                            2. randomer \
                            3. trusting_fool \
                            4. majority_seeker \
                            5. tft \
                            6. alt")
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
   
