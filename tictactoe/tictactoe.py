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
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    num_move = 0
    for row in board:
        for cell in row:
            if cell != EMPTY:
                num_move += 1

    if num_move % 2 != 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)

    if new_board[action[0]][action[1]] != EMPTY or not (0 <= action[0] < 3) or not (0 <= action[1] < 3):
        raise Exception("invalid action")
    else:
        new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] == X:
            return X
        if board[row][0] == board[row][1] == board[row][2] == O:
            return O

    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == X:
            return X
        if board[0][col] == board[1][col] == board[2][col] == O:
            return O

    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O

    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

def max_result(board, alpha):
    if terminal(board):
        return utility(board)

    p = -math.inf
    for action in actions(board):
        if p >= alpha:
            return p
        p = max(p, min_result(result(board, action), p))
    return p

def min_result(board, alpha):
    if terminal(board):
        return utility(board)

    p = math.inf
    for action in actions(board):
        if p <= alpha:
            return p
        p = min(p, max_result(result(board, action), p))
    return p

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
        
    cur_player = player(board)
    optimal_action = None

    if cur_player == X:
        p = -math.inf

        for action in actions(board):
            q = min_result(result(board, action), p)
            if p < q:
                p = q
                optimal_action = action
    elif cur_player == O:
        p = math.inf

        for action in actions(board):
            q = max_result(result(board, action), p)
            if p > q:
                p = q
                optimal_action = action
    return optimal_action
