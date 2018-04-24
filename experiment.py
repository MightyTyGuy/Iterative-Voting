class experiment:
    
    def __init__(self, agent_init_func, agent_util_func, election_func, generator_func, c, n, alpha = None):
        self._candidates = list(range(c))
        ballots = generator_func(self._candidates, n, alpha)
        self._agents = []
        for b in ballots:
            self._agents.append(agent_init_func(b, agent_util_func))
        self._election_func = election_func
        self._c = c
        self._n = n
        self._iterations = 0
    
    def iterate(self, iterations = 1):
        #determine votes from each agent
        votes = []
        for a in self._agents:
            votes.append([a.vote()])
        
        #compute the results of the election
        results = self._election_func(self._candidates, votes)
        
        #adapt agents so they respond in future elections
        for a in self._agents:
            a.adapt(results)
        
        #add iterations just to keep track of it in case we want it
        self._iterations += iterations
        
        return results
