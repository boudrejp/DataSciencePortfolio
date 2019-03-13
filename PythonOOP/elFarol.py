# A script to run the main routine of simulating the El Farol problem
# background: https://en.wikipedia.org/wiki/El_Farol_Bar_problem

import random
import math
import sys
import FarolModule.agent as agent
import FarolModule.simulation as simulation
import FarolModule.strategy as strategy
import matplotlib.pyplot as plt

# fun text from: https://www.messletters.com/en/big-text/
print("")
print(""":::::::::: :::         ::::::::::     :::     :::::::::   ::::::::  :::
:+:        :+:         :+:          :+: :+:   :+:    :+: :+:    :+: :+:
+:+        +:+         +:+         +:+   +:+  +:+    +:+ +:+    +:+ +:+
+#++:++#   +#+         :#::+::#   +#++:++#++: +#++:++#:  +#+    +:+ +#+
+#+        +#+         +#+        +#+     +#+ +#+    +#+ +#+    +#+ +#+
#+#        #+#         #+#        #+#     #+# #+#    #+# #+#    #+# #+#
########## ##########  ###        ###     ### ###    ###  ########  ##########  """)

print("")
print("Let's run a simulation of the El Farol problem. I'll need a few parameters...")
print("")

# user input for parameter selection
iterations = int(input("Select a number of iterations for your simulation (integer value): "))
num_of_agents = int(input("Select a number of agents for your simulation (integer value): "))
mem_length = int(input("Select a number for the length of the agent memories (integer value): "))
num_strats = int(input("Select a number of strategies for each agent (integer value): "))
cutoff = int(input("Select a cutoff percentage (integer value): ")) / 100
seed = int(input("Choose a seed value (integer value): "))
logging = input("Do you want to save a log file? [y/n]: ").lower()
if logging != 'y' and logging != 'n':
    raise ValueError("Invalid input for logging- must choose y or n")

plot_option = input("Moving average plot or plot each iteration? [ma] or [it]: ")
if plot_option == "ma":
    moving_avg_num = int(input("Select a number of iterations for moving average plot: "))
elif plot_option != "it":
    raise ValueError("Invalid input for plot options- must choose ma or it")

# for reproducibility
random.seed(seed)

print("")
# create and run the simulation
el_farol = simulation.simulation(num_of_agents, iterations, cutoff, mem_length, num_strats)
el_farol.run_simulation()

# plotting
if plot_option == "it":
    # create chart of each iteration
    title_string = "El Farol Bar Attendance"

    plt.plot(el_farol.history)
    plt.axis([0, iterations, 0, num_of_agents])
    plt.title(title_string)
    plt.show()

elif plot_option == "ma":
    # create moving average from history
    moving_avg = []
    history_length = len(el_farol.history)

    for i in range(history_length- moving_avg_num):
        if i < moving_avg_num:
            moving_avg_val = sum(el_farol.history[0:i+1])/\
                             len(el_farol.history[0:i+1])
        else:
            moving_avg_val = sum(el_farol.history[i-moving_avg_num:i+1])/\
                             len(el_farol.history[i-moving_avg_num:i+1])
        moving_avg.append(moving_avg_val)

    # create moving average chart
    title_string = "El Farol Bar Attendance: " + str(moving_avg_num) +\
                   "-point Moving Average"

    plt.plot(moving_avg)
    plt.axis([0, iterations, 0, num_of_agents])
    plt.title(title_string)
    plt.show()

# log the results
def log_results(iterations, num_of_agents, mem_length, cutoff, seed, history):
    '''A function that will take the results of a simulation and write them into
    a log file in the repository to use for further analysis'''
    iter_string = "Iterations: " + str(iterations)
    agents_string = "Number of agents: " + str(num_of_agents)
    mem_string = "Agent memory length: " + str(mem_length)
    cutoff_string = "Attendance percentage cutoff: " + str(cutoff * 100)
    seed_string = "Random seed: " + str(seed)

    log_string = iter_string + "\n" + agents_string + "\n" +\
                 mem_string + "\n" + cutoff_string + "\n" +\
                 seed_string + "\n\n" + "History: " + "\n" +\
                 ', '.join(map(str, el_farol.history))

    fh = open("Farol_logfile.txt", "w")
    fh.writelines(log_string)
    fh.close()
    print("Log file created in this directory at 'Farol_logfile.txt'")

if logging == "y":
    log_results(iterations, num_of_agents, mem_length, cutoff, seed, el_farol.history)
