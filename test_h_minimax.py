if __name__ == "__main__":
    from games import *
    import chess
    
    np.random.seed(20220813)
    
    # initiliaze a chess games
    board = chess.Board()
    print('The current board is:')
    print(board)
    print('----------------------------------------------------------------------------')
    # starting player is always white
    # let's use h-minimax with some depth-limit to select a move for white
    value, move = h_minimax(board, depth_limit=2)
    
    print('After calling h_minimax the board should not change:')
    print(board)
    print('----------------------------------------------------------------------------')
    
    board.push(move)
    print('White player uses h-minimax. hvalue {}, move {}'.format(value, move))
    print(board)
    print('----------------------------------------------------------------------------')
    
    # The black player's turn, just pick a random move
    random_move = np.random.choice(list(board.legal_moves))
    board.push(random_move)
    
    # let use progress a couple of moves ahead to get into interesting positions
    for _ in range(10):
        # White player uses h-minimax to select moves
        value, move = h_minimax(board, depth_limit=2)
        board.push(move)
        print('White player uses h-minimax. hvalue {}, move {}'.format(value, move))
        
        # The black player's turn, just pick a random move
        random_move = np.random.choice(list(board.legal_moves))
        board.push(random_move)
        
    
    print('----------------------------------------------------------------------------')
    print('progressing game until it is over.')
    # now let us just keep progressing the game until it is over
    while board.outcome() is None:
        # White player uses h-minimax to select moves
        value, move = h_minimax(board, depth_limit=2)
        board.push(move)
        print('White player uses h-minimax. hvalue {}, move {}'.format(value, move))
        
        if board.outcome() is None:
            # The black player's turn, just pick a random move
            random_move = np.random.choice(list(board.legal_moves))
            board.push(random_move)
    
    
    # once game is over, show the outcome and winner
    print('----------------------------------------------------------------------------')
    outcome = board.outcome()
    winner = outcome.winner
    if winner is not None:
        winner = 'WHITE' if winner else 'BLACK'
        
    print('game is over with outcome status {} and winner {}'.format(outcome.termination, winner))