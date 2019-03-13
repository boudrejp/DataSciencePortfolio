# __author__ = John Boudreaux
import math
from FarolModule.agent import agent

class simulation:
    '''A class to house all the parameters for a simulation of the El Farol
    problem, and to store its outputs'''
    # going to need to pass all parameters through here, since agents are More
    # or less a child class, and strategies are a child class of agents

    def __init__(self, num_of_agents, iterations, cutoff_val, mem_length, num_strats):
        '''Simulation object expects agents of class agent,
         and a number of iterations that is an integer'''
        self.num_of_agents = num_of_agents
        self.mem_length = mem_length
        self.target_value = math.ceil(cutoff_val * self.num_of_agents)
        self.iterations = iterations
        self.num_strats = num_strats
        self.history = []
        # create an object to contain all the agents and create them
        self.agents = {}
        for i in range(self.num_of_agents):
            self.agents[i] = agent(memory_length = self.mem_length, num_strats = self.num_strats)


    def run_simulation(self):
        '''Code to loop through and run simulation. Takes variables from
        namespace of simulation'''
        print("Beginning simulation")
        for i in range(self.iterations):
            agents_going_to_bar = 0
            for j in range(len(self.agents)):
                self.agents[j].select_and_eval_strat(history = self.history, \
                cutoff_val = self.target_value, num_of_agents = self.num_of_agents)
                agents_going_to_bar += self.agents[j].current_strat['go']

            # if the total amount of agents at the bar is above the target value,
            # I would have had more fun staying home
            self.history.append(agents_going_to_bar)

            if agents_going_to_bar > self.target_value:
                winning_val = 0
            else:
                winning_val = 1

            for j in range(len(self.agents)):
                self.agents[j].update_votes(winning_val)

            if i == self.iterations / 2:
                print("50% Completed!")

        print("Simulation completed!")
