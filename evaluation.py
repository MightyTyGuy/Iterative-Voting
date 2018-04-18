# Return a Condorcet winner if one exists
# or None otherwise
def condorcet(candidates, ballots):
    pair_votes = {}

    # Count the number of ballots where i beats j for each pair
    for ballot in ballots:
        for i in range(len(ballot)):
            for j in range(i+1, len(ballot)):
                # i beats j in this ranking
                candidate_i = ballot[i]
                candidate_j = ballot[j]

                pair_votes[(candidate_i, candidate_j)] = pair_votes.get((candidate_i, candidate_j), 0) + 1

    for potential_condorcet in candidates:
        condorcet = True
        for other_candidate in candidates:
            win_count = pair_votes.get((potential_condorcet, other_candidate), 0)
            lose_count = pair_votes.get((other_candidate, potential_condorcet), 0)
            if  win_count < lose_count:
                condorcet = False
                continue
        if condorcet:
            return potential_condorcet
    
    return None

# Return Condorcet Efficiency Ratio
# Takes a candidate list,
# a list of profiles and a list of winners
def condorcet_efficiency(candidates, profiles, winners):
    assert len(profiles) == len(winners)
    
    cond_elections = []

    for i in range(len(profiles)):
        cond_winner = condorcet(candidates, profiles[i])
        if cond_winner is not None:
            if cond_winner == winners[i]:
                cond_elections.append(True)
            else:
                cond_elections.append(False)
    
    return sum(cond_elections) / len(cond_elections)

# Returns Borda score for each candidate
def borda_scores(candidates, ballots):
    scores = dict((candidate, 0) for candidate in candidates)
    for ballot in ballots:
        for i in range(len(ballot)):
            # Assuming ballots are valid
            candidate = ballot[i]
            scores[candidate] += len(ballot) - i - 1

    return scores

# Return the average ratio of Borda score 
# to maximal Borda score among all candidates
# across all profiles
def avg_borda_ratio(candidates, profiles, winners):
    assert len(profiles) == len(winners)

    ratios = []

    for i in range(len(profiles)):
        scores = borda_scores(candidates, profiles[i])
        max_score = max(scores.values())
        winner_score = scores[winners[i]]

        ratios.append(winner_score / max_score)

    return sum(ratios) / len(ratios)