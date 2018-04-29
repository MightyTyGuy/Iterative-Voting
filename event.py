import evaluation
import elections

class event:
    
    def __init__(self, agent_init_func, agent_util_func, ballots, candidates):
        self._candidates = candidates
        self._ballots = ballots
        #get condorcet winner
        self._cond_winner = evaluation.get_condorcet_winner(self._candidates, self._ballots)
        #create agents
        self._agents = []
        for b in self._ballots:
            self._agents.append(agent_init_func(b, agent_util_func))
        
    def iterate(self, iterations = 1):
        for i in range(iterations):
            #determine votes from each agent
            votes = []
            for a in self._agents:
                votes.append([a.vote()])
            
            #compute the results of the election
            results = elections.plurality_counts(self._candidates, votes)
            
            #adapt agents so they respond in future elections
            for a in self._agents:
                a.adapt(results)
            
            #compute the winner of the election
            winner = elections.plurality(self._candidates, votes)
            #get borda and condorcet scores
            borda_rat = evaluation.get_borda_ratio(self._candidates, self._ballots, winner)
            cond = False
            if winner == self._cond_winner:
                cond = True
        
        return borda_rat, cond