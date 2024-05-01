import boxing_state

import pygame
pygame.init()

window_width = 1100
window_height = 720


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Chess Boxing!')
font = pygame.font.SysFont('freesansbold.ttf', 60)
font_small = pygame.font.SysFont('freesansbold.ttf', 25)

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

current_turn = 0
selection = 200
valid_moves = []

# Load in game pieces
white_pawn = pygame.image.load("files/WhitePawn.png")
white_pawn = pygame.transform.scale(white_pawn, (65, 65))

white_bishop = pygame.image.load("files/WhiteBishop.png")
white_bishop = pygame.transform.scale(white_bishop, (70, 70))

white_knight = pygame.image.load("Files/WhiteKnight.png")
white_knight = pygame.transform.scale(white_knight, (70, 70))

white_rook = pygame.image.load("files/WhiteRook.png")
white_rook = pygame.transform.scale(white_rook, (70, 70))

white_queen = pygame.image.load("files/WhiteQueen.png")
white_queen = pygame.transform.scale(white_queen, (70, 70))

white_king = pygame.image.load("files/WhiteKing.png")
white_king = pygame.transform.scale(white_king, (70, 70))

black_pawn = pygame.image.load("files/BlackPawn.png")
black_pawn = pygame.transform.scale(black_pawn, (65, 65))

black_bishop = pygame.image.load("files/BlackBishop.png")
black_bishop = pygame.transform.scale(black_bishop, (70, 70))

black_knight = pygame.image.load("files/BlackKnight.png")
black_knight = pygame.transform.scale(black_knight, (70, 70))

black_rook = pygame.image.load("files/BlackRook.png")
black_rook = pygame.transform.scale(black_rook, (70, 70))

black_queen = pygame.image.load("files/BlackQueen.png")
black_queen = pygame.transform.scale(black_queen, (70, 70))

black_king = pygame.image.load("files/BlackKing.png")
black_king = pygame.transform.scale(black_king, (70, 70))

white_images = [white_pawn, white_bishop, white_knight, white_rook, white_queen, white_king]
black_images = [black_pawn, black_bishop, black_knight, black_rook, black_queen, black_king]

chess_piece_list = ["pawn", "bishop", "knight", "rook", "queen", "king"]

chess_piece_health_and_damage = {
    "pawn": (50, 10),
    "bishop": (75, 15),
    "knight": (75, 15),
    "rook": (75, 20),
    "queen": (100, 20),
    "king": (150, 10),
}


# Draws important things that will show up before pieces
def draw_game():
    chessboard = pygame.image.load('files/chess board.png')
    window.blit(chessboard, (0, 0))
    pygame.draw.rect(window, 'gold', [720, 0, 380, window_height], 5)

    pygame.draw.rect(window, 'gold', [720, 600, 380, 120], 5)
    status_text = ['White turn', 'White to move',
                   'Black turn', 'Black to move']

    text = font.render(status_text[current_turn], True, 'black')
    text_rect = text.get_rect(center=(910, 660))
    window.blit(text, text_rect)


# Draws the pieces in their designated spots
def draw_pieces():
    for i in range(len(black_pieces)):
        index = chess_piece_list.index(black_pieces[i])
        if black_pieces[i] == "pawn":
            window.blit(black_pawn, (black_locations[i][0] * 80 + 45, black_locations[i][1] * 80 + 45))
        else:
            window.blit(black_images[index], (black_locations[i][0] * 80 + 45, black_locations[i][1] * 80 + 45))

        if current_turn > 2:
            if selection == i:
                pygame.draw.rect(window, "red", [black_locations[i][0] * 80 + 40, black_locations[i][1] * 80 + 40, 80, 80], 2)

    for i in range(len(white_pieces)):
        index = chess_piece_list.index(white_pieces[i])
        if white_pieces[i] == "pawn":
            window.blit(white_pawn, (white_locations[i][0] * 80 + 45, white_locations[i][1] * 80 + 45))
        else:
            window.blit(white_images[index], (white_locations[i][0] * 80 + 45, white_locations[i][1] * 80 + 45))

        if current_turn < 2:
            if selection == i:
                pygame.draw.rect(window, "red", [white_locations[i][0] * 80 + 40, white_locations[i][1] * 80 + 40, 80, 80], 2)


# Checks all valid options to move
def option_checker(pieces, locations, turn):
    moves_list = []
    all_moves_list = []

    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]

        if piece == "pawn":
            moves_list = check_pawn_moves(location, turn)
        elif piece == "bishop":
            moves_list = check_bishop_moves(location, turn)
        elif piece == "knight":
            moves_list = check_knight_moves(location, turn)
        elif piece == "rook":
            moves_list = check_rook_moves(location, turn)
        elif piece == "queen":
            moves_list = check_queen_moves(location, turn)
        elif piece == "king":
            moves_list = check_king_moves(location, turn)

        all_moves_list.append(moves_list)

    return all_moves_list


# Check pawn moves
def check_pawn_moves(position, turn):
    available_moves = []

    if turn == "black":
        if (position[0], position[1] + 1) not in black_locations and (position[0], position[1] + 1) not in white_locations and position[1] < 7:
            available_moves.append((position[0], position[1] + 1))

        if (position[0], position[1] + 2) not in black_locations and (position[0], position[1] + 2) not in white_locations and position[1] == 1 and (position[0], position[1] + 1) not in black_locations and (position[0], position[1] + 1) not in white_locations:
            available_moves.append((position[0], position[1] + 2))

        if (position[0] + 1, position[1] + 1) in white_locations:
            available_moves.append((position[0] + 1, position[1] + 1))

        if (position[0] - 1, position[1] + 1) in white_locations:
            available_moves.append((position[0] - 1, position[1] + 1))
    elif turn == "white":
        if (position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            available_moves.append((position[0], position[1] - 1))

        if (position[0], position[1] - 2) not in white_locations and (position[0], position[1] - 2) not in black_locations and position[1] == 6 and (position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations:
            available_moves.append((position[0], position[1] - 2))

        if (position[0] + 1, position[1] - 1) in black_locations:
            available_moves.append((position[0] + 1, position[1] - 1))

        if (position[0] - 1, position[1] - 1) in black_locations:
            available_moves.append((position[0] - 1, position[1] - 1))

    return available_moves


# Check bishop moves
def check_bishop_moves(position, turn):
    available_moves = []

    if turn == 'white':
        opposition_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        opposition_list = white_locations

    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                available_moves.append((position[0] + (chain * x), position[1] + (chain * y)))

                if (position[0] + (chain * x), position[1] + (chain * y)) in opposition_list:
                    path = False
                chain += 1
            else:
                path = False

    return available_moves


# Check knight moves
def check_knight_moves(position, turn):
    available_moves = []

    if turn == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations

    # All 8 combinations of moves a knight can do
    available_paths = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        check_move = (position[0] + available_paths[i][0], position[1] + available_paths[i][1])
        if check_move not in friends_list and 0 <= check_move[0] <= 7 and 0 <= check_move[1] <= 7:
            available_moves.append(check_move)

    return available_moves


# Check rook moves
def check_rook_moves(position, turn):
    available_moves = []

    if turn == 'white':
        opposition_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        opposition_list = white_locations

    # Straight line movements
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                available_moves.append((position[0] + (chain * x), position[1] + (chain * y)))

                if (position[0] + (chain * x), position[1] + (chain * y)) in opposition_list:
                    path = False
                chain += 1
            else:
                path = False
    return available_moves


# Check queen moves
def check_queen_moves(position, turn):
    available_moves = []

    available_moves = check_bishop_moves(position, turn)
    moves_list_rook = check_rook_moves(position, turn)
    for i in range(len(moves_list_rook)):
        available_moves.append(moves_list_rook[i])

    return available_moves


# Check king moves
def check_king_moves(position, turn):
    available_moves = []

    if turn == 'white':
        opposition_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        opposition_list = white_locations

    # Only 8 spots to check for
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            available_moves.append(target)

    return available_moves


# Check valid moves for selected piece only
def check_valid_moves():
    if current_turn < 2:
        options_list = white_options
    else:
        options_list = black_options

    valid_options = options_list[selection]
    return valid_options


# Draw valid moves onto the window
def draw_valid_moves(moves_valid):
    for i in range(len(moves_valid)):
        pygame.draw.circle(window, "gray", (moves_valid[i][0] * 80 + 80, moves_valid[i][1] * 80 + 80), 5)


# Draw captured pieces
def draw_captured_pieces():
    pygame.draw.line(window, 'black', (910, 5), (910, 600), 10)
    for i in range(len(white_captured_pieces)):
        captured_piece = white_captured_pieces[i]
        index = chess_piece_list.index(captured_piece)

        if i >= 8:
            window.blit(black_images[index], (800, 10 + 70 * (i - 8)))
        else:
            window.blit(black_images[index], (725, 10 + 70 * i))
    for i in range(len(black_captured_pieces)):
        captured_piece = black_captured_pieces[i]
        index = chess_piece_list.index(captured_piece)
        if i >= 8:
            window.blit(white_images[index], (1010, 10 + 70 * (i - 8)))
        else:
            window.blit(white_images[index], (935, 10 + 70 * i))


# Counter for king check flashing
counter = 0


# King in check
def draw_check():
    checked = False
    if current_turn < 2:
        if "king" in white_pieces:
            king_index = white_pieces.index("king")
            king_location = white_locations[king_index]

            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(window, "dark red", (white_locations[king_index][0] * 80 + 40, white_locations[king_index][1] * 80 + 40, 80, 80), 5)
    else:
        if "king" in black_pieces:
            king_index = black_pieces.index("king")
            king_location = black_locations[king_index]

            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(window, "dark red", (black_locations[king_index][0] * 80 + 40, black_locations[king_index][1] * 80 + 40, 80, 80), 5)


black_options = option_checker(black_pieces, black_locations, "black")
white_options = option_checker(white_pieces, white_locations, "white")

# Timer and frames per second for flashing check
timer = pygame.time.Clock()
frames_per_second = 60

# Boxing-State check
piece_taken = False

# Taker wins boxing or taken wins
taker = None
taker_wins = None
original_selection = None

attack_start = False

player1Attack1 = False
player1Block1 = False

player2Attack1 = False
player2Block1 = False

# First value is attack1, second value is block1, third value is attack2, fourth value is block2
white_piece_animation = {
    "pawn": (),
    "bishop": (),
    "knight": (),
    "rook": (),
    "queen": (),
    "king": ()
}

# First value is attack1, second value is block1, third value is attack2, fourth value is block2
black_piece_animation = {
    "pawn": (),
    "bishop": (),
    "knight": (),
    "rook": (),
    "queen": (),
    "king": ()
}

player1AttackAnimation1 = ["Files/Player1Attack1/Player1Attack1Image1.png", "Files/Player1Attack1/Player1Attack1Image2.png", "Files/Player1Attack1/Player1Attack1Image3.png","Files/Player1Attack1/Player1Attack1Image4.png"]
player1BlockAnimation1 = ["Files/Player1Block1/Player1Block1Image1.png", "Files/Player1Block1/Player1Block1Image2.png"]

player2AttackAnimation1 = ["Files/Player2Attack1/Player2Attack1Image1.png", "Files/Player2Attack1/Player2Attack1Image2.png", "Files/Player2Attack1/Player2Attack1Image3.png", "Files/Player2Attack1/Player2Attack1Image4.png"]
player2BlockAnimation1 = ["Files/Player2Block1/Player2Block1Image1.png", "Files/Player2Block1/Player2Block1Image2.png"]

# main game loop
playing = True
while playing:
    timer.tick(frames_per_second)
    if counter < 30:
        counter += 1
    else:
        counter = 0

    window.fill("gray")

    if not piece_taken:
        # Call functions
        draw_game()
        draw_pieces()
        draw_captured_pieces()

        draw_check()

        if selection != 200:
            valid_moves = check_valid_moves()
            draw_valid_moves(valid_moves)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x_coord = (event.pos[0] - 40) // 80
                y_coord = (event.pos[1] - 40) // 80
                click_cords = (x_coord, y_coord)

                # White turn information
                if current_turn <= 1:
                    if click_cords in white_locations:
                        selection = white_locations.index(click_cords)
                        if current_turn == 0:
                            current_turn = 1

                    if click_cords in valid_moves and selection != 200:
                        original_selection = white_locations[selection]
                        white_locations[selection] = click_cords
                        if click_cords in black_locations:
                            white_piece_name = white_pieces[selection]
                            black_piece_name = black_pieces[black_locations.index(click_cords)]

                            boxer1 = boxing_state.Boxer(window, 100, 200, player1AttackAnimation1, player1BlockAnimation1, chess_piece_health_and_damage[white_piece_name][1], chess_piece_health_and_damage[white_piece_name][0])
                            boxer2 = boxing_state.Boxer(window, 500, 200, player2AttackAnimation1, player2BlockAnimation1, chess_piece_health_and_damage[black_piece_name][1], chess_piece_health_and_damage[black_piece_name][0])

                            player1Attack1 = False
                            player2Attack1 = False
                            player1Block1 = False
                            player2Block1 = False

                            taker = "White"
                            taker_wins = None
                            piece_taken = True
                            break
                        black_options = option_checker(black_pieces, black_locations, "black")
                        white_options = option_checker(white_pieces, white_locations, "white")
                        current_turn = 2
                        selection = 200
                        valid_moves = []

                # Black turn information
                if current_turn >= 2:
                    if click_cords in black_locations:
                        selection = black_locations.index(click_cords)
                        if current_turn == 2:
                            current_turn = 3

                    if click_cords in valid_moves and selection != 200:
                        original_selection = black_locations[selection]
                        black_locations[selection] = click_cords
                        if click_cords in white_locations:
                            black_piece_name = black_pieces[selection]
                            white_piece_name = white_pieces[white_locations.index(click_cords)]

                            boxer1 = boxing_state.Boxer(window, 100, 200, player1AttackAnimation1, player1BlockAnimation1, chess_piece_health_and_damage[white_piece_name][1], chess_piece_health_and_damage[white_piece_name][0])
                            boxer2 = boxing_state.Boxer(window, 500, 200, player2AttackAnimation1, player2BlockAnimation1, chess_piece_health_and_damage[black_piece_name][1], chess_piece_health_and_damage[black_piece_name][0])

                            player1Attack1 = False
                            player2Attack1 = False
                            player1Block1 = False
                            player2Block1 = False

                            taker = "Black"
                            taker_wins = None
                            piece_taken = True
                            break
                        black_options = option_checker(black_pieces, black_locations, "black")
                        white_options = option_checker(white_pieces, white_locations, "white")
                        current_turn = 0
                        selection = 200
                        valid_moves = []

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    taker_wins = False

                if event.key == pygame.K_w and not player1Block1:
                    player1Attack1 = True
                if event.key == pygame.K_UP and not player2Block1:
                    player2Attack1 = True

                if event.key == pygame.K_a:
                    player1Block1 = True
                if event.key == pygame.K_LEFT:
                    player2Block1 = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player1Block1 = False
                    boxer1.reset_block_bool()
                if event.key == pygame.K_LEFT:
                    player2Block1 = False
                    boxer2.reset_block_bool()

        boxing_ring = pygame.image.load("files/BoxingRing.png")
        boxing_ring = pygame.transform.scale(boxing_ring, (1100, 720))
        window.blit(boxing_ring, (0, 0))

        if player1Attack1:
            player1Attack1 = boxer1.attack(boxer2)
        elif player1Block1:
            player1Block1 = boxer1.defend()
        if not player1Block1 and not player1Attack1:
            boxer1.idle()

        if player2Attack1:
            player2Attack1 = boxer2.attack(boxer1)
        elif player2Block1:
            player2Block1 = boxer2.defend()
        if not player2Block1 and not player2Attack1:
            boxer2.idle()

        boxer1.update_health(font, window, 100, 0)
        boxer2.update_health(font, window, 425, 720)

        # Display Controls
        pygame.draw.rect(window, 'light gray', [360, 0, 380, 125], 100)
        pygame.draw.rect(window, 'gold', [360, 0, 380, 125], 5)
        text_to_render = ["Controls (WASD and Arrow keys):", "Player 1: W for High Attack, A for High Block", "Player 2: ^ for High Attack, < for High Block"]

        for text in text_to_render:
            render = font_small.render(text, True, 'black')
            text_rect = render.get_rect(center=(550, 25 + (text_to_render.index(text) * 35)))
            window.blit(render, text_rect)

        boxer1_lose = boxer1.check_health()
        boxer2_lose = boxer2.check_health()

        if boxer1_lose or boxer2_lose:
            if taker == "White":
                if boxer1_lose:
                    taker_wins = False
                if boxer2_lose:
                    taker_wins = True
            elif taker == "Black":
                if boxer1_lose:
                    taker_wins = True
                if boxer2_lose:
                    taker_wins = False

        if taker_wins is not None:
            if taker == "White":
                if taker_wins:
                    black_piece = black_locations.index(click_cords)
                    white_captured_pieces.append(black_pieces[black_piece])
                    black_pieces.pop(black_piece)
                    black_locations.pop(black_piece)
                else:
                    white_locations[selection] = original_selection
                black_options = option_checker(black_pieces, black_locations, "black")
                white_options = option_checker(white_pieces, white_locations, "white")
                current_turn = 2
                selection = 200
                valid_moves = []
                piece_taken = False
            elif taker == "Black":
                if taker_wins:
                    white_piece = white_locations.index(click_cords)
                    black_captured_pieces.append(white_pieces[white_piece])
                    white_pieces.pop(white_piece)
                    white_locations.pop(white_piece)
                else:
                    black_locations[selection] = original_selection
                black_options = option_checker(black_pieces, black_locations, "black")
                white_options = option_checker(white_pieces, white_locations, "white")
                current_turn = 0
                selection = 200
                valid_moves = []

                taker_wins = None
                piece_taken = False



    pygame.display.update()

pygame.quit()
