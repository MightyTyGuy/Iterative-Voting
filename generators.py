import random

# Create a profile of n ballots with 
# Impartial Culture Assumption
def impartial_culture(candidates, n, alpha = None):
    return [random.sample(candidates, len(candidates)) for _ in range(n)]

# Create a profile of n ballots with
# the Polya-Eggenberger Model
# Algorithm adapted from "Learning Agents For Iterative Voting"
def polya_eggenberger(candidates, n, alpha):
    N = []
    beta = 1 / alpha - 1
    for i in range(n):
        p = random.random()
        if p < beta / (beta + len(N)):
            v = random.sample(candidates, len(candidates))
        else:
            v = N[random.randint(0, len(N) - 1)]
        N.append(v)

    return N
