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
    if board.count("X") == board.count("O"):
        return X
    elif board.count("X") > board.count("O"):
        return O
    else: raise NotImplementedError 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == "EMPTY":
                possible_actions.append((i, j))
    return possible_actions

def result(board, action): 
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new = copy.deepcopy(board)
    i, j = action
    if new[i][j] != EMPTY:
        raise NotImplementedError
    new[i][j] = player(board)
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) == 1: return X
    elif utility(board) == -1: return O
    else: return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return board.count("EMPTY") == 0 or winner(board) != None

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    while terminal(board):
        """Q.you don't neccessary need to exhuast all cells to reach ties"""
        diagonal = [[board[i][i] for i in range(3)],[board[i][len(board)-1-i] for i in range(3)]]
        row = [[cell for cell in row] for row in board]
        col = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]

        if all(cell == "X" for cell in diagonal) or all(cell == "X" for cell in row) or all(cell == "X" for cell in col):
            return 1
        elif all(cell == "O" for cell in diagonal) or all(cell == "O" for cell in row) or all(cell == "O" for cell in col):
            return -1
        else: 
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board): 
        v = -math.inf
        for action in actions(board):
            v = max(v,min_value(result(board,action)))
        return v
    def min_value(board):
        v = math.inf
        for action in actions(board):
            v = max(v,max_value(result(board,action)))
        return v

    if terminal(board):
        return None
    else: 
        if player(board) == X:
            max_value()
        elif player(board) == O:
            min_value()