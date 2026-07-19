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

already_selected_piece = False
turn = "white"

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
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Chessboard")
icon = pygame.image.load("resources/white_pawn.png")
pygame.display.set_icon(icon)

# Image loading
chessboard = pygame.image.load("resources/chessboard.png")

# Pawns
white_pawn = pygame.image.load("resources/white_pawn.png")
white_pawn_selected = pygame.image.load("resources/white_pawn_selected.png")
black_pawn = pygame.image.load("resources/black_pawn.png")
black_pawn_selected = pygame.image.load("resources/black_pawn_selected.png")

# Kings
white_king = pygame.image.load("resources/white_king.png")
white_king_selected = pygame.image.load("resources/white_king_selected.png")
black_king = pygame.image.load("resources/black_king.png")
black_king_selected = pygame.image.load("resources/black_king_selected.png")

# Queens
white_queen = pygame.image.load("resources/white_queen.png")
white_queen_selected = pygame.image.load("resources/white_queen_selected.png")
black_queen = pygame.image.load("resources/black_queen.png")
black_queen_selected = pygame.image.load("resources/black_queen_selected.png")

# Rooks
white_rook = pygame.image.load("resources/white_rook.png")
white_rook_selected = pygame.image.load("resources/white_rook_selected.png")
black_rook = pygame.image.load("resources/black_rook.png")
black_rook_selected = pygame.image.load("resources/black_rook_selected.png")

# Bishops
white_bishop = pygame.image.load("resources/white_bishop.png")
white_bishop_selected = pygame.image.load("resources/white_bishop_selected.png")
black_bishop = pygame.image.load("resources/black_bishop.png")
black_bishop_selected = pygame.image.load("resources/black_bishop_selected.png")

# Knights
white_knight = pygame.image.load("resources/white_knight.png")
white_knight_selected = pygame.image.load("resources/white_knight_selected.png")
black_knight = pygame.image.load("resources/black_knight.png")
black_knight_selected = pygame.image.load("resources/black_knight_selected.png")

# Image scaling
chessboard = pygame.transform.scale_by(chessboard, multiplier)

# Scale Pawns
white_pawn = pygame.transform.scale_by(white_pawn, multiplier * 0.8)
white_pawn_selected = pygame.transform.scale_by(white_pawn_selected, multiplier * 0.8)
black_pawn = pygame.transform.scale_by(black_pawn, multiplier * 0.8)
black_pawn_selected = pygame.transform.scale_by(black_pawn_selected, multiplier * 0.8)

# Scale Kings
white_king = pygame.transform.scale_by(white_king, multiplier * 1.2)
white_king_selected = pygame.transform.scale_by(white_king_selected, multiplier * 1.2)
black_king = pygame.transform.scale_by(black_king, multiplier * 1.2) 
white_king_selected = pygame.transform.scale_by(black_king_selected, multiplier * 1.2) 

# Scale Queens
white_queen = pygame.transform.scale_by(white_queen, multiplier * 0.85)
white_queen_selected = pygame.transform.scale_by(white_queen_selected, multiplier * 0.85)
black_queen = pygame.transform.scale_by(black_queen, multiplier * 0.85)
black_queen_selected = pygame.transform.scale_by(black_queen_selected, multiplier * 0.85)

# Scale Rooks
white_rook = pygame.transform.scale_by(white_rook, multiplier * 0.7)
white_rook_selected = pygame.transform.scale_by(white_rook_selected, multiplier * 0.7)
black_rook = pygame.transform.scale_by(black_rook, multiplier * 0.7)
black_rook_selected = pygame.transform.scale_by(black_rook_selected, multiplier * 0.7)

# Scale Bishops
white_bishop = pygame.transform.scale_by(white_bishop, multiplier * 0.8)
white_bishop_selected = pygame.transform.scale_by(white_bishop_selected, multiplier * 0.8)
black_bishop = pygame.transform.scale_by(black_bishop, multiplier * 0.8)
black_bishop_selected = pygame.transform.scale_by(black_bishop_selected, multiplier * 0.8)

# Scale Knights
white_knight = pygame.transform.scale_by(white_knight, multiplier * 0.8)
white_knight_selected = pygame.transform.scale_by(white_knight_selected, multiplier * 0.8)
black_knight = pygame.transform.scale_by(black_knight, multiplier * 0.8)
black_knight_selected = pygame.transform.scale_by(black_knight_selected, multiplier * 0.8)

# -----------------------------------------------------------------------------
# CENTRAL IMAGE DATABASE
# -----------------------------------------------------------------------------
PIECE_IMAGES = {
    "white_pawn": white_pawn,
    "white_pawn_selected": white_pawn_selected,
    "black_pawn": black_pawn,
    "black_pawn_selected": black_pawn_selected,
    
    "white_king": white_king,
    "white_king_selected": white_king_selected,
    "black_king": black_king,
    "black_king_selected": black_king_selected,
    
    "white_queen": white_queen,
    "white_queen_selected": white_queen_selected,
    "black_queen": black_queen,
    "black_queen_selected": black_queen_selected,
    
    "white_rook": white_rook,
    "white_rook_selected": white_rook_selected,
    "black_rook": black_rook,
    "black_rook_selected": black_rook_selected,
    
    "white_bishop": white_bishop,
    "white_bishop_selected": white_bishop_selected,
    "black_bishop": black_bishop,
    "black_bishop_selected": black_bishop_selected,
    
    "white_knight": white_knight,
    "white_knight_selected": white_knight_selected,
    "black_knight": black_knight,
    "black_knight_selected": black_knight_selected,
}

# generate all positions for each square on the chessboard and the center of them for good snaping
def generate_positions():
    '''This function generates the center of all positions on a chessboard (A1-H8) and returns them as a dictionary.'''
    positions = {}
    square_size = 100 * multiplier
    # generate positions for each square on the chessboard
    for row in range(1, 9):
        for col, times in zip("abcdefgh", range(8)):
            
            letter = col + str(row)
            x = (SCREEN_WIDTH // 2 - 400 * multiplier) + times * square_size
            y = (SCREEN_HEIGHT // 2 - 400 * multiplier) + (8 - row) * square_size
            positions[letter] = (x + square_size // 2, y + square_size // 2)  # center of the square
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
        screen.blit(self.image, (x - self.image.get_width() // 2, y - self.image.get_height() // 2))

    def move(self, new_position):
        board[new_position] = self
        board[self.position] = None
        self.position = new_position

    def capture(self, position):
        board[position] = None
        
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
        if (pos_x - square_size // 2 <= click_x <= pos_x + square_size // 2) and (pos_y - square_size // 2 <= click_y <= pos_y + square_size // 2):
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
                        if target_piece is not None:
                            selected_piece = target_piece
                            selected_square = clicked_square
                            
                            # TADY: Řádek je zpět v původním stavu, připraven na tvou logiku
                            target_piece.image = target_piece.image 
                            
                            already_selected_piece = True
                            print(f"Selected {selected_piece} on {selected_square}")
                    
                    # If the piece is alredy selected it check if it is a legal move and inicialize it.
                    else:
                        if already_selected_piece:
                            if_not_legal = move(selected_piece, selected_square, clicked_square, board, turn)
                            if if_not_legal != False:
                                if turn == 'white':
                                    turn = 'black'
                                else:
                                    turn = 'white'
                            already_selected_piece = False
    
    # update the display and set the frame rate (preset 144)
    pygame.display.flip()
    pygame.time.Clock().tick(framerate)

# Terminates the program
pygame.quit()