# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"
        #calculate food score
        food_score = 0
        cur_pos = newPos
        def find_next_min_food(unvisited_foods, cur_pos):
            min = util.manhattanDistance(unvisited_foods[0], cur_pos)
            res_pos = unvisited_foods[0]
            for f_pos in unvisited_foods:
                f_distance = manhattanDistance(f_pos, cur_pos)
                if (f_distance < min):
                    min = f_distance
                    res_pos = f_pos
            return min, res_pos

        unvisited_foods = newFood.asList()
        while len(unvisited_foods) > 0:
            distance, next_food = find_next_min_food(unvisited_foods, cur_pos)
            unvisited_foods.remove(next_food)
            food_score += distance
            cur_pos = next_food


        # calculate ghostScore
        ghost_score = 0
        for ghoststate in newGhostStates:
            dist = manhattanDistance(newPos, ghoststate.getPosition())
            # ghost is too close
            if dist < 4:
                ghost_score -= dist

        score = ghost_score + 1 / (1+food_score)
        return score

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # initilize -infinity for Pacman
        value = float('-inf')

        next_action = Directions.STOP
        for action in gameState.getLegalActions(self.index):
            successor_game_state = gameState.generateSuccessor(self.index, action)

            temp_value = self.calculate_min_value(successor_game_state, 0, 1)
            if temp_value > value:
                value = temp_value
                next_action = action

        return next_action


    def calculate_max_value(self,state, depth, agent):
        if depth == self.depth:
            return self.evaluationFunction(state)
        else:
            if (state.isLose() or state.isWin()):
                value = self.evaluationFunction(state)
            else:
                actions = state.getLegalActions(agent)
                value = float('-inf')

                for action in actions:
                    next_state = state.generateSuccessor(agent, action)
                    cur_value = self.calculate_min_value(next_state, depth, 1)
                    if cur_value > value:
                        value = cur_value
            return value


    def calculate_min_value(self, state, depth, agent):
        if depth == self.depth:
            return self.evaluationFunction(state)
        else:
            #initialize  infinity for MIN
            if (state.isLose() or state.isWin()):
                value = self.evaluationFunction(state)
            else:
                value = float('inf')

                actions = state.getLegalActions(agent) #actions for agent 1 at first time
                for action in actions:
                    if agent == state.getNumAgents() - 1:
                        #last agent, ready go to next layer
                        next_state = state.generateSuccessor(agent, action)
                        cur_value = self.calculate_max_value(next_state, depth + 1, 0)
                        if cur_value < value:
                            value = cur_value
                    else:
                        # update state since ghost is not counted completely
                        next_state = state.generateSuccessor(agent, action)
                        cur_value = self.calculate_min_value(next_state, depth, agent + 1)
                        if cur_value < value:
                            value = cur_value

            return value





class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        value = float('-inf')
        alpha = float('-inf')
        beta = float('inf')

        next_action = Directions.STOP
        for action in gameState.getLegalActions(self.index):
            successor_game_state = gameState.generateSuccessor(self.index, action)

            temp_value = self.alpha_beta(successor_game_state, 0, 1, alpha, beta)
            if temp_value > value:
                value = temp_value
                next_action = action

            if value >= beta:
                return value
            alpha = max(alpha, value)

        return next_action

    def alpha_beta(self, state, depth, agent, alpha, beta):
        if depth == self.depth or state.isLose() or state.isWin():
            return self.evaluationFunction(state)
        else:
            if agent == 0:
                # agent is MAX
                value = float('-inf')
            else:
                value = float('inf')

            actions = state.getLegalActions(agent)
            for action in actions:
                next_state = state.generateSuccessor(agent, action)
                if agent == 0: #MAX
                    nxt_value = self.alpha_beta(next_state, depth, 1, alpha, beta)
                    if value < nxt_value:
                        value = nxt_value

                    if value >= beta:
                        return value

                    alpha = max(alpha, value)
                else: #MIN
                    if agent == state.getNumAgents() - 1:
                        nxt_value = self.alpha_beta(next_state, depth + 1, 0, alpha, beta)
                        if value > nxt_value:
                            value = nxt_value


                    else:
                        nxt_value = self.alpha_beta(next_state, depth, agent+1, alpha, beta)
                        if nxt_value < value:
                            value = nxt_value

                    if value <= alpha:
                        return value

                    beta = min(beta, value)
            return value



class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        value = float('-inf')

        next_action = Directions.STOP
        for action in gameState.getLegalActions(self.index):
            successor_game_state = gameState.generateSuccessor(self.index, action)

            temp_value = self.expectimax(successor_game_state, 0, 1)
            if temp_value > value:
                value = temp_value
                next_action = action
        return next_action


    def expectimax(self, state, depth, agent):
        if depth == self.depth or state.isLose() or state.isWin():
            return self.evaluationFunction(state)
        else:
            if agent == 0:
                # agent is MAX
                value = float('-inf')
            else:
                value = 0

            actions = state.getLegalActions(agent)
            for action in actions:
                next_state = state.generateSuccessor(agent, action)
                if agent == 0: #MAX
                    nxt_value = self.expectimax(next_state, depth, 1)
                    if value < nxt_value:
                        value = nxt_value

                else: #MIN
                    if agent == state.getNumAgents() - 1:
                        value += self.expectimax(next_state, depth + 1, 0)

                    else:
                        value += self.expectimax(next_state, depth, agent+1)

            if agent == 0:
                return value
            else:
                return value / len(actions)

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION:
    Win: inf
    Lose: -inf
    x1: cloest manhattan distance sum (Pacman and available foods)
    x2: number of food remaining
    x3: sum of ghost scared time
    x4: if Pacman is too close to a ghost
    x5: available capsule
    """
    "*** YOUR CODE HERE ***"
    food_lst = currentGameState.getFood().asList()
    Pacman_pos = currentGameState.getPacmanPosition()
    GhostStates = currentGameState.getGhostStates()
    cupsules = currentGameState.getCapsules()

    #print(len(cupsules))

    if currentGameState.isWin():
        return float('inf')
    elif currentGameState.isLose():
        return -float('inf')

    food_score = 0
    cur_pos = Pacman_pos

    def find_next_min_food(unvisited_foods, cur_pos):
        min = util.manhattanDistance(unvisited_foods[0], cur_pos)
        res_pos = unvisited_foods[0]
        for f_pos in unvisited_foods:
            f_distance = manhattanDistance(f_pos, cur_pos)
            if (f_distance < min):
                min = f_distance
                res_pos = f_pos
        return min, res_pos


    if len(food_lst) != 0:
        distance, next_food = find_next_min_food(food_lst, cur_pos)
        food_score = distance
        #print(food_score)

    ghost_score = 0
    for i in range(1, currentGameState.getNumAgents()):
        g = currentGameState.getGhostState(i)
        ghost_score += g.scaredTimer


    for ghoststate in GhostStates:
        dist = manhattanDistance(Pacman_pos, ghoststate.getPosition())
        # ghost is too close
        if dist < 4 and ghoststate.scaredTimer < dist:
            ghost_score -= 4

    cupsule_score = 0
    for c in cupsules:
        dist = manhattanDistance(Pacman_pos, c)
        # ghost is too close
        if dist < 3:
            cupsule_score += 4 - dist

    # print("food score\n")
    # print(1.0 / (1 + food_score))
    # print('\n')
    # print("current food number\n")
    # print(currentGameState.getNumFood())
    # print('\n')
    # print("ghost score\n")
    # print(ghost_score)
    # print('\n')
    # print("cupsule score\n")
    # print(cupsule_score)

    return 1.0 / (1.5 + food_score) - 0.5*currentGameState.getNumFood() + ghost_score + cupsule_score


# Abbreviation
better = betterEvaluationFunction
