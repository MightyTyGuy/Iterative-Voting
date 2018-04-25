from experiment import experiment
from matplotlib import pyplot as plt

class experiment_group:
    
    def __init__(self, agent_type, agent_util, generator, n, c, iterations, experiments, alpha = None):
        self._agent = agent_type
        self._util = agent_util
        self._generator = generator
        self._n = n
        self._c = c
        self._iterations = iterations
        #experiments should be an integer telling how many experiments there are
        self._experiments = experiments
        self._alpha = alpha
        #create empty list to hold all experiments
        self._list = []
        self._borda_static = {'borda': 0, 'copeland':0,'plurality':0, 'stv': 0}
        #keep track of average borda score at each iteration
        self._borda_iter = [0] * self._iterations
        #keep track of total number of experiments with condorcet winner
        self._cond_total = 0
        #keep track of condorcet efficiency
        self._cond_static = {'borda': 0, 'copeland':0,'plurality':0, 'stv': 0}
        self._cond_iters = [0] * self._iterations
        self.run()
        self.computeStats()
        
    
    def run(self):
        for i in range(self._experiments):
            e = experiment(self._agent, self._util, self._generator, self._c, self._n, self._alpha)
            e.iterate(self._iterations)
            self._list.append(e)
    
    def computeStats(self):
        for e in self._list:
            #get the static values. For now there's just a sum
            self._borda_static['borda'] += e._borda_static['borda']
            self._borda_static['copeland'] += e._borda_static['copeland']
            self._borda_static['plurality'] += e._borda_static['plurality']
            self._borda_static['stv'] += e._borda_static['stv']
            #determine if there is a condorcet winner
            if e._isCond:
                #keep track of total experiments with condorcet winner
                self._cond_total += 1
                #keep track of how many of each election type get the condorcet winner
                if e._cond_static['borda']:
                    self._cond_static['borda'] += 1
                if e._cond_static['copeland']:
                    self._cond_static['copeland'] += 1
                if e._cond_static['plurality']:
                    self._cond_static['plurality'] += 1
                if e._cond_static['stv']:
                    self._cond_static['stv'] += 1
                #keep track of which iteration picked condorcet winner
                for i in range(self._iterations):
                    if e._cond_iters[i]:
                        self._cond_iters[i] += 1
                        self._borda_iter[i] += e._borda_iters[i]
            else:
                #this if else statement is just to not have to loop through twice
                for i in range(self._iterations):
                    #get the borda at each iteration
                    self._borda_iter[i] += e._borda_iters[i]
            
        #turn everything into an average
        self._borda_static['borda'] = self._borda_static['borda'] / self._experiments
        self._borda_static['copeland'] = self._borda_static['copeland'] / self._experiments
        self._borda_static['plurality'] = self._borda_static['plurality'] / self._experiments
        self._borda_static['stv'] = self._borda_static['stv'] / self._experiments
        self._borda_iter = [x / self._experiments for x in self._borda_iter]
        self._cond_static['borda'] = self._cond_static['borda'] / self._cond_total
        self._cond_static['copeland'] = self._cond_static['copeland'] / self._cond_total
        self._cond_static['plurality'] = self._cond_static['plurality'] / self._cond_total
        self._cond_static['stv'] = self._cond_static['stv'] / self._cond_total
        self._cond_iters = [x / self._cond_total for x in self._cond_iters]
        
    def visualize_borda(self, title = ""):
        x = range(self._iterations)
        y_0 = [self._borda_static['borda']] * self._iterations
        y_1 = [self._borda_static['copeland']] * self._iterations
        y_2 = [self._borda_static['plurality']] * self._iterations
        y_3 = [self._borda_static['stv']] * self._iterations
        y_4 = self._borda_iter
        plt.plot(x, y_0, label = "Borda")
        plt.plot(x, y_1, label = "Copeland")
        plt.plot(x, y_2, label = "Plurality")
        plt.plot(x, y_3, label = "STV")
        plt.plot(x, y_4, label = "Iterative")
        plt.legend()
        plt.xlabel('Iterations')
        plt.ylabel('Borda Score')
        plt.title(title)
        plt.show()
    
    def visualize_condorcet(self, title = ""):
        x = range(self._iterations)
        y_0 = [self._cond_static['borda']] * self._iterations
        y_1 = [self._cond_static['copeland']] * self._iterations
        y_2 = [self._cond_static['plurality']] * self._iterations
        y_3 = [self._cond_static['stv']] * self._iterations
        y_4 = self._cond_iters
        plt.plot(x, y_0, label = "Borda")
        plt.plot(x, y_1, label = "Copeland")
        plt.plot(x, y_2, label = "Plurality")
        plt.plot(x, y_3, label = "STV")
        plt.plot(x, y_4, label = "Iterative")
        plt.legend()
        plt.xlabel('Iterations')
        plt.ylabel('Condorcet Efficiency')
        plt.title(title)
        plt.show()