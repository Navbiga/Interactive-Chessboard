    
def move(piece, square, target_square, board, your_color):
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
                piece.move(target_square)
            #check for single move forward
            elif int(square[1]) - int(target_square[1]) == -1 and board[target_square] is None:
                piece.move(target_square)
        elif abs(ord(square[0]) - ord(target_square[0])) == 1 and int(square[1]) - int(target_square[1]) == -1:
            # check for diagonal capture
            if board[target_square] is not None and board[target_square].color != piece.color:
                if target_square is not None:
                    print(target_square)
                    piece.capture(target_square)
                piece.move(target_square)
                

        
    return False