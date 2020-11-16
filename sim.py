#!/usr/bin/env python3

import random
''' Simulation of Two Person symmetric Prisoner's Dilemma Game with the following parameters

    R (reward for cooperation)          = 3
    S (sucker's choice)                 = 0
    T (defection score)                 = 5
    P (punishment for mutual defection) = 1

    Each player (A and B) is assumed to be a rational agent such that
    they maximize their payoff
'''

# Parameters and Assumptions
R, S, T, P = 3, 0, 5, 1   # payoffs

payoff_mat = [ [(R,R), (S,T)],   # 0th payoff values belong to player A and 1st payoff 
               [(T,S), (P,P)] ]  # values belong to player B (other player)

w = 0.7                        # w > (T-R)/(T-P) & (T-R)/(R-S)

choices = [0,1]                # Cooperate = 0 and Defect = 1
def strategy():
    ''' 
      pick a strategy at random 
    '''
    return random.choice(choices)

# One-time Game
def play():
    ''' play a one time prisoner's
        dilemma game
    '''
    A = strategy() #player A's strategy
    B = strategy() #player A's strategy

    return payoff_mat[A][B][0] # return player A's payoff

# play One-time game n times

if __name__ == "__main__":
    # definition of the game, must hold
    assert T > R > P > S
    assert R > (S + T)/2
    print(play())
