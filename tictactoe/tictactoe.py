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
    # TODO Loop through the board and count instances of player's turn
    # TODO If board is empty, then it's X's go. 
    # TODO Return the player with the least turns
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # TODO return legal moves for this board
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
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # TODO
    # if max's turn: 
	# pick action a that produces highest value of
	# min-value(result(s, a))
    # if min's turn:
	# pick action a that produces lowest value of 
	# all options max-value(result(s, a))
    
    raise NotImplementedError
