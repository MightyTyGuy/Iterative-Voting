import agent, elections, evaluation, generators
import math

# Unit testing
# generators.py
def t1():
    # Generate an ICA profile of 10 voters for 4 candidates
    profile = generators.impartial_culture(['j','b','s','k'], 10)
    print('Verify appearance of ICA Profile:', profile)
    assert len(profile) == 10
    for pref in profile:
        assert len(pref) == 4

def t2():
    # Generate a Polya-Eggenberger Profile of 10 voters for 4 candidates
    profile = generators.polya_eggenberger(['j','b','s','k'], 10, .3)
    print('Verify appearance of Polya-Eggenberger Profile:', profile)
    assert len(profile) == 10
    for pref in profile:
        assert len(pref) == 4

# evaluation.py
def t3():
    # Verify Condorcet Efficiency calculation
    candidates = ['j','b','s']

    b1 = ['j','b','s']
    b2 = ['j','b','s']
    b3 = ['s','j','b']
    b4 = ['s','b','j']
    b5 = ['b','s','j']

    p1 = [b1, b2, b3, b4, b5] # No Condorcet winner
    p2 = [b1, b1, b1, b2, b3, b4, b5] # 'j' is Condorcet winner

    cws = [evaluation.get_condorcet_winner(candidates, p) for p in [p1, p2]]

    assert cws[0] is None
    assert cws[1] == 'j'

def t4():
    # Verify Borda-Ratio calculation
    candidates = ['j','b','s']

    b1 = ['j','b','s']
    b2 = ['j','b','s']
    b3 = ['s','j','b']
    b4 = ['s','b','j']
    b5 = ['b','s','j']
    b6 = ['b','s','j']

    p1 = [b1, b2, b3, b4, b5, b6]

    scores = evaluation.borda_scores(candidates, p1)

    assert scores['j'] == 5
    assert scores['b'] == 7
    assert scores['s'] == 6
    
    assert math.isclose(evaluation.get_borda_ratio(candidates, p1, 'j'), 5/7)
    assert math.isclose(evaluation.get_borda_ratio(candidates, p1, 'b'), 1)
    assert math.isclose(evaluation.get_borda_ratio(candidates, p1, 's'), 6/7)

# elections.py
def t5():
    # Test Borda election
    candidates = ['j','b','s']

    b1 = ['j','b','s']
    b2 = ['j','b','s']
    b3 = ['s','j','b']
    b4 = ['s','b','j']
    b5 = ['b','s','j']
    b6 = ['b','s','j']

    p1 = [b1, b2, b3, b4, b5, b6] # 'b' should win

    assert elections.borda(candidates, p1) == 'b'

def t6():
    # Test plurality
    candidates = ['j','b','s']

    b1 = ['j','b','s']
    b2 = ['j','b','s']
    b3 = ['s','j','b']
    b4 = ['s','b','j']
    b5 = ['b','s','j']
    b6 = ['b','s','j']
    b7 = ['j','s','b']

    p1 = [b1, b2, b3, b4, b5, b6, b7] # 'j' should win

    counts = elections.plurality_counts(candidates, p1)
    assert counts['j'] == 3
    assert counts['s'] == 2
    assert counts['b'] == 2

    assert elections.plurality(candidates, p1) == 'j'

def t7():
    # Test Copeland
    candidates = ['j','b','s']

    b1 = ['j','b','s']
    b2 = ['j','b','s']
    b3 = ['s','j','b']
    b4 = ['s','b','j']
    b5 = ['b','s','j']

    p2 = [b1, b1, b1, b2, b3, b4, b5] # 'j' is Condorcet winner

    assert elections.copeland(candidates, p2) == 'j'

def t8():
    # Test STV
    candidates = ['j','b','s']

    b1 = ['j','b','s']
    b2 = ['j','s','b']
    b3 = ['s','j','b']
    b4 = ['s','b','j']
    b5 = ['b','s','j']

    p1 = [b1, b2, b3, b4, b5]

    assert elections.stv(candidates, p1) == 's'

def t9():
    # Test lexicographic tie breaking
    candidates = ['j','b','s']

    b1 = ['j','b','s']
    b2 = ['j','s','b']
    b3 = ['s','j','b']
    b4 = ['s','b','j']
    b5 = ['b','s','j']
    b6 = ['b','j','s']

    p1 = [b1, b2, b3, b4, b5, b6]

    # b should win by lexicographic tie breaking
    assert elections.borda(candidates, p1) == 'b'
    assert elections.plurality(candidates, p1) == 'b'
    assert elections.copeland(candidates, p1) == 'b'
    assert elections.stv(candidates, p1) == 'b'

def t10():
    # Test utility functions
    a = [1, 3/4, 2/4, 1/4, 0]
    b = [1, 1/2, 1/4, 1/8, 1/16]
    c = [1 - 1 / (1 + math.exp(-2 * (i - 2))) for i in range(4)]

    for i in range(4):
        assert math.isclose(agent.linear_util(i, 5), a[i])
        assert math.isclose(agent.exp_util(i, 5), b[i])
        assert math.isclose(agent.log_util(i, 5), c[i])

def t11():
    # Test BestResponseAgent
    pass

def t12():
    # Test 3-PragmatistAgent
    pass

def t13():
    # Test LearningAgent
    pass

def t14():
    # Test LearningBestResponseAgent
    pass

def t15():
    # Test LearningBayesianAgent
    pass

if __name__ == '__main__':
    tests = [t1, t2,  t3,  t4,\
             t5, t6,  t7,  t8,\
             t9, t10, t11, t12,\
             t13, t14, t15]

    for test in tests:
        test()