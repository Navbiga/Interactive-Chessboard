# import all modules BEWARE SCALING ISSUES WITH OTHER OS THAN WINDOWS
import sys
if sys.platform == "win32":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
import pygame
from functions import *
from config import Display, Theme, Highlight, GeneralConfig

# pygame start and preset variables
pygame.init()

turn = 'white'
is_selected = False
your_color = 'white'


# Chessboard
class Chessboard:


    def __init__(self):
        self.square_size = Display.SQUARE_SIZE
        self.board_size = Display.BOARD_SIZE
        self.is_frozen = False
        self.turn = turn
        self.should_change_turns = GeneralConfig.CHANGE_TURNS


        if Display.FULLSCREEN == False:
            self.SCREEN_WIDTH, self.SCREEN_HEIGHT = Display.SCREEN_WIDTH, Display.SCREEN_HEIGHT
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        else:
            info = pygame.display.Info()
            self.SCREEN_WIDTH, self.SCREEN_HEIGHT = info.current_w, info.current_h
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)

        pygame.display.set_caption("Chessboard")
        icon = pygame.image.load("resources/icon.png")
        pygame.display.set_icon(icon)

        self.set_theme()
        self.generate_board()
        self.reset()

    def no_turns(self):
        self.should_change_turns = False

    def switch_turns(self):
        self.turn = 'white' if self.turn == 'black' else 'black'

    def switch_sides(self):
        new_positions = {}
        
        center_x = self.SCREEN_WIDTH / 2
        center_y = self.SCREEN_HEIGHT / 2

        for square, (x, y) in self.positions.items():
            new_x = 2 * center_x - x - self.square_size
            new_y = 2 * center_y - y - self.square_size
            
            new_positions[square] = (new_x, new_y)

        self.positions = new_positions

    def set_theme(self, board=None, piece=None):
        global PIECE_IMAGES

        self.board_style = board if board else Theme.BOARD_STYLE
        self.piece_style = piece if piece else Theme.PIECE_SET
        try:
            self.image = chessboard = pygame.image.load(f"resources/boards/{self.board_style}.jpg")
        except:
            self.image = pygame.image.load(f"resources/boards/{self.board_style}.png").convert_alpha()

        self.image = pygame.transform.smoothscale(chessboard, (self.board_size, self.board_size))

        piece_files = {
            "white_pawn": "wp.png",   "black_pawn": "bp.png",
            "white_king": "wk.png",   "black_king": "bk.png",
            "white_queen": "wq.png",  "black_queen": "bq.png",
            "white_rook": "wr.png",   "black_rook": "br.png",
            "white_bishop": "wb.png", "black_bishop": "bb.png",
            "white_knight": "wn.png", "black_knight": "bn.png",
        }

        self.PIECE_IMAGES = {}

        for piece_key, filename in piece_files.items():
            raw_img = pygame.image.load(f"resources/pieces/{self.piece_style}/{filename}").convert_alpha()
            self.PIECE_IMAGES[piece_key] = pygame.transform.smoothscale(raw_img, (self.square_size, self.square_size))

    def generate_board(self):

        positions = {}
        for row in range(1, 9):
            for col, times in zip("abcdefgh", range(8)):
                
                letter = col + str(row)
                x = (self.SCREEN_WIDTH // 2 - 4 * self.square_size) + times * self.square_size
                y = (self.SCREEN_HEIGHT // 2 - 4 * self.square_size) + (8 - row) * self.square_size
                positions[letter] = (x, y)

        self.positions = positions
        self.board = {pos: None for pos in positions.keys()}

    def reset(self):
        for key in self.board:
            self.board[key] = None

        their_color = 'black' if your_color == 'white' else 'white'
        # Pawns
        for col in "abcdefgh":
            self.board[col + "2"] = Piece(your_color, col + "2", "pawn", self.PIECE_IMAGES)
            self.board[col + "7"] = Piece(their_color, col + "7", "pawn", self.PIECE_IMAGES)
        # Kings
        self.board["e1"] = Piece(your_color, "e1", "king", self.PIECE_IMAGES)
        self.board["e8"] = Piece(their_color, "e8", "king", self.PIECE_IMAGES)

        # Queens
        self.board["d1"] = Piece(your_color, "d1", "queen", self.PIECE_IMAGES)
        self.board["d8"] = Piece(their_color, "d8", "queen", self.PIECE_IMAGES)

        # Rooks
        self.board["a1"] = Piece(your_color, "a1", "rook", self.PIECE_IMAGES)
        self.board["h1"] = Piece(your_color, "h1", "rook", self.PIECE_IMAGES)
        self.board["a8"] = Piece(their_color, "a8", "rook", self.PIECE_IMAGES)
        self.board["h8"] = Piece(their_color, "h8", "rook", self.PIECE_IMAGES)

        # Bishops
        self.board["c1"] = Piece(your_color, "c1", "bishop", self.PIECE_IMAGES)
        self.board["f1"] = Piece(your_color, "f1", "bishop", self.PIECE_IMAGES)
        self.board["c8"] = Piece(their_color, "c8", "bishop", self.PIECE_IMAGES)
        self.board["f8"] = Piece(their_color, "f8", "bishop", self.PIECE_IMAGES)

        # Knights
        self.board["b1"] = Piece(your_color, "b1", "knight", self.PIECE_IMAGES)
        self.board["g1"] = Piece(your_color, "g1", "knight", self.PIECE_IMAGES)
        self.board["b8"] = Piece(their_color, "b8", "knight", self.PIECE_IMAGES)
        self.board["g8"] = Piece(their_color, "g8", "knight", self.PIECE_IMAGES)

    def freeze(self):
        self.is_frozen = True

    def unfreeze(self):
        self.is_frozen = False

    def draw(self):
        self.screen.blit(self.image, (self.SCREEN_WIDTH / 2 - self.board_size / 2, self.SCREEN_HEIGHT / 2 - self.board_size / 2))
        for pos_name, piece in self.board.items():
            if piece is not None:
                piece.draw(self.screen, self.positions)

    def move_piece(self, start_pos, end_pos):
        piece = self.board[start_pos]
        if piece is not None:
            self.board[end_pos] = piece
            self.board[start_pos] = None
            piece.position = end_pos
        else:
            print('ERROR: move_piece() - the start pos you entered has no piece on that square')

    def get_board(self):
        return self.board

    def create_piece(self, color, type, position):
        if self.board[position] is None:
            self.board[position] = Piece(color, position, type, self.PIECE_IMAGES)
        else:
            print('ERROR: create_piece() - your cant create a piece on top of another piece')

    def delete_piece(self, position):
        self.board[position] = None

    def promote(self, position, type):
        if self.board[position] is not None:
            self.board[position].piece = type
            self.board[position].image = self.PIECE_IMAGES[f"{self.board[position].color}_{type}"]
        else:
            print('ERROR: promote() - You can promote a blank square')

    def update(self):
        global is_selected

        self.draw()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return 'quit'

            if not self.is_frozen:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_x, click_y = event.pos
                        square = get_clicked_square(click_x, click_y, self.square_size, self.positions)

                        if square:
                            piece = self.board[square]

                            if not is_selected and piece is not None and piece.color == self.turn:
                                self.selected_piece = self.board[square]
                                self.selected_square = square
                                is_selected = True

                            elif is_selected:
                                is_legal = check_move(self.selected_piece, self.selected_square, square, self.board, self.turn)

                                if is_legal:
                                    if self.should_change_turns:
                                        self.switch_turns()
                                    self.move_piece(self.selected_square, square)
                                    is_selected = False
                                    return 'move'

                                is_selected = False


        pygame.display.flip()
        pygame.time.Clock().tick(Display.FPS)
        



class Piece:
    def __init__(self, color, position, piece_type, PIECE_IMAGES):
        self.color = color
        self.position = position
        self.piece = piece_type
        self.image = PIECE_IMAGES[f"{self.color}_{self.piece}"]

    def draw(self, screen, positions):
        x, y = positions[self.position]
        screen.blit(self.image, (x, y))

run = True
board = Chessboard()    

while run:
    event = board.update()

    if event == 'quit':
        run = False