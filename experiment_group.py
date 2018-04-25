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
        self._borda_static = {'borda':0, 'copeland':0,'plurality':0, 'stv': 0}
        self._borda_iter = [0] * self._iterations
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
            for i in range(self._iterations):
                #get the borda at each iteration
                self._borda_iter[i] += e._borda_iters[i]
            
        #turn everything into an average
        self._borda_static['borda'] = self._borda_static['borda'] / self._experiments
        self._borda_static['copeland'] = self._borda_static['copeland'] / self._experiments
        self._borda_static['plurality'] = self._borda_static['plurality'] / self._experiments
        self._borda_static['stv'] = self._borda_static['stv'] / self._experiments
        self._borda_iter = [x / self._experiments for x in self._borda_iter]
    
    def visualize(self):
        x = range(self._iterations)
        y_0 = [self._borda_static['borda']] * self._iterations
        y_1 = [self._borda_static['copeland']] * self._iterations
        y_2 = [self._borda_static['plurality']] * self._iterations
        y_3 = [self._borda_static['stv']] * self._iterations
        y_4 = self._borda_iter
        plt.plot(x, y_0, x, y_1, x, y_2, x, y_3, x, y_4)