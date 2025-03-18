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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    return X if x_count <= o_count else O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid move")
    
    new_board = [row[:] for row in board]  # Create a copy of the board
    new_board[action[0]][action[1]] = player(board)  # Place X or O
    
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in [X, O]:
        # Check rows & columns
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)):
                return player
        
        # Check diagonals
        if all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3)):
            return player

    return None  # No winner yet


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or not any(EMPTY in row for row in board)



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None  # No move possible

    current_player = player(board)

    if current_player == X:
        best_value = -math.inf
        best_move = None
        for action in actions(board):
            move_value = minimax_value(result(board, action), False)
            if move_value > best_value:
                best_value = move_value
                best_move = action
    else:
        best_value = math.inf
        best_move = None
        for action in actions(board):
            move_value = minimax_value(result(board, action), True)
            if move_value < best_value:
                best_value = move_value
                best_move = action

    return best_move

def minimax_value(board, is_maximizing):
    """
    Returns the minimax value of a given board.
    """
    if terminal(board):
        return utility(board)

    if is_maximizing:
        best_value = -math.inf
        for action in actions(board):
            best_value = max(best_value, minimax_value(result(board, action), False))
    else:
        best_value = math.inf
        for action in actions(board):
            best_value = min(best_value, minimax_value(result(board, action), True))

    return best_value

