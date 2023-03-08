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
import random

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
        
        for k in range(self.iterations):
            copy = self.values.copy()
            for state in self.mdp.getStates() : 
                if self.mdp.isTerminal(state):
                    # if the state is terminal value = 0
                    copy[state] = 0
                    continue 
                Qmax = -99999999999
    
                for action in self.mdp.getPossibleActions(state) : 
                    Qval = self.computeQValueFromValues(state , action)
                    if Qval > Qmax : 
                        Qmax = Qval  
                        # updating the maximum value 
                copy[state] = Qmax
                # All these changes are made to a copy of the original Counter
            self.values = copy 
            # New Counter is now made as Old Counter



    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        # return the value of the state
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        Qval = 0 
        if self.mdp.isTerminal(state):
            # return the Q-value 0 if the state is terminal
            return 0 

        for pairs in self.mdp.getTransitionStatesAndProbs(state, action) : 
        # For a given state and action we find the expaected value by considering all the non deterministic actions with their transition probabilities and rewards
            Qval += pairs[1]*(self.mdp.getReward(state , action , pairs[0]) + self.discount * self.getValue(pairs[0]))
        return Qval
        # Calculated Q-value is returned
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
        if self.mdp.isTerminal(state):
            return None 
        temp_counter= util.Counter()
        for action in self.mdp.getPossibleActions(state):
            temp_counter[action] = self.computeQValueFromValues(state, action)

        best_action = temp_counter.argMax()
        return best_action
      

        # Another way of doing this is :         
        #     # terminal state has no action to execute
        # Qmax = -99999999
        # best_action = [] 
        # for action in  self.mdp.getPossibleActions(state) : 
        #     #take all actions possible in a given state 
        #     value_for_this_action = self.computeQValueFromValues(state , action)
        #     # storing the value for this action temporarily
        #     # Now compute the best value
        #     if value_for_this_action > Qmax :
        #         best_action = [action]
        #         Qmax = value_for_this_action 
        #     if value_for_this_action == Qmax : 
        #         best_action.append(action)
        #         # adds all those actions having maximum value
        # return random.choice(best_action)
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)