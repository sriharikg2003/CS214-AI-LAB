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

   
    util.raiseNotDefined()



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
  
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first.
    
    
    """
    start = problem.getStartState() 

    #Priority queue containing the coordinates of the node and the cost along with path to reach it
    ptqueue = util.PriorityQueue() 
    
    ptqueue.update((problem.getStartState(),[]),0)
  
    temppath=[]

    #Dictionary containing cost of action reaching to the node from the best path to reach it so far
    visited = {}  
    visited[start] = 0

    
    while not ptqueue.isEmpty(): 

        # Pops the node with the least cost of action
        cordinates,path_to_current = ptqueue.pop()
       
        
        # Check for the Minimum reachable goal state
        if problem.isGoalState(cordinates):
         
            return path_to_current
        
        # Get all the successors
        succ = problem.getSuccessors(cordinates)

        for point,dir,cost in succ :

        # condition to update the cost of action to already existing nodes and also to enter the new node along with its cost
            if point not in visited or cost + visited[cordinates] < visited[point] :
            
                visited[point] = cost + visited[cordinates]

                # Path to reach the current point obtained from the previous path through its parent
                temppath=path_to_current+[dir]

                # Calculates the cost of the current node from the sequence of path to reach it 
                newcost=problem.getCostOfActions(temppath)

                # Adds the node to Priority Queue 
                ptqueue.push((point,temppath),newcost)
              
    return []





def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #Priority queue containing the coordinates of the node and the cost along with path to reach it
    options = util.PriorityQueue()

    #pushing start state into the priority queue .
    start = problem.getStartState()
    start_heu = heuristic(start , problem) 
    options.push((start , [] , 0) , start_heu)
    
    #list to keep track of already visited nodes 
    visited = []
    

    while not options.isEmpty() :
        #pops the node with least cost of action 
        cordinates , direction , cost = options.pop()
        
        #check for minimum reachable goal state 
        if(problem.isGoalState(cordinates)):
            return direction

        # condition to update the cost of action to already existing nodes and also to enter the new node along with its cost
        if cordinates not in visited : 
            visited.append(cordinates)

            for xy , dir , succ_cost in problem.getSuccessors(cordinates) : 
                if xy not in visited : 
                    # Path to reach the current point obtained from the previous path through its parent
                    actions = list(direction) + [dir]
                    
                    # Calculates the cost of the current node from the sequence of path to reach it
                    cost_so_far = problem.getCostOfActions(actions)
                     # Calculates the heuristic from current node to the goal node
                    heu_so_far = heuristic(xy , problem)
                    
                    # Adds the node to Priority Queue
                    options.push((xy , actions , 1) , cost_so_far + heu_so_far)
    return [] 
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
