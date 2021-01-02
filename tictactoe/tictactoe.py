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


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # TODO return all legal moves for this board.
    # TODO Gives us all the possible actions (much like classical search)
    # TODO return all the actions for this board.
    possible_actions = set()
    for row in range(0, len(board)):
        for column in range(0, len(board[0])):
            if board[row][column] == EMPTY:
                possible_actions.add((row, column))
    return possible_actions


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
    return None

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
            if EMPTY in row:
                return False
    # No space left on the board and no winner - so game is terminal
    return True


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


def max_value(board):
    # TODO CHECK if terminal: return winner or result
    # TODO create a variable called V to track the value of the state.
    # TODO initially, we set it to as low as possible (positive infinity).
    if terminal(board):
        return utility(board), None
    else:
        v = float('-inf')
        for action in actions(board):
            aux, act = min_value(result(board, action))
            print("aux:" + str(type(aux)))
            print("v:" + str(type(v)))
            if aux > v:
                v = aux
                move = action
                if v == 1:
                    return v, move
        return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None
    else:
        v = float('inf')
        for action in actions(board):
            # print(action)
            aux, act = max_value(result(board, action))
            print("aux:" + str(type(aux)))
            print("v:" + str(type(v)))
            if aux < v:
                v = aux
                move = action
                if v == -1:
                    return v, move
        return v, move


def minimax(board):
    # TODO Recursive algorithm
    if terminal(board):
        return None
    else:
        if player(board) == "X":
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move

# TODO:

# Done:
# - initial_state
# - player
# - terminal
# - winner
# - actions
# - result
# - utility
# - minvalue
# - maxvalue
# - minimax