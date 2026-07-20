# This purely a functions/modeule file







def move(piece, square, target_square, board, turn):
    '''This function returns false statement if move is not legal otherwise it does the move'''

    if turn == 'white':
        direction = -1
    else:
        direction = 1

    # Check if piece color matches the color of the playing player
    if piece.color != turn:
        return False
    
    # Check if the target square is occupied by a piece of the playing color
    if board[target_square] is not None:
        if board[target_square].color == turn:
            return False
        
    # Pawn move logic
    
    if piece.piece == "pawn":

        # Logic in the same file
        if square[0] == target_square[0]:  
            # check for double move from starting position
            if turn == 'white':
                if square[1] == "2" and target_square[1] == "4" and board[target_square] is None and board[square[0] + "3"] is None:
                    piece.move(target_square)
                    return True
            else:
                if square[1] == "7" and target_square[1] == "5" and board[target_square] is None and board[square[0] + "6"] is None:
                    piece.move(target_square)
                    return True
            
            #check for single move forward
            if int(square[1]) - int(target_square[1]) == direction and board[target_square] is None:
                piece.move(target_square)
                return True
        
        # Capture logic
        elif abs(ord(square[0]) - ord(target_square[0])) == 1 and int(square[1]) - int(target_square[1]) == direction:
            # check for diagonal capture
            if board[target_square] is not None and board[target_square].color != piece.color:
                if target_square is not None:
                    print(target_square)
                    piece.capture(target_square)
                piece.move(target_square)
                return True
                
        # Check if the pawn didnt promote

        return False # if nothing works the move is not legal

    # Knight Movement
    elif piece.piece == 'knight':

        
        # two rows up and  column
        if abs(int(square[1]) - int(target_square[1])) == 2 and abs(ord(square[0]) - ord(target_square[0])) == 1:
            if board[target_square] is not None:
                piece.capture(target_square)
            piece.move(target_square)
            return True

        # two collums and one row
        if abs(int(square[1]) - int(target_square[1])) == 1 and abs(ord(square[0]) - ord(target_square[0])) == 2:
            if board[target_square] is not None:
                piece.capture(target_square)
            piece.move(target_square)
            return True


    
    # Rook Movement
    elif piece.piece == 'rook':
        jump_check = True

        # Logic and the same row
        if square[1] == target_square[1]:

            # Make a variable suitible for the range() function
            start_ascii = min(ord(square[0]), ord(target_square[0]))
            end_ascii = max(ord(square[0]), ord(target_square[0]))

            for current_col in range(start_ascii + 1, end_ascii):
                if jump_check and board[chr(current_col) + square[1]] is None:
                    jump_check = True
                else:
                    jump_check = False
                    return False

            if jump_check:
                # Success no obstacles in the way
                if board[target_square] is not None:
                    piece.capture(target_square)
                piece.move(target_square)
                return True


        # Logic in the same collum SO MUCH EASIER AHH
        elif square[0] == target_square[0]:

            # numbers suitable for range()
            start_int = min(int(square[1]), int(target_square[1]))
            end_int = max(int(square[1]), int(target_square[1]))

            for current_row in range(start_int + 1, end_int):
                if jump_check and board[square[0] + str(current_row)] is None:
                    jump_check = True
                else:
                    jump_check = False
                    return False
            
            if jump_check:    
                # Success no obstacles in the way
                if board[target_square] is not None:
                    piece.capture(target_square)
                piece.move(target_square)
                return True
        

    # Bishop Movement
    elif piece.piece == 'bishop':
        jump_check = True

        # Check if its along a diagonal
        if abs(int(square[1]) - int(target_square[1])) == abs(ord(square[0]) - ord(target_square[0])):
            
            # how many squares to check if the piece is not jumping over other piece
            steps = abs(int(square[1]) - int(target_square[1]))

            # checking all squares
            for times in range(1, steps):
                
                # selection of a letter
                if ord(square[0]) < ord(target_square[0]):
                    letter = chr(ord(square[0]) + times) 
                else:
                    letter = chr(ord(square[0]) - times)  

                # selection of a nmber
                if int(square[1]) < int(target_square[1]):
                    row_num = int(square[1]) + times      
                else:
                    row_num = int(square[1]) - times      

                # checking if the posiotion (letter + number) is None ==> no piece is there
                check_pos = letter + str(row_num)
                if board[check_pos] is not None:
                    jump_check = False
                    return False

            # if i turn out that no piece is obstruction the vision proceed with the move
            if jump_check:
                if board[target_square] is not None:
                    piece.capture(target_square)
                piece.move(target_square)
                return True

    
    # if nothing worked out the move is illegal
    return False
