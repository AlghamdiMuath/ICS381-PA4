#!/usr/bin/env python
# coding: utf-8

# In[1]:



# In[2]:


import chess
from numpy import infty
def heuristic_chess(board):
    outcome = board.outcome()
    if outcome is not None:
        if outcome.winner:
            return 1 # W win
        elif outcome.winner is None:
            return 0 # draw
        else:
            return -1 # Black wins

    fpawn = len(board.pieces(chess.PAWN, chess.WHITE)) - len(board.pieces(chess.PAWN, chess.BLACK))
    fknight = len(board.pieces(chess.KNIGHT, chess.WHITE)) - len(board.pieces(chess.KNIGHT, chess.BLACK))
    fbishop = len(board.pieces(chess.BISHOP, chess.WHITE)) - len(board.pieces(chess.BISHOP, chess.BLACK))
    frook = len(board.pieces(chess.ROOK, chess.WHITE)) - len(board.pieces(chess.ROOK, chess.BLACK))
    fqueen = len(board.pieces(chess.QUEEN, chess.WHITE)) - len(board.pieces(chess.QUEEN, chess.BLACK))

    # Calculate heuristic value
    heuristic_value = (fpawn + 3*fknight + 4*fbishop + 5 *frook + 9*fqueen)
    heuristic_value = heuristic_value / 100
    return heuristic_value

def is_cutoff(board, current_depth, depth_limit=2):
    if board.outcome() is not None or current_depth == depth_limit:
        return True
    
   # if current_depth == depth_limit:
       # return True
    
    else:
        return False


def max_node(board, current_depth, depth_limit):
    if is_cutoff(board, current_depth, depth_limit):
        return heuristic_chess(board), None
    
    v= -infty
    move = None
    for a in board.legal_moves:
        board.push(a)
        v2, a2 = min_node(board, current_depth + 1, depth_limit)
        if v2 > v:
            v = v2
            move = a
        board.pop()
    
    return v, move

def min_node(board, current_depth, depth_limit):
    if is_cutoff(board, current_depth, depth_limit):
        return heuristic_chess(board), None
    
    v = infty
    move = None
    for a in board.legal_moves:
        board.push(a)
        v2, a2 = max_node(board, current_depth + 1, depth_limit)
        if v2 < v:
            v = v2
            move = a
        board.pop()
    
    return v, move

def h_minimax(board , depth_limit = 2):
    heuristic_value, move = max_node(board , 0 , depth_limit)
    return heuristic_value, move



def max_node_ab(board, current_depth, depth_limit, alpha, beta):
    if is_cutoff(board, current_depth, depth_limit):
        return heuristic_chess(board), None
    
    v= -infty
    #move = None
    for a in board.legal_moves:
        board.push(a)
        v2, a2 = min_node_ab(board, current_depth + 1, depth_limit , alpha,beta)
        if v2 > v:
            v = v2
            move = a
            alpha = max(alpha,v)
        board.pop()
        if v >= beta:
            return v , move
    return v, move

def min_node_ab(board, current_depth, depth_limit, alpha, beta):
    if is_cutoff(board, current_depth, depth_limit):
        return heuristic_chess(board), None
    
    v = infty
  #  move = None
    for a in board.legal_moves:
        board.push(a)
        v2, a2 = max_node_ab(board, current_depth + 1, depth_limit, alpha, beta)
        if v2 < v:
            v = v2
            move = a
            beta = min(beta,v)
        board.pop()
        if v <= alpha:
            return v, move
    return v, move
def h_minimax_alpha_beta(board, depth_limit=2):
    heuristic_value, move = max_node_ab(board , 0 , depth_limit , -infty , infty)
    return heuristic_value, move