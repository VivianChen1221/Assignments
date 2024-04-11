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
    board_count = [item for sublist in board for item in sublist]
    if board_count.count("X") == board_count.count("O"):
        return X
    elif board_count.count("X") > board_count.count("O"):
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == "EMPTY":
                possible_actions.add((i, j)) #.add for set() instead of .append
    return possible_actions

def result(board, action): 
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if new[i][j] is not EMPTY:
        raise NotImplementedError
    new = [row.copy() for row in board] #why not board.copy
    new[i][j] = player(board)
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[2][0] is not EMPTY:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return [item for sublist in board for item in sublist].count("EMPTY") == 0 or winner(board) is not None

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    else: return 0

def minimax(board): #key part for revision
    """
    Returns the optimal action for the current player on the board.
    """
    #comparing output values of actions
    def max_value(board): 
        if terminal(board): return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v,min_value(result(board,action)))
        return v
    def min_value(board):
        if terminal(board): return utility(board)      
        v = math.inf
        for action in actions(board):
            v = max(v,max_value(result(board,action)))
        return v

    if terminal(board):
        return None

    #generating the best actions
    if player(board) == X:
        for action in actions(board):
            if min_value(result(board,action)) > math.-inf
                v = min_value(result(board,action)) #don't forget to update the value for futher comparison
        return action
    elif player(board) == O:
        for action in actions(board):
            if min_value(result(board,action)) > math.-inf
                v = min_value(result(board,action)) #don't forget to update the value for futher comparison
        return action
        
