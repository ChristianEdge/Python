class GameData:
    """This class defines game data. Try not adjust any value except scale."""
    SCALE = 2.5
    TILE_SIZE = int(96 * SCALE)
    BORDER = TILE_SIZE // 12
    WIN_WD = BORDER * 2 + TILE_SIZE * 3 #Window width
    WIN_HT = WIN_WD #height
    GRID_WD = WIN_WD // TILE_SIZE
    GRID_HT = GRID_WD
    FPS = 60
    TITLE = "Tic Tac Toe"
