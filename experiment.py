import evaluation
import elections

class experiment:
    
    def __init__(self, agent_init_func, agent_util_func, generator_func, c, n, alpha = None):
        self._candidates = list(range(c))
        #generate preference orderings
        self._ballots = generator_func(self._candidates, n, alpha)
        #get condorcet winner
        self._cond_winner = evaluation.get_condorcet_winner(self._candidates, self._ballots)
        #determine if there is a condorcet winner
        if self._cond_winner == None:
            self._isCond = False
        else:
            self._isCond = True
        #create agents
        self._agents = []
        for b in self._ballots:
            self._agents.append(agent_init_func(b, agent_util_func))
        self._c = c
        self._n = n
        self._iterations = 0
        self._borda_static = {}
        self._cond_static = {}
        self.getStaticResults(self._ballots)
        self._borda_iters = []
        self._cond_iters = []
        self._results = []
        
    def getStaticResults(self):
        #run borda election
        winner = elections.borda(self._candidates, self._ballots)
        #determine condorcet
        if winner == self._cond_winner:
            self._cond_static['borda'] = True
        else:
            self._cond_static['borda'] = False
        #get borda score for winner
        self._borda_static['borda'] = evaluation.get_borda_ratio(self._candidates, self._ballots, winner)
        
        #run plurality election
        winner = elections.plurality(self._candidates, self._ballots)
        #determine condorcet
        if winner == self._cond_winner:
            self._cond_static['plurality'] = True
        else:
            self._cond_static['plurality'] = False
        #get borda score for winner
        self._borda_static['plurality'] = evaluation.get_borda_ratio(self._candidates, self._ballots, winner)
        
        #run copeland election
        winner = elections.copeland(self._candidates, self._ballots)
        #determine condorcet
        if winner == self._cond_winner:
            self._cond_static['copeland'] = True
        else:
            self._cond_static['copeland'] = True
        #get borda score
        self._borda_static['copeland'] = evaluation.get_borda_ratio(self._candidates, self._ballots, winner)
        
        #run stv election
        winner = elections.stv(self._candidates, self._ballots)
        #determine condorcet
        if winner == self._cond_winner:
            self._cond_static['stv'] = True
        else:
            self._cond_static['stv'] = True
        #get borda score
        self._borda_static['stv'] = evaluation.get_borda_ratio(self._candidates, self._ballots, winner)
        
    def iterate(self, iterations = 1):
        for i in range(iterations):
            #determine votes from each agent
            votes = []
            for a in self._agents:
                votes.append(a.vote())
            
            #compute the results of the election
            results = elections.plurality_counts(self._candidates, votes)
            
            #keep track of results at each iteration
            self._results.append(results)
            
            #adapt agents so they respond in future elections
            for a in self._agents:
                a.adapt(results)
            
            #add iterations just to keep track of it in case we want it
            self._iterations += iterations
            
            #compute the winner of the election
            winner = min(results.keys(), key=(lambda key: (-results[key], key)))
            #get borda and condorcet scores
            self._borda_iters.append(evaluation.get_borda_ratio(self._candidates, self._ballots, winner))
            if winner == self._cond_winner:
                self._cond_iters.append(True)
            else:
                self._cond_iters.append(False)
        
        return results