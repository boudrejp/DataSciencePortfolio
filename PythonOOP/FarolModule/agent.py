## __author__ = John Boudreaux
import random
import FarolModule.strategy as strat

class agent:
    '''A class to store properties about agents for El Farol and minority
    problem games. Expects a memory length as an integer (default is 2),
    and a number of strategies as an integer'''

    def __init__(self, memory_length=3, num_strats=3):
        # need to select n at random from uniform distribution,
        # strategy at random from uniform distribution
        available_strats = strat.strategy.approved_strats
        self.current_strat = {"index": None, "expected_val": None, "go": None}

        self.strategies = {}
        for i in range(0, num_strats):
            picked_strat = random.choice(available_strats)
            picked_n = random.choice(list(range(1, memory_length+1)))
            self.strategies[i] = {'strat': strat.strategy(picked_strat, picked_n),\
                                  'n': picked_n, 'votes': 0,
                                 'strat_type': picked_strat}

    def select_and_eval_strat(self, history, cutoff_val, num_of_agents):
        # although it may seem a bit much to have both selection and evaluation
        # in one method, it will reduce the number of temporary objects
        votes_list = [self.strategies[i]['votes'] for i in range(len(self.strategies))]
        max_votes = max(votes_list)
        max_indices = [index for index, val in enumerate(votes_list) if val == max_votes]
        # choose the strategy with the most votes. if tied, choose random
        if len(max_indices) > 1:
            which_index = random.choice(max_indices)
        else:
            which_index = max_indices[0]
        active_strat = self.strategies[which_index]
        self.current_strat['index'] = which_index
        # evaluate the selected strategy, bring back the expected val
        # provide convenient vars for readability
        local_n = self.strategies[which_index]['n']
        local_strat_type = self.strategies[which_index]['strat'].strat_type
        expected_val = active_strat['strat'].strat_evaluate(num_of_agents, \
                       history, n = local_n, strat_type = local_strat_type)
        self.current_strat['expected_val'] = expected_val

        if expected_val < cutoff_val:
            self.current_strat['go'] = 1
        else:
            self.current_strat['go'] = 0

    def update_votes(self, winning_num):
        #function to update the votes for strategies
        which_index = self.current_strat['index']

        if self.current_strat['go'] == winning_num:
            self.strategies[which_index]['votes'] += 1
        else:
            self.strategies[which_index]['votes'] -= 1
