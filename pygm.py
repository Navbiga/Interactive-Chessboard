
# import all modules BEWARE SCALING ISSUES WITH OTHER OS THAN WINDOWS
import sys
if sys.platform == "win32":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
import pygame
from functions import *


# pygame start
pygame.init()
run = True
framerate = 144
color_of_your_pieces = "white"  # change this to "black" if you want to play as black
color_of_other_pieces = "black"
already_selected_piece = False
# Screen dimensions

screen_info = pygame.display.Info()

# resolution check
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
    run = False

SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

chessboard = pygame.image.load("resources/chessboard.jpg")
white_pawn = pygame.image.load("resources/white_pawn.png")
black_pawn = pygame.image.load("resources/black_pawn.png")
white_king = pygame.image.load("resources/white_king.png")
black_king = pygame.image.load("resources/black_king.png")
white_queen = pygame.image.load("resources/white_queen.png")
black_queen = pygame.image.load("resources/black_queen.png")
white_rook = pygame.image.load("resources/white_rook.png")
black_rook = pygame.image.load("resources/black_rook.png")
white_bishop = pygame.image.load("resources/white_bishop.png")
black_bishop = pygame.image.load("resources/black_bishop.png")
white_knight = pygame.image.load("resources/white_knight.png")
black_knight = pygame.image.load("resources/black_knight.png")

# Image scaling
chessboard = pygame.transform.scale_by(chessboard, multiplier)
black_pawn = pygame.transform.scale_by(black_pawn, multiplier * 0.8)
white_pawn = pygame.transform.scale_by(white_pawn, multiplier * 0.8)
white_king = pygame.transform.scale_by(white_king, multiplier * 1.2)
black_king = pygame.transform.scale_by(black_king, multiplier * 1.2) 
black_queen = pygame.transform.scale_by(black_queen, multiplier * 0.85)
white_queen = pygame.transform.scale_by(white_queen, multiplier * 0.85)
black_rook = pygame.transform.scale_by(black_rook, multiplier * 0.7)
white_rook = pygame.transform.scale_by(white_rook, multiplier * 0.7)
black_bishop = pygame.transform.scale_by(black_bishop, multiplier * 0.8)
white_bishop = pygame.transform.scale_by(white_bishop, multiplier * 0.8)
black_knight = pygame.transform.scale_by(black_knight, multiplier * 0.8)
white_knight = pygame.transform.scale_by(white_knight, multiplier * 0.8)

# generate positions for each square on the chessboard
def generate_positions():
    '''This function generates the center of all positions on a chessboard (A1-H8) and returns them as a dictionary.'''
    positions = {}
    square_size = 100 * multiplier
    # generate positions for each square on the chessboard
    for row in range(1, 9):
        for col, times  in zip("abcdefgh", range(8)):
            
            letter = col + str(row)
            x = (SCREEN_WIDTH // 2 - chessboard.get_width() // 2) + times * square_size
            y = (SCREEN_HEIGHT // 2 - chessboard.get_height() // 2) + (8 - row) * square_size
            positions[letter] = (x + square_size // 2, y + square_size // 2)  # center of the square
    return positions

positions = generate_positions()
board = {pos: None for pos in positions.keys()}

# information about the pieces
class Piece:
    def __init__(self, color, position, piece_type):
        self.color = color
        self.position = position
        self.piece = piece_type
        if self.piece == "pawn":
            if self.color == "white":
                self.image = white_pawn
            elif self.color == "black":
                self.image = black_pawn
        if self.piece == "king":
            if self.color == "white":
                self.image = white_king
            elif self.color == "black":
                self.image = black_king
        if self.piece == "queen":
            if self.color == "white":
                self.image = white_queen
            elif self.color == "black":
                self.image = black_queen
        if self.piece == "rook":
            if self.color == "white":
                self.image = white_rook
            elif self.color == "black":
                self.image = black_rook
        if self.piece == "bishop":
            if self.color == "white":
                self.image = white_bishop
            elif self.color == "black":
                self.image = black_bishop
        if self.piece == "knight":
            if self.color == "white":
                self.image = white_knight
            elif self.color == "black":
                self.image = black_knight

    def draw(self, screen):
        x, y = positions[self.position]
        screen.blit(self.image, (x - self.image.get_width() // 2, y - self.image.get_height() // 2))

    def move(self, new_position):
        board[new_position] = self
        board[self.position] = None
        self.position = new_position

    def capture(position):
        board[position] = None
        
# create pieces and place them on the board

def create_pieces():
    '''This function creates and places the pieces on the starting positions of a chess game.'''
    # Pawns
    for col in "abcdefgh":
        board[col + "2"] = Piece(color_of_your_pieces, col + "2", "pawn")
        board[col + "7"] = Piece(color_of_other_pieces, col + "7", "pawn")
    # Kings
    board["e1"] = Piece(color_of_your_pieces, "e1", "king")
    board["e8"] = Piece(color_of_other_pieces, "e8", "king")

    # Queens
    board["d1"] = Piece(color_of_your_pieces, "d1", "queen")
    board["d8"] = Piece(color_of_other_pieces, "d8", "queen")

    # Rooks
    board["a1"] = Piece(color_of_your_pieces, "a1", "rook")
    board["h1"] = Piece(color_of_your_pieces, "h1", "rook")
    board["a8"] = Piece(color_of_other_pieces, "a8", "rook")
    board["h8"] = Piece(color_of_other_pieces, "h8", "rook")

    # Bishops
    board["c1"] = Piece(color_of_your_pieces, "c1", "bishop")
    board["f1"] = Piece(color_of_your_pieces, "f1", "bishop")
    board["c8"] = Piece(color_of_other_pieces, "c8", "bishop")
    board["f8"] = Piece(color_of_other_pieces, "f8", "bishop")

    # Knights
    board["b1"] = Piece(color_of_your_pieces, "b1", "knight")
    board["g1"] = Piece(color_of_your_pieces, "g1", "knight")
    board["b8"] = Piece(color_of_other_pieces, "b8", "knight")
    board["g8"] = Piece(color_of_other_pieces, "g8", "knight")
create_pieces()

def get_clicked_square(click_x, click_y):
    '''This function returns the name of the square that was clicked on.'''
    for pos_name, (pos_x, pos_y) in positions.items():
        square_size = 100 * multiplier
        if (pos_x - square_size // 2 <= click_x <= pos_x + square_size // 2) and (pos_y - square_size // 2 <= click_y <= pos_y + square_size // 2):
            return pos_name
    return None


# Main loop
while run:

    #print images
    screen.blit(chessboard, (SCREEN_WIDTH // 2 - chessboard.get_width() // 2, SCREEN_HEIGHT // 2 - chessboard.get_height() // 2))
    
    for pos_name, piece in board.items():
        if piece is not None:
            piece.draw(screen)



    #close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left mouse button
                click_x, click_y = event.pos
                clicked_square = get_clicked_square(click_x, click_y)
                
                if clicked_square: 
                    target_piece = board.get(clicked_square) 

                    if not already_selected_piece:
                        if target_piece is not None:
                            selected_piece = target_piece
                            selected_square = clicked_square
                            already_selected_piece = True
                            print(f"Selected {selected_piece} on {selected_square}")
                    
                    else:
                        if already_selected_piece:
                            move(selected_piece, selected_square, clicked_square, board, your_color=color_of_your_pieces)
                            already_selected_piece = False
    
    # update the display and set the frame rate (preset 144)
    pygame.display.flip()
    pygame.time.Clock().tick(framerate)


pygame.quit()