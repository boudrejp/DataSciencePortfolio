# __author__ = John Boudreaux
import random

class strategy:
    '''An object to contain different types of strategies for the El Farol
    problem that can be adopted by different agents. Expects a "strat_type" arg,
    which descibes the type of strategy adopted. Valid strategy options include:
    "same_as_past", which picks a strategy from n iterations ago,
    "flip", which takes the number of attendees at week n and subtracts it
    from the total number of agents,
    "minimum_of_last", which will return the minimum attendees from
    the last n iterations,
    "avg", which takes the average of the past n weeks,
    "maximum_of_last", which will return the maximum attendees from the last
    n iterations'''

    approved_strats = ["same_as_past", "flip", "minimum_of_last", "avg", \
                       "maximum_of_last", "rand_n"]

    def __init__(self, strat_type, n):
        if strat_type not in strategy.approved_strats:
            raise ValueError("Please pick an approved strategy from documentation")
        else:
            self.strat_type =  strat_type
            self.n = n

    def strat_evaluate(self, num_of_agents, history, n, strat_type):
        '''A script to evaluate the strategy for a given agent and the history'''
        # note to self: I wish Python had a convenient switch/case protocol
        # all scripts here follow similar order: what to do if the length of the
        # history is zero, then if it is less than the required n, and then the
        # general case.

        if strat_type == "same_as_past":
            if len(history) < n:
                if len(history) == 0:
                    expected_num = 0
                else:
                    expected_num = history[0]
            else:
                expected_num = history[len(history)-n]

        elif strat_type == "flip":
            if len(history) < n:
                expected_num = num_of_agents
            else:
                expected_num = num_of_agents - history[len(history)-n]

        elif strat_type == "minimum_of_last":
            if len(history) < n:
                if len(history) == 0:
                    expected_num = 0
                else:
                    valid_search = history[0:len(history)]
                    expected_num = min(valid_search)
            else:
                valid_search = history[(len(history)-n):len(history)]
                expected_num = min(valid_search)

        elif strat_type == "maximum_of_last":
            if len(history) < n:
                if len(history) == 0:
                    expected_num = num_of_agents
                else:
                    valid_search = history[0:len(history)]
                    expected_num = max(valid_search)
            else:
                valid_search = history[(len(history)-n):len(history)]
                expected_num = max(valid_search)

        elif strat_type == "avg":
            if len(history) < n:
                if len(history) == 0:
                    expected_num = round(num_of_agents / 2)
                else:
                    valid_search = history[0:len(history)]
                    expected_num = round(sum(valid_search)/len(valid_search))
            else:
                valid_search = history[(len(history)-n):len(history)]
                expected_num = round(sum(valid_search)/len(valid_search))

        elif strat_type == "rand_n":
            if len(history) < n:
                if len(history) == 0:
                    expected_num = round(num_of_agents / 2)
                else:
                    valid_search = history[0:len(history)]
                    expected_num = random.choice(valid_search)
            else:
                valid_search = history[(len(history)-n):len(history)]
                expected_num = random.choice(valid_search)

        return(expected_num)
