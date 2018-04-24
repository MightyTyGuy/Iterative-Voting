import experiment

class experiment_group:
    
    def __init__(self, agent_type, agent_util, generator, n, c, iterations, experiments, alpha = None):
        self._agent = agent_type
        self._util = agent_util
        self._generator = generator
        self._n = n
        self._c = c
        self._iterations = iterations
        self._experiments = experiments
        self._alpha = alpha
        self._list = []
    
    def run(self):
        for i in range(self._experiments):
            e = experiment(self._agent, self._util, self._generator, self._c, self._n, self._alpha)
            e.iterate(self.__iterations)
            self._list.append(e)