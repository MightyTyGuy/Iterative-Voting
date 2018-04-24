# Return a Condorcet winner if one exists
# or None otherwise
def get_condorcet_winner(candidates, ballots):
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

# Returns Borda score for each candidate
def borda_scores(candidates, ballots):
    scores = dict((candidate, 0) for candidate in candidates)
    for ballot in ballots:
        for i in range(len(ballot)):
            # Assuming ballots are valid
            candidate = ballot[i]
            scores[candidate] += len(ballot) - i - 1

    return scores

# Returns Borda ratio for the specified candidate
def get_borda_ratio(candidates, ballots, spec_candidate):
    scores = borda_scores(candidates, ballots)
    max_score = max(scores.values())
    return scores[spec_candidate] / max_score