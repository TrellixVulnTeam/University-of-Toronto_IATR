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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # util.raiseNotDefined()

    open = util.Stack()
    open_item_for_start = ([problem.getStartState()], [], 0)
    open.push(open_item_for_start)


    while not open.isEmpty():
        p = open.pop()
        path = p[0]
        final_of_path = path[-1]
        dir_path = p[1]
        accum_cost = p[2]

        if problem.isGoalState(final_of_path):
            return dir_path

        for successor in problem.getSuccessors(final_of_path):
            successor_pos = successor[0]

            successor_action = successor[1]
            successor_cost = successor[2]

            if successor_pos not in path:
                # print('!!!!!!!!!!!')
                # print(path)
                # print(successor_pos)
                stack_item = (path + [successor_pos], dir_path + [successor_action], accum_cost+successor_cost)
                open.push(stack_item)
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    open = util.Queue()
    open_item_for_start = (problem.getStartState(), [], 0)
    open.push(open_item_for_start)
    # print('!!!!!!!!!!!!!\n')
    # print(problem.getStartState())
    visited_dict = {problem.getStartState():0}

    while not open.isEmpty():
        p = open.pop()
        final_of_path = p[0]
        path = p[1]
        accum_cost = p[2]
        if accum_cost <= visited_dict[final_of_path]:
            if problem.isGoalState(final_of_path):

                return path

            for successor in problem.getSuccessors(final_of_path):
                successor_pos = successor[0]
                successor_action = successor[1]
                successor_cost = successor[2]
                new_accum_cost = accum_cost + successor_cost

                if successor_pos not in visited_dict:
                    queue_item = (successor_pos, path + [successor_action], new_accum_cost)
                    open.push(queue_item)
                    visited_dict[successor_pos] = new_accum_cost
                else:
                    if new_accum_cost < visited_dict[successor_pos]:
                        # print('*****************************\n')
                        queue_item = (successor_pos, path + [successor_action], new_accum_cost)
                        open.push(queue_item)
                        visited_dict[successor_pos] = new_accum_cost
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    open = util.PriorityQueue()
    open_item_for_start = (problem.getStartState(), [], 0)
    open.push(open_item_for_start, 0)

    visited_dict = {}

    while not open.isEmpty():
        p = open.pop()
        final_of_path = p[0]
        path = p[1]
        accum_cost = p[2]

        if final_of_path not in visited_dict:
            visited_dict[final_of_path] = True
            if problem.isGoalState(final_of_path):
                return path

            for successor in problem.getSuccessors(final_of_path):
                successor_pos = successor[0]
                successor_action = successor[1]
                successor_cost = successor[2]
                if successor_pos not in visited_dict:
                    #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                    queue_item = (successor_pos, path + [successor_action], accum_cost + successor_cost)
                    open.push(queue_item, accum_cost + successor_cost)
                else:
                    #check if corresponding item priority in heap is lower
                    for i in range(len(open.heap)):
                        old_priority = open.heap[i][0]
                        count = open.heap[i][1]
                        state = open.heap[i][2][0]
                        new_priority = accum_cost + successor_cost
                        if state == successor_pos and new_priority < old_priority:
                            new_item = (successor_pos, path + [successor_action], new_priority)
                            new_entry = (old_priority, count, new_item)
                            open.heap[i] = new_entry
                            open.update(new_item, new_priority)

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
    # util.raiseNotDefined()
    open = util.PriorityQueue()
    f = 0 + heuristic(problem.getStartState(), problem)
    open_item_for_start = (problem.getStartState(), [], 0)
    open.push(open_item_for_start, f)

    visited_dict = {problem.getStartState():0}

    while not open.isEmpty():
        priority_lst = [entry[0] for entry in open.heap]
        min_priority = min(priority_lst)
        min_count = priority_lst.count(min_priority)

        if min_count != 1:
            g_value_lst = []
            item_lst = []
            for i in range(min_count):
                item = open.pop()
                g_value = item[2]

                g_value_lst.append(g_value)
                item_lst.append(item)

            while len(g_value_lst) > 0:
                local_max = max(g_value_lst)
                item_index = g_value_lst.index(local_max)

                open.push(item_lst[item_index], min_priority)

                g_value_lst.remove(g_value_lst[item_index])
                item_lst.remove(item_lst[item_index])


        p = open.pop()
        final_of_path = p[0]
        path = p[1]
        accum_cost = p[2]

        if accum_cost <= visited_dict[final_of_path]:
            if problem.isGoalState(final_of_path):
                return path

            for successor in problem.getSuccessors(final_of_path):
                successor_pos = successor[0]
                successor_action = successor[1]
                successor_cost = successor[2]
                h = heuristic(successor_pos, problem)
                new_cost = accum_cost + successor_cost
                new_priority = new_cost + h
                if successor_pos not in visited_dict:
                    #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                    queue_item = (successor_pos, path + [successor_action], new_cost)
                    open.push(queue_item, new_priority)
                    visited_dict[successor_pos] = new_cost
                else:
                    #check if corresponding item priority in heap is lower
                    if new_cost < visited_dict[successor_pos]:
                        new_item = (successor_pos, path + [successor_action], new_cost)
                        open.push(new_item, new_priority)
                        visited_dict[successor_pos] = new_cost
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
