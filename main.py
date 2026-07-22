# import all modules BEWARE SCALING ISSUES WITH OTHER OS THAN WINDOWS
import sys
if sys.platform == "win32":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
import pygame
from functions import *

# pygame start and preset variables
pygame.init()

run = True
framerate = 144
your_color = "white"  # change this to "black" if you want to play as black
promotion_piece = 'queen' # this is the preset
already_selected_piece = False
turn = "white"
game_state = 'playing'

# resolution check
screen_info = pygame.display.Info() # screen info (resolution)

if screen_info.current_w == 1920 and screen_info.current_h == 1080:
    print("You are using FULLHD resolution.")
    multiplier = 1
elif screen_info.current_w == 2560 and screen_info.current_h == 1440:
    print("You are using QHD resolution.")
    multiplier = 1.5
elif screen_info.current_w == 3840 and screen_info.current_h == 2160:
    print("You are using 4K resolution.")
    multiplier = 2
else:
    print(f"Your current resolution {screen_info.current_w}x{screen_info.current_h} is not supported. Please use FULLHD, QHD, or 4K resolution.")

# Initialize the window
SCREEN_WIDTH = 800 * multiplier
SCREEN_HEIGHT = 800 * multiplier    
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chessboard")
icon = pygame.image.load("resources/icon.png")
pygame.display.set_icon(icon)


# Preset style
chessboard_style = 'blue'
pieces_style = 'anime'

# board and square size preset
square_size = int(100 * multiplier)
board_size = square_size * 8

# Chessboard
chessboard = pygame.image.load(f"resources/boards/{chessboard_style}.png").convert_alpha()
chessboard = pygame.transform.smoothscale(chessboard, (board_size, board_size))

# pieces
piece_files = {
    "white_pawn": "wp.png",   "black_pawn": "bp.png",
    "white_king": "wk.png",   "black_king": "bk.png",
    "white_queen": "wq.png",  "black_queen": "bq.png",
    "white_rook": "wr.png",   "black_rook": "br.png",
    "white_bishop": "wb.png", "black_bishop": "bb.png",
    "white_knight": "wn.png", "black_knight": "bn.png",
}

# load and smoothscale of pieces
PIECE_IMAGES = {}

for piece_key, filename in piece_files.items():
    raw_img = pygame.image.load(f"resources/pieces/{pieces_style}/{filename}").convert_alpha()
    PIECE_IMAGES[piece_key] = pygame.transform.smoothscale(raw_img, (square_size, square_size))




# generate all positions for each square on the chessboard
# BEWARE ONLY WORKS IF THE CHESSBOARD IS IN THE CENTER OF THE SCREEN

def generate_positions():
    '''This function generates the start of a square (right up corner) and return a dictionary in this syntax "a4": (x, y)'''
    positions = {}
    for row in range(1, 9):
        for col, times in zip("abcdefgh", range(8)):
            
            letter = col + str(row)
            x = (SCREEN_WIDTH // 2 - 4 * square_size) + times * square_size
            y = (SCREEN_HEIGHT // 2 - 400 * multiplier) + (8 - row) * square_size
            positions[letter] = (x, y)
    return positions

positions = generate_positions()

# IMPORTANT copies all names of posiotions and makes a dictonary in which every piece on the board is stored with the name of the position
board = {pos: None for pos in positions.keys()}

# class for generatin moving terminating atd a piece
class Piece:
    def __init__(self, color, position, piece_type):
        self.color = color
        self.position = position
        self.piece = piece_type
        self.image = PIECE_IMAGES[f"{self.color}_{self.piece}"]

    def draw(self, screen):
        x, y = positions[self.position]
        screen.blit(self.image, (x, y))

    def move(self, new_position):
        board[new_position] = self
        board[self.position] = None
        self.position = new_position

    def capture(self, position):
        board[position] = None


    def promote(self, piece):
        self.piece = piece
        self.image = PIECE_IMAGES[f"{self.color}_{self.piece}"]


        
# create pieces and places them on the staring positions
def create_pieces():
    '''This function creates and places the pieces on the starting positions of a chess game.'''
    if your_color == 'white':
        their_color = 'black'
    else:
        their_color = 'white'
    # Pawns
    for col in "abcdefgh":
        board[col + "2"] = Piece(your_color, col + "2", "pawn")
        board[col + "7"] = Piece(their_color, col + "7", "pawn")
    # Kings
    board["e1"] = Piece(your_color, "e1", "king")
    board["e8"] = Piece(their_color, "e8", "king")

    # Queens
    board["d1"] = Piece(your_color, "d1", "queen")
    board["d8"] = Piece(their_color, "d8", "queen")

    # Rooks
    board["a1"] = Piece(your_color, "a1", "rook")
    board["h1"] = Piece(your_color, "h1", "rook")
    board["a8"] = Piece(their_color, "a8", "rook")
    board["h8"] = Piece(their_color, "h8", "rook")

    # Bishops
    board["c1"] = Piece(your_color, "c1", "bishop")
    board["f1"] = Piece(your_color, "f1", "bishop")
    board["c8"] = Piece(their_color, "c8", "bishop")
    board["f8"] = Piece(their_color, "f8", "bishop")

    # Knights
    board["b1"] = Piece(your_color, "b1", "knight")
    board["g1"] = Piece(your_color, "g1", "knight")
    board["b8"] = Piece(their_color, "b8", "knight")
    board["g8"] = Piece(their_color, "g8", "knight")
create_pieces()

# It estimates in which square was the left click registered with POSITIONS and outputs the name of the position for example 'a4'
def get_clicked_square(click_x, click_y):
    '''This function returns the name of the square that was clicked on.'''
    for pos_name, (pos_x, pos_y) in positions.items():
        square_size = 100 * multiplier
        if (pos_x <= click_x <= pos_x + square_size) and (pos_y <= click_y <= pos_y + square_size):
            return pos_name
    return None

# Main loop
while run:

    # display all of the pieces with the chessboard
    screen.blit(chessboard, (SCREEN_WIDTH // 2 - chessboard.get_width() // 2, SCREEN_HEIGHT // 2 - chessboard.get_height() // 2))
    for pos_name, piece in board.items():
        if piece is not None:
            piece.draw(screen)

    # pygame event
    for event in pygame.event.get():

        # for terminating the program
        if event.type == pygame.QUIT:
            run = False 

        # for registering clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # for left clicks
            if event.button == 1:  # left mouse button
                click_x, click_y = event.pos

                # gets the square that was clicked
                clicked_square = get_clicked_square(click_x, click_y)
                
                if clicked_square:    # if it got a value

                    # Check if there is a stored piece in this position if not this variable is None
                    target_piece = board.get(clicked_square) 

                    # For selection of a figure. it checks if a figure is not alredy selected and if there is a piece.
                    if not already_selected_piece:
                        if target_piece is not None and target_piece.color == turn:
                            selected_piece = target_piece
                            selected_square = clicked_square

                            
                            already_selected_piece = True
                            print(f"Selected {selected_piece} on {selected_square}")
                    
                    # If the piece is alredy selected it check if it is a legal move and inicialize it.
                    else:
                        if already_selected_piece:
                            if_not_legal = move(selected_piece, selected_square, clicked_square, board, turn)

                            if if_not_legal != False:
                                if turn ==  'white':
                                    turn = 'black'
                                    
                                    selected_piece.move(clicked_square)
                                else:
                                    turn = 'white'
                                    selected_piece.move(clicked_square)

                            
                            
                            already_selected_piece = False
    
    # update the display and set the frame rate (preset 144)
    pygame.display.flip()
    pygame.time.Clock().tick(framerate)

# Terminates the program
pygame.quit()