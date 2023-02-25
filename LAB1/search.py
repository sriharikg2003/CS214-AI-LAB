# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
# import sys

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    dfs_stack = util.Stack()
    # dfs_stack maintains the stack of successors
    dfs_stack.push(problem.getStartState())

    explored_set= set()
    # exlored set contains the set of all explored_set nodes
    path=util.Stack()
    # path here is used to keep track of path to a node from the initial state instead of maintaining the parent
    path_list=util.Stack()
    # path_list maintaims list of path and keeps on getting popped so as to retain the final path at the end
    path_list.push([])
    while not dfs_stack.isEmpty():
        state=dfs_stack.pop()
        path= path_list.pop()
        if state not in explored_set:
            explored_set.add(state)
            # adding to explored_set because we are exploring all its successors now

            if problem.isGoalState(state):
                return path
                
    # Same algorithm as told in class

            for x in problem.getSuccessors(state):
                if  (x[0] not in explored_set):
                    dfs_stack.push(x[0])
                    path_list.push(path+[str(x[1])])


    return []



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # from util import *

    # very similar to depthFirstSearch except for usage of queue instead of stack
    bfs_queue = util.Queue()
    bfs_queue.push(problem.getStartState())

    path_list=util.Queue()
    path_list.push([])


    explored_set= set()
    path=util.Queue()

    while not bfs_queue.isEmpty():

        state=bfs_queue.pop()
        path=path_list.pop()

        explored_set.add(state)

        if problem.isGoalState(state):
            return path
    # Same algorithm as told in class
        for x in problem.getSuccessors(state):
            if (x[0] not in bfs_queue.list ) and (x[0] not in explored_set):
                bfs_queue.push(x[0])
                path_list.push(path+[str(x[1])])
                

    return []

    


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

# Slight changes in thought
# DFS  
    # start_state = problem.getStartState()
    # q_coordinates = util.Stack()
    # q_directions = util.Stack()
    # visited_coordinates = [] 
    # q_coordinates.push(start_state)
    # q_directions.push([])

    # if problem.isGoalState(start_state):
    #     return []
    
    # while not q_coordinates.isEmpty():
    #     current_state = q_coordinates.pop() 
    #     direction = q_directions.pop()
    #     if current_state not in visited_coordinates : 
    #         visited_coordinates.append(current_state)

    #         if problem.isGoalState(current_state):
    #             return direction
                
    #         for successor , heading_direction , k in problem.getSuccessors(current_state):
    #             new_directions = direction + [heading_direction]
    #             q_coordinates.push(successor)
    #             q_directions.push(new_directions)
            
            
    
    # util.raiseNotDefined()

# bfs

#     start_state = problem.getStartState()
#     q_coordinates = util.Queue()
#     q_directions = util.Queue()
#     visited_coordinates = [] 
#     q_coordinates.push(start_state)
#     q_directions.push([])

#     if problem.isGoalState(start_state):
#         return []
    
#     while not q_coordinates.isEmpty():
#         current_state = q_coordinates.pop() 
#         direction = q_directions.pop()
#         if current_state not in visited_coordinates : 
#             visited_coordinates.append(current_state)

#             if problem.isGoalState(current_state):
#                 return direction

#             for successor , heading_direction , k in problem.getSuccessors(current_state):
#                 new_directions = direction + [heading_direction]
#                 q_coordinates.push(successor)
#                 q_directions.push(new_directions)
            

    
#     util.raiseNotDefined()