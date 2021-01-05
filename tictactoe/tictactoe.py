"""
Tic Tac Toe Player
"""

import math
import copy

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
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


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
    if winner(board) == "X" or winner(board) == "O":
        return True
    else:
        for row in board:
            if EMPTY in row:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        print("Endgame detected in max_value")
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        print("Endgame detected in min_value")
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def minimax(board):
    if terminal(board):
        return None
    else:
        if player(board) == X:
            best_v = -math.inf
            for move in actions(board):
                max_v = min_value(result(board, move))
                print("V: " + str(best_v))
                if max_v > best_v:
                    best_v = max_v
                    best_move = move

        elif player(board) == O:
            best_v = math.inf
            for move in actions(board):
                min_v = max_value(result(board, move))
                print("V: " + str(best_v))
                if min_v < best_v:
                    best_v = min_v
                    best_move = move
        return best_move

