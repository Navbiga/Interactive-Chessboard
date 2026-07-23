# This purely a functions/modeule file






def check_move(piece, square, target_square, board, turn, check_for_chess=True):
    '''This function returns false statement if move is not legal otherwise it does the move'''

    geometric_move = False
    direction = -1 if turn == 'white' else 1
    not_turn = 'white' if turn == 'black' else 'black'

    
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
                    geometric_move = True
            else:
                if square[1] == "7" and target_square[1] == "5" and board[target_square] is None and board[square[0] + "6"] is None:
                    geometric_move = True
            
            #check for single move forward
            if int(square[1]) - int(target_square[1]) == direction and board[target_square] is None:
                geometric_move = True
        
        # Capture logic
        elif abs(ord(square[0]) - ord(target_square[0])) == 1 and int(square[1]) - int(target_square[1]) == direction:
            # check for diagonal capture
            if board[target_square] is not None and board[target_square].color != piece.color:
                geometric_move = True
                
        # Check if the pawn didnt promote


    # Knight Movement
    elif piece.piece == 'knight':

        
        # two rows up and  column
        if abs(int(square[1]) - int(target_square[1])) == 2 and abs(ord(square[0]) - ord(target_square[0])) == 1:
            geometric_move = True

        # two collums and one row
        if abs(int(square[1]) - int(target_square[1])) == 1 and abs(ord(square[0]) - ord(target_square[0])) == 2:
            geometric_move = True


    
    # THE ROOOOOOOOOOOK
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
                geometric_move = True


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
                geometric_move = True
        

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
                geometric_move = True

    

    # The Queen Just rook and a bishop together nice to slack of right?
    elif piece.piece == 'queen':

        jump_check = True

        # Rook Part
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
                geometric_move = True


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
                geometric_move = True

        # bishop part 

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
                geometric_move = True

    # And finaly the king    
    elif piece.piece == 'king':
        row_diff = abs(int(square[1]) - int(target_square[1]))
        col_diff = abs(ord(square[0]) - ord(target_square[0]))

        if row_diff <= 1 and col_diff <=1 and (row_diff > 0 or col_diff > 0):
            geometric_move = True


    # If it passed the geometricly acurate move it moves on to the king safety check
    if geometric_move == True:

        # This prevents for is_check() to infinitly move
        if not check_for_chess:
            return True
        
        board_copy = board.copy()
        board_copy[target_square] = board_copy[square]
        board_copy[square] = None
        if is_check(turn, board_copy):
            return False
        else:
            return True
    else:
        return False



def all_legal_moves(board, turn):

    '''This move tells the user how many legal moves there is for a playing player'''
    # the color of not playing player
    not_turn = 'white' if turn == 'black' else 'black'
    moves = 0
    for pos, piece in board.items():
        if piece is not None and piece.color == turn:
            for try_pos in board:
                if check_move(piece, pos, try_pos, board, turn):
                    moves +=1

    return moves

def is_check(turn, board):
    '''Checks if the playing player is experiencing a check'''

    king_pos = None
    # get kings position
    for position, piece in board.items():
        if piece is not None:
            if piece.piece == 'king' and piece.color == turn:
                king_pos = position
                break

    # if somehow no king existed then who should be in check? ==> False
    if not king_pos:
        return False
    
    opponent_turn = 'white' if turn == 'black' else 'black'

    # Loops throught all of the not playing players pieces and checks if it has a legal move to take his king if yes ==> check
    for pos, piece in board.items():
        if piece is not None and piece.color == opponent_turn:

            # Check for ... c h e c k       hahahhahaa
            check = check_move(piece, pos, king_pos, board, opponent_turn, False)

            if check:
                return True
    
    # if the for loop doesnt find a check ==> no check
    return False

# It estimates in which square was the left click registered with POSITIONS and outputs the name of the position for example 'a4'
def get_clicked_square(click_x, click_y, square_size, positions):
    '''This function returns the name of the square that was clicked on.'''
    for pos_name, (pos_x, pos_y) in positions.items():
        if (pos_x <= click_x <= pos_x + square_size) and (pos_y <= click_y <= pos_y + square_size):
            return pos_name
        
    return None
