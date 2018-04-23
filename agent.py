from abc import ABC, abstractmethod
import copy

class Agent(ABC):
    def __init__(self, pref_order, util_func):
        self._pref_order = pref_order
        self._util_func = util_func
        self._util = dict((pref_order[i], self._util_func(i)) for i in range(len(pref_order)))
        self._exp_util = copy.deepcopy(self._util)
        self._prev_vote = None
        self._to_vote = None

    def get_preference(self):
        return self._pref_order

    # Using plurality voting rules,
    # determine the utility of an outcome
    def result_utility(self, results):
        winner = min(results.keys(), key=(lambda key: (-results[key], key)))
        return self._util[winner]

    # Returns a single candidate based
    # on the agent's state
    def vote(self):
        # If no future vote is set, vote for the candidate
        # with the highest expected utility
        if self._to_vote is None:
            self._to_vote = max(self._exp_util.keys(), key=(lambda key: self._exp_util[key]))
        
        # Mark the previous vote, reset the future vote,
        # and return the vote
        self._prev_vote = self._to_vote
        self._to_vote = None
        return self._prev_vote

    @abstractmethod
    # Receives results in the form of a dictionary
    # With candidates and their vote totals
    def adapt(self, results):
        pass

class BestResponseAgent(Agent):
    def __init__(self, pref_order, util_func, truth_bias = False):
        super().__init__(pref_order, util_func)
        self._truth_bias = truth_bias

    def adapt(self, results):
        # Compute best response
        if self._prev_vote is not None:
            curr_util = self.result_utility(results)
            manip_results = copy.deepcopy(results)
            response_util = {}
            for candidate in self._pref_order:
                # Try a different candidate, fixing all
                # other votes
                manip_results[self._prev_vote] -= 1
                manip_results[candidate] += 1
                # Determine utility of manipulating in this way
                manip_utility = self.result_utility(manip_results)
                response_util[candidate] = manip_utility
                # Reset the votes to previous results
                manip_results[self._prev_vote] += 1
                manip_results[candidate] -= 1

            # Set next vote to the manipulation which yields the highest utility
            # If no manipulation yields highest utility, hold vote fixed for unbiased agent,
            # Or vote for most preferred candidate with equality utility if biased
            self._to_vote = max(response_util.keys(), key=(lambda key: (response_util[key], self._util[key])))

            if not self._truth_bias and response_util[self._to_vote] == curr_util:
                self._to_vote = self._prev_vote
            
class PragmatistAgent(Agent):
    def __init__(self, pref_order, util_func, num_pragmatists = 3):
        super().__init__(pref_order, util_func)
        self._num_pragmatists = min(num_pragmatists, len(pref_order))

    def adapt(self, results):
        # Set next vote to the most preferred candidate among
        # the num_pragmatists most voted-for candidates
        top_candidates = sorted(results.keys(), key=(lambda key: (-results[key], key)))[:self._num_pragmatists]
        self._to_vote = max(top_candidates, key=(lambda key: self._util[key]))

class LearningAgent(Agent):
    def __init__(self, pref_order, util_func, learning_rate = 0.1):
        super().__init__(pref_order, util_func)
        self._learning_rate = learning_rate
    
    def adapt(self, results):
        # Compute the winner of the plurality election
        winner = min(results.keys(), key=(lambda key: (-results[key], key)))

        # Update the voted-for candidate
        if self._prev_vote is not None:
            self._exp_util[self._prev_vote] = self._learning_rate * self._util[winner] + \
                (1 - self._learning_rate) * self._exp_util[self._prev_vote]

class LearningBayesianAgent(Agent):
    def __init__(self, pref_order, util_func, learning_rate = 0.1):
        super().__init__(pref_order, util_func)
        self._learning_rate = learning_rate
        # Initially assume that the proportions are
        # Distributed according to a Dirichlet(1,1,...,1) distribution
        # (Analogous to uniform distribution); so expected
        # proportions are the mean of the Dirichlet - alpha_i / sum(alpha_i)
        # Set expected utility accordingly
        self._Dirichlet_params = dict((candidate, 1) for candidate in pref_order)
        for candidate in self._pref_order:
            self._exp_util[candidate] = self._util[candidate] * self.exp_prop()[candidate] 
    
    def exp_prop(self):
        sum_alpha = sum(self._Dirichlet_params.values())
        return dict((candidate, self._Dirichlet_params[candidate] / sum_alpha) for candidate in self._Dirichlet_params)
    
    def adapt(self, results):
        # Compute the winner of the plurality election
        winner = min(results.keys(), key=(lambda key: (-results[key], key)))

        # Update all candidates using Bayesian update
        for candidate in self._pref_order:
            self._Dirichlet_params[candidate] = results[candidate] + self._Dirichlet_params[candidate]
            self._exp_util[candidate] = self._learning_rate * self._util[candidate] * self.exp_prop()[candidate] + \
                (1 - self._learning_rate) * self._exp_util[candidate]