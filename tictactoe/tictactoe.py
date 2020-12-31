"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    XCOUNT = 0
    OCOUNT = 0
    # TODO Loop through the board and count instances of player's turn
    for row in board:
        for column in row:
            if column == "X":
                XCOUNT += 1
            if column == "O":
                OCOUNT += 1
    if XCOUNT < OCOUNT:
        return "X"
    elif OCOUNT < XCOUNT:
        return "O"
    else:
        return "NONE"

    # TODO If board is empty, then it's X's go. 
    # TODO Return the player with the least turns
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # TODO return all legal moves for this board.
    # TODO Gives us all the possible actions (much like classical search)
    # TODO return all the actions for this board.
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # TODO returns the state after action a taken in state s
    # TODO This is the transitional model. We take a state and an action,
    # TODO when we apply the action and the state, we return the board
    # TODO that is now in place. 
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # TODO check if state s is terminal 
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # TODO return a final value for the game
    # TODO For each terminal state, what is the value?
    # TODO If X will win, then value of that state is 1
    # TODO If O will win, then value of that state is -1
    # TODO If draw, then value of that state is 0

# MAX-VALUE function
# TODO CHECK if terminal:
    # return utility state
# TODO create a variable called V to track the value of the state.
# TODO initially, we set it to as low as possible (negative infinity).
# For every action in actions(state):
    # v = MAX(v, MIN-VALUE(Result(state, action)))

# MIN-VALUE function
# TODO CHECK if terminal:
    # return utility state
# TODO create a variable called V to track the value of the state.
# TODO initially, we set it to as low as possible (positive infinity).
# For every action in actions(state):
# v = MIN(v, MAX-VALUE(Result(state, action)))

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # TODO Recursive algorithm
    # Repeat the process, but from opponent's viewpoint. 
    # if max's turn: 
        # pick action a that produces highest value of:
        # action = highest value of min-value(result(state, action))
    # if min's turn:
        # pick action a that produces lowest value of
        # action = lowest value of max-value(result(state, action))
    # Actions is a function that takes a state and returns all the possible
    # actions that can be taken by that player.
    # TODO loop round all the possible actions and send them to utility.
    # From utility, we can work out our best action.

    raise NotImplementedError
