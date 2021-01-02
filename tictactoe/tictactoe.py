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
    xcount = 0
    ocount = 0
    # TODO Loop through the board and count instances of player's turn
    for row in board:
        for column in row:
            if column == "X":
                xcount += 1
            if column == "O":
                ocount += 1
    if ocount < xcount:
        return "O"
    else:
        return "X"
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # TODO return all legal moves for this board.
    # TODO Gives us all the possible actions (much like classical search)
    # TODO return all the actions for this board.
    possible_actions = set()
    for row in range(0, len(board)):
        print("Row:" + str(row))
        for column in range(0, len(board[0])):
            print("Column:" + str(column))
            if board[row][column] == "EMPTY":
                possible_actions.add((row, column))
    return possible_actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # TODO returns the state after action a taken in state s
    # TODO This is the transitional model. We take a state and an action,
    # TODO when we apply the action and the state, we return the board
    # TODO that is now in place. 
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        print(row[0])
        if row[0] == EMPTY or row[1] == EMPTY or row[2] == EMPTY:
            pass
        elif row[0] == row[1] and row[1] == row[2]:
            return row[0]

    # Check columns
    transposed_board = [*zip(*board)]
    for column in transposed_board:
        if column[0] == EMPTY or column[1] == EMPTY or column[2] == EMPTY:
            pass
        elif column[0] == column[1] and column[1] == column[2]:
            return column[0]

    # Check diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return board[0][2]


    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if state s is terminal
    # Check if we have a winner
    if winner(board) == "X" or winner(board) == "O":
        return True
    # No winner - so are there spaces on the board?
    else:
        for row in board:
            for column in row:
                if EMPTY in column:
                    return False

    # No space left on the board and no winner - so game is terminal
    return True

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
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

# MAX-VALUE function
def maxvalue():
    pass
# TODO CHECK if terminal:
    # return utility state
# TODO create a variable called V to track the value of the state.
# TODO initially, we set it to as low as possible (negative infinity).
# For every action in actions(state):
    # v = MAX(v, MIN-VALUE(Result(state, action)))


def minvalue():
    pass
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

# TODO:


# - minvalue
# - maxvalue
# - minimax

# Done:
# - initial_state
# - player
# - terminal
# - winner
# - actions
# - result
# - utility
