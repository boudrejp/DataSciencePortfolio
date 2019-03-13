# Design Document
Overall design proposal for Project 1 by John Boudreaux

## Background
* Simulations of the El Farol problem
  * https://en.wikipedia.org/wiki/El_Farol_Bar_problem

The overall goal of this project would be to run simulations around the El Farol problem,\
which tries to answer the question "should I go to the bar tonight?" The underlying premises\
are that there is a threshold value of people at the bar that, above the threshold\
the bar is too crowded and you would have had more fun at home, and below the threshold\
you would have had more fun at the bar. All of the decision making "agents" must\
make a decision to go out or stay in at the same time, and will adjust their strategies\
to try to maximize their happiness. Each agent will have a slightly different willingness\
to change their strategy, but each will have the same memory length (unless it \
looks like I need more lines of code, then maybe we look at agents of different \
memory lengths).

This is a fundamental problem in complexity theory, and shows how even very random\
situations can lead to emergent behavior. Because of this, I think adding graphing\
capabilities to this project would help people understand that. I think I will only\
add graphing if it seems like I have already met the other requirements.

## Dependencies
* math
* random
* *In scope or out of scope... matplotlib? Seaborn?*


## Object based considerations
* Class Simulation
  * attributes:
    * num_of_iterations
    * num_of_agents
    * set_seed
    * threshold
    * memory_length
    * dict_bar_attendance
  * methods:
    * run_simulation
    * go_to_bar
* Class agent(dict)
  * attributes:
    * strategies
    * willingness_to_change
  * methods:
    * evaluate_best_strategy
    * adjust_strategy_weights
* *Question as to whether this is in scope or out of scope: Graphing via seaborn or matplotlib*
