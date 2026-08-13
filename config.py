
# Config.py 

class Display:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    FULLSCREEN = False   # if you eneble this then the window will be in full screen the scrren widht and height doesnt matter
    BOARD_SIZE = 800
    SQUARE_SIZE = BOARD_SIZE / 8
    FPS = 144

class Theme:
    # Note this is the preset you can change it directly with Chessboard.set_theme("marble", "anime") in your file
    BOARD_STYLE = "blue"
    PIECE_SET = "cburnett"

class Highlight:
    # The color of the selected square
    SELECTED_COLOR = (20, 85, 30)
    SELECTED_ALPHA = 128
    SELECT_TYPE = 'fill'

    # All legal move when you select a piece
    MOVE_COLOR = (0, 200, 255)
    MOVE_ALPHA = 150
    MOVE_TYPE = 'dot'


    LAST_MOVE_COLOR = (155, 199, 0)
    LAST_MOVE_ALPHA = 105
    ENABLED = True

    RIGHT_CLICK_COLOR = (255, 0, 0)
    RIGHT_CLICK_ALPHA = (150)
    RIGHT_CLICK_TYPE = 'fill'
    RIGHT_CLICK_ENABLED = True

class GeneralConfig:
    CHANGE_TURNS = True