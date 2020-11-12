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

                max_value = float('-inf')
                best_action = None

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
                    if expected > max_value:
                        max_value = expected
                        best_action = action

                # store the best value for this state in the final values dict
                self.values[state] = max_value

            # since the assignment page specified to use a static vector for the v_k-1 iteration, instead of 
            # updating the values dict in-place, we'll store the values from this iteration to be used in the next one
            prev_values = self.values


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
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
