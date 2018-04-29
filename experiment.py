import evaluation
import elections
from event import event
import agent

class experiment:
    
    def __init__(self, agent_util_func, generator_func, c, n, exp_num, \
                 exp_rep, meta_file, res_file, iterations, alpha = None):
        self._iterations = iterations
        self._candidates = list(range(c))
        #generate preference orderings
        self._ballots = generator_func(self._candidates, n, alpha)
        self._generator = generator_func
        self._util = agent_util_func
        self._alpha = alpha
        #get condorcet winner
        self._cond_winner = evaluation.get_condorcet_winner(self._candidates, self._ballots)
        #determine if there is a condorcet winner
        if self._cond_winner == None:
            self._isCond = False
        else:
            self._isCond = True
        # ExpNum denotes the ID of experiments with the same parameters
        # ExpRep denotes which repetition of the experiment
        self._expnum = exp_num
        self._exprep = exp_rep
        self._c = c
        self._n = n
        self._meta = meta_file
        self._res = res_file
        self.getStaticResults() #write these to a file
        self._learning = event(agent.LearningAgent, agent_util_func, 
                               self._ballots, self._candidates)
        self._bestresponse = event(agent.BestResponseAgent, agent_util_func, 
                               self._ballots, self._candidates)
        self._bayes = event(agent.LearningBayesianAgent, agent_util_func, 
                               self._ballots, self._candidates)
        self._learnbr = event(agent.LearningBestResponseAgent, agent_util_func,
                              self._ballots, self._candidates)
        self._prag = event(agent.PragmatistAgent, agent_util_func,
                           self._ballots, self._candidates)
        self.run()
    
    def run(self):
        with open(self._res, 'a') as res:
            for i in range(self._iterations):
                borda = {}
                cond = {}
                borda['learn'], cond['learn'] = self._learning.iterate()
                borda['bestres'], cond['bestres'] = self._bestresponse.iterate()
                borda['bayes'], cond['bayes'] = self._bayes.iterate()
                borda['learnbr'], cond['learnbr'] = self._learnbr.iterate()
                borda['prag'], cond['prag'] = self._prag.iterate()
                res.write(str(self._expnum) + " " + str(self._exprep) + " " + str(i) + " " + \
                          str(borda['learn']) + " " + str(cond['learn']) + " " + \
                          str(borda['bestres']) + " " + str(cond['bestres']) \
                          + " " + str(borda['bayes']) + " " + str(cond['bayes']) + " " + \
                          str(borda['learnbr']) + " " + str(cond['learnbr']) + " " + \
                          str(borda['prag']) + " " + str(cond['prag']) + "\n")
                
    
    def getStaticResults(self):
        borda = {}
        cond = {}
        
        #run borda election
        winner = elections.borda(self._candidates, self._ballots)
        #determine condorcet
        if winner == self._cond_winner:
            cond['borda'] = True
        else:
            cond['borda'] = False
        #get borda score for winner
        borda['borda'] = evaluation.get_borda_ratio(self._candidates, self._ballots, winner)
        
        #run plurality election
        winner = elections.plurality(self._candidates, self._ballots)
        #determine condorcet
        if winner == self._cond_winner:
            cond['plur'] = True
        else:
            cond['plur'] = False
        #get borda score for winner
        borda['plur'] = evaluation.get_borda_ratio(self._candidates, self._ballots, winner)
        
        #run copeland election
        winner = elections.copeland(self._candidates, self._ballots)
        #determine condorcet
        if winner == self._cond_winner:
            cond['cope'] = True
        else:
            cond['cope'] = False
        #get borda score
        borda['cope'] = evaluation.get_borda_ratio(self._candidates, self._ballots, winner)
        
        #run stv election
        winner = elections.stv(self._candidates, self._ballots)
        #determine condorcet
        if winner == self._cond_winner:
            cond['stv'] = True
        else:
            cond['stv'] = False
        #get borda score
        borda['stv'] = evaluation.get_borda_ratio(self._candidates, self._ballots, winner)
        
        with open(self._meta, 'a') as meta:
            meta.write(str(self._expnum) + " " + str(self._exprep) + " " +  self._util.__name__ + \
                       " " + self._generator.__name__ + " " + str(self._alpha) + " " + \
                       str(self._n) + " " + str(self._c) + " " + str(self._iterations) + " " + \
                       str(borda['borda']) + " " + str(borda['cope']) + " " + str(borda['plur']) + \
                       " " + str(borda['stv']) + " " + str(self._isCond) + " " + str(cond['borda']) \
                       + " " + str(cond['cope']) + " " + str(cond['plur']) + " " + \
                       str(cond['stv']) + "\n")