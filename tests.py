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
    # Test BestResponseAgent (Non-truth-biased)
    candidates = ['j','b','s']

    b1 = ['j','b','s','k']
    b2 = ['j','s','b','k']
    b3 = ['s','j','b','k']
    b4 = ['s','b','j','k']
    b5 = ['b','s','j','k']
    b6 = ['k','j','s','b']

    p1 = [b1, b2, b3, b4, b5, b6]

    ag1 = agent.BestResponseAgent(b5, agent.linear_util)
    ag2 = agent.BestResponseAgent(b6, agent.linear_util)

    assert ag1.vote() == 'b'
    assert ag2.vote() == 'k'
    results = {'j': 2, 's': 2, 'b': 1, 'k': 1}
    ag1.adapt(results)
    assert ag1.vote() == 's'

    results = {'j': 2, 's': 3, 'b': 0, 'k': 1}
    ag2.adapt(results)
    assert ag2.vote() == 'j'

    results = {'j':3, 's': 3, 'b': 0, 'k': 0}
    ag1.adapt(results)
    # Non-truth bias: Maintain vote
    assert ag1.vote() == 's'

def t12():
    # Test BestResponseAgent (Truth Biased)
    candidates = ['j','b','s']

    b1 = ['j','b','s','k']
    b2 = ['j','s','b','k']
    b3 = ['s','j','b','k']
    b4 = ['s','b','j','k']
    b5 = ['b','s','j','k']
    b6 = ['k','j','s','b']

    p1 = [b1, b2, b3, b4, b5, b6]

    ag1 = agent.BestResponseAgent(b5, agent.linear_util, True)
    ag2 = agent.BestResponseAgent(b6, agent.linear_util, True)

    assert ag1.vote() == 'b'
    assert ag2.vote() == 'k'
    results = {'j': 2, 's': 2, 'b': 1, 'k': 1}
    ag1.adapt(results)
    assert ag1.vote() == 's'

    results = {'j': 2, 's': 3, 'b': 0, 'k': 1}
    ag2.adapt(results)
    assert ag2.vote() == 'j'

    results = {'j':3, 's': 3, 'b': 0, 'k': 0}
    ag1.adapt(results)
    # Truth bias
    assert ag1.vote() == 'b'

def t13():
    # Test 3-PragmatistAgent
    candidates = ['j','b','s','k']

    b1 = ['j','b','s','k']
    b2 = ['j','s','b','k']
    b3 = ['j','s','k','b']
    b4 = ['s','j','b','k']
    b5 = ['s','b','j','k']
    b6 = ['b','s','j','k']
    b7 = ['b','j','s','k']
    b8 = ['k','s','j','b']

    p1 = [b1, b2, b3, b4, b5, b6, b7, b8]

    ag1 = agent.PragmatistAgent(b8, agent.linear_util)
    assert ag1.vote() == 'k'
    results = {'j': 3, 's': 2, 'b': 2, 'k': 1}
    ag1.adapt(results)
    assert ag1.vote() == 's'

def t14():
    # Test LearningAgent
    candidates = ['j','b','s','k']

    b1 = ['j','b','s','k']
    b2 = ['j','s','b','k']
    b3 = ['j','s','k','b']
    b4 = ['s','j','b','k']
    b5 = ['s','b','j','k']
    b6 = ['b','s','j','k']
    b7 = ['b','j','s','k']
    b8 = ['k','s','j','b']

    p1 = [b1, b2, b3, b4, b5, b6, b7, b8]

    ag1 = agent.LearningAgent(b8, agent.linear_util)
    util = {'k': 1, 's': 2/3, 'j': 1/3, 'b': 0}
    for c in util:
        assert math.isclose(util[c], ag1._util[c])
    assert ag1.vote() == 'k'

    results = {'j': 3, 's': 2, 'b': 2, 'k': 1}
    ag1.adapt(results)

    new_util = {'k': 28/30, 's': 2/3, 'j': 1/3, 'b': 0}
    # Adjusted Expected Utility, same True Utility
    for c in new_util:
        assert math.isclose(new_util[c], ag1._exp_util[c])
    for c in util:
        assert math.isclose(util[c], ag1._util[c])
    assert ag1.vote() == 'k'

    ag1.adapt(results)

    new_util = {'k': 131/150, 's': 2/3, 'j': 1/3, 'b': 0}
    # Adjusted Expected Utility, same True Utility
    for c in new_util:
        assert math.isclose(new_util[c], ag1._exp_util[c])
    for c in util:
        assert math.isclose(util[c], ag1._util[c])
    assert ag1.vote() == 'k'

    # After 7 iterations, agent should change vote
    for _ in range(2,7):
        ag1.adapt(results)
    assert ag1._exp_util['k'] < 2/3
    for c in util:
        assert math.isclose(util[c], ag1._util[c])
    assert ag1.vote() == 's'

def t15():
    # Test LearningBestResponseAgent
    candidates = ['j','b','s','k']

    b1 = ['j','b','s','k']
    b2 = ['j','s','b','k']
    b3 = ['j','s','k','b']
    b4 = ['s','j','b','k']
    b5 = ['s','b','j','k']
    b6 = ['b','s','j','k']
    b7 = ['b','j','s','k']
    b8 = ['k','s','j','b']

    p1 = [b1, b2, b3, b4, b5, b6, b7, b8]

    ag1 = agent.LearningBestResponseAgent(b8, agent.linear_util)
    util = {'k': 1, 's': 2/3, 'j': 1/3, 'b': 0}
    for c in util:
        assert math.isclose(util[c], ag1._util[c])
    assert ag1.vote() == 'k'

    results = {'j': 3, 's': 2, 'b': 2, 'k': 1}
    ag1.adapt(results)

    new_util = {'k': 14/15, 's': 19/30, 'j': 1/3, 'b': 0}
    # Adjusted Expected Utility, same True Utility
    for c in new_util:
        assert math.isclose(new_util[c], ag1._exp_util[c])
    for c in util:
        assert math.isclose(util[c], ag1._util[c])
    assert ag1.vote() == 'k'

    results = {'j': 3, 's': 2, 'b': 2, 'k': 1}
    ag1.adapt(results)

    new_util = {'k': 131/150, 's': 181/300, 'j': 1/3, 'b': 0}
    # Adjusted Expected Utility, same True Utility
    for c in new_util:
        assert math.isclose(new_util[c], ag1._exp_util[c])
    for c in util:
        assert math.isclose(util[c], ag1._util[c])
    assert ag1.vote() == 'k'

def t16():
    # Test LearningBayesianAgent
    candidates = ['j','b','s','k']

    b1 = ['j','b','s','k']
    b2 = ['j','s','b','k']
    b3 = ['j','s','k','b']
    b4 = ['s','j','b','k']
    b5 = ['s','b','j','k']
    b6 = ['b','s','j','k']
    b7 = ['b','j','s','k']
    b8 = ['k','s','j','b']

    p1 = [b1, b2, b3, b4, b5, b6, b7, b8]

    ag1 = agent.LearningBayesianAgent(b8, agent.linear_util)
    util = {'k': 1, 's': 2/3, 'j': 1/3, 'b': 0}
    for c in util:
        assert math.isclose(util[c], ag1._util[c])

    exp_util = {'k': 1/4, 's': 1/6, 'j': 1/12, 'b': 0}
    for c in exp_util:
        assert math.isclose(exp_util[c], ag1._exp_util[c])
    assert ag1.vote() == 'k'

    results = {'j': 3, 's': 2, 'b': 2, 'k': 1}
    ag1.adapt(results)

    exp_prop = {'k': 2/12, 's': 3/12, 'j': 4/12, 'b': 3/12}
    for c in exp_prop:
        assert math.isclose(exp_prop[c], ag1._exp_prop[c])

    new_util = {'k': 2/12, 's': 2/12, 'j': 1/9, 'b': 0}
    # Adjusted Expected Utility, same True Utility
    for c in new_util:
        assert math.isclose(new_util[c], ag1._exp_util[c])
    for c in util:
        assert math.isclose(util[c], ag1._util[c])
    assert ag1.vote() == 'k' or ag1.vote() == 's'

if __name__ == '__main__':
    tests = [t1,  t2,  t3,  t4,\
             t5,  t6,  t7,  t8,\
             t9,  t10, t11, t12,\
             t13, t14, t15, t16]

    for test in tests:
        test()