import pygame
pygame.init()

window_width = 1000
window_height = 720

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Chess Boxing!')
font = pygame.font.SysFont('Arial', 30)

timer = pygame.time.Clock()
fps = 60

# Set up
white_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook",
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
white_captured_pieces = []

black_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook",
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_captured_pieces = []

# 0 - white turn: no piece selected, 1 - white turn: piece selected
# 2 - black turn: no piece selected, 3 - black turn: piece selected
turn_step = 0
selection = 200
valid_moves = []

# Load in game pieces
white_pawn = pygame.image.load("files/King.png")
white_pawn = pygame.transform.scale(white_pawn, (70, 70))
white_pawn_small_side_display = pygame.transform.scale(white_pawn, (45, 45))

white_bishop = pygame.image.load("files/King.png")
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small_side_display = pygame.transform.scale(white_bishop, (45, 45))

white_knight = pygame.image.load("files/King.png")
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small_side_display = pygame.transform.scale(white_knight, (45, 45))

white_rook = pygame.image.load("files/King.png")
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small_side_display = pygame.transform.scale(white_rook, (45, 45))

white_queen = pygame.image.load("files/King.png")
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small_side_display = pygame.transform.scale(white_queen, (45, 45))

white_king = pygame.image.load("files/King.png")
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small_side_display = pygame.transform.scale(white_king, (45, 45))

black_pawn = pygame.image.load("files/King.png")
black_pawn = pygame.transform.scale(black_pawn, (70, 70))
black_pawn_small_side_display = pygame.transform.scale(black_pawn, (45, 45))

black_bishop = pygame.image.load("files/King.png")
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small_side_display = pygame.transform.scale(black_bishop, (45, 45))

black_knight = pygame.image.load("files/King.png")
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small_side_display = pygame.transform.scale(black_knight, (45, 45))

black_rook = pygame.image.load("files/King.png")
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small_side_display = pygame.transform.scale(black_rook, (45, 45))

black_queen = pygame.image.load("files/King.png")
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small_side_display = pygame.transform.scale(black_queen, (45, 45))

black_king = pygame.image.load("files/King.png")
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small_side_display = pygame.transform.scale(black_king, (45, 45))

white_images = [white_pawn, white_bishop, white_knight, white_rook, white_queen, white_king]
small_display_white_images = [white_pawn_small_side_display, white_bishop_small_side_display,
                              white_knight_small_side_display, white_rook_small_side_display,
                              white_queen_small_side_display, white_king_small_side_display]

black_images = [black_pawn, black_bishop, black_knight, black_rook, black_queen, black_king]
small_display_black_images = [black_pawn_small_side_display, black_bishop_small_side_display,
                              black_knight_small_side_display, black_rook_small_side_display,
                              black_queen_small_side_display, black_king_small_side_display]

piece_list = ["pawn", "bishop", "knight", "rook", "queen", "king"]

# main game loop
playing = True
while playing:
    timer.tick(fps)
    window.fill((128, 64, 64))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    pygame.display.update()

pygame.quit()
