# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

import copy

# for step 2 of the hw
import matplotlib.pyplot as plt
import os

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        prev_values = util.Counter()

        values_02 = []

        # at v0, the value of every state will be 0
        for state in self.mdp.getStates():
            prev_values[state] = 0

        # for the next k iterations, we'll update the items of v_k using the 
        # static vector v_k-1 from the previous iteration
        for k in range(1, iterations + 1):
            
            # and at each iteration, we'll loop through the states and compute 
            # their respective values

            # outer loop is to compute new values for every state

            for state in self.mdp.getStates():

                # print(state)

                # for plotting the value of the state in the upper left corner
                if state == (0, 2):
                    values_02.append(self.values[state])

                max_value = float('-inf')
                # best_action = None

                # this loop is to compute the "max_a" (max over the actions) part of the Bellman equation
                for action in self.mdp.getPossibleActions(state):

                    # this loop is for computing the inner sum (over the states reachable from the current state)
                    # in the Bellman equation
                    expected = 0

                    for state_prime, prob in self.mdp.getTransitionStatesAndProbs(state, action):

                        # in here, we have the main part of the Bellman equation:
                        # using the transition function * (immediate reward + discounted future reward)
                        expected += prob * (self.mdp.getReward(state, action, state_prime) + discount * prev_values[state_prime])

                    # update our best values/actions if applicable
                    max_value = max(max_value, expected)

                # store the best value for this state in the final values dict
                # if there were no possible actions, max_value would not update so we'd keep the same value we had before
                self.values[state] = max_value if max_value != float('-inf') else prev_values[state]

            # since the assignment page specified to use a static vector for the v_k-1 iteration, instead of 
            # updating the values dict in-place, we'll store the values from this iteration to be used in the next one
            prev_values = copy.deepcopy(self.values)

        # plot the recorded values for (0, 2)
        plt.plot(list(range(len(values_02))), values_02, 'ro-')
        plt.title("Evolution of Value Iteration Values at State (0, 2)")
        plt.ylabel("Value")
        plt.xlabel("Iteration")
        plt.show()

        if not os.path.isdir("homework_journal/plots"):
            os.makedirs("homework_journal/plots")

        plt.savefig("homework_journal/plots/value_iteration_{}iters.png".format(iterations))

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        
        # this will be similar to what we did above (just using less of the Bellman eqn., since we're 
        # given a state and action already)
        
        # and this is based off of the separated equations for calculating V*(s) and Q*(s, a) from the Berkeley slides
        expected_q = 0

        for state_prime, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            expected_q += prob * (self.mdp.getReward(state, action, state_prime) + self.discount * self.values[state_prime])

        return expected_q

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        
        # now we just use the computed q-values for the given state and each possible action to find out which 
        # one we should take at this state

        max_val = float('-inf')
        best_action = None

        for action in self.mdp.getPossibleActions(state):
            q = self.computeQValueFromValues(state, action)

            if q > max_val:
                max_val = q
                best_action = action

        return best_action

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
