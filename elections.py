import itertools

# Borda count
def borda(candidates, ballots):
    scores = dict((candidate, 0) for candidate in candidates)
    for ballot in ballots:
        for i in range(len(ballot)):
            # Assuming ballots are valid
            candidate = ballot[i]
            scores[candidate] += len(ballot) - i - 1
    
    # Report winner, breaking ties lexicographically
    return min(scores.keys(), key=(lambda key: (-scores[key], key)))

# Simple plurality
def plurality_counts(candidates, ballots):
    scores = dict((candidate, 0) for candidate in candidates)
    for ballot in ballots:
        candidate = ballot[0]
        scores[candidate] += 1
    
    return scores
    
def plurality(candidates, ballots):
    # Report winner, breaking ties lexicographically
    scores = plurality_counts(candidates, ballots)
    return min(scores.keys(), key=(lambda key: (-scores[key], key)))

# Copeland scores
def copeland(candidates, ballots):
    pair_votes = {}

    # Count the number of ballots where i beats j for each pair
    for ballot in ballots:
        for i in range(len(ballot)):
            for j in range(i+1, len(ballot)):
                # i beats j in this ranking
                candidate_i = ballot[i]
                candidate_j = ballot[j]

                pair_votes[(candidate_i, candidate_j)] = pair_votes.get((candidate_i, candidate_j), 0) + 1

    # Initialize Copeland scores
    scores = dict((candidate, 0) for candidate in candidates)

    # Tally the number of pairwise elections where a beats b
    for pair in itertools.combinations(candidates, 2):
        if pair_votes.get(pair, 0) > pair_votes.get(pair[::-1], 0):
            scores[pair[0]] += 1
        elif pair_votes.get(pair, 0) < pair_votes.get(pair[::-1], 0):
            scores[pair[1]] += 1
        else:
            scores[pair[0]] += 0.5
            scores[pair[1]] += 0.5

    # Report winner, breaking ties lexicographically
    return min(scores.keys(), key=(lambda key: (-scores[key], key)))

# Single Transferable Vote
def stv(candidates, ballots):
    scores = dict((candidate, 0) for candidate in candidates)

    # Give each first ranked candidate a vote
    for ballot in ballots:
        candidate = ballot[0]
        scores[candidate] += 1

    # Initialize the current vote indices and the
    # list of eliminated candidates
    curr_votes = [0 for ballot in ballots]
    eliminated = []

    while max(scores.values()) <= len(ballots) / 2:
        # Eliminate lowest candidate
        min_candidate = min(scores.keys(), key=(lambda key: scores[key]))
        eliminated.append(min_candidate)
        del scores[min_candidate]

        # Transfer votes
        for ballot_index in range(len(ballots)):
            ballot = ballots[ballot_index]
            to_transfer = False
            while ballot[curr_votes[ballot_index]] in eliminated:
                to_transfer = True
                curr_votes[ballot_index] += 1
            if to_transfer:
                candidate = ballot[curr_votes[ballot_index]]
                scores[candidate] += 1

    # Report winner, breaking ties lexicographically
    return min(scores.keys(), key=(lambda key: (-scores[key], key)))
