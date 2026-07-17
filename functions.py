    
def is_legal_move(piece, square, target_square, board, your_color):
    '''This function returns a boolean if the move is legal'''
    # Placeholder implementation - replace with actual legal move logic

    # Check if piece color matches the player's color
    if piece.color != your_color:
        return False
    # Check if the target square is occupied by a piece of your color
    if board[target_square] is not None:
        if board[target_square].color == your_color:
            return False
        

    # Pawn move logic
    
    if piece.piece == "pawn":
        if square[0] == target_square[0]:  #same file
            # check for double move from starting position
            if square[1] == "2" and target_square[1] == "4" and board[target_square] is None and board[square[0] + "3"] is None:
                return True
            #check for single move forward
            elif int(square[1]) - int(target_square[1]) == -1 and board[target_square] is None:
                return True
            

        
    return False